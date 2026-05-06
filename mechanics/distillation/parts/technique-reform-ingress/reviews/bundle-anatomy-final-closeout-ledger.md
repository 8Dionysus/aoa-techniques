# Bundle Anatomy Final Closeout Ledger

Source packet: [Technique Reform Ingress](../README.md)

Status: final closeout ledger for the post-tree bundle anatomy reform pass.

## Verdict

Close the first full post-tree technique bundle reform pass.

The pass audited all `107` authored technique bundles after the tree migration,
validated the corpus as healthy enough for the next reform direction, repaired
the only generated-reader defect found by the audit, and refused broad churn
where the evidence did not justify it.

Final state:

- `107` authored technique bundles.
- `10` active bundle trunks with techniques.
- `28` active shelves with techniques.
- `25` canonical bundles and `82` promoted bundles.
- `107/107` generated catalog and capsule presence.
- `107/107` examples, checks, and notes present.
- `105/107` bundles needed no repair in this pass.
- `2/107` capsule gaps were repaired through the builder.
- `0/107` route-away, split, merge, deprecation, path movement, frontmatter
  migration, or status promotion actions remain open from this pass.

Retained frontmatter-lane route directories `agent-workflows`, `docs`, and
`evaluation` still exist under `techniques/`, but they carry no active bundle
leaves. Active bundle paths are under the `10` generated/catalogued trunks.

## Landed Packets

| packet | result |
|---|---|
| [Bundle Anatomy Baseline Inventory](bundle-anatomy-baseline-inventory.md) | counted all bundles, paths, generated presence, examples, checks, and notes |
| [Bundle Anatomy Rubric Hardening](bundle-anatomy-rubric-hardening.md) | turned the audit into repeatable labels and repair-action posture |
| [Bundle Anatomy Wave A Review](bundle-anatomy-wave-a-review.md) | audited execution and instruction shelves |
| [Bundle Anatomy Wave B Review](bundle-anatomy-wave-b-review.md) | audited proof, continuity, and governance shelves |
| [Bundle Anatomy Wave C Review](bundle-anatomy-wave-c-review.md) | audited knowledge-lift, ingest, history, recovery, and tool-use shelves |
| [Bundle Anatomy Corpus Synthesis](bundle-anatomy-corpus-synthesis.md) | synthesized all `107` rows and chose the first repair cohort |
| [Bundle Anatomy Capsule Gap Repair Cohort](bundle-anatomy-capsule-gap-repair-cohort.md) | repaired wrapped Markdown list extraction for generated capsules |
| [Bundle Anatomy Template And Contract Feedback](bundle-anatomy-template-contract-feedback.md) | recorded that no template, Atom, Topology, Tree, or ADR change was needed |
| [Bundle Anatomy Post-Repair Follow-Through](bundle-anatomy-post-repair-follow-through.md) | closed repair waves, topology scout, capsule, promotion, and route-away gates |
| [Bundle Anatomy Legacy And Provenance Hygiene](bundle-anatomy-legacy-provenance-hygiene.md) | confirmed no new legacy receipt or mechanic-local legacy update was needed |

## Repair Closed

The audit found two concrete generated-reader failures:

- `AOA-T-0095` capsule validation shortened a wrapped bullet into `before the;`.
- `AOA-T-0096` capsule risk ended at `older or.`

The source techniques were coherent. The defect was in capsule extraction:
wrapped Markdown list items were not preserving indented continuation lines.

The landed repair changed builder behavior, added regression coverage,
documented capsule extraction expectations, and regenerated capsule reader
surfaces. The repair affected `11` generated entries where wrapped sentence
tails had previously been dropped.

No generated file was hand-edited. No technique source was changed for cosmetic
reader reasons.

## No-Change Decisions

These were reviewed and intentionally left unchanged:

- no path movement
- no `tree_path` frontmatter
- no `family`, `capability_class`, `substrate`, `execution_profile`, or
  `risk_posture` frontmatter promotion
- no `domain` or `kind` remap
- no old-template mass rewrite
- no bundle status promotion
- no route-away handoff
- no new root legacy receipt
- no new mechanic-local legacy receipt
- no ADR
- no root Questbook update

`ROADMAP.md` is updated by this closeout because repo-level direction moved:
the next honest move is no longer "start bundle anatomy audit"; it is to choose
the next bounded reform slice from this closed evidence.

## Next Direction

The next clean direction is targeted reform, not corpus churn.

Good candidate lanes:

- choose one concrete technique-bundle reform slice from direct evidence;
- improve a bundle-local template shape only when a target bundle already
  needs nearby work;
- prepare future topology or generated selector work only through a separate
  decision, builder, and validator wave;
- keep generated capsules and compact cards tuned for small-agent execution
  after orchestration has selected the technique and packed context.

Do not turn `old-template-watch`, `owner-boundary-watch`,
`promotion-evidence-hold`, or `portability-watch` into automatic work queues.
They are review pressure, not authority.

## Validation

Final closeout validation:

1. `python scripts/release_check.py`
2. `python scripts/validate_repo.py`

The temporary rhythm plan was distilled into this ledger and removed from the
working tree. It was local scratch, not source truth.
