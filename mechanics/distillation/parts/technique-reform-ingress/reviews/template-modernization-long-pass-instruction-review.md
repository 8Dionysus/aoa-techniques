# Template Modernization Long-Pass Instruction Review

Status: closed Phase 5 instruction-trunk review.

This packet covers all `19` instruction-trunk bundles. It accepts no source
repair.

## Evidence Read

- `techniques/instruction/AGENTS.md`
- all instruction-trunk `TECHNIQUE.md` sources
- instruction-trunk checklists, examples, and note skeletons
- direct-read migration reviews for `docs-boundary`, `instruction-surface`,
  `capability-boundary`, `capability-registry`, and `skill-discovery`
- selector/relation, portability, owner-boundary, bundle-anatomy, and
  execution-profile packets touching instruction surfaces

## Verdict

Instruction bundles are already source-truth and capability-boundary heavy, but
their current source shape keeps authored source, generated targets, capability
specs, registry entries, command boundaries, and skill discovery objects
separate. Optional sections would be useful only where a future bundle-specific
defect hides an atom. No such defect appeared in this pass.

## Bundle Rows

| id | shelf | bundle | verdict | reason |
|---|---|---|---|---|
| AOA-T-0002 | `instruction/docs-boundary` | `source-of-truth-layout` | held-no-repair | document role separation is already canonical and explicit |
| AOA-T-0009 | `instruction/docs-boundary` | `lightweight-status-snapshot` | held-no-repair | status snapshot atom is clear and compact |
| AOA-T-0033 | `instruction/docs-boundary` | `decision-rationale-recording` | held-no-repair | decision note shape is already bounded |
| AOA-T-0034 | `instruction/docs-boundary` | `public-safe-artifact-sanitization` | held-no-repair | sanitization move is explicit without approval-gate import |
| AOA-T-0012 | `instruction/instruction-surface` | `deterministic-context-composition` | held-no-repair | deterministic composition atom is clear from source and examples |
| AOA-T-0013 | `instruction/instruction-surface` | `single-source-rule-distribution` | held-no-repair | single-source distribution already names authority and target split |
| AOA-T-0024 | `instruction/instruction-surface` | `upstream-mirroring-with-provenance` | held-no-repair | mirror-with-provenance stop-line is explicit |
| AOA-T-0027 | `instruction/instruction-surface` | `cross-agent-skill-propagation` | held-no-repair | propagation source/target boundary is already visible |
| AOA-T-0029 | `instruction/instruction-surface` | `nested-rule-loading` | held-no-repair | nested precedence atom is explicit |
| AOA-T-0030 | `instruction/instruction-surface` | `fragmented-agent-context` | held-no-repair | fragment-before-assembly object is clear |
| AOA-T-0035 | `instruction/instruction-surface` | `profile-preset-composition` | held-no-repair | preset composition is bounded against launcher doctrine |
| AOA-T-0040 | `instruction/capability-boundary` | `skill-vs-command-boundary` | held-no-repair | skill/command split is already the atom |
| AOA-T-0043 | `instruction/capability-boundary` | `multi-source-primary-input-provenance` | held-no-repair | primary/supporting source priority is explicit |
| AOA-T-0093 | `instruction/capability-boundary` | `recommendation-truth-vs-host-actionability` | held-no-repair | recommendation/actionability split is clear and current |
| AOA-T-0025 | `instruction/capability-registry` | `capability-spec-versioning` | held-no-repair | versioned spec artifact shape is already bounded |
| AOA-T-0063 | `instruction/capability-registry` | `versioned-agent-registry-contract` | held-no-repair | registry record contract is visible without product-policy import |
| AOA-T-0064 | `instruction/capability-registry` | `capability-discovery` | held-no-repair | query-over-entries discovery is explicit |
| AOA-T-0041 | `instruction/skill-discovery` | `skill-marketplace-curation` | held-no-repair | curated discoverability layer is already bounded against marketplace ownership |
| AOA-T-0042 | `instruction/skill-discovery` | `upstream-skill-health-checking` | held-no-repair | health-checking surface is explicit without generic monitoring doctrine |

## Phase Counts

| class | count |
|---|---:|
| bundles reviewed | 19 |
| long-pass source repairs | 0 |
| held-no-repair | 19 |
| route-to-other-lane | 0 |

## Next

Proceed to knowledge, history, ingest, and tool-use. Keep future instruction
repairs bundle-local rather than schema-wide.
