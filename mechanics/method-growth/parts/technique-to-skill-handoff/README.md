# Technique To Skill Handoff

Version: v0.7
Owner surface: `aoa-techniques`
Seed family: Experience Adoption Forge

## Purpose

When technique adoption should generate a skill proposal.

## Core Law

- Adoption must be explicit.
- Local owner consent is required.
- Durable behavior change needs evidence, rollback and retention.

## Lifecycle Hooks

- request
- readiness
- shadow
- decision
- activation
- retention

## Outputs

- technique_to_skill_handoff

## Stop Lines

- No hidden assistant self-adoption.
- No adoption without local owner consent.
- No direct Tree-of-Sophia runtime write or runtime adoption.
- No KAG forced adoption into source repos.
- No routing layer authorship of meaning.
- No persistent change without rollback or explicit quarantine fallback.

## Notes

This document belongs to the v0.7 downstream adoption wave. It assumes the v0.6
federation harvest has already approved a shared pattern, but it refuses to
treat approval as automatic adoption. Adoption is a second sovereign act: local
owner consent, compatibility, shadow proof, rollback path, retention watch, and
kind-safe projection are required.

## Extracted Atom

[AOA-T-0102 skill-proposal-handoff-packet](../../../../techniques/agent-workflows/skill-proposal-handoff-packet/TECHNIQUE.md)
carries the reusable handoff move from this part: emit one bounded proposal
packet when technique-side adoption pressure should be reviewed by a
skill-owning surface.

This part still owns the broader Method-growth lifecycle pressure around
request, readiness, shadow, decision, activation, and retention. The extracted
atom does not create, accept, install, or activate a skill; receiving owner
acceptance stays outside `aoa-techniques`.
