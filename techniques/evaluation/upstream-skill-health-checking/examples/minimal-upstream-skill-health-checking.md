# Minimal Upstream Skill Health Checking

Check upstream-backed skill entries before they appear in a local selector.

```bash
skills-source-check sources.yaml --before-selector
```

Example result:

```text
ready   github/team/skill-a      SKILL.md reachable and minimally parseable
review  github/team/skill-b      source reachable; metadata shape needs manual review
blocked github/team/skill-c      declared manifest missing at source path
```

The important behavior is bounded:

- `ready` means the source is reachable and minimally shaped enough to surface for inspection or selection
- `review` means the source is present but ambiguous enough that a human should look before it is surfaced
- `blocked` means the source should stay out of the selector until the declared path or manifest is fixed
- this step does not mirror the source, curate categories, assign trust scores, or run security scans
