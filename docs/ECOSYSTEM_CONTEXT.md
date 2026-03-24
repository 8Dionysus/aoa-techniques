# Ecosystem Context

This note explains where `aoa-techniques` sits in the AoA layer map and why
its canon stays narrower than neighboring repositories.

Use it when the question is not "which technique should I open next?" but
"why does this repository exist as its own public layer at all?"

## Why This Repo Exists

`aoa-techniques` exists to hold the reusable practice canon of AoA.

That means this repo owns:

- technique meaning
- bounded technique contracts
- validation and adaptation notes for reusable practice
- generated reader surfaces that stay subordinate to authored technique markdown

It does not exist to store scenario method, role doctrine, runtime policy,
verdict logic, or project-local execution overlays.

## Ontology Spine Inheritance

AoA's ontology spine separates reusable practice from the layers that execute,
evaluate, route, remember, or narrate that practice.

Inside that spine, `aoa-techniques` is the reusable-practice layer:

- it inherits the rule that each layer should own one bounded kind of meaning
- it keeps technique canon distinct from skill canon, playbook canon, eval
  doctrine, runtime policy, routing policy, and memory objects
- it gives downstream layers a stable public source of truth for reusable
  engineering practice without asking them to own technique meaning themselves

This is why `aoa-techniques` can feed `aoa-skills`, `aoa-playbooks`,
`aoa-evals`, and other repos without collapsing into them.

## Method And Neighboring Layers

Technique canon is not the same as scenario method.

- `aoa-techniques` owns reusable practice units such as workflows, validation
  patterns, documentation structures, and safety patterns
- `aoa-skills` owns bounded execution workflows that package techniques for
  agent-facing use
- `aoa-playbooks` owns recurring scenario method, executable route structure,
  and longer-horizon composition
- `aoa-evals` owns verdict doctrine and bounded proof surfaces
- runtime, routing, and memory repos own their own operational boundaries

The important seed boundary is simple: method lives in `aoa-playbooks`, not
here. A technique may support a playbook, but a playbook still owns the
scenario-level route.

## Boundary Reminder

When authoring or reviewing changes here:

- keep technique meaning source-first and public-safe
- prefer small reusable practices over package-shaped scenario bundles
- route scenario composition up to `aoa-playbooks`
- route bounded execution packaging to `aoa-skills`
- route verdict logic to `aoa-evals`
- route runtime and routing policy to their own repos

This repo is one layer of the AoA / ToS ecosystem, not an isolated project and
not the place to absorb neighboring meaning for convenience.
