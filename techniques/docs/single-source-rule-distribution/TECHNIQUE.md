---
id: AOA-T-0013
name: single-source-rule-distribution
domain: docs
status: promoted
origin:
  project: ruler
  path: README.md
  note: Adapted from the open-source ruler project, which keeps AI instructions in one canonical rule source and applies them to multiple agent-facing instruction files.
owners:
  - 8Dionysus
tags:
  - docs
  - source-of-truth
  - rule-distribution
  - agent-instructions
  - anti-drift
summary: Keep one canonical rule source and distribute it to multiple agent-facing instruction surfaces without turning each target into a hand-maintained source of truth.
---

# single-source-rule-distribution

## Intent

Reduce drift and duplicated maintenance by keeping one canonical rule source and propagating it to multiple agent-facing instruction surfaces instead of hand-editing each target separately.

## When to use

- repositories that support multiple coding agents or agent-facing instruction formats
- projects that already feel the cost of copying the same guidance into `AGENTS.md`, `CLAUDE.md`, or similar files
- teams that can regenerate or re-apply instruction targets from one canonical rule source
- repositories that want target surfaces to stay consistent without making every output file canonical

## When not to use

- repositories that only need one instruction surface
- projects that are unwilling to treat target files as managed or derived outputs
- workflows where each target must hold materially different guidance rather than a shared core rule set
- cases where the real need is MCP propagation, skills propagation, or broader orchestration rather than instruction distribution

## Inputs

- one canonical rule source location such as `.ruler/`, `rules/`, or an equivalent docs directory
- one distribution step that applies the same core rules to multiple target surfaces
- explicit target instruction surfaces such as `AGENTS.md`, `CLAUDE.md`, or other agent-facing files
- one managed/generated policy that makes clear which files are canonical inputs and which are derived targets

## Outputs

- multiple synchronized agent-facing instruction surfaces
- one retained canonical rule source
- lower risk of copy-paste drift across target files
- repeatable update path when rules change

## Core procedure

1. Choose one canonical location where the shared rule set will be authored and reviewed.
2. Define which agent-facing instruction surfaces should receive that shared rule set.
3. Apply the shared rules to each target surface with only the minimum target-specific formatting needed for the destination file.
4. Mark target files as managed or otherwise derived so contributors do not treat them as the editable source of truth.
5. Re-run the distribution step whenever the canonical rules change.
6. Review diffs at the canonical source first and only use target-file diffs to confirm distribution stayed synchronized.

## Contracts

- one canonical rule source owns the shared instruction content
- target instruction files are managed or derived outputs, not canonical editable homes
- the same source update can be propagated repeatedly without introducing duplication drift
- target-specific wrappers or formatting must not change the shared rule intent
- manual edits to target files are either forbidden or clearly subordinate to the canonical source

Relationship to adjacent techniques: unlike `AOA-T-0002 source-of-truth-layout`, this technique is about one rule source fanning out to many target surfaces rather than assigning canonical roles to many document classes inside one repository. Unlike `AOA-T-0012 deterministic-context-composition`, this technique is about one canonical source propagating to multiple target instruction files rather than composing many fragments into one generated artifact.

## Risks

- per-agent quirks can tempt maintainers to widen the pattern into agent-specific product behavior instead of keeping one shared rule core
- contributors may edit target files directly and reintroduce drift
- distribution can look consistent while silently duplicating content unless repeatability is checked after re-apply
- an import can sprawl if MCP propagation, skills propagation, nested loading, or backup/revert behavior are treated as part of the same technique

## Validation

Verify the technique by confirming that:
- one canonical rule source is named explicitly
- at least two target instruction surfaces receive the same shared rule core
- target files are treated as managed or derived outputs rather than canonical editable files
- re-applying distribution does not duplicate the shared rules in target files
- a source change routes through the canonical rule source first instead of through target-file edits

See `checks/single-source-rule-distribution-checklist.md`.
For external provenance and bounded repo-local adaptation, see `notes/external-origin.md` and `notes/second-context-adaptation.md`.

## Adaptation notes

What can vary across projects:
- the canonical source directory name such as `.ruler/`, `rules/`, or another docs folder
- the exact set of target instruction files
- whether the distribution step is a CLI command, script, build task, or CI-enforced local check
- the target-specific wrapper format used around shared instructions

What should stay invariant:
- one canonical rule source owns the shared instruction content
- multiple agent-facing instruction surfaces can be refreshed from that source
- target files remain derived rather than hand-maintained canonical documents
- distribution exists to reduce drift, not to create many divergent instruction variants

Project-shaped details that should not be treated as invariant:
- the donor repository's exact supported-agent matrix
- Node, npm, or any specific packaging/runtime assumptions
- nested loading behavior, which may support broader systems but is not part of this first technique contract
- MCP propagation, skills propagation, `.gitignore` automation, backup/revert flows, and other wider product behavior

See `notes/second-context-adaptation.md` for a bounded docs-repository adaptation sketch.

## Public sanitization notes

This imported technique narrows the donor repository to one docs pattern: one canonical rule source distributed to multiple agent-facing instruction surfaces. MCP propagation, skills propagation, nested-loading semantics, `.gitignore` automation, backup/revert behavior, beta-preview breadth, and the donor's full product matrix were intentionally left out of the public technique contract.

## Example

See `examples/minimal-single-source-rule-distribution.md`.

## Checks

See `checks/single-source-rule-distribution-checklist.md`.

## Promotion history

- adapted from open-source `ruler`
- imported into `aoa-techniques` on 2026-03-15 as the second bounded external-import draft with explicit exclusions around MCP, skills, nested loading, and other product-width behavior

## Future evolution

- split out `nested-rule-loading` as a separate sibling technique if experimental multi-directory layering proves reusable on its own
- split out `instruction-surface-mcp-propagation` as a separate sibling technique if MCP distribution deserves its own bounded contract
- add stronger second-context evidence once a live repository uses one canonical rule source across multiple agent-facing outputs
