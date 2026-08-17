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


if __name__ == "__main__":
    main()
