# Second Context Adaptation

## Technique
- id: AOA-T-0026
- name: session-capture-as-repo-artifact

## Target project
- name: Aider plus public `.aider.chat.history.md` artifact family
- environment: open-source terminal AI coding tool with repo-aware configuration and a default Markdown chat-history file
- runtime: local Markdown chat history saved in or near the project tree, with public repositories showing those logs retained as committed project-visible artifacts

## What changed
- paths: the donor uses `.specstory/history/`, while Aider's default chat-history file is `.aider.chat.history.md` and public repositories show both root-level and subdirectory-retained variants
- services: Aider also supports sharing copied chat logs through gists and has broader coding-tool behavior, but this adaptation narrows to the saved Markdown chat-history artifact
- dependencies: the adaptation depends on local file capture and project visibility, not on the donor product wrapper, cloud sync, search UI, or memory database
- operating assumptions: contributors should read this as capture-as-artifact evidence, not as an instruction to commit every raw Aider log or to treat ignored local logs as automatically versioned history

## What stayed invariant
- contract: AI coding sessions are persisted as local project-scoped artifacts
- validation logic: a reviewer can inspect or share the saved Markdown history later without hidden runtime state
- safety rules: session history remains separate from authored instructions, memory recall, search ranking, and policy authority

## Risks introduced by adaptation
- Aider also recommends `.aider*` gitignore behavior in its release history, so ordinary ignored local logs are adjacent until a project deliberately retains or publishes the artifact
- public `.aider.chat.history.md` files can be accidental leaks if teams do not review and sanitize them before commit or sharing
- teams may mistake generic Aider chat history for a retention policy, memory substrate, or transcript-packaging technique unless the capture boundary stays explicit

## Evidence
- Aider's public options reference documents `--chat-history-file` with default `.aider.chat.history.md`.
- Aider's public configuration docs say `.aider.conf.yml` can live at the root of a git repository, making repo-scoped history configuration a first-class local shape.
- Aider's public FAQ treats `.aider.chat.history.md` as Markdown chat logs that can be copied into a gist or otherwise published as raw Markdown.
- GitHub code search found committed `.aider.chat.history.md` artifacts in public non-fork repositories, including `launchapp-dev/animus-cli` at the repository root, `terraphim/terraphim-ai` under `crates/terraphim_atomic_client/`, and `CEDARScript/cedarscript-llm-prompt-engineering` under an examples tree.
- Those public artifacts preserve the reusable core: local AI coding sessions become inspectable Markdown project artifacts without making search, recall, cloud history, or instruction authority the primary object.

## Result
- works as a real public second context and closes the prior live-adopter gap for `AOA-T-0026`
- canonical use remains bounded to deliberately retained, reviewable session artifacts; ignored local tool state, transcript export, search/indexing, and memory behavior stay adjacent or sibling concerns
