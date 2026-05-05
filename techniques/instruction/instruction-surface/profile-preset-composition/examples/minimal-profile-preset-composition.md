# Minimal Profile Preset Composition

## Layout

```text
compose/modules/10-core.yml
compose/modules/20-api.yml
compose/modules/50-observability.yml

compose/profiles/app.txt
compose/profiles/ops.txt

compose/presets/app-full.txt
```

## Profile Definitions

```text
# compose/profiles/app.txt
10-core.yml
20-api.yml
```

```text
# compose/profiles/ops.txt
50-observability.yml
```

## Preset Definition

```text
# compose/presets/app-full.txt
app
ops
```

## Inspection-First Use

```bash
stack-preset-profiles --preset app-full --paths
stack-profile-modules --preset app-full --paths
stack-profile-endpoints --preset app-full
```

## What The Contract Shows

- `app-full` expands to `app` and then `ops`
- the resolved module order becomes `10-core.yml`, `20-api.yml`, `50-observability.yml`
- if a direct `--profile debug` is added later, it should append after preset expansion rather than rewriting the preset
- duplicate profiles or modules should be kept only once, at first appearance
