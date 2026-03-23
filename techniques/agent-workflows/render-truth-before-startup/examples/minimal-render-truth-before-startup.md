# Minimal Render Truth Before Startup

Use a layered runtime selection, but render what the engine actually resolves before launch.

```bash
stack-profile-modules --profile app --profile ops --paths
stack-profile-endpoints --profile app --profile ops
stack-render-services --profile app --profile ops
stack-render-config --profile app --profile ops --write /tmp/app-ops.rendered.yml
```

Review questions before startup:

- which services are actually present in the composed runtime view
- did the additive profile introduce the services you expected
- did any overlay or merged setting change the final result in a surprising way
- should the local rendered config file be deleted after inspection because it may contain sensitive values

Only after that review step:

```bash
stack-up --profile app --profile ops
```
