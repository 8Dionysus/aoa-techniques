# Canonical Readiness

## Technique

- id: AOA-T-0038
- name: one-command-service-lifecycle

## Verdict

- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around memory semantics, logging and OAuth side programs, global install behavior, and broader launcher doctrine
- exact-fit second context: Metaflow Devstack exposes `make up`, `make all-up`, service subset startup, `make shell`, and `make down` as a real local-stack lifecycle surface over Minikube and Tilt
- external review: the first import review passed, and the new Metaflow pass confirms the lifecycle contract survives outside the donor repo without importing deployment, platform, render, readiness, or benchmark authority
- validation strength: the bundle now carries one checklist, one example, donor evidence, exact-fit public second-context evidence, and an adverse-effects review

## Default-use rationale

- this is the right canonical default when the main reusable object is one explicit lifecycle entrypoint for a bounded local multi-service stack
- it remains distinct from `AOA-T-0036`, which stays centered on pre-start rendered runtime truth rather than on startup and shutdown ownership
- it remains distinct from `AOA-T-0037`, which stays centered on selector-aware readiness verdicts rather than on launch control
- it remains distinct from `AOA-T-0039`, which compares benchmark profiles rather than owning the local service lifecycle
- Metaflow confirms that the default move can survive outside the donor stack even when the implementation substrate changes from Node scripts to Make, Minikube, Tilt, service selection, wait paths, and teardown targets

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable local-lifecycle contract and excludes donor-specific ports, paths, integration surfaces, and memory breadth
- public reuse check: the example, checklist, adaptation notes, and Metaflow evidence remain understandable without hidden donor-repo context
- public-safety boundary: Metaflow service names are cited only as evidence of bounded-stack lifecycle ownership, not as universal required services or Kubernetes doctrine

## Remaining gaps

- no blocking promotion gap remains as long as the bundle stays centered on local lifecycle ownership with visible startup, status/follow-through, and teardown
- future review should reject surfaces that are only generic launchers, install wizards, remote deployment workflows, readiness checks, render previews, smoke checks, or benchmark harnesses without the same local stack lifecycle seam

## Recommendation

- promote `AOA-T-0038` to `canonical`
- use `AOA-T-0038` as the default local-stack lifecycle technique when one explicit operator-facing entrypoint should start and stop a bounded local stack while sibling techniques own composition, render truth, readiness, smoke, benchmark comparison, and deployment concerns
