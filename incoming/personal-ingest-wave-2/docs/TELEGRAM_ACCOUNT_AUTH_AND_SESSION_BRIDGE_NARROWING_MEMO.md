# Narrowing Memo - telegram-account-auth-and-session-bridge

This memo records the current narrowing result for the remaining personal-ingest hold candidate `telegram-account-auth-and-session-bridge`.

It is a staging note only.
It does not create a canonical bundle or authorize import by itself.

## Candidate chosen

- `telegram-account-auth-and-session-bridge`
- donors:
  - `LonamiWebs/Telethon`
  - `thedemons/opentele`
  - `chaindead/telegram-mcp`

## Overlap watch

- [AOA-T-0074](../../../techniques/agent-workflows/telegram-export-normalization-to-local-store/TECHNIQUE.md)
- auth and runtime control-plane doctrine

## Boundary statement

The current donor evidence does not yet expose one standalone session-bridge contract that is smaller than Telegram auth/bootstrap posture.

What is public today is a mixed cluster:

- account login and session lifecycle handling
- conversion between Telegram account/session formats
- operator approval and secret-handling posture
- live runtime control over an authenticated Telegram surface

That is useful workflow substrate, but it is not yet one sharply bounded technique in the `aoa-techniques` sense.

The narrowest plausible extraction target is:

- one approval-gated session-bridge handoff that converts or exposes a reusable Telegram session object without also owning auth bootstrap, live runtime control, or downstream memory behavior

Even that smaller target is not stable enough yet, because the donor family still presents the live seam mainly as account access plus runtime capability rather than as one reusable session-bridge artifact contract.

## What stays out

- secret storage policy and credential-handling doctrine
- live account bootstrap and operator login workflow
- runtime control-plane behavior over an authenticated Telegram client
- automatic memory writeback, recall, or agent-autonomy claims
- any wording that makes the candidate sound like general Telegram operations doctrine

## Evidence snapshot

- `Telethon` exposes Telegram client login and session handling as a live account-access surface rather than a small neutral handoff object
- `opentele` centers on moving between Telegram Desktop account material and Telethon session state, which keeps the seam close to session conversion and secret-bearing runtime posture
- `telegram-mcp` presents an authenticated Telegram surface as a runtime tool/control layer rather than as one bounded reusable session-bridge artifact
- [AOA-T-0074](../../../techniques/agent-workflows/telegram-export-normalization-to-local-store/TECHNIQUE.md) already owns the smaller normalized-local-store seam, so any future bridge candidate must stay clearly upstream of storage normalization and clearly downstream of auth/bootstrap doctrine

## Verdict

- keep `telegram-account-auth-and-session-bridge` in the `incubation-hold` lane
- do not create a bundle yet
- do not assign a technique ID yet

## Honest reopen trigger

Reopen this candidate only if the draft can say, in plain language:

- what the reusable session-bridge object is
- how it stays separate from auth bootstrap and live runtime control
- what operator approval seam belongs to the bridge itself rather than to general Telegram account handling
- why the reusable center is a bounded handoff artifact and not broader Telegram access doctrine

## Files touched or proposed

- touched: this memo
- touched: personal-ingest wave staging docs and registry to keep the incubation hold explicit and reviewable
- not proposed yet: no `TECHNIQUE.md`, no bundle-local example, no checklist seed, no note package

## Whether operator approval is needed

- no operator approval needed to keep this candidate in incubation-hold state
- operator approval is required before any future move from this memo into a real technique bundle
