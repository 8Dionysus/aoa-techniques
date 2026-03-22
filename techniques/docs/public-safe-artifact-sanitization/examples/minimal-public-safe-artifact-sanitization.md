# Scenario

A support summary needs to share a command failure, but the raw output includes hostnames, private paths, and internal IDs.

## Why this technique fits

- the material is useful, but not safe to share raw
- the goal is to preserve the lesson while removing unsafe detail
- the result should remain reviewable without exposing the private context

## Expected inputs

- the raw material to share
- the intended audience
- known sensitive surfaces
- the minimum detail needed to preserve the point

## Expected outputs

- a sanitized shareable version of the material
- a short note on what was removed or generalized
- any remaining sensitivity warning that still matters

## Boundary notes

- if the material is already public-safe, do not add unnecessary redaction
- if the main task is deciding whether the underlying action should proceed, use the approval-gate workflow first
- if the main task is to preview or execute the action, use the preview or safe-change workflow first

## Verification notes

- confirm sensitive surfaces were checked deliberately
- confirm the result still teaches the intended lesson
- confirm raw paths, tokens, and private identifiers were not preserved by accident
- confirm any remaining uncertainty was stated plainly
