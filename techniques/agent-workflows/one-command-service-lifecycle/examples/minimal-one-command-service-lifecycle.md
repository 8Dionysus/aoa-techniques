# Minimal One-Command Service Lifecycle

Start a bounded local stack through one visible lifecycle entrypoint instead of asking the operator to coordinate several terminals.

```bash
dev-stack start --preset local-dev
```

Example result:

```text
checking prerequisites...
ok   runtime engine available
ok   selected preset local-dev
ok   context service built
starting bounded local stack...
running:
- core service
- context service
stop with Ctrl+C
```

After the operator interrupts the run:

```text
shutting down bounded local stack...
ok   core service stopped
ok   context service stopped
shutdown complete
```

The important behavior is lifecycle ownership:

- one visible entrypoint owns startup for the bounded local stack
- the operator does not need a second terminal just to launch dependent services
- startup output says what is now running and how to stop it
- shutdown is part of the same contract, not a separate cleanup ritual
- render review and readiness checks should already have happened through sibling techniques before this lifecycle step starts
