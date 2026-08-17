<div align="center">

<img src="https://raw.githubusercontent.com/omlahore/omlahore/main/assets/hero.svg" alt="A terminal replaying a real bug: an unchecked Go type assertion that panicked inside Kyverno, the guard that fixed it, and the note that it shipped in release 1.19." width="880" />

<br />

<img src="https://raw.githubusercontent.com/omlahore/omlahore/main/assets/stats.svg" alt="Pull requests merged upstream, open right now, projects contributed to, and their combined stars." width="880" />

<br /><br />

<a href="https://omlahore.com"><img src="https://img.shields.io/badge/omlahore.com-11151c?style=for-the-badge&logo=google-chrome&logoColor=7aa2f7" alt="Website" /></a>
<a href="https://linkedin.com/in/om-lahorey"><img src="https://img.shields.io/badge/LinkedIn-11151c?style=for-the-badge&logo=linkedin&logoColor=7aa2f7" alt="LinkedIn" /></a>
<a href="https://medium.com/@omlahore47"><img src="https://img.shields.io/badge/Writing-11151c?style=for-the-badge&logo=medium&logoColor=7aa2f7" alt="Medium" /></a>
<a href="https://x.com/OmLahorey"><img src="https://img.shields.io/badge/X-11151c?style=for-the-badge&logo=x&logoColor=7aa2f7" alt="X" /></a>
<a href="mailto:omlahore47@gmail.com"><img src="https://img.shields.io/badge/Email-11151c?style=for-the-badge&logo=gmail&logoColor=7aa2f7" alt="Email" /></a>

</div>

<br />

## Om Lahore

Backend and cloud-native, mostly TypeScript and Go, out of Pune. I read other people's
code until I find something wrong with it, and most of what is below started that way
rather than from an issue tracker.

<br />

## Things I found by reading the code

<table>
<tr>
<td width="50%" valign="top">

### [Kyverno](https://github.com/kyverno/kyverno) <sup>CNCF, Go</sup>

`msgRaw.(string)` on a policy message that is a single variable. That resolves to
the raw value, so it is not always a string, and the assertion took the process
down.

**[#16977](https://github.com/kyverno/kyverno/pull/16977) merged, backported to
release-1.19.** Three more panic fixes open.

</td>
<td width="50%" valign="top">

### [SigNoz](https://github.com/SigNoz/signoz) <sup>OpenTelemetry</sup>

Their OpAMP parser reads the collector config an agent reports about *itself*, then
asserts its types outright. Four ordinary YAML mistakes panic it, the easiest being a
processor indented one level too deep.

**[#12572](https://github.com/SigNoz/signoz/pull/12572)**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Grafana](https://github.com/grafana/grafana)

Sparklines rendered flat below `1e-6`. Counting decimals with `'' + num` counts the
exponent's characters once JavaScript switches to exponential notation, so
`1.5e-7` reported four.

**[#130413](https://github.com/grafana/grafana/pull/130413)**

</td>
<td width="50%" valign="top">

### [kured](https://github.com/kubereboot/kured) <sup>Kubernetes</sup>

A reboot lock taken while `--lock-ttl` was unset records a zero TTL and can never
expire. When the autoscaler removes that node, every future reboot blocks until
someone deletes the annotation by hand.

**[#1410](https://github.com/kubereboot/kured/pull/1410)**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [ToolJet](https://github.com/ToolJet/ToolJet)

A cleanup function that was written but never returned, so no avatar blob URL was
ever revoked. In a virtualized list that leaks once per scrolled row, and the same
recycling let a stale response paint the wrong face.

**[#17527](https://github.com/ToolJet/ToolJet/pull/17527)**

</td>
<td width="50%" valign="top">

### Reported privately

Three cryptography findings in a European end-to-end encrypted photo service,
including a PBKDF2 iteration count that truncated to a single round on 32-bit
builds.

**All three confirmed, patched and shipped the same day.**

</td>
</tr>
</table>

Also in [Headlamp](https://github.com/kubernetes-sigs/headlamp/pull/7073),
[Infisical](https://github.com/Infisical/infisical/pull/7517),
[Phase](https://github.com/phasehq/console/pull/970),
[OpenWISP](https://github.com/openwisp/openwisp-radius/pull/750) and
[MDN](https://github.com/mdn/content/pull/38998).

<br />

## What I actually use

<p>
<img src="https://img.shields.io/badge/TypeScript-11151c?style=flat-square&logo=typescript&logoColor=7aa2f7" alt="TypeScript" />
<img src="https://img.shields.io/badge/Go-11151c?style=flat-square&logo=go&logoColor=7aa2f7" alt="Go" />
<img src="https://img.shields.io/badge/Node.js-11151c?style=flat-square&logo=node.js&logoColor=9ece6a" alt="Node.js" />
<img src="https://img.shields.io/badge/React-11151c?style=flat-square&logo=react&logoColor=7dcfff" alt="React" />
<img src="https://img.shields.io/badge/Python-11151c?style=flat-square&logo=python&logoColor=e0af68" alt="Python" />
<img src="https://img.shields.io/badge/PostgreSQL-11151c?style=flat-square&logo=postgresql&logoColor=7aa2f7" alt="PostgreSQL" />
<img src="https://img.shields.io/badge/Docker-11151c?style=flat-square&logo=docker&logoColor=7dcfff" alt="Docker" />
<img src="https://img.shields.io/badge/Kubernetes-11151c?style=flat-square&logo=kubernetes&logoColor=7aa2f7" alt="Kubernetes" />
<img src="https://img.shields.io/badge/AWS-11151c?style=flat-square&logo=amazon-web-services&logoColor=e0af68" alt="AWS" />
<img src="https://img.shields.io/badge/GitHub_Actions-11151c?style=flat-square&logo=github-actions&logoColor=7aa2f7" alt="GitHub Actions" />
</p>

<br />

## Writing

- [Dead dependencies don't get archived. They get quiet.](https://medium.com/@omlahore47/dead-dependencies-dont-get-archived-they-get-quiet-5916613a7a39)
- [Your local agent is spending 39% of its system prompt on skills it will never use](https://medium.com/@omlahore47/your-local-agent-is-spending-39-of-its-system-prompt-on-skills-it-will-never-use-232f6515515c)
- [shadPS4 shipped 239 commits and none of them say "fix memory leak"](https://medium.com/@omlahore47/shadps4-shipped-239-commits-and-none-of-them-say-fix-memory-leak-a61f32b5cbd8)

<br />

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/omlahore/omlahore/output/snake.svg" />
  <img alt="A snake eating this year's contribution graph" src="https://raw.githubusercontent.com/omlahore/omlahore/output/snake.svg" width="880" />
</picture>

</div>
