#!/usr/bin/env python3
"""Generate assets/stats.svg from the GitHub API.

The profile used to depend on third party services for this. They all went down
at once: github-readme-stats started returning 503 and three others returned 402
because their Vercel deployments hit spending limits. This generates the same
information from the API and commits the result, so the only thing that can
break it is this repository.

Run: GITHUB_TOKEN=... python3 .github/scripts/gen_stats.py
"""

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

USER = os.environ.get("PROFILE_USER", "omlahore")
TOKEN = os.environ.get("GITHUB_TOKEN")
OUT = "assets/stats.svg"

# Repos owned by the user are not outside contributions, so they do not count
# toward the reach number. Matching on owner rather than a hardcoded list.
API = "https://api.github.com"


def get(path, params=None):
    url = f"{API}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USER}-profile-stats",
        **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} for {url}", file=sys.stderr)
        raise


def search_prs(qualifier):
    """All PRs matching a qualifier, paged."""
    items, page = [], 1
    while page <= 10:
        data = get("/search/issues", {
            "q": f"type:pr author:{USER} {qualifier}",
            "per_page": 100,
            "page": page,
        })
        items.extend(data.get("items", []))
        if len(data.get("items", [])) < 100:
            break
        page += 1
    return items


def repo_of(item):
    # repository_url looks like https://api.github.com/repos/owner/name
    return item["repository_url"].split("/repos/", 1)[1]


EXT_LANG = {
    ".go": "Go", ".ts": "TypeScript", ".tsx": "TypeScript", ".js": "JavaScript",
    ".jsx": "JavaScript", ".py": "Python", ".rb": "Ruby", ".java": "Java",
    ".rs": "Rust", ".sh": "Shell", ".yaml": "YAML", ".yml": "YAML",
    ".css": "CSS", ".scss": "CSS", ".md": "Markdown", ".sql": "SQL",
}

LANG_COLOR = {
    "Go": "#7dcfff", "TypeScript": "#7aa2f7", "JavaScript": "#e0af68",
    "Python": "#9ece6a", "YAML": "#bb9af7", "Shell": "#73daca",
    "Markdown": "#5b6673", "Ruby": "#f7768e", "CSS": "#7dcfff",
    "Java": "#e0af68", "Rust": "#f7768e", "SQL": "#9ece6a",
}


