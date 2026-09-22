# Structural AGENTS Route Guard Boundary

Status: accepted
Date: 2026-09-22

## Index Metadata

- Decision ID: AOA-TECH-D-0078
- Original date: 2026-09-22
- Surface classes: agent route, validation guard
- Technique axes: agent mesh, topology
- Mechanic parents: none
- Guard families: AGENTS/mesh, release/tooling
- Posture: accepted structural route-card validator boundary

## Context

`scripts/validate_semantic_agents.py` was checking exact prose fragments in a
small set of `AGENTS.md` cards. Those fragments had no production consumer
beyond that script; the focused test only mirrored them into fixtures. The
canonical machine contract is the AGENTS mesh configuration and the shared
`agents_mesh_common.active_card_route_issues` helper. Exact prose matching
rejected harmless wording changes such as a safe paraphrase of a public-safety
reminder while still being unable to prove the meaning of arbitrary prose.

The repository already has stronger owners for canonical card shape, route
handles, command authority, and public hygiene. This change needs a durable
boundary so a future validator extension does not turn editorial wording into
an automatic semantic or security verdict.

## Options considered

1. Keep the exact prose snippets as blocking assertions. This preserves the
   false-negative behavior and creates false assurance that keyword presence
   proves meaning.
2. Strip HTML comments before checking the snippets. This only changes where
   literal text may appear and does not make safe paraphrases pass.
3. Remove the selected-card validator entirely. This loses its declared
   selected-path and missing-document coverage.
4. Keep the selected paths and missing-document check, but delegate structural
   route validation to the canonical AGENTS mesh helper and leave prose meaning
   to owner review. **Chosen.**

## Decision

The selected AGENTS route guard checks only its declared card paths, the
`# AGENTS.md` header, and the existing canonical route-card helper. Route
semantics remain the responsibility of
`agents_mesh_common.active_card_route_issues`, including the Validation
section, `VALIDATION.md`, `config/validation_lanes.json`, and applicable lane
requirements.

`validate_semantic_agents.py` keeps its script name, public `validate` entry
point, `AgentsDocSpec` shape, selected paths, and source-fast lane placement
for compatibility. Its route metadata no longer asserts editorial phrases.
Prose meaning, public-safety interpretation, and owner acceptance remain
review or public-hygiene concerns; this guard does not claim to prove them.

## Rationale

The canonical helper already owns the route grammar and is shared by the mesh
shape validator. Reusing it gives this focused selected-path check the same
route semantics without creating a second Markdown parser or another keyword
policy. Keeping the selected paths retains the existing missing-document
failure boundary, while removing prose anchors lets safe rewrites survive.

## Consequences

- Safe paraphrases of card prose no longer fail this guard.
- Missing selected cards and broken canonical validation routes still fail.
- A green result proves structural route-card completeness only; it does not
  prove semantic meaning, absence of secrets, security, or owner acceptance.
- Future route changes must update the shared mesh helper and its owner tests,
  not add a new list of prose keywords here.

## Source surfaces

- `scripts/validate_semantic_agents.py`
- `scripts/agents_mesh_common.py`
- `scripts/validate_agents_md_shape.py`
- `scripts/validate_agents_mesh.py`
- `tests/test_validate_semantic_agents.py`
- `tests/test_docs_surface_guardrails.py`
- `docs/validation/script_inventory.json`
- `docs/testing/test_inventory.json`
- `config/agents_mesh.json`
- `config/validation_lanes.json`
- `docs/guardrails/AGENTS_MESH_PROTOCOL.md`
- `VALIDATION.md`
- `docs/decisions/AOA-TECH-D-0045-agent-surface-design-and-mesh.md`
- `docs/decisions/AOA-TECH-D-0060-agents-mesh-canonical-closure.md`
- `docs/decisions/AOA-TECH-D-0066-validation-lane-command-authority.md`
- `docs/decisions/AOA-TECH-D-0076-prompt-light-agent-routes-and-on-demand-validation.md`

## Follow-up route

Keep prose and public-safety claims with the owning card review and
`public_hygiene` validators. If the canonical AGENTS route grammar changes,
update `agents_mesh_common`, its focused tests, and this decision's affected
source route together. Do not widen this guard into semantic keyword matching,
secret detection, or an independent route registry.

## Verification

Use the `source-fast` lane, the focused semantic-agent and docs-surface tests,
the nearest `scripts/` and `tests/` owner checks, and generated decision-index
parity. These checks prove the local structural contract only; they do not
claim full release, KAG, CI, review, merge, runtime, or owner acceptance.
