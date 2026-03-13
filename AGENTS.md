# AGENTS.md

Guidelines for coding agents and humans contributing to `aoa-techniques`.

## Purpose

This repository stores **public, reusable, sanitized techniques**.

Do not treat it as:
- a dump of project-specific code
- a notebook of raw experiments
- a backup of private operational context

## Core rule

Only contribute techniques that are:
- reusable
- sanitized
- documented
- bounded
- verifiable

## Hard NO

Do not contribute:
- secrets
- tokens
- internal-only URLs
- private infrastructure details
- project-only dumps
- raw logs with sensitive data
- environment-specific hacks without adaptation notes
- techniques with unclear boundaries

## Required for every technique

Every technique should include:
- a canonical `TECHNIQUE.md`
- clear intent
- current status
- origin
- when to use
- when not to use
- risks
- validation method
- at least one example or example outline
- adaptation notes

## Public hygiene

Assume everything here is public and reusable by strangers.

Write for portability:
- generalize paths
- generalize hostnames
- generalize private IDs
- strip secrets
- explain assumptions
- prefer small explicit contracts

## Contribution doctrine

Use this flow:

`PLAN -> DIFF -> VERIFY -> REPORT`

### PLAN
State what is being added or changed and why.

### DIFF
Keep the change focused and reviewable.

### VERIFY
Confirm that the technique is still public-safe, coherent, and useful.

### REPORT
Summarize what changed and any remaining limits.

## Promotion rule

Prefer techniques that were first tested in a real project.
Do not mark a technique `canonical` based only on abstraction or preference.

## Preferred PR shape

Prefer:
- one new technique per PR
- or one focused update to an existing technique
- or one clear status transition

## Quality bar

A technique is stronger when it has:
- evidence of reuse
- a check, smoke, or validation checklist
- clean adaptation notes
- clear public sanitization notes