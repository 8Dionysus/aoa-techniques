# Minimal Skill Marketplace Curation

Use one small local discovery surface over upstream-owned skills.

```text
skills/
  workflow/
    orchestration/
      SKILL.md
  tools/
    dev-browser/
      SKILL.md

docs/skill-marketplace.md
```

```md
## Workflow
- `orchestration`
  - summary: multi-agent task coordination
  - source: upstream-owned skill

## Tools
- `dev-browser`
  - summary: browser automation with persistent page state
  - source: upstream-owned skill
```

What the contract shows:

- the local surface groups and summarizes skills for discovery
- upstream ownership stays visible
- sync or provenance artifacts may exist elsewhere, but they are not the center of this curated surface
- installer, registry, and command syntax details stay outside the example
