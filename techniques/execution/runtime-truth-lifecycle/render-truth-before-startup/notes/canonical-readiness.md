# Canonical Readiness

## Technique
- id: AOA-T-0036
- name: render-truth-before-startup

## Verdict
- approve for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- Dockform now provides an exact-fit public second context: it exposes a plan/apply workflow over Docker Compose stacks, analyzes planned service/config state, renders fully resolved Compose config, masks secrets by default, and asks for confirmation before applying the prebuilt plan unless explicitly skipped
- the second context adaptation keeps the contract bounded around pre-start rendered truth rather than lifecycle, readiness, deployment, dashboard, volume, secret, or image-management breadth
- the bundle now has a checklist, a public-safe example, origin evidence, exact-fit second-context evidence, and an adverse-effects review, so the pattern is no longer proven mainly through one donor lineage

## Default-use rationale
- this is the right canonical default when the missing object is a reviewable pre-start render step over the actual composed runtime view
- it is strongest when declared composition and actual runtime truth can diverge in meaningful ways before launch
- it remains narrower than `AOA-T-0035` because it assumes a selected runtime path and reviews the resolved output rather than owning profile/preset composition
- it remains narrower than `AOA-T-0037` and `AOA-T-0038` because it does not prove host readiness and does not own startup or shutdown
- Dockform confirms that the default move can survive outside `abyss-stack`: preview or render resolved Compose runtime truth, review it locally, then hand off to apply/startup

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the published technique keeps the render-review seam while stripping donor-specific service names, deployed paths, host details, and local secret material
- Dockform evidence strengthens the public-safety boundary because its full-config render masks secrets by default and explicitly treats secret display as dangerous

## Remaining gaps
- no blocking promotion gap remains as long as the bundle stays centered on render/plan review of resolved runtime truth before apply/startup
- future review should keep rejecting surfaces that are only lifecycle wrappers, readiness checks, generic config renderers, deployment previews, or dry-run simulations without a distinct operator review seam over effective local runtime truth

## Recommendation
- promote `AOA-T-0036` to `canonical`
- use `AOA-T-0036` as the default runtime-truth technique when a selected local runtime should expose the actual resolved service/config view before startup, while routing host readiness, lifecycle, deployment, monitoring, and proof verdicts to sibling owners
