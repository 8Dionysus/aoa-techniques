# Concrete Capability Upgrade With Compat Window

Scenario: a repository exposes a `render_release_report` capability to several agent-facing surfaces.

1. Keep one capability spec as the source of truth.
2. Version the contract from `2.0.0` to `2.1.0` when a new optional `include_warnings` input is added.
3. Write a short compatibility note saying existing consumers can stay on the old call shape during one review window.
4. Update providers only after the spec change is reviewed.
5. Keep orchestration, provider registration, and routing policy outside the capability spec.

This keeps the capability boundary explicit instead of burying contract change inside provider code or runtime glue.
