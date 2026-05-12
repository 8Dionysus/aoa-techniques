# Second Context Adaptation

## Technique

- id: AOA-T-0038
- name: one-command-service-lifecycle

## Target project

- name: Metaflow Devstack
- environment: public local Kubernetes development stack for Metaflow, built around Minikube and Tilt
- runtime: operator-facing `make` lifecycle targets under `devtools/` for selecting, starting, waiting on, entering, and tearing down a bounded local service stack

## What changed

- paths: the donor `npm start` and companion stop helpers map to Metaflow's `make up`, `make all-up`, `make shell`, and `make down` lifecycle targets
- services: donor-specific memory and desktop-integration breadth maps to Metaflow's selectable local stack services such as MinIO, PostgreSQL, metadata service, UI, localbatch, Argo, Airflow, and cloud emulators
- dependencies: the invariant is not one process manager; Metaflow uses Make, Minikube, Tilt, Helm, and a service picker while preserving one operator-facing lifecycle surface
- operating assumptions: this proves the technique as local lifecycle ownership, not as generic project bootstrap, installer doctrine, fleet deployment, or readiness proof

## What stayed invariant

- contract: one explicit operator-facing entrypoint owns local stack startup
- validation logic: the entrypoint checks prerequisites, installs local tools as needed, selects or accepts services, starts the stack, and exposes a follow-up shell/wait path
- safety rules: shutdown remains part of the contract through `make down`, Tilt teardown, Minikube cleanup, tunnel process cleanup, and generated-file cleanup

## Risks introduced by adaptation

- Metaflow Devstack is larger than the donor stack, so the technique must not absorb Kubernetes platform doctrine, CI UX tests, cloud emulator semantics, or deployment ownership
- `make up` installs some local tooling on first run, so the transferable evidence is lifecycle ownership of a bounded local stack, not install-wizard breadth
- `make shell` waits for readiness before opening a configured shell, so later reuse must keep readiness and shell-entry support subordinate to the lifecycle seam

## Evidence

- Metaflow `devtools/README.md` documents `make up` as an interactive service picker that starts the stack, `make all-up` as the all-services entrypoint, `SERVICES_OVERRIDE=... make up` as bounded subset startup, `make shell` as the configured development shell, and `make down` as teardown.
- Metaflow `devtools/README.md` names the bounded service set and says service dependencies are resolved automatically.
- Metaflow `devtools/Makefile` implements `up` with Docker checks, local tool setup, service selection or override, Minikube tunnel startup, Tilt startup, visible next steps, and a generated `start.sh` with traps.
- Metaflow `devtools/Makefile` implements `down` by stopping all services, killing the Minikube tunnel, tearing down Minikube, removing Tilt, and cleaning generated `.devtools` scripts.
- Metaflow `devtools/ci/start-devstack.sh` provides a CI/local non-TUI lifecycle path that starts Tilt, waits for the API server, waits for the Tiltfile, and waits for the devstack services to become ready.

## Result

- verdict: exact-fit second context
- note: Metaflow proves the same reusable move outside the donor lineage: one explicit local lifecycle surface owns a selectable bounded stack, resolves dependent services, provides visible operator follow-through, and owns teardown without becoming render truth, host doctor, benchmark, or deployment authority
