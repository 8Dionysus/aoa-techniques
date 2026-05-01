# Technique Atom Contract

Date: 2026-05-01

## Status

Accepted

## Context

The repository already described techniques as reusable, bounded, and portable,
and it already separated techniques from skills, evals, routing, roles, and
playbooks. That was enough for the first hardening stage, where the main risk
was public safety, reviewability, generated-surface parity, and corpus hygiene.

As the corpus grows, that wording is not specific enough. A broad "minimal
reproducible unit" can still drift into a mini-skill, a workflow chain, or a
large method document. The project direction now needs `aoa-techniques` to scale
toward many hundreds or thousands of compact practices that can be classified,
selected, templated, and handed to small agents after orchestration supplies the
right context.

## Options

- Keep the existing wording and rely on reviewers to infer atomicity from
  "bounded" and "portable".
- Turn techniques into richer skill-like workflows so each bundle carries more
  context and more execution chain.
- Add an explicit atom contract while keeping skills, playbooks, routing, evals,
  memory, KAG, and runtime behavior in their owning repositories.

## Decision

Add a repo-owned Technique Atom Contract and wire it into the root route card,
root README, Start Here, docs map, and technique template.

The contract defines one technique as one atomic executable move: compact enough
to classify, template, verify, and execute from a small runtime card once the
right context has been supplied.

## Consequences

Future technique candidates should be narrowed before promotion if they need
several independent moves, long-running state, orchestration policy, scenario
composition, role identity, proof verdicts, or routing behavior.

The template now asks authors to name the atomic move and small-agent execution
shape explicitly. This adds a little authoring friction, but it gives the corpus
a clearer path toward `1000+` techniques without turning the repository into a
pile of broad mini-skills.

Existing bundles are not rewritten by this decision. They can be audited
gradually through normal review, distillation, promotion, capsule, and selection
surfaces.
