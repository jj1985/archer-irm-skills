# Archer IRM skills

A plugin marketplace for AI coding agents that work with the **Archer IRM** (formerly RSA Archer) platform APIs.
It ships one plugin, `archer-irm-api`, built from the official Archer API Help release 2026.08.

| What you get | Where |
|---|---|
| OpenAPI 3.1 spec for the RESTful Platform API, V2 API, Data Gateway API, Content API (OData) and the NGRX entry point (115 operations) | [`openapi/archer-irm.openapi.yaml`](openapi/archer-irm.openapi.yaml) (also bundled in the skill) |
| Agent skill: routing table, core mechanics, workflow, references, gotchas | [`plugins/archer-irm-api/skills/archer-irm-api/SKILL.md`](plugins/archer-irm-api/skills/archer-irm-api/SKILL.md) |
| Generated catalog of all 108 SOAP Web Services methods, full `SearchReport` grammar | `.../references/web-services-*.md` |
| Markdown snapshot of all 245 help pages plus 84 example payloads | `.../references/source-docs/` |
| Dependency-free Python clients (REST/V2/Content API and SOAP) | `.../scripts/archer_rest.py`, `.../scripts/archer_soap.py` |

## Install

### GitHub Copilot CLI

```bash
copilot plugin marketplace add jj1985/archer-irm-skills
copilot plugin install archer-irm-api@archer-irm
```

Or install the plugin directly from the repository subdirectory:

```bash
copilot plugin install jj1985/archer-irm-skills:plugins/archer-irm-api
```

To enable it declaratively for a repository, add it to `.github/copilot/settings.json`:

```json
{
  "extraKnownMarketplaces": { "archer-irm": { "source": "github", "repo": "jj1985/archer-irm-skills" } },
  "enabledPlugins": { "archer-irm-api@archer-irm": true }
}
```

### Claude Code

```text
/plugin marketplace add jj1985/archer-irm-skills
/plugin install archer-irm-api@archer-irm
```

### Any agent that reads `SKILL.md`

Copy `plugins/archer-irm-api/skills/archer-irm-api/` into your skills directory (for example `~/.copilot/skills/`, `~/.claude/skills/` or `.agents/skills/`).

## Repository layout

```text
archer-irm-skills/
├── .github/plugin/marketplace.json        Copilot CLI marketplace manifest
├── .claude-plugin/marketplace.json        Claude Code mirror of the marketplace manifest
├── openapi/archer-irm.openapi.yaml        OpenAPI 3.1 spec (canonical copy)
└── plugins/
    └── archer-irm-api/
        ├── plugin.json                    Agent Plugins 1.0 manifest (Copilot CLI, Codex and other clients)
        ├── .claude-plugin/plugin.json     Claude Code manifest
        └── skills/
            └── archer-irm-api/
                ├── SKILL.md
                ├── references/            quick references, SOAP catalog, docs snapshot, OpenAPI copy
                └── scripts/               archer_rest.py, archer_soap.py
```

The plugin follows the [Agent Plugins 1.0](https://agent-plugins.org/) layout that Copilot CLI documents: the manifest sits at the plugin root, and skills are discovered from `skills/<name>/SKILL.md`. Claude Code reads the `.claude-plugin/` mirrors.

## Using the scripts

Both scripts use only the Python standard library and read connection settings from environment variables
(`ARCHER_URL`, `ARCHER_INSTANCE`, `ARCHER_USER`, `ARCHER_PASSWORD`, or `ARCHER_PAT` for a Personal Access Token).

```bash
export ARCHER_URL=https://archer.example.com/Archer ARCHER_PAT=apat-...
python plugins/archer-irm-api/skills/archer-irm-api/scripts/archer_rest.py apps
python plugins/archer-irm-api/skills/archer-irm-api/scripts/archer_rest.py contentapi-dump Risk_Register --out rr.json
```

## Scope and caveats

- Sources: [Archer API Help 2026.08](https://help.archerirm.cloud/api_202608/content/api/archer_apis.htm). Archer publishes no machine-readable spec, so response schemas in the OpenAPI document are derived from the documented examples and are representative rather than exhaustive.
- The SOAP Web Services API cannot be expressed in OpenAPI; it is covered by the method catalog and the WSDL each instance serves at `/ws/<service>.asmx?WSDL`.
- The NGRX API's full Swagger is only served inside a customer's non-production tenant, so only its documented bootstrap call is included.
- Nothing here has been run against a live Archer instance. Issues and corrections are welcome.

## License

MIT. Archer Technologies LLC owns the underlying product documentation; this repository is an independent, derived reference and is not affiliated with Archer.
