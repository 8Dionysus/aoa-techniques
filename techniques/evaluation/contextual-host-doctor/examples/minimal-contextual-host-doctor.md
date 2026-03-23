# Minimal Contextual Host Doctor

Run a pre-start readiness check against the selected runtime rather than against one generic host checklist.

```bash
stack-doctor --preset accel-full
```

Example result:

```text
ok   platform linux
ok   cmd  container-engine
ok   compose backend available
warn gpu device missing for selected accelerated runtime
warn internal-only layers selected; run deeper internal checks after startup
doctor check passed
warnings: 2
```

The important behavior is contextual:

- the GPU-device warning matters because the selected runtime includes acceleration
- the internal-only reminder matters because the selected runtime includes layers that need deeper post-start checks
- a different preset without acceleration should not raise the same hardware warning
- this verdict helps decide whether startup is sensible, but it does not replace render review or smoke checks
