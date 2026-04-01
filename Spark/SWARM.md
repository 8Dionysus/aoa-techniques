# Spark Swarm Recipe — aoa-techniques

Рекомендуемый путь назначения: `Spark/SWARM.md`

## Для чего этот рой
Используй Spark здесь для одного technique seam: refinement существующей техники, sanitization donor -> technique, notes/adaptation tightening, bounded release-prep check. Это canon reusable practice, а не свалка snippets и project hacks.

## Читать перед стартом
- `README.md`
- `docs/START_HERE.md`
- `TECHNIQUE_INDEX.md`
- `WALKTHROUGH.md`
- `CONTRIBUTING.md`

## Форма роя
- **Coordinator**: выбирает одну технику или один donor seam
- **Scout**: картографирует origin, boundaries, adaptation notes, maturity и validation needs
- **Builder**: делает минимальный technique-level diff
- **Verifier**: использует только repo-documented validation path для touched surface
- **Boundary Keeper**: не даёт тащить сюда случайные snippets, unsanitized donor content или layer drift

## Параллельные дорожки
- Lane A: authored technique content
- Lane B: notes / adaptation / shadow review / manifests when directly relevant
- Lane C: release-prep or validation helper path only when in scope
- Не запускай больше одного пишущего агента на одну и ту же семью файлов.

## Allowed
- refine one existing technique
- выделить одну reusable practice из donor surface в public-safe form
- прояснить intent, boundaries, inputs/outputs, risks, validation method, adaptation notes
- подтянуть maturity wording (`promoted`, `canonical`, `deprecated`) при явном основании

## Forbidden
- добавлять random snippets или private hacks without adaptation notes
- маскировать source-specific artifact под reusable technique
- превращать technique в skill/eval/role/playbook
- скрывать origin and promotion history
- выдумывать validation commands, которых нет в repo-documented path

## Launch packet для координатора
```text
We are working in aoa-techniques with a one-repo one-swarm setup.
Pick exactly one target:
- one named technique
- one named donor -> technique extraction seam
- one bounded release-prep seam

First return:
1. chosen target
2. whether this is refinement or extraction
3. exact files to touch
4. validation path you intend to use from repo docs

The swarm must preserve:
truth and reproducibility over legend,
public by design, sanitized by default.
```

## Промпт для Scout
```text
Map only. Do not edit.
Return:
- target technique files
- origin / donor context
- current maturity state
- adaptation/validation gaps
- whether release-prep is actually in scope
- whether this belongs in a neighboring layer instead
```

## Промпт для Builder
```text
Make the smallest reviewable change.
Rules:
- keep the technique minimal and reproducible
- keep origin and promotion history legible
- preserve usage boundaries and validation method
- sanitize donor material before lifting it here
```

## Промпт для Verifier
```text
Use only repo-documented validation paths relevant to the touched surface.
If the change touched the bounded release-prep path, run:
- python -m pip install -r requirements-dev.txt
- python scripts/release_check.py
Otherwise:
- identify the exact validation helper(s) documented for the touched surface
- run only those commands
- report them explicitly
Do not invent a repo-wide validator if the docs do not define one.
```

## Промпт для Boundary Keeper
```text
Review only for anti-scope.
Check:
- still a reusable technique, not a one-off project hack
- donor content sanitized
- no secret-bearing configs or raw logs
- no neighboring-layer collapse
- maturity language justified
```

## Verify
```bash
python -m pip install -r requirements-dev.txt
python scripts/release_check.py   # only when the bounded release-prep path is in scope
# otherwise: run only the repo-documented validation helper(s) for the touched technique surface
```

## Done when
- одна техника стала яснее, уже и переносимее
- origin, boundaries, risks, validation method и adaptation notes явны
- validation path реально назван и прогнан, если он определён для touched surface
- слой техники не схлопнулся с соседними слоями

## Handoff
Если из техники рождается agent-facing execution flow, follow-up почти всегда идёт в `aoa-skills`.
