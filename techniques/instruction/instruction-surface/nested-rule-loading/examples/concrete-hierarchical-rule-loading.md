# Concrete Hierarchical Rule Loading

This example shows one parent source with two nested layers that resolve through explicit precedence.

## Parent source

`rules/global-rule-set.md`

```md
# Global Rule Set

- Prefer small, reviewable diffs.
- Keep one canonical source for shared guidance.
- Treat nested layers as scoped and subordinate.
- Make precedence explicit before loading.
```

## Nested layers

`rules/teams/team-a/rules.md`

```md
<!-- Derived output from rules/global-rule-set.md plus team-a additions. -->
# Global Rule Set

- Prefer small, reviewable diffs.
- Keep one canonical source for shared guidance.
- Treat nested layers as scoped and subordinate.
- Make precedence explicit before loading.

## Team A addition

- Add one team-specific override for approval wording.
```

`rules/teams/team-a/feature-x/rules.md`

```md
<!-- Derived output from rules/global-rule-set.md plus team-a and feature-x additions. -->
# Global Rule Set

- Prefer small, reviewable diffs.
- Keep one canonical source for shared guidance.
- Treat nested layers as scoped and subordinate.
- Make precedence explicit before loading.

## Team A addition

- Add one team-specific override for approval wording.

## Feature X addition

- Add one feature-specific override for file naming.
```

## What this proves

- parent and child layers can be resolved in a declared order
- nested additions stay visible without becoming new canonical homes
- explicit precedence keeps the hierarchy reviewable
