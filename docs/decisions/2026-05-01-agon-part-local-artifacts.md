# Move Agon Technical Artifacts Into Part-Local Homes

Status: accepted
Date: 2026-05-01

## Context

After the active/legacy Agon split, current behavior lived in
`mechanics/agon/parts/`, but its seeds, generated indexes, schemas, examples,
scripts, tests, and recurrence manifests still lived in root technical
districts. That preserved old paths but kept the live Agon mechanic split across
two authority shapes: active part docs in the mechanic package, and technical
artifacts in repo-wide folders.

The AoA mechanics pattern is stricter: legacy preserves source growth, while
active mechanics own the current surfaces that grow from it. If Agon is the
first one-mechanic pass for `aoa-techniques`, its current candidate artifacts
should sit beside the part that owns their meaning.

## Options

- Keep root `config/`, `generated/`, `schemas/`, `examples/`, `scripts/`,
  `tests/`, and recurrence manifests as the permanent home for Agon artifacts.
- Move only generated outputs under `mechanics/agon/` and leave builders,
  validators, and tests in root helper folders.
- Move each Agon-owned artifact family into the nearest active part and update
  commands, tests, manifests, and entrypoint docs in one checked pass.

## Decision

Move Agon-owned technical artifacts into part-local homes:

- Wave IV binding artifacts live under
  `mechanics/agon/parts/move-technique-bridge/`.
- Wave XV epistemic candidate artifacts live under
  `mechanics/agon/parts/epistemic-technique-candidates/`.
- Agon recurrence manifests live under
  `mechanics/agon/parts/recurrence-adapter/`.

Root technical districts remain for repo-wide surfaces. Mechanic-owned
generated outputs stay with the mechanic part that owns the candidate meaning.

## Consequences

- Agon validation commands are longer, but they now name the owning part
  explicitly.
- Legacy raw wave receipts remain unchanged as preserved evidence, even when
  they mention old paths.
- Future Agon candidate families should land in a part-local artifact topology
  unless they are genuinely repo-wide.
- Release and roadmap parity checks must look for the part-local artifacts, not
  root Agon artifacts.
