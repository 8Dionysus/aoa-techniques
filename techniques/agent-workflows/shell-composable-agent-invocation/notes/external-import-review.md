# External Import Review

## Technique
- id: AOA-T-0031
- name: shell-composable-agent-invocation

## Verdict
- pass
- review date: 2026-03-21

## Evidence summary

- the bundle includes the expected bounded external-import package: `TECHNIQUE.md`, `notes/external-origin.md`, `notes/second-context-adaptation.md`, one checklist, and two public-safe examples
- the technique document states one narrow contract: agent runs stay shell-composable through explicit stdin, stdout, files, and pipes
- the provenance note records the donor source plus explicit exclusions around generic shell advice, confirmation as the core invariant, and broader autonomous loop behavior
- the second-context note shows the same contract surviving as a documentation-first adaptation inside `aoa-techniques`

## Boundedness check

- result: pass
- the invariant core stays narrow: one-shot shell-visible invocation, explicit I/O boundaries, and pipe or file composability
- excluded donor features remain explicit and out of scope: generic shell best practices, confirmation-boundary doctrine, provider-specific breadth, and broader autonomous loop behavior
- the examples reinforce shell-side composability without widening the bundle into a general stateless workflow or mutation-safety system

## Provenance readability

- result: pass
- a reviewer can trace the path from donor repository to public technique through the external-origin note, bounded exclusions, and documentation-first adaptation without hidden internal context
- the bundle reads as one reusable workflow pattern rather than a disguised product wrapper or shell-style guide
- the current import path is public-safe and reviewable at the present repo scale

## Import-path assessment

- result: pass
- this is a successful bounded external import and the bundle is strong enough to enter the corpus as a `promoted` technique
- the import path is strong enough for initial publication, but not strong enough to justify canonical default status without another live reuse context

## Remaining gaps

- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- this new adjacent import does not count as live closure evidence for `AOA-T-0023`, because shell composability is a narrower contract than the broader stateless fast-path posture

## Recommendation

- accept `AOA-T-0031` as a bounded external import and publish it as `promoted`
- defer any canonical review until another live adopter confirms that shell-composable one-shot invocation survives outside the donor repository
