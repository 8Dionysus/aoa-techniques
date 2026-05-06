# Minimal Example

## Situation

A coordination repository tracks one final owner-side contract change, but the
owner repository is intentionally handled through GitHub only in the current
environment.

## Minimal route

1. Write one bounded track packet with goal, non-goals, validator of record,
   stop condition, and rollback marker.
2. Open one owner-side issue and one PR branch in GitHub.
3. Land the smallest owner-side contract doc or config change.
4. Wait for the named PR checks to pass and merge the owner PR.
5. In the same closeout pass, update the coordination repository so its
   lifecycle markers and reality checks now point at the merged owner anchors.

## Honest result

- the owner repo remains the source of truth
- GitHub-native validation proves only the bounded owner-side claim
- the coordination layer no longer reports staged truth after the merge

## Non-example

Do not treat one green owner-side PR as proof of broad runtime parity or full
product support beyond the merged owner contract.
