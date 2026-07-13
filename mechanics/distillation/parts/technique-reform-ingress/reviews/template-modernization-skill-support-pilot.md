# Template Modernization Skill-Support Pilot

Source packet: [Technique Reform Ingress](../README.md)

Primary evidence:

- [Bundle Anatomy Template And Contract Feedback](bundle-anatomy-template-contract-feedback.md)
- [Bundle Anatomy Final Closeout Ledger](bundle-anatomy-final-closeout-ledger.md)
- [Owner-Boundary Bridge Long-Pass Closeout Ledger](owner-boundary-bridge-long-pass-closeout-ledger.md)
- [Selector Relation Wave B Instruction Knowledge Review](selector-relation-wave-b-instruction-knowledge-review.md)
- [Landed Skill-Support Pilot Review](landed-skill-support-pilot-review.md)
- [Template Modernization Optional Sections Decision](../../../../../docs/decisions/AOA-TECH-D-0044-template-modernization-optional-sections.md)

Status: bounded template-modernization pilot plus validator alignment,
source-shape repair over one shelf, not schema migration, not frontmatter
promotion, not path movement, not relation repair, not empirical small-agent
proof.

## Verdict

Accept `proof/skill-support` as the first template modernization pilot.

The pilot updates three canonical technique sources:

- `AOA-T-0015` `contract-test-design`
- `AOA-T-0016` `bounded-context-map`
- `AOA-T-0017` `property-invariants`

Each source now exposes the sections already named by the current template:

- `Atomic move`
- `Topology fit`
- `Small-agent execution shape`

No `id`, `status`, `domain`, `kind`, `relations`, path, support-file, example,
checklist, or template-contract change is accepted by this pilot.

The first rebuild found that `templates/TECHNIQUE.template.md` already names
these sections, while `scripts/validate_repo.py` still rejected them as
unexpected top-level sections. This pilot therefore accepts a bounded validator
alignment: the new template sections are optional in existing bundles, allowed
only once, and allowed only in their fixed template slots. They are not made
required across all `107` bundles.

## Why This Shelf

`proof/skill-support` is compact, canonical, recently reviewed, and close to
the active skill surface without becoming skill authority. The shelf also had
the right kind of old-template pressure: the executable center was present, but
the source shape made a small agent work too hard to isolate the one move, the
input packet, the expected output, and the stop-line.

This is why the pilot edits the bundle sources instead of changing
`templates/TECHNIQUE.template.md`. The template already names the desired
shape; the older leaves needed a local modernization pass.

## Direct-Read Outcomes

| bundle | existing executable center | modernization added | stop-line preserved |
|---|---|---|---|
| `AOA-T-0015` `contract-test-design` | make one consumer-visible boundary explicit through contract checks | names one boundary-to-contract-check atom, the scout topology fit, and the small-agent input/output packet | broad invariant coverage, hidden internal correctness, and eval-suite verdicts stay outside |
| `AOA-T-0016` `bounded-context-map` | name neighboring contexts, responsibilities, handoffs, and vocabulary | names one responsibility-area-to-context-map atom, the scout topology fit, and the small-agent input/output packet | generic architecture taxonomy, DDD formalism, and owner-authority decisions stay outside |
| `AOA-T-0017` `property-invariants` | express one stable truth as invariant-oriented checks | names one stable-rule-to-invariant-check atom, the scout topology fit, and the small-agent input/output packet | consumer-boundary contract design, vague random-data testing, and eval verdict authority stay outside |

## What Changed

The source edits are deliberately narrow:

- [AOA-T-0015 contract-test-design](../../../../../techniques/proof/skill-support/contract-test-design/TECHNIQUE.md)
- [AOA-T-0016 bounded-context-map](../../../../../techniques/proof/skill-support/bounded-context-map/TECHNIQUE.md)
- [AOA-T-0017 property-invariants](../../../../../techniques/proof/skill-support/property-invariants/TECHNIQUE.md)

Each changed file adds:

1. the atomic move as a single executable action;
2. a `Topology fit` note that keeps only `domain` and `kind` as current
   frontmatter truth while using scout axes as review notes;
3. a `Small-agent execution shape` block that names the context packet, output
   shape, and stopping boundary.

The validator edit is equally narrow:

- [validate_repo.py](../../../../../scripts/validate_repo.py) allows
  `Atomic move`, `Topology fit`, and `Small-agent execution shape` as optional
  template-modernization sections in fixed positions;
- [test_validate_repo.py](../../../../../tests/test_validate_repo.py) covers
  accepted optional-section order, rejected misplaced optional sections, and
  rejected duplicate optional sections.

## What Did Not Change

- no frontmatter mutation;
- no status or maturity promotion;
- no path movement;
- no relation source change;
- no template file change;
- no support-file rewrite;
- no global required-section migration;
- no full-corpus old-template rewrite;
- no generated hand edit;
- no sibling-skill acceptance claim;
- no empirical local-model pass/fail claim.

## Pilot Rhythm

Use this rhythm for the next template-modernization expansion:

1. Start from a small evidence-backed shelf, not from a global
   `old-template-watch` list.
2. Read each `TECHNIQUE.md` directly with its checklist, examples, generated
   capsule, and recent review packets.
3. Accept source-shape repair only when the current headings make the atomic
   move, input packet, output shape, or stop-line materially easier to execute.
4. Add `Atomic move`, `Topology fit`, and `Small-agent execution shape` without
   changing frontmatter unless a separate decision and validator wave exists.
5. Rebuild generated surfaces from source and validate; never hand-edit
   generated companions.
6. Stop after the chosen cohort and record whether the rhythm is ready for the
   full long pass.

## Next Clean Move

After this pilot is rebuilt and validated, start the template modernization
long pass using the same rhythm. Good first shelves should be selected from
direct evidence, not from symmetry alone. The first pressure points to inspect
inside the full pass are:

- `proof/evaluation-chain`, because it is proof-adjacent and close to
  skill-support without owning eval verdicts;
- `execution/ready-work-graphs`, because relation and small-agent selection
  pressure already found exact object boundaries there;
- `continuity/handoff-continuation`, because it has dense handoff leaves and
  already served as a selector and portability calibration shelf.

Do not start the long pass until the generated diff from this pilot is reviewed
as source-derived parity rather than noise.

## Validation Menu

Close this pilot with:

1. the diff hygiene check
2. public-safety grep over touched public-share surfaces
3. bridge-block grep over touched public-share surfaces
4. the targeted tests
5. the nested-agent check
6. repository validation
7. the release lane
