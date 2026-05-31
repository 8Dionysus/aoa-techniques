# Mechanic Contract Packet Homes

Status: accepted

Date: 2026-05-14

## Index Metadata

- Decision ID: AOA-TECH-D-0047
- Original date: 2026-05-14
- Surface classes: mechanic package, mechanic part
- Technique axes: mechanic bridge
- Mechanic parents: none
- Guard families: mechanic topology, part-local artifact
- Posture: accepted

## Context

The root `schemas/` and `examples/` directories still carried JSON
schema/example pairs that described one mechanic part rather than a repo-wide
contract:

- Experience appeal, governance-precedent, sealed-decision, scope-boundary,
  handoff-compression, and service-clarity packets
- Method-growth adoption, handoff, retention, and obsolescence packets
- Release-support installation and sovereign-release packets

Root `schemas/` and `examples/` are valid districts, but their durable role is
repo-wide contracts, shared export shapes, and public examples. A contract that
only one mechanic part can interpret belongs beside that part.

## Decision

Move mechanic-local schema/example packets to owning part homes:

- `mechanics/experience/parts/<part>/{schemas,examples}/`
- `mechanics/method-growth/parts/<part>/{schemas,examples}/`
- `mechanics/release-support/parts/<part>/{schemas,examples}/`

Replace the old internal local-host JSON `$id` values with public part-local
schema URLs under
`https://github.com/8Dionysus/aoa-techniques/mechanics/...`. In this pass the
repository home and public identifier changed, but the contract fields and
example semantics did not. Contract tests now load the packets from their
part-local paths, and topology tests assert that the old root paths stay absent.

Root `schemas/` remains the home for repo-wide schemas such as technique,
quest, evidence, relation, index, dispatch, and catalog contracts. Root
`examples/` remains available for repo-wide or public-entry examples, but not
mechanic-local schema/example pairs.

## Consequences

- Part owners carry their own machine contracts and examples.
- Future mechanic-local contract packets should be added under the owning part,
  not under root `schemas/` or `examples/`.
- Internal-host JSON identifiers must not travel into public part-local
  surfaces. Future identifier changes need an explicit contract decision.
- Root cleanup becomes easier to audit because repo-wide contract districts no
  longer hide part-local mechanics material.

## Verification

```bash
python -m unittest tests.test_experience_adoption_contracts tests.test_experience_governance_contracts tests.test_experience_release_contracts
python -m unittest tests.test_experience_mechanics_topology tests.test_method_growth_mechanics_topology tests.test_release_support_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
```
