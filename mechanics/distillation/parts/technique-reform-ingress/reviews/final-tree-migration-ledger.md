# Final Tree Migration Ledger

Source packet:
[Technique Reform Ingress](../README.md)

Closeout basis:
[Whole-Tree Closeout Review](whole-tree-closeout-review.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Generated lens:
[Technique Tree Projection](../reports/technique_tree_projection.md)

Root legacy index:
[Root Legacy Index](../../../../../legacy/INDEX.md)

Status: final-ledger-validated, generated-parity-clean, receipts-complete,
temporary-plan-distilled, ready-for-technique-bundle-reform, not path
movement, not `tree_path` frontmatter.

## Verdict

Close the first technique-tree migration program.

The current corpus has `107` authored technique bundles under
`techniques/<trunk>/<shelf>/<slug>/`, across `10` trunks and `28` shelves.
Every current path matches its generated projection path, every shelf has a
root legacy tree-pilot receipt, and no split, singleton, or unassigned hold
row remains.

This ledger does not move another bundle, add frontmatter, promote `family`,
change `domain` or `kind`, or make generated projections source truth. It
distills the temporary migration plan into permanent route surfaces and leaves
the next work to technique-bundle reform rather than more path migration.

## Final Counts

| check | result |
|---|---:|
| authored technique bundles | `107` |
| current trunks | `10` |
| current shelves | `28` |
| root legacy tree-pilot receipts | `28` |
| shelves with matching receipt | `28/28` |
| current path equals projected path | `107/107` |
| direct `techniques/<domain>/<slug>/TECHNIQUE.md` leaves | `0` |
| `split-review-needed` projection rows | `0` |
| `singleton-hold` projection rows | `0` |
| `unassigned-hold` projection rows | `0` |

## Receipt Coverage

| trunk | shelves | bundles | receipt coverage |
|---|---:|---:|---:|
| `continuity` | `3` | `14` | `3/3` |
| `execution` | `4` | `14` | `4/4` |
| `governance` | `5` | `14` | `5/5` |
| `history` | `1` | `6` | `1/1` |
| `ingest` | `1` | `5` | `1/1` |
| `instruction` | `5` | `19` | `5/5` |
| `knowledge-lift` | `1` | `8` | `1/1` |
| `proof` | `5` | `18` | `5/5` |
| `recovery` | `2` | `8` | `2/2` |
| `tool-use` | `1` | `1` | `1/1` |

Receipt matching is by projected shelf name to
`legacy/receipts/*-<shelf>-tree-pilot.md`, because early tree pilots landed
on `2026-05-04` and later pilots landed on `2026-05-05`.

## Generated Parity

The final pass rebuilt and validated generated reader and report surfaces with
`python scripts/release_check.py`.

The release check rebuilt catalogs, capsules, section/checklist/example/evidence
surfaces, semantic and shadow manifests, topology scout, tree projection, KAG
export, and repo-doc surfaces, then ran the full unittest suite, nested AGENTS
validation, and repository validation.

No generated output became authority. Generated surfaces remain evidence and
reader projections below authored bundle meaning, route cards, contracts, and
review packets.

## Temporary Plan Disposition

The tree-migration temporary plan was a working scratch file, not a canonical
contract, generated output, or migration receipt.

Its durable content is now distilled into:

- this final ledger
- [Whole-Tree Closeout Review](whole-tree-closeout-review.md)
- [Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)
- [Distillation Landing Log](../../../LANDING_LOG.md)
- [Distillation Roadmap](../../../ROADMAP.md)
- [Root Roadmap](../../../../../ROADMAP.md)

After this ledger lands, the scratch file should remain uncommitted and may be
deleted locally. Future agents should not treat it as source truth.

## Next Reform Direction

Start technique-bundle reform from the current tree.

The next program should begin with a corpus-wide bundle anatomy and small-agent
usability audit before changing individual techniques. Use
[Technique Atom Contract](../../../../../docs/TECHNIQUE_ATOM_CONTRACT.md),
[Technique Topology Contract](../../../../../docs/TECHNIQUE_TOPOLOGY_CONTRACT.md),
and [Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)
as the entry contracts.

The first slice should inspect bundle structure, template fitness, examples,
checks, adaptation notes, and capsule readability. It should not move paths,
promote new required frontmatter axes, or collapse `domain`, `kind`, family,
capability, substrate, execution profile, and risk posture into one selector.

## Stop Lines

- Do not reopen tree migration without a new projection-first review.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter from this ledger.
- Do not change `domain`, `kind`, ID, status, maturity, evidence, relation
  metadata, examples, checks, or notes from this ledger.
- Do not treat the temporary plan as a source artifact after this closeout.
- Do not begin leaf rewrites before the next bundle-reform ingress names its
  audit scope and verification path.
