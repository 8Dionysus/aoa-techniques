# Second Context Adaptation

## Technique
- id: AOA-T-0027
- name: cross-agent-skill-propagation

## Target project
- name: ai-rulez
- environment: public cross-tool AI configuration manager
- runtime: `.ai-rulez/` source tree plus `generate` command that emits native agent-tool outputs for multiple supported targets

## What changed

- paths: ai-rulez keeps rules, context, skills, agents, and commands under `.ai-rulez/`, then emits native target files for Claude, Cursor, Copilot, Gemini, Cline, Continue, Codex, OpenCode, and related tools
- services: the proof surface is the managed source-to-target generation path, not the MCP server, marketplace, remote include, or builtin-domain breadth
- dependencies: the adaptation depends on one editable source layer, declared presets or profiles, and repeatable target generation
- operating assumptions: generated target files are downstream outputs of the `.ai-rulez/` source tree and should not become independent hand-maintained authorities

## What stayed invariant

- contract: one canonical skill or rule source declares the shared meaning
- validation logic: managed targets remain traceable to that source through repeatable propagation
- safety rules: local copies stay subordinate to the canonical source and do not silently become new canonical homes

## Risks introduced by adaptation

- the target list is wider than this technique needs, so the reusable proof must stay on managed-target propagation rather than cross-tool product governance
- ai-rulez also covers agents, commands, MCP, profiles, builtins, and remote includes; those remain adjacent product breadth, not part of the technique contract
- generated target files can still drift if a downstream repository edits them directly and stops regenerating from `.ai-rulez/`

## Evidence

- ai-rulez `README.md` at `Goldziher/ai-rulez@c704b8cfbeb752a9e1273a2ccfae7511054ff107` describes writing rules, context, skills, agents, and commands once in `.ai-rulez/`, then running `generate` for native tool outputs across 19 platforms
- ai-rulez `docs/configuration.md` at the same commit describes file-based source inputs for `.ai-rulez/rules/*.md`, `.ai-rulez/context/*.md`, `.ai-rulez/skills/{name}/SKILL.md`, `.ai-rulez/agents/*.md`, profile-scoped generation, and built-in presets that map to target surfaces such as `CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`, and `.clinerules/`
- this is exact-fit reinforcement because the same editable source layer fans out into multiple managed agent-facing outputs while skills and rules stay authored before target generation

## Result

- exact-fit second context confirmed
- the bundle can move from documentation-first promoted posture to canonical default, as long as product-width target support, MCP management, marketplace behavior, and profile policy remain outside the technique
