## Om Lahore

Software engineer in Pune, India. I work on backend and cloud-native things, mostly in
TypeScript and Go, and I spend most of my spare time reading other people's code until I find
something wrong with it.

<p align="left">
  <a href="https://omlahore.com" target="_blank">
    <img src="https://img.shields.io/badge/Website-omlahore.com-111111?style=flat-square&logo=google-chrome&logoColor=white" alt="Website" />
  </a>
  <a href="https://linkedin.com/in/om-lahorey" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://medium.com/@omlahore47" target="_blank">
    <img src="https://img.shields.io/badge/Medium-111111?style=flat-square&logo=medium&logoColor=white" alt="Medium" />
  </a>
  <a href="https://x.com/OmLahorey" target="_blank">
    <img src="https://img.shields.io/badge/X-111111?style=flat-square&logo=x&logoColor=white" alt="X" />
  </a>
  <a href="mailto:omlahore47@gmail.com">
    <img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email" />
  </a>
</p>

### Open source

Most of these came from reading the code rather than from an issue tracker.

**[Kyverno](https://github.com/kyverno/kyverno)** (CNCF policy engine, Go)
[#16977](https://github.com/kyverno/kyverno/pull/16977) is merged and backported to their 1.19
release. An unchecked type assertion on `request.operation` condition values took the process
down when a policy compared against a non-string. Three more panic fixes are open.

**[SigNoz](https://github.com/SigNoz/signoz)** (OpenTelemetry observability)
[#12572](https://github.com/SigNoz/signoz/pull/12572): their OpAMP parser read the collector
config an agent reports about itself and asserted its types outright, so four ordinary YAML
mistakes panicked it.

**[Grafana](https://github.com/grafana/grafana)**
[#130413](https://github.com/grafana/grafana/pull/130413): sparklines rendered flat for values
below 1e-6, because counting decimals with `'' + num` counts the exponent's characters once
JavaScript switches to exponential notation.

**[kured](https://github.com/kubereboot/kured)** (Kubernetes reboot daemon)
[#1410](https://github.com/kubereboot/kured/pull/1410): a lock taken while `--lock-ttl` was unset
records a zero TTL and can never expire, so a node removed by the autoscaler blocks every reboot
until someone deletes the annotation by hand.

**[ToolJet](https://github.com/ToolJet/ToolJet)**
[#17527](https://github.com/ToolJet/ToolJet/pull/17527): a cleanup function that was written but
never returned, so no avatar blob URL was ever revoked, in a component that renders per row in a
virtualized list.

Also: [Headlamp](https://github.com/kubernetes-sigs/headlamp/pull/7073),
[Infisical](https://github.com/Infisical/infisical/pull/7517),
[Phase](https://github.com/phasehq/console/pull/970),
[OpenWISP](https://github.com/openwisp/openwisp-radius/pull/750),
[MDN](https://github.com/mdn/content/pull/38998), and a set of cryptography findings in a
European end-to-end encrypted photo service, all three confirmed by the vendor and patched the
same day.

### What I actually use

`TypeScript` `Node` `React` `Go` `Python` `PostgreSQL` `Docker` `Kubernetes` `AWS` `GitHub Actions`

### Contributions

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/omlahore/omlahore/output/snake.svg" />
  <img alt="contribution graph" src="https://raw.githubusercontent.com/omlahore/omlahore/output/snake.svg" />
</picture>

### Writing

- [Dead dependencies don't get archived. They get quiet.](https://medium.com/@omlahore47/dead-dependencies-dont-get-archived-they-get-quiet-5916613a7a39)
- [Your local agent is spending 39% of its system prompt on skills it will never use](https://medium.com/@omlahore47/your-local-agent-is-spending-39-of-its-system-prompt-on-skills-it-will-never-use-232f6515515c)
- [shadPS4 shipped 239 commits and none of them say "fix memory leak"](https://medium.com/@omlahore47/shadps4-shipped-239-commits-and-none-of-them-say-fix-memory-leak-a61f32b5cbd8)
