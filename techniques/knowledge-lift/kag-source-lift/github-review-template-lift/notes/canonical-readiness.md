# Canonical Readiness

## Technique
- id: AOA-T-0047
- name: github-review-template-lift

## Verdict
- defer for now

## Evidence summary
- origin evidence: `aoa-techniques` already projects authored `.github` issue and pull-request templates into a bounded review-template manifest.
- second context: GitHub's public template model turns authored repository templates into issue chooser entries, rendered issue forms, and pull request body intake surfaces.
- validation strength: the bundle now has first non-origin intake evidence, but the second context is platform-native template rendering rather than another repo's explicit downstream template manifest or review reader.

## Default-use rationale
- the technique is the right default when a repository needs a bounded prompt-shape lookup over review or intake templates.
- it is narrower than triage automation, approval policy, review-state storage, or workflow routing.
- the fresh evidence confirms that source templates can become downstream intake surfaces, but canonical promotion should wait until a review-specific consumer uses the template inventory as a derived reader without smuggling in workflow verdicts.

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the note cites public GitHub documentation and source-template behavior only.
- public reuse check: the pattern remains understandable as template intake, not as hidden GitHub policy or private repository workflow.

## Remaining gaps
- one public review-specific template manifest or intake reader beyond platform-native issue and pull request rendering would make the default-use case stronger.
- a future canonical review should confirm that the technique still refuses approval, triage, and review-state logic.
- 2026-05-14 residual queue pass: `aoa-playbooks` review intake is a useful adjacent reader over review packet and status surfaces, but it carries gate verdict and composition posture and is not an inventory-only GitHub review-template manifest; exact GitHub phrase search returned no hits.

## Recommendation
- keep `AOA-T-0047` `promoted`
- carry GitHub templates as first second-context support, not as a status flip
