# Bundle Anatomy Template And Contract Feedback

Source packets:

- [Bundle Anatomy Corpus Synthesis](bundle-anatomy-corpus-synthesis.md)
- [Bundle Anatomy Capsule Gap Repair Cohort](bundle-anatomy-capsule-gap-repair-cohort.md)

Status: template-contract-feedback, no technique leaf repair, no schema change,
no frontmatter migration, no path movement.

## Verdict

No broad template, atom-contract, topology-contract, or tree-contract change is
needed after the first repair cohort.

The only contract surface that actually moved was the capsule guide, and that
change already landed with the wrapped-bullet repair:

- [Technique Capsule Guide](../../../../../docs/TECHNIQUE_CAPSULE_GUIDE.md)

The repair clarified that wrapped Markdown list items remain one source item
when indented continuation lines belong to the same bullet. That is a capsule
builder contract detail, not a new technique authoring law.

## Feedback Decisions

| surface | decision | rationale |
|---|---|---|
| `templates/TECHNIQUE.template.md` | no change | the template already requires `Atomic move`, `Topology fit`, and `Small-agent execution shape`; the audit did not prove mass template failure |
| `docs/TECHNIQUE_ATOM_CONTRACT.md` | no change | the atom contract already says capsules must preserve the executable center and techniques must stay compact enough for small-agent execution |
| `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md` | no change | the audit found watch pressure, not a new frontmatter or schema requirement |
| `docs/TECHNIQUE_TREE_CONTRACT.md` | no change | the tree held 107/107 path parity and no route-away or path repair was found |
| `docs/TECHNIQUE_CAPSULE_GUIDE.md` | already changed | wrapped list continuation behavior was clarified in the capsule repair cohort |
| `scripts/validate_repo.py` capsule builder | already changed | wrapped list item extraction now keeps continuation lines in the same capsule source item |

## Repeated Gaps

The repeated `old-template-watch` label does not mean the old bundles are
broken. It means many bundles predate the newest explicit headings. Direct
reading showed the executable center remains recoverable, so this should remain
an opportunistic modernization note rather than a mass rewrite program.

The repeated `owner-boundary-watch` label is also healthy. It says the corpus is
portable while still near stronger AoA organs. It should not become route-away
or imported law unless direct bundle review finds actual ownership collapse.

## Decision Record Review

No ADR is needed from this feedback stage.

The only behavior change was a bounded generator bug fix with tests,
regenerated derived surfaces, and a repair-cohort review packet. Future agents
can understand the why from the repair packet and the regression test.

## Stop Lines

- Do not start mass old-template modernization from this feedback note.
- Do not add future topology axes to required frontmatter.
- Do not change tree paths.
- Do not turn watch labels into route-away decisions.
- Do not add a decision record unless a later stage changes schema, template
  requirements, path contracts, or generated-source authority.
