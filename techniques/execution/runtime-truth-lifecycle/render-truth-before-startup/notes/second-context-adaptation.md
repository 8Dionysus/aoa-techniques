# Second Context Adaptation

## Technique
- id: AOA-T-0036
- name: render-truth-before-startup

## Target project
- name: Dockform
- environment: public Docker Compose management tool for declarative stacks, multi-context Compose projects, SOPS-backed secrets, and plan/apply operation
- runtime: local operator workflow that previews desired changes, renders fully resolved Compose config for a stack, then applies the prebuilt plan to Docker Compose

## What changed
- the donor's `abyss-stack` render commands become Dockform's public `dockform plan`, `dockform compose render`, and `dockform apply` surfaces
- the donor's selected profile/preset becomes Dockform's discovered or declared `context/stack` plus Compose profiles, environment files, inline environment, and SOPS-backed secrets
- the donor's lightweight service-list render maps to Dockform plan state and service detection over `docker compose config --services` plus config hashes
- the donor's deeper full-config render maps to `dockform compose render`, which renders the fully resolved Docker Compose config and masks secrets by default
- the donor's startup handoff maps to Dockform `apply`, which builds the plan, shows it, asks for confirmation unless explicitly skipped, then applies the same prebuilt plan through Docker Compose

## What stayed invariant
- the review surface still happens before the stack is applied or started
- the reviewed view still comes from resolved Docker Compose truth rather than only manifest narration
- service-level inspection remains the lighter pass and fully rendered config remains the deeper local pass
- full rendered config remains sensitive enough to need masking and local handling
- startup, readiness, and lifecycle control remain outside the render-review atom

## Risks introduced by adaptation
- Dockform is a broader declarative management tool, so the technique must not absorb volume, secret, dashboard, image-upgrade, prune, or multi-host deployment ownership
- Dockform's `plan` and `compose render` are separate commands, so the reusable evidence is the bounded plan/render-before-apply seam rather than one mandatory command name
- Docker Compose `config`, `--dry-run`, Helm `template`, Kustomize, or Skaffold render remain adjacent unless a source also preserves an explicit operator review seam before startup or apply

## Evidence
- Dockform public docs describe it as a declarative Docker Compose workflow over stacks, supporting discovery, profiles, environment, secrets, and multi-context operation.
- Dockform `dockform plan` is a read-only preview surface for the desired state before `dockform apply`.
- Dockform stack docs say plan/apply analyze planned services with `docker compose config --services`, running services with `docker compose ps`, and config drift with `docker compose config --hash`.
- Dockform `dockform compose render` renders a stack's fully resolved Docker Compose config and exposes masking controls, with `--show-secrets` explicitly marked dangerous.
- Dockform source confirms `apply` builds and prints a plan, requires confirmation unless `--skip-confirmation` is passed, then applies the same prebuilt plan; Docker Compose `up -d` is the later handoff, not the review step.
- Docker's own Compose docs support the substrate: `docker compose config` renders the actual data model to be applied to Docker Engine, while `docker compose --dry-run up` is still adjacent because it simulates command steps rather than owning the reviewable rendered-truth seam by itself.

## Result
- verdict: exact-fit second context
- note: Dockform proves the same reusable move outside the donor lineage: render or preview resolved runtime truth before starting or applying a Compose stack, keep sensitive full config local or masked, and hand off to startup only after the reviewed plan/render seam
