# External Import Runbook

Use this runbook when a donor already looks like a bounded reusable technique candidate and the next question is how to move it from triage to merge without inventing a new local process each time.

See also:
- [Donor Refinery Rubric](../donor-refinery/README.md)
- [External Technique Candidates](../external-candidate-ledger/README.md)
- [Long-Gap Canon Design](../long-gap-reentry/README.md)
- [Contributing](../../../../CONTRIBUTING.md)
- [`templates/ORIGIN_EVIDENCE.template.md`](../../../../templates/ORIGIN_EVIDENCE.template.md)
- [`templates/ADAPTATION_NOTE.template.md`](../../../../templates/ADAPTATION_NOTE.template.md)
- [`templates/EXTERNAL_ORIGIN.template.md`](../../../../templates/EXTERNAL_ORIGIN.template.md)
- [`templates/EXTERNAL_REVIEW.template.md`](../../../../templates/EXTERNAL_REVIEW.template.md)
- [`external-import-review` issue template](../../../../.github/ISSUE_TEMPLATE/external-import-review.md)

## Preconditions

Open this runbook only when all of the following are already true:

- the donor exposes one bounded reusable pattern rather than a wider doctrine, runtime, or architecture package
- the pattern's canonical home should be `aoa-techniques`
- the public-safe extraction path is plausible
- the candidate is not blocked by an unresolved overlap with an existing technique
- the candidate can name one atomic move, likely `domain`, primary `kind`, and
  nearest relation or conflict points
- the candidate can name source owner or boundary, extraction route, and stop
  line without making OS Abyss a hidden dependency for portable use

If those checks still fail, stop and record the result in the candidate or review surface instead of drafting a bundle.

## Gate Packet

Every import entering this runbook must carry the Distillation gate packet from
the active ledger, donor refinery, or review surface.

Atom/Topology fields:

- `atomic_move_note`
- `atomic_move_status`
- likely `domain` and primary `kind`
- likely family or reason no stable family exists yet
- `capability_class`
- `substrate`
- `execution_profile`
- `risk_posture`
- nearest landed technique, alternative, or conflict point

Boundary/portability fields:

- `higher_law`
- `local_route`
- `bridge_stop_line`
- `portable_core`
- `aoa_only_context`
- donor exclusions

The runbook may refine wording, but it must not widen the packet. If drafting
requires a broader move, a different domain, a new owner, or a hidden OS Abyss
dependency, return the candidate to the ledger or incubation lane.

## Operator Path

1. Triage the donor.
   - name the reusable object being extracted
   - name the gate packet's atomic move and likely topology posture
   - name the nearest existing technique or overlap watch
   - name the source owner or boundary, extraction route, and stop line
   - state what stays out of the donor
2. Confirm canonical-home fit.
   - keep technique meaning here
   - route skills, eval doctrine, routing policy, role contracts, memory semantics, and private operations back to their owning layers
   - keep AoA-only integration detail out of the portable technique center
3. Draft the bundle.
   - create or update `TECHNIQUE.md`
   - add the smallest useful example, check, and note set
   - keep wording public-safe and reviewable
4. Draft provenance and review notes.
   - add any repo-local origin or adaptation note that the current maturity claim needs
   - add `notes/external-origin.md` from `templates/EXTERNAL_ORIGIN.template.md`
   - add or update any bundle-local evidence notes required for the current maturity target
   - name expected generated surfaces before opening the PR
5. Open the import review surface.
   - use the `external-import-review` issue template
   - record overlap check, donor exclusions, expected evidence notes, expected generated surfaces, and downstream repo impact
6. Validate the repo package.
   - follow [AGENTS](../../../../AGENTS.md#validation) and
     [RELEASING](../../../../docs/RELEASING.md)
   - fix source markdown first, then regenerate derived surfaces through the release path
7. Merge and restage.
   - if the import lands, update any affected candidate or audit docs
   - if the import does not land, record the blocker instead of widening the technique contract

## Expected Evidence Package

For a normal bounded external import, expect at least:

- one `TECHNIQUE.md`
- one `notes/external-origin.md`
- one example, checklist, or equivalent validation surface
- any generated surfaces that change because the bundle now exists

Do not add extra notes just to imitate a later canonical bundle. Add only what the current maturity claim needs.

## Required Intake Fields

For every import issue or PR, name these explicitly:

- nearest existing technique or overlap watch
- atomic move
- atomic move status
- likely `domain` and primary `kind`
- likely family or reason no family is stable yet
- capability class, substrate, execution profile, and risk posture
- boundary fields: `higher_law`, `local_route`, and `bridge_stop_line`
- standalone portability note, or `portable_core`, for readers outside OS Abyss
- `aoa_only_context` that must not become a hidden dependency
- what stays out of the donor
- expected evidence notes and note paths
- expected generated surfaces
- downstream repo impact

If one of those fields is unknown, stop and resolve it before merge.

## Stop Conditions

Do not merge the import if:

- the donor still overlaps an existing technique without a clean boundary
- the candidate is really a skill, eval, routing rule, role contract, or memory object
- the imported wording carries internal-only URLs, secrets, or project-only operational detail
- the proposed bundle needs schema growth, graph behavior, or a new domain just to stay coherent
- the candidate only works when the reader has the whole AoA or OS Abyss stack
  rather than one portable practice plus local context

## Hosting-Side Governance Checklist

These settings are external to the repo and may require admin access. Prepare them now even if they are applied later:

- protect `main`
- require pull requests before merge
- require the single status check emitted by the `Repo Validation` workflow
  after it is aligned to the root release lane
- disable force-push to `main`
- disable branch deletion for the protected branch

If admin access is unavailable, keep this checklist in the operator path and do not block repo-side hardening on it.
