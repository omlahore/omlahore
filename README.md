<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1f6feb,100:7aa2f7&height=180&section=header&text=Om%20Lahore&fontColor=ffffff&fontSize=52&fontAlignY=36&desc=Backend%20and%20cloud%20native%20%7C%20Go%20%C2%B7%20TypeScript%20%C2%B7%20Kubernetes&descAlignY=58&descSize=18" width="100%" alt="Om Lahore" />

<a href="https://github.com/omlahore?tab=repositories"><img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=500&size=20&duration=3600&pause=700&color=7AA2F7&center=true&vCenter=true&width=700&lines=I+read+other+people's+code+until+I+find+something+wrong+with+it." alt="I read other people's code until I find something wrong with it." /></a>

<br />

<img src="https://img.shields.io/github/issues-search?query=is%3Apr%20author%3Aomlahore%20is%3Amerged&label=MERGED%20UPSTREAM&style=for-the-badge&color=1f6feb&labelColor=0d1117" alt="Merged upstream" />
<img src="https://img.shields.io/github/issues-search?query=is%3Apr%20author%3Aomlahore%20is%3Aopen&label=OPEN%20NOW&style=for-the-badge&color=7aa2f7&labelColor=0d1117" alt="Open pull requests" />
<img src="https://komarev.com/ghpvc/?username=omlahore&style=for-the-badge&color=0d1117&label=PROFILE+VIEWS" alt="Profile views" />

<a href="https://linkedin.com/in/om-lahorey"><img src="https://img.shields.io/badge/LinkedIn-0d1117?style=for-the-badge&logo=linkedin&logoColor=7aa2f7" alt="LinkedIn" /></a>
<a href="https://medium.com/@omlahore47"><img src="https://img.shields.io/badge/Writing-0d1117?style=for-the-badge&logo=medium&logoColor=7aa2f7" alt="Medium" /></a>
<a href="https://x.com/OmLahorey"><img src="https://img.shields.io/badge/X-0d1117?style=for-the-badge&logo=x&logoColor=7aa2f7" alt="X" /></a>
<a href="mailto:omlahore47@gmail.com"><img src="https://img.shields.io/badge/Email-0d1117?style=for-the-badge&logo=gmail&logoColor=7aa2f7" alt="Email" /></a>

</div>

---

Backend and cloud native, mostly Go and TypeScript, out of Mumbai. I'm the first engineer at Ensueno, where I own the API and the Postgres schema for three services. Most of what's below started with me reading a repository, not picking up an issue.

---

## Things I found by reading the code

| | |
|---|---|
| **[Kyverno](https://github.com/kyverno/kyverno)** <sup>CNCF</sup><br />`msgRaw.(string)` on a policy message that resolves to a raw value takes the process down.<br />[#16977](https://github.com/kyverno/kyverno/pull/16977) **merged, backported to release-1.19** | **[zot](https://github.com/project-zot/zot)** <sup>CNCF</sup><br />`tags/list` returned 404 when `last` named a tag that had since been deleted, so a client paging through tags just stopped.<br />[#4448](https://github.com/project-zot/zot/pull/4448) **merged** |
| **[Grafana](https://github.com/grafana/grafana)**<br />Sparklines rendered flat below `1e-6`, because counting decimals with `'' + num` counts the exponent once JavaScript switches notation.<br />[#130413](https://github.com/grafana/grafana/pull/130413) and [#131844](https://github.com/grafana/grafana/pull/131844) **merged** | **[maglev](https://github.com/OneBusAway/maglev)** <sup>OneBusAway</sup><br />Stop delays were keyed by `stop_id`, so on a loop route that visits a stop twice the delay landed on the wrong visit.<br />[#1415](https://github.com/OneBusAway/maglev/pull/1415) **merged**, 9 merged there in total |
| **[SigNoz](https://github.com/SigNoz/signoz)** <sup>OpenTelemetry</sup><br />The OpAMP parser asserts types on config an agent reports about itself. Four ordinary YAML mistakes panic it.<br />[#12572](https://github.com/SigNoz/signoz/pull/12572) | **[Volcano](https://github.com/volcano-sh/volcano)** <sup>CNCF</sup><br />A quoted number in the scheduler YAML, `cpu: "20"`, takes the scheduler down through an unchecked assertion.<br />[#5947](https://github.com/volcano-sh/volcano/pull/5947) |

Reported privately: three cryptography findings in a European end to end encrypted photo service, including a PBKDF2 iteration count that truncated to a single round on 32 bit builds. All three confirmed, patched and shipped the same day.

Also in [Keploy](https://github.com/keploy/keploy/pull/4611), [kthena](https://github.com/volcano-sh/kthena/pull/1745), [PipeCD](https://github.com/pipe-cd/pipecd/pull/7319), [OpenKruise](https://github.com/openkruise/agents/pull/902), [Headlamp](https://github.com/kubernetes-sigs/headlamp/pull/7073), [kured](https://github.com/kubereboot/kured/pull/1410), [Infisical](https://github.com/Infisical/infisical/pull/7517), [Phase](https://github.com/phasehq/console/pull/970), [OpenWISP](https://github.com/openwisp/openwisp-radius/pull/750) and [MDN](https://github.com/mdn/content/pull/38998).

---

## Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=go,ts,nodejs,react,python,postgres,docker,kubernetes,aws,githubactions,redis,linux&theme=dark&perline=12" alt="Go, TypeScript, Node.js, React, Python, PostgreSQL, Docker, Kubernetes, AWS, GitHub Actions, Redis, Linux" />

</div>

---

## The numbers

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=omlahore&theme=github_dark" width="98%" alt="Profile summary" />

<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=omlahore&theme=github_dark" width="49%" alt="Repositories per language" />
<img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=omlahore&theme=github_dark" width="49%" alt="Most committed language" />

<img src="https://streak-stats.demolab.com/?user=omlahore&theme=github-dark-blue&hide_border=true&date_format=j%20M%5B%20Y%5D" width="60%" alt="Contribution streak" />

</div>

---

## Writing

- [Dead dependencies don't get archived. They get quiet.](https://medium.com/@omlahore47/dead-dependencies-dont-get-archived-they-get-quiet-5916613a7a39)
- [Your local agent is spending 39% of its system prompt on skills it will never use](https://medium.com/@omlahore47/your-local-agent-is-spending-39-of-its-system-prompt-on-skills-it-will-never-use-232f6515515c)
- [shadPS4 shipped 239 commits and none of them say "fix memory leak"](https://medium.com/@omlahore47/shadps4-shipped-239-commits-and-none-of-them-say-fix-memory-leak-a61f32b5cbd8)

---

<div align="center">

<img src="https://raw.githubusercontent.com/omlahore/omlahore/output/snake.svg" width="100%" alt="A snake eating this year's contribution graph" />

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7aa2f7,50:1f6feb,100:0d1117&height=110&section=footer" width="100%" alt="" />

</div>
