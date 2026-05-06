# One-Command Service Lifecycle Checklist

- [ ] One explicit operator-facing entrypoint starts the bounded local stack.
- [ ] The lifecycle entrypoint owns the dependent services instead of requiring several manual terminal commands.
- [ ] Prerequisite or build checks fail early or report the blocker clearly before startup continues.
- [ ] Startup output names what is running and how to stop it.
- [ ] Interrupt or a companion stop helper shuts down the started services together.
- [ ] Leftover child processes are treated as a lifecycle defect, not as normal operator cleanup.
- [ ] The technique stays local and bounded rather than drifting into deployment orchestration or platform-launcher doctrine.
- [ ] The technique does not drift into profile composition, rendered truth, or readiness verdict ownership.
- [ ] Logging extras, dashboard helpers, or integration side programs are not treated as the core contract.
- [ ] Project bootstrap or install flows remain separate from the lifecycle bundle.
