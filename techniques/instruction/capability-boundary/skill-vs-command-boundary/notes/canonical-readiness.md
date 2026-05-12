# Canonical Readiness

## Technique
- id: AOA-T-0040
- name: skill-vs-command-boundary

## Verdict
- approve for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- the first second context adaptation keeps the contract bounded with live support from `aoa-skills` and `aoa-routing`
- exact public reinforcement: Claude Code skills keep reusable capability instructions in `SKILL.md` directories with optional supporting files, frontmatter, automatic loading, and direct `/skill-name` invocation, while built-in commands remain fixed session controls and invocation controls such as `disable-model-invocation` preserve command-like user timing for side-effectful actions
- validation strength: the bundle now has a checklist, a public-safe example, origin evidence, one documentation-first adaptation, one exact-fit public skill/command invocation surface beyond the donor lineage, and an adverse-effects review

## Default-use rationale
- this is the right canonical default when a repository has both reusable skill meaning and explicit user-facing entrypoints and needs the ownership split to remain visible
- it is strongest when command syntax, arguments, invocation timing, or structured workflow should stay separate from reusable capability meaning
- it remains narrower than marketplace curation, routing policy, shell-command doctrine, or one-source propagation

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- source checked: Claude Code skills and slash-command documentation
- sanitization still holds: the published bundle keeps only the reusable ownership split while stripping donor-specific plugin mechanics, model routing, command catalogs, and product naming
- public reuse check: the examples, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- no blocking promotion gap remains for the current canonical contract
- future work should still revisit the boundary if a platform fully collapses command files into skills and the reusable object becomes invocation-control policy rather than a skill-command ownership split

## Recommendation
- promote `AOA-T-0040` to `canonical`
- keep `notes/adverse-effects-review.md` as the watch surface for command syntax swallowing reusable skill meaning, routing creep, and shell-command overreach
