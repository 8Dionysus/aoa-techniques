# Minimal Isolated Service Stop

This example shows a bounded helper-service closeout where one service should stop while the shared substrate remains available for later checks.

## Situation

- Target service: `route-helper`
- Shared substrate that should remain alive: `postgres`, `redis`, `graph-store`
- Reason: the helper lane is closing, but later validation still needs the shared substrate

## Bounded stop

1. Name `route-helper` as the only target that should stop.
2. Name `postgres`, `redis`, and `graph-store` as the services that should remain alive.
3. Stop only `route-helper` with the narrowest runtime handle available.
4. Check that `route-helper` no longer answers on its health seam.
5. Check that `postgres`, `redis`, and `graph-store` still answer their continuity probes.
6. Record that the helper lane is closed and that broader rollback is not currently required.

## Anti-Drift Rule

If the shared substrate also needs to stop, this is no longer an isolated-service stop.
If the target cannot be named precisely, the route is still too vague for this technique.
