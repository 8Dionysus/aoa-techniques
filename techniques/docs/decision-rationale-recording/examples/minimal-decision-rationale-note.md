# Minimal Decision Rationale Note

## Decision

Use one short reviewable note to capture the rationale for a meaningful docs change.

## Context

This change affects future reviewers because it changes how the decision will be remembered.

## Options

- record the decision in a bounded note
- leave the rationale only in chat or commit context

## Not chosen

Leave the rationale only in chat or commit context.

## Rationale

The note keeps the choice reviewable without turning the change into governance or taxonomy work.

## Consequences

- future reviewers can see why the path was chosen
- the note stays small enough to keep its own scope
- trivial edits do not get inflated into decision records
- the repo accepts one more bounded note instead of pretending the tradeoff will stay recoverable from commit history alone

## Follow-up

If the change becomes a recurring pattern, split out a separate technique instead of widening this note.
