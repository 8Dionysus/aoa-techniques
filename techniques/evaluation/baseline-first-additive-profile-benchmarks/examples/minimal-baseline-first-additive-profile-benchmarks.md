# Minimal Baseline First Additive Profile Benchmarks

Run one stable baseline profile first, then run the additive profile against the same summary shape.

```bash
bench-suite --profile baseline_first --summary-json runs/baseline/summary.json
bench-suite --profile additive --summary-json runs/additive/summary.json
```

Example comparison:

```text
baseline:  profile=baseline_first  surface=local  status=ok
additive:  profile=additive        surface=local  status=ok
shape:     summary schema matched for both runs
delta:     additive profile remained comparable on the same measurement surface
```

The important behavior is the ordering and the shape:

- baseline first
- same measurement surface
- same artifact shape
- additive setup stays separate from the default path
- the report stays about comparison, not about ranking