def language_bar(prs, out_path="assets/languages.svg"):
    """Lines changed per language, counted from the files in each PR.

    This is deliberately not "languages in my own repos". Almost none of the
    work is in repos owned by this account, so that number would describe the
    wrong thing. This counts code that actually landed in someone else's tree.
    """
    lines = {}
    for it in prs:
        full = repo_of(it)
        if full.split("/")[0].lower() == USER.lower():
            continue
        num = it["number"]
        try:
            files = get(f"/repos/{full}/pulls/{num}/files", {"per_page": 100})
        except Exception:
            continue
        for f in files:
            ext = os.path.splitext(f.get("filename", ""))[1].lower()
            lang = EXT_LANG.get(ext)
            if not lang:
                continue
            lines[lang] = lines.get(lang, 0) + f.get("additions", 0) + f.get("deletions", 0)

    if not lines:
        return None

    total = sum(lines.values())
    # Anything under 1% is noise on a card meant to show where the depth is.
    ranked = [kv for kv in sorted(lines.items(), key=lambda kv: -kv[1]) if kv[1] / total >= 0.01][:6]
    total = sum(n for _, n in ranked)

    w, h, pad = 880, 150, 20
    bar_y, bar_h, bar_w = 46, 14, w - pad * 2
    segs, legend, x = [], [], float(pad)
    for i, (lang, n) in enumerate(ranked):
        frac = n / total
        seg_w = max(bar_w * frac, 3)
        colour = LANG_COLOR.get(lang, "#5b6673")
        r = "4" if i == 0 else "0"
        segs.append(f'<rect x="{x:.1f}" y="{bar_y}" width="{seg_w:.1f}" height="{bar_h}" fill="{colour}" rx="{r}"/>')
        lx = pad + (i % 3) * 290
        ly = 92 + (i // 3) * 26
        legend.append(
            f'<g class="lg" style="animation-delay:{i * .08:.2f}s">'
            f'<circle cx="{lx + 4}" cy="{ly - 4}" r="4.5" fill="{colour}"/>'
            f'<text class="mono nm" x="{lx + 16}" y="{ly}" font-size="12.5">{lang}</text>'
            f'<text class="mono pc" x="{lx + 16 + len(lang) * 7.6 + 10}" y="{ly}" font-size="12.5">{frac * 100:.1f}%</text>'
            f"</g>"
        )
        x += seg_w

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Languages by lines changed in pull requests to other people's repositories: {', '.join(f'{l} {n / total * 100:.0f} percent' for l, n in ranked)}.">
  <style>
    .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace }}
    .nm {{ fill: #c9d3df }} .pc {{ fill: #5b6673 }} .hd {{ fill: #5b6673 }}
    .lg {{ opacity: 0; animation: fade .5s ease-out forwards }}
    @keyframes fade {{ to {{ opacity: 1 }} }}
    @media (prefers-reduced-motion: reduce) {{ .lg {{ animation: none; opacity: 1 }} }}
  </style>
  <rect width="{w}" height="{h}" rx="10" fill="#11151c" stroke="#1b2330"/>
  <text class="mono hd" x="{pad}" y="26" font-size="11.5">what I wrote, in repositories I do not own</text>
  {chr(10).join(segs)}
  {chr(10).join(legend)}
</svg>
'''
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"{out_path}: " + ", ".join(f"{l} {n}" for l, n in ranked))
    return ranked


def main():
    merged = search_prs("is:merged")
    open_prs = search_prs("is:open")

    external = {}
    for it in merged + open_prs:
        full = repo_of(it)
        if full.split("/")[0].lower() == USER.lower():
            continue
        external.setdefault(full, {"merged": 0, "open": 0})
        external[full]["merged" if it in merged else "open"] += 1

    stars = 0
    for full in external:
        try:
            stars += get(f"/repos/{full}").get("stargazers_count", 0)
        except Exception:
            pass

    n_merged = sum(v["merged"] for v in external.values())
    n_open = sum(v["open"] for v in external.values())

    cards = [
        (f"{n_merged}", "merged upstream"),
        (f"{n_open}", "open right now"),
        (f"{len(external)}", "projects"),
        (f"{stars // 1000}k", "combined stars"),
    ]

    w, h, pad = 880, 132, 20
    cw = (w - pad * 2 - 12 * 3) // 4
    parts = []
    for i, (big, label) in enumerate(cards):
        x = pad + i * (cw + 12)
        parts.append(f'''  <g class="card" style="animation-delay:{i * .12:.2f}s">
    <rect x="{x}" y="34" width="{cw}" height="78" rx="8" fill="#161b23" stroke="#242c37"/>
    <text class="mono num" x="{x + cw // 2}" y="78" font-size="30" text-anchor="middle">{big}</text>
    <text class="mono lbl" x="{x + cw // 2}" y="98" font-size="11" text-anchor="middle">{label}</text>
  </g>''')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{n_merged} pull requests merged upstream, {n_open} open, across {len(external)} projects with {stars // 1000} thousand combined stars.">
  <style>
    .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace }}
    .num {{ fill: #c9d3df; font-weight: 600 }}
    .lbl {{ fill: #5b6673 }}
    .hd  {{ fill: #5b6673 }}
    .card {{ opacity: 0; animation: rise .6s ease-out forwards }}
    @keyframes rise {{ from {{ opacity: 0 }} to {{ opacity: 1 }} }}
    @media (prefers-reduced-motion: reduce) {{ .card {{ animation: none; opacity: 1 }} }}
  </style>
  <rect width="{w}" height="{h}" rx="10" fill="#11151c" stroke="#1b2330"/>
  <text class="mono hd" x="{pad}" y="22" font-size="11.5">contributions to other people's code</text>
{chr(10).join(parts)}
</svg>
'''

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"{OUT}: {n_merged} merged, {n_open} open, {len(external)} repos, {stars} stars")

    language_bar(merged + open_prs)


if __name__ == "__main__":
    main()
