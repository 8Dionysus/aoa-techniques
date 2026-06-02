from __future__ import annotations

import json
import re
import unittest
from functools import lru_cache
from pathlib import Path

from scripts import validate_repo


REPO_ROOT = Path(__file__).resolve().parents[4]
# Historical tree-migration assertions read the preserved receipt, not the live
# root roadmap, so root direction can stay compact.
TREE_MIGRATION_BREADCRUMB_ROADMAP = (
    REPO_ROOT
    / "mechanics"
    / "distillation"
    / "legacy"
    / "raw"
    / "ROOT_ROADMAP_TREE_MIGRATION_BREADCRUMBS_2026-05-14.md"
)

ACTIVE_DISTILLATION_SURFACES = (
    "mechanics/distillation/AGENTS.md",
    "mechanics/distillation/README.md",
    "mechanics/distillation/DIRECTION.md",
    "mechanics/distillation/PARTS.md",
    "mechanics/distillation/PROVENANCE.md",
    "mechanics/distillation/LANDING_LOG.md",
    "mechanics/distillation/ROADMAP.md",
    "mechanics/distillation/parts/AGENTS.md",
    "mechanics/distillation/parts/README.md",
    "mechanics/distillation/legacy/AGENTS.md",
    "mechanics/distillation/legacy/README.md",
    "mechanics/distillation/legacy/INDEX.md",
    "mechanics/distillation/legacy/DISTILLATION_LOG.md",
    "mechanics/distillation/legacy/raw/README.md",
)

RAW_DISTILLATION_RECEIPTS = (
    "mechanics/distillation/legacy/raw/EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md",
    "mechanics/distillation/legacy/raw/CROSS_LAYER_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md",
)

PART_LOCAL_DISTILLATION_READMES = (
    "mechanics/distillation/parts/donor-refinery/README.md",
    "mechanics/distillation/parts/external-import-runbook/README.md",
    "mechanics/distillation/parts/external-candidate-ledger/README.md",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/README.md",
    "mechanics/distillation/parts/technique-reform-ingress/README.md",
    "mechanics/distillation/parts/long-gap-reentry/README.md",
)

PART_LOCAL_EXTERNAL_CANDIDATE_REGISTRY_ARTIFACTS = (
    "mechanics/distillation/parts/external-candidate-ledger/config/external_candidate_registry.source.json",
    "mechanics/distillation/parts/external-candidate-ledger/generated/external_candidate_registry.min.json",
    "mechanics/distillation/parts/external-candidate-ledger/schemas/external-candidate-registry-entry.schema.json",
    "mechanics/distillation/parts/external-candidate-ledger/schemas/external-candidate-registry.schema.json",
    "mechanics/distillation/parts/external-candidate-ledger/examples/external_candidate_registry_entry.example.json",
    "mechanics/distillation/parts/external-candidate-ledger/scripts/build_external_candidate_registry.py",
    "mechanics/distillation/parts/external-candidate-ledger/scripts/validate_external_candidate_registry.py",
    "mechanics/distillation/parts/external-candidate-ledger/tests/test_external_candidate_registry.py",
)

PART_LOCAL_CROSS_LAYER_CANDIDATE_REGISTRY_ARTIFACTS = (
    "mechanics/distillation/parts/cross-layer-candidate-ledger/config/cross_layer_candidate_registry.source.json",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/generated/cross_layer_candidate_registry.min.json",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/schemas/cross-layer-candidate-registry-entry.schema.json",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/schemas/cross-layer-candidate-registry.schema.json",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/examples/cross_layer_candidate_registry_entry.example.json",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/scripts/build_cross_layer_candidate_registry.py",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/scripts/validate_cross_layer_candidate_registry.py",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/tests/test_cross_layer_candidate_registry.py",
)

PART_LOCAL_AGON_CANDIDATE_HANDOFF_ARTIFACTS = (
    "mechanics/distillation/parts/agon-candidate-handoff/config/agon_candidate_handoff.source.json",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/request-evidence-bundle-readiness-review.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/checklists/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/checklists/request-evidence-gate-checklist.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/evidence-notes/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/evidence-notes/request-evidence-gate-evidence-note.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/examples/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/examples/request-evidence-minimal-public-safe.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/request-evidence-practice.md",
    "mechanics/distillation/parts/agon-candidate-handoff/generated/agon_candidate_handoff.min.json",
    "mechanics/distillation/parts/agon-candidate-handoff/schemas/agon-candidate-handoff-entry.schema.json",
    "mechanics/distillation/parts/agon-candidate-handoff/schemas/agon-candidate-handoff.schema.json",
    "mechanics/distillation/parts/agon-candidate-handoff/examples/agon_candidate_handoff_entry.example.json",
    "mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py",
    "mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py",
    "mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py",
)

