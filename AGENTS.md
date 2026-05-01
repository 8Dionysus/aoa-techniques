# AGENTS.md

Root route card for `aoa-techniques`.

## Purpose

`aoa-techniques` is the public practice canon of AoA.
It stores reusable, sanitized, bounded, reviewable engineering techniques that can later be lifted into skills, evals, routing, KAG exports, or other derived artifacts.
A technique is a portable unit of method, not a skill bundle, proof surface, questline, or agent identity.
The corpus must work both as an AoA organ and as a standalone public library: external builders should be able to reuse a technique without deploying OS Abyss.
The primary unit is an atomic executable move: one compact technique should be small enough to classify, template, and hand to a small agent after orchestration supplies the right context.
Technique classification is faceted: `domain` and `kind` are current frontmatter truth, while family, capability, substrate, execution profile, risk posture, and relation topology should stay explicit design axes instead of being collapsed into tags.

## Owner lane

This repository owns:

- technique bundle meaning, IDs, intent, contracts, and adaptation notes
- public-safe technique wording and topology selection, including current
  domain/kind truth and future family/capability/substrate/risk axes
- owner-local participation in AoA cross-mechanics around reusable practice movement
- generated technique catalogs, capsules, feat-card reader surfaces, and source-lift surfaces

It does not own:

- skill workflow meaning, proof doctrine, routing, role contracts, memory, playbooks, KAG substrate meaning, or stats summaries
- private project operations, secrets, or infrastructure detail

## Start here

1. `README.md`
2. `ROADMAP.md`
3. `docs/START_HERE.md`
4. `docs/TECHNIQUE_ATOM_CONTRACT.md`
5. `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
6. `mechanics/README.md` when the change touches AoA mechanics or practice movement around canon
7. `WALKTHROUGH.md`
8. `docs/TECHNIQUE_SELECTION.md`
9. `docs/TECHNIQUE_KIND_GUIDE.md`
10. the target `techniques/**/TECHNIQUE.md`
11. affected generated catalogs, capsules, feat cards, or source-lift outputs
12. `docs/AGENTS_ROOT_REFERENCE.md` for preserved full root branches


## AGENTS stack law

- Start with this root card, then follow the nearest nested `AGENTS.md` for every touched path.
- Root guidance owns repository identity, owner boundaries, route choice, and the shortest honest verification path.
- Nested guidance owns local contracts, local risk, exact files, and local checks.
- Authored source surfaces own meaning. Generated, exported, compact, derived, runtime, and adapter surfaces summarize, transport, or support meaning.
- Self-agency, recurrence, quest, progression, checkpoint, or growth language must stay bounded, reviewable, evidence-linked, and reversible.
- Report what changed, what was verified, what was not verified, and where the next agent should resume.

## Route away when

- the object is an executable workflow, not a reusable practice
- the object needs a chain of several independent moves instead of one atomic technique
- the change is proof, routing, memory, role, playbook, KAG, or stats meaning
- the idea is vague philosophy without an operational method

## Verify

Default validation:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Use release checks or Agon-specific checks from `docs/AGENTS_ROOT_REFERENCE.md` when publication posture, broad generated outputs, or companion-candidate surfaces change.

## Report

State the technique or technique family changed, whether IDs, kind, domain, state, adaptation notes, or source-lift surfaces changed, and exactly what validation ran.

## Full reference

`docs/AGENTS_ROOT_REFERENCE.md` preserves the former detailed root guidance, including branch docs, promotion posture, review rules, and specialized validation paths.