PART_LOCAL_TECHNIQUE_REFORM_INGRESS_ARTIFACTS = (
    "mechanics/distillation/parts/technique-reform-ingress/config/AGENTS.md",
    "mechanics/distillation/parts/technique-reform-ingress/config/technique_family_scout.yaml",
    "mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml",
    "mechanics/distillation/parts/technique-reform-ingress/data/AGENTS.md",
    "mechanics/distillation/parts/technique-reform-ingress/data/technique_kind_overlay.yaml",
    "mechanics/distillation/parts/technique-reform-ingress/data/technique_kind_overlay.csv",
    "mechanics/distillation/parts/technique-reform-ingress/scripts/AGENTS.md",
    "mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py",
    "mechanics/distillation/parts/technique-reform-ingress/scripts/build_tree_projection.py",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/README.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/first-topology-scout-review-pack.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/first-kind-ambiguity-review-pack.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/second-kind-ambiguity-review-pack.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/0054-kind-destination-check.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/post-0054-kind-audit-hold-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/first-family-shelf-review-pack.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/first-tree-projection-review-pack.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/review-compaction-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-review-compaction-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/handoff-continuation-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-handoff-continuation-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/media-ingest-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-media-ingest-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/diagnosis-repair-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-diagnosis-repair-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/instruction-surface-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-instruction-surface-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/kag-source-lift-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-kag-source-lift-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/docs-boundary-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-docs-boundary-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/capability-registry-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-capability-registry-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/capability-boundary-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-capability-boundary-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/skill-discovery-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-skill-discovery-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/skill-support-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-skill-support-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/evaluation-chain-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-evaluation-chain-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/published-summary-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-published-summary-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/history-artifacts-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/donor-harvest-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-donor-harvest-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/decision-routing-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-decision-routing-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/approval-evidence-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-approval-evidence-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/review-evidence-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-automation-readiness-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/promotion-boundary-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-promotion-boundary-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/practice-adoption-lifecycle-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-practice-adoption-lifecycle-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/tool-gateway-direct-read-singleton-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-tool-gateway-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/whole-tree-closeout-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/final-tree-migration-ledger.md",
)

OLD_FLAT_DISTILLATION_FILES = (
    "mechanics/distillation/DONOR_REFINERY_RUBRIC.md",
    "mechanics/distillation/EXTERNAL_IMPORT_RUNBOOK.md",
    "mechanics/distillation/EXTERNAL_TECHNIQUE_CANDIDATES.md",
    "mechanics/distillation/CROSS_LAYER_TECHNIQUE_CANDIDATES.md",
    "mechanics/distillation/LONG_GAP_CANON_DESIGN.md",
)


class ReformContext(str):
    """Text context that lets older breadcrumb checks ignore wrapping drift."""

    @staticmethod
    def _compact(value: str) -> str:
        return " ".join(value.split()).lower()

    @staticmethod
    def _tokens(value: str) -> list[str]:
        return re.findall(r"[a-z0-9]+", value.lower())

    def _has_ordered_tokens(self, value: str) -> bool:
        haystack = self._tokens(self)
        needle = self._tokens(value)
        cursor = 0
        for token in needle:
            try:
                cursor = haystack.index(token, cursor) + 1
            except ValueError:
                return False
        return True

    def __contains__(self, value: object) -> bool:
        if not isinstance(value, str):
            return super().__contains__(value)
        return (
            super().__contains__(value)
            or self._compact(value) in self._compact(self)
            or self._has_ordered_tokens(value)
        )


@lru_cache(maxsize=1)
def read_distillation_reform_context() -> ReformContext:
    """Read the active Distillation contour plus its owning reform evidence."""
    reform_root = (
        REPO_ROOT
        / "mechanics"
        / "distillation"
        / "parts"
        / "technique-reform-ingress"
    )
    source_paths = [
        REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md",
        REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md",
        reform_root / "README.md",
        reform_root / "reviews" / "README.md",
        *sorted((reform_root / "reviews").glob("*.md")),
    ]
    return ReformContext("\n\n".join(path.read_text(encoding="utf-8") for path in source_paths))


@lru_cache(maxsize=1)
def read_tree_migration_context() -> ReformContext:
    """Read current tree law plus historical migration evidence."""
    reform_root = (
        REPO_ROOT
        / "mechanics"
        / "distillation"
        / "parts"
        / "technique-reform-ingress"
    )
    receipt_root = REPO_ROOT / "legacy" / "receipts"
    source_paths = [
        REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md",
        TREE_MIGRATION_BREADCRUMB_ROADMAP,
        reform_root / "README.md",
        reform_root / "reviews" / "README.md",
        *sorted((reform_root / "reviews").glob("*.md")),
        *sorted(receipt_root.glob("*-tree-pilot.md")),
    ]
    return ReformContext("\n\n".join(path.read_text(encoding="utf-8") for path in source_paths))
