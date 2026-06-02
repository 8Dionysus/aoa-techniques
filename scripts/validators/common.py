from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

REQUIRED_SECTIONS = (
    "Intent",
    "When to use",
    "When not to use",
    "Inputs",
    "Outputs",
    "Core procedure",
    "Contracts",
    "Risks",
    "Validation",
    "Adaptation notes",
    "Public sanitization notes",
    "Example",
    "Checks",
    "Promotion history",
    "Future evolution",
)
OPTIONAL_TEMPLATE_SECTIONS = (
    "Atomic move",
    "Topology fit",
    "Small-agent execution shape",
)
TECHNIQUE_SECTION_ORDER = (
    "Intent",
    "Atomic move",
    "Topology fit",
    "When to use",
    "When not to use",
    "Inputs",
    "Outputs",
    "Core procedure",
    "Small-agent execution shape",
    "Contracts",
    "Risks",
    "Validation",
    "Adaptation notes",
    "Public sanitization notes",
    "Example",
    "Checks",
    "Promotion history",
    "Future evolution",
)
SECTION_LIFT_HEADINGS = REQUIRED_SECTIONS[:10]
CAPSULE_SECTION_HEADINGS = (
    "Intent",
    "When to use",
    "When not to use",
    "Inputs",
    "Outputs",
    "Contracts",
    "Risks",
    "Validation",
)
RISK_SUBSECTION_HEADINGS = (
    "Failure modes",
    "Negative effects",
    "Misuse patterns",
    "Detection signals",
    "Mitigations",
)

REQUIRED_SUPPORT_DIRS = ("checks", "examples", "notes")
REQUIRED_STAGE1_FILES = (
    "DESIGN.md",
    "DESIGN.AGENTS.md",
    "docs/review/CANONICAL_RUBRIC.md",
    "docs/DOMAIN_MAP.md",
    "schemas/technique.schema.json",
    "schemas/evidence-note.schema.json",
    "schemas/relation.schema.json",
    "schemas/index-entry.schema.json",
    "schemas/technique_intelligence_registry.schema.json",
    "schemas/technique_intelligence_dag.schema.json",
    "scripts/build_catalog.py",
    "scripts/build_kind_manifest.py",
    "mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py",
    "mechanics/distillation/parts/technique-reform-ingress/scripts/build_tree_projection.py",
    "scripts/build_capsules.py",
    "scripts/build_sections.py",
    "scripts/build_section_manifest.py",
    "scripts/build_checklist_manifest.py",
    "scripts/build_example_manifest.py",
    "scripts/build_evidence_note_manifest.py",
    "scripts/build_github_review_template_manifest.py",
    "scripts/build_semantic_review_manifest.py",
    "scripts/build_shadow_review_manifest.py",
    "scripts/build_promotion_readiness.py",
    "scripts/build_repo_doc_surface_manifest.py",
    "scripts/technique_intelligence_surface.py",
    "scripts/technique_intelligence.py",
    "scripts/build_technique_intelligence.py",
    "scripts/agents_mesh_common.py",
    "scripts/build_agents_mesh_index.py",
    "scripts/validate_agents_md_shape.py",
    "scripts/validate_agents_mesh.py",
    "scripts/validate_agents_mesh_index.py",
    "scripts/build_kag_export.py",
    "scripts/release_check.py",
    "config/agents_mesh.json",
    "docs/guardrails/AGENTS_MESH_PROTOCOL.md",
    "docs/guardrails/AGENTS_MESH_INDEX.md",
    "generated/technique_catalog.json",
    "generated/technique_catalog.min.json",
    "generated/technique_capsules.json",
    "generated/technique_capsules.min.json",
    "generated/technique_sections.full.json",
    "generated/technique_section_manifest.json",
    "generated/technique_section_manifest.min.json",
    "generated/technique_checklist_manifest.json",
    "generated/technique_checklist_manifest.min.json",
    "generated/technique_example_manifest.json",
    "generated/technique_example_manifest.min.json",
    "generated/technique_evidence_note_manifest.json",
    "generated/technique_evidence_note_manifest.min.json",
    "generated/github_review_template_manifest.json",
    "generated/github_review_template_manifest.min.json",
    "generated/semantic_review_manifest.json",
    "generated/semantic_review_manifest.min.json",
    "generated/shadow_review_manifest.json",
    "generated/shadow_review_manifest.min.json",
    "generated/technique_promotion_readiness.min.json",
    "generated/repo_doc_surface_manifest.json",
    "generated/repo_doc_surface_manifest.min.json",
    "generated/agents_mesh.min.json",
    "generated/kag_export.json",
    "generated/kag_export.min.json",
    "generated/technique_intelligence_registry.json",
    "generated/technique_intelligence_registry.min.json",
    "generated/technique_intelligence_dag.json",
    "generated/technique_intelligence_dag.min.json",
    "docs/readers/intelligence/README.md",
    "docs/readers/intelligence/TECHNIQUE_INTELLIGENCE.md",
)
REQUIRED_SELECTION_FILES = (
    "docs/selection/TECHNIQUE_SELECTION_GUIDE.md",
    "docs/selection/TECHNIQUE_INTELLIGENCE_GUIDE.md",
    "docs/readers/selection/TECHNIQUE_SELECTION.md",
    "docs/readers/selection/SELECTION_PATTERNS.md",
    "docs/readers/review/SHADOW_PATTERNS.md",
)
REQUIRED_SEMANTIC_REVIEW_GUIDE_FILES = ("docs/review/SEMANTIC_REVIEW_GUIDE.md",)
REQUIRED_KAG_SOURCE_READER_FILES = (
    "docs/readers/source-lift/TECHNIQUE_SECTIONS.md",
    "docs/readers/source-lift/TECHNIQUE_CHECKLISTS.md",
    "docs/readers/source-lift/TECHNIQUE_EXAMPLES.md",
    "docs/readers/source-lift/EVIDENCE_NOTE_SURFACES.md",
)
REQUIRED_CAPSULE_SURFACE_FILES = ("docs/readers/runtime/TECHNIQUE_CAPSULES.md",)
REQUIRED_REPO_DOC_SURFACE_FILES = ("docs/readers/repo/REPO_DOC_SURFACES.md",)
REQUIRED_KAG_EXPORT_FILES = ("docs/source-lift/KAG_EXPORT.md",)
REQUIRED_KIND_DOCTRINE_FILES = (
    "docs/selection/TECHNIQUE_KIND_GUIDE.md",
    "docs/selection/TECHNIQUE_KIND_HANDOFF_PACK.md",
)
TECHNIQUE_REFORM_INGRESS_DIR = "mechanics/distillation/parts/technique-reform-ingress"
TECHNIQUE_REFORM_REPORTS_DIR = (
    f"{TECHNIQUE_REFORM_INGRESS_DIR}/reports"
)
TECHNIQUE_REFORM_REPORT_LINK_PREFIX = "../../../../../"
TECHNIQUE_KIND_COUNTS_REPORT_PATH = (
    f"{TECHNIQUE_REFORM_REPORTS_DIR}/technique_kind_counts.md"
)
REQUIRED_KIND_DATA_FILES = (
    "config/technique_kind_registry.yaml",
    f"{TECHNIQUE_REFORM_INGRESS_DIR}/config/technique_family_scout.yaml",
    f"{TECHNIQUE_REFORM_INGRESS_DIR}/config/technique_topology_axes.yaml",
    f"{TECHNIQUE_REFORM_INGRESS_DIR}/data/technique_kind_overlay.yaml",
    f"{TECHNIQUE_REFORM_INGRESS_DIR}/data/technique_kind_overlay.csv",
    TECHNIQUE_KIND_COUNTS_REPORT_PATH,
)
SEMANTIC_REVIEW_PACKET_DIR = (
    "mechanics/distillation/parts/technique-reform-ingress/reviews/semantic"
)
SHADOW_REVIEW_PACKET_DIR = (
    "mechanics/distillation/parts/technique-reform-ingress/reviews/shadow"
)
REQUIRED_KIND_SURFACE_FILES = (
    "generated/technique_kind_manifest.json",
    "generated/technique_kind_manifest.min.json",
    "docs/readers/kind/TECHNIQUE_KINDS.md",
)
REQUIRED_KIND_REPORT_FILES = (
    f"{TECHNIQUE_REFORM_REPORTS_DIR}/technique_family_scout.md",
    f"{TECHNIQUE_REFORM_REPORTS_DIR}/technique_family_scout.json",
    f"{TECHNIQUE_REFORM_REPORTS_DIR}/kind_ambiguity_audit.md",
    f"{TECHNIQUE_REFORM_REPORTS_DIR}/technique_topology_scout.md",
    f"{TECHNIQUE_REFORM_REPORTS_DIR}/technique_topology_scout.json",
)
REQUIRED_TREE_REPORT_FILES = (
    f"{TECHNIQUE_REFORM_REPORTS_DIR}/technique_tree_projection.md",
    f"{TECHNIQUE_REFORM_REPORTS_DIR}/technique_tree_projection.json",
)
KAG_EXPORT_TECHNIQUE_ID = "AOA-T-0043"
KAG_EXPORT_SECTION_HANDLES = (
    "intent",
    "inputs",
    "outputs",
    "contracts",
    "risks",
    "validation",
)
KAG_EXPORT_PRIMARY_QUESTION = (
    "How should one bridge keep primary and supporting source inputs explicit "
    "without widening into graph semantics?"
)
KAG_EXPORT_SUMMARY_50 = (
    "Source-owned tiny export for explicit primary and supporting provenance."
)
KAG_EXPORT_SUMMARY_200 = (
    "Source-owned tiny export capsule for a technique that keeps multi-source "
    "input ordering visible so downstream KAG and bridge readers preserve "
    "provenance priority without replacing the authored bundle."
)
KAG_EXPORT_PROVENANCE_NOTE = (
    "Guide to source, not source replacement, built from source-owned "
    "technique surfaces."
)
KAG_EXPORT_NON_IDENTITY_BOUNDARY = (
    "Derived export capsule for KAG consumers; authored technique meaning "
    "remains in aoa-techniques markdown."
)
SELECTION_REVIEW_DOCS = {
    "agent_workflows_core": f"{SEMANTIC_REVIEW_PACKET_DIR}/AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md",
    "published_summary": f"{SEMANTIC_REVIEW_PACKET_DIR}/PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md",
    "evaluation_chain": f"{SEMANTIC_REVIEW_PACKET_DIR}/EVALUATION_CHAIN_SEMANTIC_REVIEW.md",
    "docs_boundary": f"{SEMANTIC_REVIEW_PACKET_DIR}/DOCS_BOUNDARY_SEMANTIC_REVIEW.md",
    "intent_chain": f"{SEMANTIC_REVIEW_PACKET_DIR}/INTENT_CHAIN_SEMANTIC_REVIEW.md",
    "instruction_surface": f"{SEMANTIC_REVIEW_PACKET_DIR}/INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md",
    "skill_support": f"{SEMANTIC_REVIEW_PACKET_DIR}/SKILL_SUPPORT_SEMANTIC_REVIEW.md",
    "kag_source_lift": f"{SEMANTIC_REVIEW_PACKET_DIR}/KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md",
}
WORKING_SET_SPECS = (
    {
        "title": "Agent-workflows canonical core",
        "technique_ids": ("AOA-T-0001", "AOA-T-0004", "AOA-T-0014"),
        "review_doc": SELECTION_REVIEW_DOCS["agent_workflows_core"],
        "note": "Canonical workflow backbone, intent-chain specialization, and bounded execution slicing for the current agent-workflows core.",
    },
    {
        "title": "Published-summary cluster",
        "technique_ids": ("AOA-T-0006", "AOA-T-0008", "AOA-T-0010", "AOA-T-0011"),
        "review_doc": SELECTION_REVIEW_DOCS["published_summary"],
        "note": "Storage, remediation, integrity, and rendering policy for published summary systems.",
    },
    {
        "title": "Evaluation-chain pair",
        "technique_ids": ("AOA-T-0003", "AOA-T-0007"),
        "review_doc": SELECTION_REVIEW_DOCS["evaluation_chain"],
        "note": "Summary-contract production plus staged promotion from observation to narrow enforcement.",
    },
    {
        "title": "Docs boundary pair",
        "technique_ids": ("AOA-T-0002", "AOA-T-0009"),
        "review_doc": SELECTION_REVIEW_DOCS["docs_boundary"],
        "note": "Repository-wide document-role layout plus lightweight entrypoint snapshot discipline.",
    },
    {
        "title": "Intent-chain pair",
        "technique_ids": ("AOA-T-0004", "AOA-T-0005"),
        "review_doc": SELECTION_REVIEW_DOCS["intent_chain"],
        "note": "Artifact-first intent normalization and dry-run contract validation plus safe rollout of one new intent type on top of that chain.",
    },
    {
        "title": "Instruction-surface cluster",
        "technique_ids": ("AOA-T-0012", "AOA-T-0013", "AOA-T-0027", "AOA-T-0024", "AOA-T-0029", "AOA-T-0030"),
        "review_doc": SELECTION_REVIEW_DOCS["instruction_surface"],
        "note": "Fragment-first composition into one generated context artifact plus local single-source fan-out, managed-target propagation, upstream mirroring with provenance, hierarchical rule loading, and fragment-first source partitioning for adjacent instruction-facing surfaces.",
    },
    {
        "title": "Skill-support cluster",
        "technique_ids": ("AOA-T-0015", "AOA-T-0017", "AOA-T-0016"),
        "review_doc": SELECTION_REVIEW_DOCS["skill_support"],
        "note": "Boundary-contract evaluation, invariant coverage broadening, and semantic scoping for the current skill-support seam cluster.",
    },
    {
        "title": "KAG/source-lift family",
        "technique_ids": ("AOA-T-0018", "AOA-T-0019", "AOA-T-0020", "AOA-T-0021", "AOA-T-0022"),
        "review_doc": SELECTION_REVIEW_DOCS["kag_source_lift"],
        "note": "Section lift, metadata spine, provenance lift, bounded relation lift, and markdown-first caution lift for the current reusable KAG/source-lift family.",
    },
)
DOMAIN_START_SPECS = (
    {
        "domain": "agent-workflows",
        "lead_ids": ("AOA-T-0001",),
        "review_docs": (SELECTION_REVIEW_DOCS["agent_workflows_core"],),
        "note": "Start with the canonical workflow contract, then add narrower chain helpers only when the path gets more specialized.",
    },
    {
        "domain": "docs",
        "lead_ids": ("AOA-T-0002", "AOA-T-0009", "AOA-T-0012"),
        "review_docs": (
            SELECTION_REVIEW_DOCS["docs_boundary"],
            SELECTION_REVIEW_DOCS["instruction_surface"],
        ),
        "note": "Start with the canonical document-role layout, then inspect the docs boundary pair or instruction-surface cluster when generation, source ownership, and entrypoint discipline become the next bounded question.",
    },
    {
        "domain": "evaluation",
        "lead_ids": ("AOA-T-0003", "AOA-T-0006", "AOA-T-0007", "AOA-T-0008", "AOA-T-0010", "AOA-T-0011"),
        "review_docs": (
            SELECTION_REVIEW_DOCS["published_summary"],
            SELECTION_REVIEW_DOCS["evaluation_chain"],
        ),
        "note": "Start with the canonical summary/storage backbone, then move into remediation, integrity, or rendering policy as downstream needs appear.",
    },
    {
        "domain": "system-recovery",
        "lead_ids": ("AOA-T-0097",),
        "review_docs": (),
        "note": "Start with bounded degraded continuation and regrounding posture before inventing wider repair or runtime-control doctrine.",
    },
    {
        "domain": "validation-patterns",
        "lead_ids": ("AOA-T-0098",),
        "review_docs": (),
        "note": "Start with receipt-led failure analysis when the next question is what changed, why, and how improvement should be checked without widening into a full eval bundle.",
    },
    {
        "domain": "history",
        "lead_ids": ("AOA-T-0044", "AOA-T-0053"),
        "review_docs": (),
        "note": "Start with the canonical post-capture history pair: `AOA-T-0044` for readable transcript artifacts and `AOA-T-0053` for derivative local lookup over saved artifacts; widen to capture or witness layers only when those become the real bounded question.",
    },
)
COMMON_MOVE_BASIS_DIRECT_RELATION = "direct_relation"
COMMON_MOVE_BASIS_DOMAIN_START = "domain_start"
COMMON_MOVE_SPECS = (
    {
        "prompt": "I have a summary producer and need history/trend-safe storage",
        "target_id": "AOA-T-0006",
        "basis_type": COMMON_MOVE_BASIS_DIRECT_RELATION,
        "anchor_ids": ("AOA-T-0003",),
        "note": "Natural next move after a stable summary contract such as `AOA-T-0003`.",
    },
    {
        "prompt": "I already publish summaries and need one remediation backlog",
        "target_id": "AOA-T-0008",
        "basis_type": COMMON_MOVE_BASIS_DIRECT_RELATION,
        "anchor_ids": ("AOA-T-0006",),
        "note": "Use when several latest summaries should collapse into one bounded follow-up surface.",
    },
    {
        "prompt": "I already publish summaries and need one trust verdict",
        "target_id": "AOA-T-0010",
        "basis_type": COMMON_MOVE_BASIS_DIRECT_RELATION,
        "anchor_ids": ("AOA-T-0006",),
        "note": "Use when several consumers should not duplicate integrity checks independently.",
    },
    {
        "prompt": "I need strict-vs-optional rendering policy",
        "target_id": "AOA-T-0011",
        "basis_type": COMMON_MOVE_BASIS_DIRECT_RELATION,
        "anchor_ids": ("AOA-T-0010",),
        "note": "Use when supporting summaries should stay visible but non-fatal in one consumer.",
    },
    {
        "prompt": "I need doc-role separation",
        "target_id": "AOA-T-0002",
        "basis_type": COMMON_MOVE_BASIS_DOMAIN_START,
        "domain": "docs",
        "note": "Start here when the repository needs explicit canonical homes and update-routing rules.",
    },
    {
        "prompt": "I need top-level docs to stay short",
        "target_id": "AOA-T-0009",
        "basis_type": COMMON_MOVE_BASIS_DIRECT_RELATION,
        "anchor_ids": ("AOA-T-0002",),
        "note": "Inspect alongside `AOA-T-0002` when entrypoint docs start duplicating operational detail.",
    },
)
SHADOW_REVIEW_DOCS = {
    "published_summary": f"{SHADOW_REVIEW_PACKET_DIR}/PUBLISHED_SUMMARY_SHADOW_REVIEW.md",
    "evaluation_chain": f"{SHADOW_REVIEW_PACKET_DIR}/EVALUATION_CHAIN_SHADOW_REVIEW.md",
}
SHADOW_WORKING_SET_SPECS = (
    {
        "title": "Published-summary shadow cluster",
        "technique_ids": ("AOA-T-0006", "AOA-T-0008", "AOA-T-0010", "AOA-T-0011"),
        "review_doc": SHADOW_REVIEW_DOCS["published_summary"],
        "note": "Canonical storage, remediation, integrity, and rendering techniques whose caution language now shares one bounded shadow watch surface.",
    },
    {
        "title": "Evaluation-chain shadow pair",
        "technique_ids": ("AOA-T-0003", "AOA-T-0007"),
        "review_doc": SHADOW_REVIEW_DOCS["evaluation_chain"],
        "note": "Canonical producer-contract and staged-enforcement techniques whose caution language now shares one bounded evaluation-chain shadow watch surface.",
    },
)
SHADOW_COMMON_QUESTION_SPECS = (
    {
        "prompt": "I need to check whether the latest summary looks clean while history trust is already broken",
        "target_id": "AOA-T-0006",
        "note": "Start with the latest-plus-history storage contract and its alias/history false-confidence seam.",
    },
    {
        "prompt": "I need to stop remediation output from drifting into integrity or rendering policy",
        "target_id": "AOA-T-0008",
        "note": "Inspect the bounded remediation rollup before widening backlog language into trust verdicts or renderer instructions.",
    },
    {
        "prompt": "I need to keep a diagnostic helper from turning into an implicit enforcement gate",
        "target_id": "AOA-T-0010",
        "note": "Inspect the diagnostic-only trust layer and its optional-check noise seam before any stricter rollout decision.",
    },
    {
        "prompt": "I need optional-source warnings to stay visible without becoming noisy or package-shaped",
        "target_id": "AOA-T-0011",
        "note": "Inspect the required-versus-optional rendering policy and its warning-fatigue plus package-appendix seam.",
    },
    {
        "prompt": "I need a summary producer to stay diagnostic instead of collapsing back into log scraping",
        "target_id": "AOA-T-0003",
        "note": "Inspect the summary-contract producer and its false-success plus thin-failure-context seam before widening storage or rollout detail.",
    },
    {
        "prompt": "I need staged enforcement to stay narrow instead of leaking into hidden strictness",
        "target_id": "AOA-T-0007",
        "note": "Inspect the staged-promotion pattern and its shallow-history plus strict-surface leakage seam before adding more rollout telemetry.",
    },
)
REPO_DOC_SURFACE_GROUP_ORDER = (
    "entrypoint/map",
    "canon/authority",
    "contribution/policy",
    "status/release",
)
REPO_DOC_SURFACE_GROUP_SPECS = (
    {
        "group": "entrypoint/map",
        "heading": "Entrypoint / Map",
        "note": "Open these first when the question is where to start or which public repo map or self-serve entrypoint should anchor the next read.",
    },
    {
        "group": "canon/authority",
        "heading": "Canon / Authority",
        "note": "Use these when the question is what the repository may claim, how technique canon is shaped, where root surfaces belong, or which corpus map is authoritative.",
    },
    {
        "group": "contribution/policy",
        "heading": "Contribution / Policy",
        "note": "Use these when the question is how to contribute safely, publicly, and within the repo's current review posture.",
    },
    {
        "group": "status/release",
        "heading": "Status / Release",
        "note": "Use these when the question is what changed, what is currently unreleased, and how the public release path is validated.",
    },
)
REPO_DOC_NAVIGATION_SPECS = (
    {
        "question": "Where should I start if I am new to the repository?",
        "doc_ids": ("readme", "charter", "start_here", "technique_index"),
        "note": "Use the root README only for purpose and first handoff, then use the Charter, Start Here, and technique index for bounded navigation.",
    },
    {
        "question": "Where is the repo-only self-serve route before deeper guides split out?",
        "doc_ids": ("start_here", "docs_readme"),
        "note": "Use Start Here for the shortest repo-owned route, then open the docs map only when you need the deeper guide and generated-surface tree.",
    },
    {
        "question": "Where is this repository positioned inside the AoA layer map?",
        "doc_ids": ("charter", "ecosystem_context", "start_here"),
        "note": "Use the Charter for the repository authority boundary, Ecosystem Context for the layer-position note, then Start Here for the shortest bounded route through the rest of the public surface.",
    },
    {
        "question": "Where do system design and agent-surface design live?",
        "doc_ids": ("design", "design_agents", "agents", "root_surface_law"),
        "note": "Use DESIGN for practice-canon system form, DESIGN.AGENTS for the agent-facing mesh form, AGENTS for operational route law, and Root Surface Law for placement.",
    },
    {
        "question": "Where do root and docs-root placement rules live?",
        "doc_ids": ("root_surface_law", "charter", "docs_readme"),
        "note": "Use Root Surface Law before adding or moving root or docs-root surfaces, with the Charter and docs map as supporting route context.",
    },
    {
        "question": "Where do technique atom and topology contracts live?",
        "doc_ids": (
            "technique_atom_contract",
            "technique_topology_contract",
            "technique_tree_contract",
            "technique_index",
        ),
        "note": "Use the atom contract to decide whether a candidate is one technique, the topology contract to classify it, the tree contract to reason about path architecture, and the technique index to inspect the live corpus.",
    },
    {
        "question": "Where do contribution rules and PR boundaries live?",
        "doc_ids": ("contributing", "agents"),
        "note": "Use CONTRIBUTING for the public PR path and AGENTS for the repo's public-safe PLAN -> DIFF -> VERIFY -> REPORT doctrine.",
    },
    {
        "question": "Where do public-safety expectations and contributor conduct live?",
        "doc_ids": ("security", "agents", "code_of_conduct"),
        "note": "Use SECURITY for disclosure and hygiene, AGENTS for public-repo authoring discipline, and the Code of Conduct for collaboration expectations.",
    },
    {
        "question": "Where do direction, obligations, release flow, and status history live?",
        "doc_ids": ("roadmap", "questbook", "changelog", "docs_releasing"),
        "note": "Use ROADMAP for live direction, QUESTBOOK for durable obligations, CHANGELOG for release history, and RELEASING for the bounded validation path behind public corpus updates.",
    },
)
REPO_DOC_SURFACE_SPECS = (
    {
        "doc_id": "readme",
        "doc_path": "README.md",
        "surface_group": "entrypoint/map",
        "bounded_role": "root entrypoint for repository purpose, scope, and first handoff",
    },
    {
        "doc_id": "charter",
        "doc_path": "CHARTER.md",
        "surface_group": "canon/authority",
        "bounded_role": "root authority boundary for the reusable practice canon and standalone plus AoA organ posture",
    },
    {
        "doc_id": "design",
        "doc_path": "DESIGN.md",
        "surface_group": "canon/authority",
        "bounded_role": "root system-form surface for the reusable practice canon and standalone plus AoA organ posture",
    },
    {
        "doc_id": "design_agents",
        "doc_path": "DESIGN.AGENTS.md",
        "surface_group": "canon/authority",
        "bounded_role": "root agent-surface design form for the AGENTS mesh and portable agent guidance",
    },
    {
        "doc_id": "start_here",
        "doc_path": "docs/START_HERE.md",
        "surface_group": "entrypoint/map",
        "bounded_role": "repo-owned self-serve entrypoint for route selection, corpus posture, and stay-here versus leave-here decisions",
    },
    {
        "doc_id": "ecosystem_context",
        "doc_path": "docs/ECOSYSTEM_CONTEXT.md",
        "surface_group": "entrypoint/map",
        "bounded_role": "repo-owned positioning note for the AoA ontology spine, neighboring layer boundaries, and why scenario-level method stays in aoa-playbooks",
    },
    {
        "doc_id": "root_surface_law",
        "doc_path": "docs/ROOT_SURFACE_LAW.md",
        "surface_group": "canon/authority",
        "bounded_role": "root and docs-root placement law for keeping public entry surfaces compact and owner-routed",
    },
    {
        "doc_id": "technique_atom_contract",
        "doc_path": "docs/TECHNIQUE_ATOM_CONTRACT.md",
        "surface_group": "canon/authority",
        "bounded_role": "canonical contract for one atomic executable technique rather than a skill, playbook, chain, or workflow object",
    },
    {
        "doc_id": "technique_topology_contract",
        "doc_path": "docs/TECHNIQUE_TOPOLOGY_CONTRACT.md",
        "surface_group": "canon/authority",
        "bounded_role": "classification topology contract for scaling the technique corpus beyond overloaded domains or flat categories",
    },
    {
        "doc_id": "technique_tree_contract",
        "doc_path": "docs/TECHNIQUE_TREE_CONTRACT.md",
        "surface_group": "canon/authority",
        "bounded_role": "corpus tree contract for current scalable technique path architecture across trunks, shelves, and leaf bundles",
    },
    {
        "doc_id": "technique_index",
        "doc_path": "TECHNIQUE_INDEX.md",
        "surface_group": "canon/authority",
        "bounded_role": "public corpus map by status, technique id, and domain",
    },
    {
        "doc_id": "docs_readme",
        "doc_path": "docs/README.md",
        "surface_group": "entrypoint/map",
        "bounded_role": "docs-layer map for deeper guides, generated surfaces, and recommended reading paths after the main entrypoint",
    },
    {
        "doc_id": "agents",
        "doc_path": "AGENTS.md",
        "surface_group": "contribution/policy",
        "bounded_role": "contributor doctrine for public-safe planning, focused diffs, verification, and reporting",
    },
    {
        "doc_id": "contributing",
        "doc_path": "CONTRIBUTING.md",
        "surface_group": "contribution/policy",
        "bounded_role": "public contribution path, review criteria, and status-transition rules",
    },
    {
        "doc_id": "security",
        "doc_path": "SECURITY.md",
        "surface_group": "contribution/policy",
        "bounded_role": "private reporting route and public-hygiene security expectations",
    },
    {
        "doc_id": "code_of_conduct",
        "doc_path": "CODE_OF_CONDUCT.md",
        "surface_group": "contribution/policy",
        "bounded_role": "public collaboration and enforcement expectations for contributors",
    },
    {
        "doc_id": "roadmap",
        "doc_path": "ROADMAP.md",
        "surface_group": "status/release",
        "bounded_role": "live repo-level direction and horizon posture for technique-canon growth",
    },
    {
        "doc_id": "questbook",
        "doc_path": "QUESTBOOK.md",
        "surface_group": "status/release",
        "bounded_role": "compact root index for durable technique-canon obligations that should survive the current diff",
    },
    {
        "doc_id": "changelog",
        "doc_path": "CHANGELOG.md",
        "surface_group": "status/release",
        "bounded_role": "release and unreleased status history for the public corpus",
    },
    {
        "doc_id": "docs_releasing",
        "doc_path": "docs/RELEASING.md",
        "surface_group": "status/release",
        "bounded_role": "bounded release flow and validation path for public docs and technique updates",
    },
)

SECTION_STATUS = {
    "Canonical techniques": "canonical",
    "Promoted techniques": "promoted",
    "Deprecated techniques": "deprecated",
}

STATUS_SECTION = {value: key for key, value in SECTION_STATUS.items()}
DOMAIN_VALUES = {
    "agent-workflows",
    "docs",
    "evaluation",
    "system-recovery",
    "validation-patterns",
    "history",
}
DOMAIN_ORDER = (
    "agent-workflows",
    "docs",
    "evaluation",
    "system-recovery",
    "validation-patterns",
    "history",
)
TREE_TRUNK_ORDER = (
    "execution",
    "instruction",
    "proof",
    "continuity",
    "governance",
    "knowledge-lift",
    "ingest",
    "recovery",
    "history",
    "tool-use",
)
TREE_TRUNK_VALUES = set(TREE_TRUNK_ORDER)
TECHNIQUE_BUNDLE_SOURCE_GLOB = "techniques/**/TECHNIQUE.md"
KIND_ORDER = (
    "workflow",
    "guardrail",
    "validation",
    "composition",
    "distribution",
    "artifact",
    "lift",
    "discovery",
    "handoff",
    "ingest",
    "assessment",
    "recovery",
)
KIND_VALUES = set(KIND_ORDER)
KIND_INDEX = {kind: index for index, kind in enumerate(KIND_ORDER)}
TECHNIQUE_KIND_REGISTRY_PATH = "config/technique_kind_registry.yaml"
TECHNIQUE_FAMILY_SCOUT_PATH = f"{TECHNIQUE_REFORM_INGRESS_DIR}/config/technique_family_scout.yaml"
TECHNIQUE_TOPOLOGY_AXES_PATH = f"{TECHNIQUE_REFORM_INGRESS_DIR}/config/technique_topology_axes.yaml"
TECHNIQUE_KIND_OVERLAY_PATH = f"{TECHNIQUE_REFORM_INGRESS_DIR}/data/technique_kind_overlay.yaml"
TECHNIQUE_KIND_OVERLAY_CSV_PATH = f"{TECHNIQUE_REFORM_INGRESS_DIR}/data/technique_kind_overlay.csv"
TOPOLOGY_SCOUT_AXIS_ORDER = (
    "capability_class",
    "substrate",
    "execution_profile",
    "risk_posture",
)
TOPOLOGY_SCOUT_AXIS_CARDINALITY = {
    "capability_class": "one-or-more",
    "substrate": "one-or-more",
    "execution_profile": "exactly-one",
    "risk_posture": "one-or-more",
}
KIND_MANIFEST_VERSION = 1
KIND_MANIFEST_SOURCE_OF_TRUTH = {
    "kind_registry": TECHNIQUE_KIND_REGISTRY_PATH,
    "catalog": "generated/technique_catalog.json",
    "bundles": TECHNIQUE_BUNDLE_SOURCE_GLOB,
}
FAMILY_SCOUT_REPORT_VERSION = 1
FAMILY_SCOUT_SOURCE_OF_TRUTH = {
    "family_scout": TECHNIQUE_FAMILY_SCOUT_PATH,
    "kind_registry": TECHNIQUE_KIND_REGISTRY_PATH,
    "kind_overlay": TECHNIQUE_KIND_OVERLAY_PATH,
    "catalog": "generated/technique_catalog.json",
}
FAMILY_SCOUT_AUTHORITY_NOTE = (
    "This report is scout-only, non-authoritative, and weaker than bundle frontmatter. "
    "It must not be treated as schema truth, frontmatter truth, or automatic remap authority."
)
KIND_AMBIGUITY_AUTHORITY_NOTE = (
    "This audit is scout-only, non-authoritative, and weaker than bundle frontmatter. "
    "Use it to review tie-break seams, not to remap techniques automatically."
)
TOPOLOGY_SCOUT_REPORT_VERSION = 1
TOPOLOGY_SCOUT_SOURCE_OF_TRUTH = {
    "axis_registry": TECHNIQUE_TOPOLOGY_AXES_PATH,
    "family_scout": TECHNIQUE_FAMILY_SCOUT_PATH,
    "kind_overlay": TECHNIQUE_KIND_OVERLAY_PATH,
    "catalog": "generated/technique_catalog.json",
}
TOPOLOGY_SCOUT_AUTHORITY_NOTE = (
    "This projection is scout-only, non-authoritative, and weaker than bundle frontmatter. "
    "It must not be treated as schema truth, frontmatter truth, or automatic remap authority."
)
TREE_PROJECTION_REPORT_VERSION = 1
TREE_PROJECTION_TARGET_PATH_SHAPE = "techniques/<trunk>/<shelf>/<technique-slug>/TECHNIQUE.md"
TREE_PROJECTION_SOURCE_OF_TRUTH = {
    "tree_contract": "docs/TECHNIQUE_TREE_CONTRACT.md",
    "family_review": "mechanics/distillation/parts/technique-reform-ingress/reviews/first-family-shelf-review-pack.md",
    "family_scout": TECHNIQUE_FAMILY_SCOUT_PATH,
    "kind_overlay": TECHNIQUE_KIND_OVERLAY_PATH,
    "catalog": "generated/technique_catalog.json",
}
TREE_PROJECTION_AUTHORITY_NOTE = (
    "This projection is non-authoritative and weaker than authored bundle meaning. "
    "It is a placement review surface only; it must not be treated as frontmatter truth, "
    "schema truth, or automatic path migration authority."
)
TREE_PROJECTION_REVIEW_STATUS_ORDER = (
    "pilot-candidate",
    "candidate",
    "boundary-watch",
    "split-review-needed",
    "singleton-hold",
    "unassigned-hold",
)
TREE_FAMILY_PLACEMENT = {
    "agent-workflows-core": ("execution", "candidate"),
    "intent-chain": ("execution", "candidate"),
    "docs-boundary": ("instruction", "candidate"),
    "instruction-surface": ("instruction", "pilot-candidate"),
    "evaluation-chain": ("proof", "candidate"),
    "published-summary": ("proof", "candidate"),
    "skill-support": ("proof", "candidate"),
    "kag-source-lift": ("knowledge-lift", "pilot-candidate"),
    "history-artifacts": ("history", "candidate"),
    "runtime-truth-lifecycle": ("execution", "boundary-watch"),
    "capability-registry": ("instruction", "boundary-watch"),
    "capability-boundary": ("instruction", "boundary-watch"),
    "skill-discovery": ("instruction", "boundary-watch"),
    "ready-work-graphs": ("execution", "candidate"),
    "review-compaction": ("continuity", "pilot-candidate"),
    "handoff-continuation": ("continuity", "pilot-candidate"),
    "tool-gateway": ("tool-use", "singleton-hold"),
    "approval-evidence": ("governance", "boundary-watch"),
    "review-evidence": ("proof", "boundary-watch"),
    "media-ingest": ("ingest", "pilot-candidate"),
    "donor-harvest": ("continuity", "candidate"),
    "decision-routing": ("governance", "candidate"),
    "diagnosis-repair": ("recovery", "pilot-candidate"),
    "automation-governance": ("governance", "split-review-needed"),
    "owner-truth-closeout": ("proof", "boundary-watch"),
    "antifragility-recovery": ("recovery", "candidate"),
}
TREE_ID_PLACEMENT = {
    "AOA-T-0086": ("governance", "automation-readiness", "candidate"),
    "AOA-T-0087": ("governance", "automation-readiness", "candidate"),
    "AOA-T-0088": ("governance", "automation-readiness", "candidate"),
    "AOA-T-0089": ("governance", "promotion-boundary", "candidate"),
    "AOA-T-0090": ("governance", "promotion-boundary", "candidate"),
    "AOA-T-0102": ("governance", "promotion-boundary", "candidate"),
    "AOA-T-0101": ("governance", "practice-adoption-lifecycle", "candidate"),
    "AOA-T-0103": ("governance", "practice-adoption-lifecycle", "candidate"),
    "AOA-T-0104": ("governance", "practice-adoption-lifecycle", "candidate"),
    "AOA-T-0065": ("tool-use", "tool-gateway", "candidate"),
}
TREE_REVIEW_STATUS_STOP_LINES = {
    "pilot-candidate": "Candidate for first direct-read migration review; do not move paths from projection alone.",
    "candidate": "Use as placement evidence only; direct bundle reading is required before migration.",
    "boundary-watch": "Review split, merge, owner, proof, or governance boundary before migration.",
    "split-review-needed": "Split or merge this shelf before accepting it as a tree migration pilot.",
    "singleton-hold": "Hold until more neighboring techniques land or direct review justifies a singleton shelf.",
    "unassigned-hold": "Hold until the family assignment is reviewed; do not infer a path automatically.",
}
KIND_AMBIGUITY_SEAMS = (
    ("workflow", "guardrail"),
    ("validation", "assessment"),
    ("artifact", "lift"),
    ("composition", "distribution"),
    ("handoff", "workflow"),
)
KIND_AMBIGUITY_KEYWORDS = {
    ("workflow", "guardrail"): {
        "workflow": ("workflow", "step", "steps", "plan", "loop", "process", "procedure", "execute"),
        "guardrail": ("guardrail", "gate", "gated", "approval", "reject", "block", "fail-closed", "policy"),
    },
    ("validation", "assessment"): {
        "validation": ("validation", "validate", "proof", "verify", "integrity", "smoke", "check", "health"),
        "assessment": ("assessment", "classify", "classification", "diagnosis", "diagnose", "route", "matrix", "decision"),
    },
    ("artifact", "lift"): {
        "artifact": ("artifact", "snapshot", "transcript", "index", "capture", "record", "storage", "spec"),
        "lift": ("lift", "derived", "derive", "manifest", "surface", "projection", "overlay", "export"),
    },
    ("composition", "distribution"): {
        "composition": ("composition", "compose", "composed", "assembly", "assemble", "merge", "layer", "precedence"),
        "distribution": ("distribution", "mirror", "mirroring", "fan-out", "propagate", "propagation", "parity", "publish"),
    },
    ("handoff", "workflow"): {
        "handoff": ("handoff", "checkpoint", "receipt", "packet", "resume", "continuation", "mailbox", "episode"),
        "workflow": ("workflow", "step", "steps", "plan", "loop", "process", "procedure", "execute"),
    },
}
TOPOLOGY_CAPABILITY_BY_KIND = {
    "workflow": ("plan",),
    "guardrail": ("choose",),
    "validation": ("validate",),
    "composition": ("coordinate", "transform"),
    "distribution": ("coordinate",),
    "artifact": ("write",),
    "lift": ("transform", "summarize"),
    "discovery": ("read", "choose"),
    "handoff": ("handoff",),
    "ingest": ("read", "transform"),
    "assessment": ("compare", "choose"),
    "recovery": ("recover",),
}
TOPOLOGY_SUBSTRATE_BY_DOMAIN = {
    "agent-workflows": ("conversation", "tool-surfaces"),
    "docs": ("docs",),
    "evaluation": ("tests",),
    "system-recovery": ("runtime-state",),
    "validation-patterns": ("tests",),
    "history": ("history",),
}
TOPOLOGY_EXECUTION_PROFILE_BY_KIND = {
    "workflow": "medium-agent",
    "guardrail": "small-agent",
    "validation": "small-agent",
    "composition": "medium-agent",
    "distribution": "orchestration-required",
    "artifact": "small-agent",
    "lift": "small-agent",
    "discovery": "tiny-card",
    "handoff": "small-agent",
    "ingest": "orchestration-required",
    "assessment": "medium-agent",
    "recovery": "orchestration-required",
}
TOPOLOGY_KEYWORD_RULES = {
    "capability_class": {
        "observe": ("observe", "inspect", "surface", "visibility", "visible"),
        "read": ("read", "source", "lookup", "discover"),
        "interpret": ("interpret", "explain", "meaning", "doctrine"),
        "plan": ("plan", "queue", "graph", "next", "roadmap", "task"),
        "choose": ("choose", "select", "route", "triage", "gate", "approval"),
        "transform": ("transform", "normalize", "convert", "derive", "lift", "render"),
        "write": ("write", "record", "artifact", "note", "spec", "template", "card"),
        "mutate": ("mutate", "change", "edit", "apply", "start", "stop", "publish"),
        "validate": ("validate", "check", "proof", "smoke", "integrity", "health"),
        "compare": ("compare", "contrast", "matrix", "versus", "taxonomy"),
        "summarize": ("summary", "summarize", "compact", "snapshot", "capsule"),
        "handoff": ("handoff", "checkpoint", "resume", "packet", "continuation"),
        "recover": ("recover", "repair", "rollback", "degraded", "reground", "failure"),
        "coordinate": ("coordinate", "parity", "mirror", "distribution", "propagate"),
        "communicate": ("request", "message", "ask", "public", "share", "answer"),
        "learn-from-artifact": ("harvest", "donor", "progression", "retention", "adoption"),
    },
    "substrate": {
        "code": ("code", "implementation", "patch"),
        "tests": ("test", "tests", "smoke", "validation", "invariant", "health"),
        "docs": ("doc", "docs", "markdown", "guide", "readme"),
        "instructions": ("instruction", "context", "prompt", "rule", "profile"),
        "config": ("config", "schema", "manifest", "frontmatter", "registry"),
        "shell": ("shell", "command", "cli", "startup"),
        "api": ("api", "endpoint", "service", "connector"),
        "data": ("data", "dataset", "row", "store", "ledger", "registry"),
        "media": ("media", "ocr", "image", "screenshot", "vision", "telegram"),
        "ui": ("interface", "layout", "screen"),
        "conversation": ("conversation", "chat", "message", "comment", "request"),
        "history": ("history", "transcript", "session", "commit", "lineage"),
        "memory-adjacent-artifacts": ("memory", "recall", "memo"),
        "graph-adjacent-artifacts": ("graph", "relations", "dependency", "topology"),
        "tool-surfaces": ("tool", "mcp", "capability", "registry", "command"),
        "runtime-state": ("runtime", "service", "host", "startup", "stop", "degraded"),
        "human-approval-surfaces": ("approval", "consent", "review", "public-share"),
    },
    "risk_posture": {
        "mutating": ("mutate", "change", "edit", "apply", "start", "stop", "publish"),
        "public-share": ("public", "share", "publish", "release", "sanitization"),
        "security-sensitive": ("secret", "auth", "credential", "security"),
        "irreversible": ("irreversible", "delete", "drop", "permanent"),
        "approval-required": ("approval", "consent", "gate", "public-share"),
        "degraded-mode": ("degraded", "failure", "recover", "repair", "rollback"),
        "external-evidence": ("external", "donor", "web", "upstream", "source-backed"),
    },
}
RELATION_TYPE_ORDER = (
    "requires",
    "complements",
    "supersedes",
    "conflicts_with",
    "used_together_for",
    "derived_from",
    "shares_contract_with",
)
SUPPORT_PATH_RE = re.compile(r"(?<!\w)(?:checks|examples|notes)/[A-Za-z0-9._/-]+\.md")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
SECTION_RE = re.compile(r"^[ ]{0,3}## (.+)$", re.MULTILINE)
SUBSECTION_RE = re.compile(r"^[ ]{0,3}### (.+)$", re.MULTILINE)
FENCE_DELIMITER_RE = re.compile(r"^[ ]{0,3}(`{3,}|~{3,})")
NOTE_FIELD_RE = re.compile(r"- ([a-z0-9][a-z0-9_ /-]*):\s*(.*)")
TEMPLATE_FIELD_RE = re.compile(r"- ([^:]+):\s*(.*)")
TEMPLATE_CHECKBOX_RE = re.compile(r"- \[( |x|X)\] (.*)")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
INLINE_CODE_RE = re.compile(r"`([^`]+)`")
LEADING_LIST_MARKER_RE = re.compile(r"^(?:[-*]\s+|\d+\.\s+)")
WHITESPACE_RE = re.compile(r"\s+")
EVIDENCE_KIND_BY_NAME = {
    "origin-evidence.md": "origin_evidence",
    "second-context-adaptation.md": "second_context",
    "canonical-readiness.md": "canonical_readiness",
    "adverse-effects-review.md": "adverse_effects_review",
    "external-origin.md": "external_origin",
    "external-import-review.md": "external_review",
}
ADVERSE_EFFECTS_REVIEW_PATH = "notes/adverse-effects-review.md"
SECTION_MANIFEST_VERSION = 1
SECTION_MANIFEST_SOURCE_OF_TRUTH = "markdown-technique-sections-v1"
SECTION_SURFACE_VERSION = 1
SECTION_SURFACE_SOURCE_OF_TRUTH = {
    "technique_markdown": TECHNIQUE_BUNDLE_SOURCE_GLOB,
    "sections": list(REQUIRED_SECTIONS),
}
SECTION_KEY_BY_HEADING = {
    "Intent": "intent",
    "When to use": "when_to_use",
    "When not to use": "when_not_to_use",
    "Inputs": "inputs",
    "Outputs": "outputs",
    "Core procedure": "core_procedure",
    "Contracts": "contracts",
    "Risks": "risks",
    "Validation": "validation",
    "Adaptation notes": "adaptation_notes",
    "Public sanitization notes": "public_sanitization_notes",
    "Example": "example",
    "Checks": "checks",
    "Promotion history": "promotion_history",
    "Future evolution": "future_evolution",
}
CAPSULE_VERSION = 1
CAPSULE_SOURCE_OF_TRUTH = "frontmatter-summary+markdown-technique-capsules-v1"
CAPSULE_MIN_FIELDS = (
    "id",
    "name",
    "summary",
    "one_line_intent",
    "use_when_short",
    "do_not_use_short",
    "core_contract_short",
    "main_risk_short",
    "validation_short",
    "technique_path",
)
CHECKLIST_MANIFEST_VERSION = 1
CHECKLIST_MANIFEST_SOURCE_OF_TRUTH = "markdown-checklists-v1"
EXAMPLE_MANIFEST_VERSION = 1
EXAMPLE_MANIFEST_SOURCE_OF_TRUTH = "markdown-examples-v1"
EVIDENCE_NOTE_MANIFEST_VERSION = 1
EVIDENCE_NOTE_MANIFEST_SOURCE_OF_TRUTH = "markdown-evidence-notes-v1"
GITHUB_REVIEW_TEMPLATE_MANIFEST_VERSION = 1
GITHUB_REVIEW_TEMPLATE_MANIFEST_SOURCE_OF_TRUTH = "github-review-templates-v1"
SEMANTIC_REVIEW_MANIFEST_VERSION = 1
SEMANTIC_REVIEW_MANIFEST_SOURCE_OF_TRUTH = "markdown-semantic-reviews-v1"
SHADOW_REVIEW_MANIFEST_VERSION = 1
SHADOW_REVIEW_MANIFEST_SOURCE_OF_TRUTH = "markdown-shadow-reviews-v1"
REPO_DOC_SURFACE_MANIFEST_VERSION = 1
REPO_DOC_SURFACE_MANIFEST_SOURCE_OF_TRUTH = "markdown-repo-doc-surfaces-v1"
QUESTBOOK_PATH = Path("QUESTBOOK.md")
QUESTS_PATH = Path("quests")
QUESTBOOK_INTEGRATION_PATH = (
    Path("mechanics")
    / "growth-cycle"
    / "parts"
    / "questbook-integration"
    / "README.md"
)
QUEST_SCHEMA_PATH = Path("schemas") / "quest.schema.json"
QUEST_DISPATCH_SCHEMA_PATH = Path("schemas") / "quest_dispatch.schema.json"
QUEST_CATALOG_PATH = Path("generated") / "quest_catalog.min.json"
QUEST_DISPATCH_PATH = Path("generated") / "quest_dispatch.min.json"
QUEST_CATALOG_EXAMPLE_PATH = Path("generated") / "quest_catalog.min.example.json"
QUEST_DISPATCH_EXAMPLE_PATH = Path("generated") / "quest_dispatch.min.example.json"
QUEST_SOURCE_LANES = ("techniques", "agon")
QUEST_LIFECYCLE_STATES = (
    "captured",
    "triaged",
    "ready",
    "active",
    "blocked",
    "reanchor",
    "done",
    "dropped",
)
QUEST_MARKDOWN_CONTRACT_MARKER = "source_contract: quest_markdown_contract_v1"
QUEST_MARKDOWN_REQUIRED_HEADINGS = (
    "## Quest",
    "## Owner Route",
    "## Next Action",
    "## Acceptance Evidence",
    "## Stop-lines",
)
QUEST_MARKDOWN_ID_LANES = {
    "AOT-Q-AGON-": "agon",
}
QUEST_MARKDOWN_KEY_RE = re.compile(r"^(AOT-Q-[A-Z]+-\d+)")
QUEST_H1_RE = re.compile(r"^[ ]{0,3}# (.+)$", re.MULTILINE)
FOUNDATION_QUEST_IDS = (
    "AOA-TECH-Q-0001",
    "AOA-TECH-Q-0002",
    "AOA-TECH-Q-0003",
    "AOA-TECH-Q-0004",
)
QUEST_IDS = FOUNDATION_QUEST_IDS
QUESTBOOK_REQUIRED_INDEX_TOKENS = (
    "donor-refinery",
    "generated/source alignment",
    "quests/<lane>/<state>/",
    "Frontier",
    "Near",
    "Harvest candidates",
)
CLOSED_QUEST_STATES = {"done", "dropped"}
QUESTBOOK_REQUIRED_INTEGRATION_TOKENS = (
    "without turning the repo into a second donor backlog",
    "docs/START_HERE.md",
    "TECHNIQUE_INDEX.md",
    "mechanics/audit/parts/promotion-readiness-matrix/README.md",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/README.md",
    "mechanics/distillation/parts/donor-refinery/README.md",
    "generated/technique_capsules.min.json",
    "docs/source-lift/KAG_EXPORT.md",
    "generated/repo_doc_surface_manifest.json",
    "Do not mint a quest for every donor note.",
)
QUEST_SCHEMA_REQUIRED_FIELDS = (
    "schema_version",
    "id",
    "title",
    "repo",
    "lane",
    "owner_surface",
    "kind",
    "state",
    "band",
    "difficulty",
    "risk",
    "control_mode",
    "delegate_tier",
    "write_scope",
    "activation",
    "anchor_ref",
    "evidence",
    "opened_at",
    "touched_at",
    "public_safe",
)
QUEST_DISPATCH_REQUIRED_FIELDS = (
    "schema_version",
    "id",
    "repo",
    "state",
    "band",
    "difficulty",
    "risk",
    "control_mode",
    "delegate_tier",
    "split_required",
    "write_scope",
    "activation_mode",
    "public_safe",
)
QUEST_DISPATCH_ARTIFACTS = {
    "AOA-TECH-Q-0001": ["bounded_plan", "work_result", "verification_result"],
    "AOA-TECH-Q-0002": ["bounded_plan", "work_result"],
    "AOA-TECH-Q-0003": ["bounded_plan", "guardrail_check", "verification_result"],
    "AOA-TECH-Q-0004": ["recurrence_evidence", "promotion_decision"],
}




NOTE_SHAPE_TYPED = "typed_sections"
NOTE_SHAPE_OPAQUE = "opaque_body"
NOTE_PAYLOAD_FIELDS = "fields"
NOTE_PAYLOAD_ITEMS = "items"
NOTE_PAYLOAD_MARKDOWN = "markdown"
REVIEW_TEMPLATE_TYPE_ISSUE = "issue_template"
REVIEW_TEMPLATE_TYPE_PULL_REQUEST = "pull_request_template"
REVIEW_TEMPLATE_PAYLOAD_FIELDS = "fields"
REVIEW_TEMPLATE_PAYLOAD_ITEMS = "items"
REVIEW_TEMPLATE_PAYLOAD_CHECKBOXES = "checkboxes"
REVIEW_TEMPLATE_PAYLOAD_MARKDOWN = "markdown"
REVIEW_TEMPLATE_METADATA_KEYS = ("name", "about", "title")
SEMANTIC_REVIEW_MAP_HEADER = "| technique | current role |"
SEMANTIC_REVIEW_MAP_DIVIDER = "|---|---|"
SEMANTIC_REVIEW_QUESTION_PREFIX = "Question: "
SEMANTIC_REVIEW_OUTCOME_MARKER = "Outcome: "
SEMANTIC_REVIEW_OVERALL_OUTCOME_PREFIX = "Overall outcome: "
SHADOW_REVIEW_MAP_HEADER = "| technique | current role | current shadow seam |"
SHADOW_REVIEW_MAP_DIVIDER = "|---|---|---|"
SHADOW_REVIEW_QUESTION_PREFIX = "Question: "
SHADOW_REVIEW_OUTCOME_MARKER = "Outcome: "
SHADOW_REVIEW_OVERALL_OUTCOME_PREFIX = "Overall outcome: "
PUBLIC_HYGIENE_SCAN_DIRS = (".github", "docs", "generated", "mechanics", "techniques", "templates")
PUBLIC_HYGIENE_EXCLUDED_ROOT_FILES = {"TODO.md", "PLANS.md"}
PUBLIC_HYGIENE_ALLOWED_URL_PREFIXES = (
    "https://github.com/",
    "http://github.com/",
    "https://raw.githubusercontent.com/",
    "http://raw.githubusercontent.com/",
)
PUBLIC_HYGIENE_URL_RE = re.compile(r"https?://[^\s)>`]+")
PUBLIC_HYGIENE_BLOCKED_PATTERNS = (
    ("absolute Windows drive path", re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:\\[^\r\n]*")),
    ("absolute /Users/ path", re.compile(r"(?<![A-Za-z0-9])/Users/")),
    ("absolute /home/ path", re.compile(r"(?<![A-Za-z0-9])/home/")),
    ("localhost reference", re.compile(r"\blocalhost\b", re.IGNORECASE)),
    ("loopback address", re.compile(r"\b127\.0\.0\.1\b")),
    (
        "RFC1918 URL",
        re.compile(
            r"https?://(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3})(?::\d+)?(?:[/?#][^\s]*)?",
            re.IGNORECASE,
        ),
    ),
    (
        "internal host suffix URL",
        re.compile(
            r"https?://[A-Za-z0-9.-]+\.(?:internal|corp|lan|local|localdomain|home\.arpa)(?::\d+)?(?:[/?#][^\s]*)?",
            re.IGNORECASE,
        ),
    ),
    ("GitHub personal access token marker", re.compile(r"\bghp_[A-Za-z0-9]+\b")),
    ("GitHub OAuth token marker", re.compile(r"\bgho_[A-Za-z0-9]+\b")),
    ("AWS access key marker", re.compile(r"\bAKIA[0-9A-Z]*\b")),
    ("private key block marker", re.compile(r"BEGIN [A-Z ]*PRIVATE KEY")),
)
GITHUB_REVIEW_TEMPLATE_SPECS = (
    {
        "template_id": "canonical-promotion",
        "template_path": ".github/ISSUE_TEMPLATE/canonical-promotion.md",
        "template_type": REVIEW_TEMPLATE_TYPE_ISSUE,
        "section_scope": (
            "Technique",
            "Review Contract",
            "Default-Use Rationale",
            "Reuse Beyond Origin",
            "Stronger Validation Than Initial Promotion Baseline",
            "Adaptation Boundary Check",
            "Public-Safety Recheck",
            "Recommendation",
        ),
    },
    {
        "template_id": "external-import-review",
        "template_path": ".github/ISSUE_TEMPLATE/external-import-review.md",
        "template_type": REVIEW_TEMPLATE_TYPE_ISSUE,
        "section_scope": (
            "Source",
            "Proposed technique",
            "Adaptation summary",
            "Validation and reuse",
            "Public-safety review",
        ),
    },
    {
        "template_id": "technique-proposal",
        "template_path": ".github/ISSUE_TEMPLATE/technique-proposal.md",
        "template_type": REVIEW_TEMPLATE_TYPE_ISSUE,
        "section_scope": (
            "Summary",
            "Why it belongs here",
            "Evidence and validation",
            "Public safety",
            "Expected contribution shape",
        ),
    },
    {
        "template_id": "pull-request-template",
        "template_path": ".github/PULL_REQUEST_TEMPLATE.md",
        "template_type": REVIEW_TEMPLATE_TYPE_PULL_REQUEST,
        "section_scope": (
            "Summary",
            "Validation",
            "Notes",
            "Checklist",
        ),
    },
)
TYPED_NOTE_KIND_ORDER = (
    "origin_evidence",
    "second_context",
    "canonical_readiness",
    "adverse_effects_review",
    "external_origin",
    "external_review",
)
TYPED_NOTE_TITLES = {
    "origin_evidence": "Origin Evidence",
    "second_context": "Second Context Adaptation",
    "canonical_readiness": "Canonical Readiness",
    "adverse_effects_review": "Adverse Effects Review",
    "external_origin": "External Origin Note",
    "external_review": "External Import Review",
}
TYPED_NOTE_SECTION_SCOPES = {
    "origin_evidence": (
        "Technique",
        "Source project",
        "Evidence",
        "Interpretation",
    ),
    "second_context": (
        "Technique",
        "Target project",
        "What changed",
        "What stayed invariant",
        "Risks introduced by adaptation",
        "Evidence",
        "Result",
    ),
    "canonical_readiness": (
        "Technique",
        "Verdict",
        "Evidence summary",
        "Default-use rationale",
        "Fresh public-safety check",
        "Remaining gaps",
        "Recommendation",
    ),
    "adverse_effects_review": (
        "Technique",
        "Review focus",
        "Failure modes",
        "Negative effects",
        "Misuse patterns",
        "Detection signals",
        "Mitigations",
        "Recommendation",
    ),
    "external_origin": (
        "Source",
        "What changed",
        "Public-safety review",
        "Review notes",
    ),
    "external_review": (
        "Technique",
        "Verdict",
        "Evidence summary",
        "Boundedness check",
        "Provenance readability",
        "Import-path assessment",
        "Remaining gaps",
        "Recommendation",
    ),
}


class ValidationError(RuntimeError):
    pass


@dataclass(frozen=True)
class TechniqueSection:
    heading: str
    markdown: str


@dataclass(frozen=True)
class ChecklistItem:
    text: str


@dataclass(frozen=True)
class TechniqueChecklist:
    check_path: str
    title: str
    intro_markdown: str
    items: tuple[ChecklistItem, ...]


@dataclass(frozen=True)
class TechniqueExample:
    example_path: str
    title: str
    body_markdown: str


@dataclass(frozen=True)
class NoteField:
    key: str
    value_markdown: str


@dataclass(frozen=True)
class NoteItem:
    text: str


@dataclass(frozen=True)
class EvidenceNoteSection:
    heading: str
    payload_type: str
    fields: tuple[NoteField, ...]
    items: tuple[NoteItem, ...]
    markdown: str


@dataclass(frozen=True)
class TechniqueNote:
    note_path: str
    kind: str
    title: str
    note_shape: str
    intro_markdown: str
    sections: tuple[EvidenceNoteSection, ...]
    body_markdown: str


@dataclass(frozen=True)
class ReviewTemplateField:
    key: str
    value_markdown: str


@dataclass(frozen=True)
class ReviewTemplateItem:
    text: str


@dataclass(frozen=True)
class ReviewTemplateCheckbox:
    text: str
    checked: bool


@dataclass(frozen=True)
class ReviewTemplateSection:
    heading: str
    payload_type: str
    fields: tuple[ReviewTemplateField, ...]
    items: tuple[ReviewTemplateItem, ...]
    checkboxes: tuple[ReviewTemplateCheckbox, ...]
    markdown: str


@dataclass(frozen=True)
class GitHubReviewTemplate:
    template_id: str
    template_path: str
    template_type: str
    metadata: dict[str, str] | None
    sections: tuple[ReviewTemplateSection, ...]


@dataclass(frozen=True)
class SemanticReviewMapEntry:
    technique_id: str
    technique_path: str
    current_role: str


@dataclass(frozen=True)
class SemanticReviewSeam:
    heading: str
    question: str
    analysis_markdown: str
    outcome: str


@dataclass(frozen=True)
class SemanticReviewContextNote:
    heading: str
    markdown: str
    outcome: str | None


@dataclass(frozen=True)
class SemanticReviewFinding:
    text: str


@dataclass(frozen=True)
class SemanticReview:
    review_id: str
    review_path: str
    title: str
    intro_markdown: str
    map_heading: str
    map_entries: tuple[SemanticReviewMapEntry, ...]
    seams: tuple[SemanticReviewSeam, ...]
    context_notes: tuple[SemanticReviewContextNote, ...]
    findings: tuple[SemanticReviewFinding, ...]
    overall_outcome: str
    next_step_markdown: str


@dataclass(frozen=True)
class ShadowReviewMapEntry:
    technique_id: str
    technique_path: str
    current_role: str
    current_shadow_seam: str


@dataclass(frozen=True)
class ShadowReviewSeam:
    heading: str
    question: str
    analysis_markdown: str
    outcome: str


@dataclass(frozen=True)
class ShadowReviewFinding:
    text: str


@dataclass(frozen=True)
class ShadowReview:
    review_id: str
    review_path: str
    title: str
    intro_markdown: str
    map_heading: str
    map_entries: tuple[ShadowReviewMapEntry, ...]
    seams: tuple[ShadowReviewSeam, ...]
    findings: tuple[ShadowReviewFinding, ...]
    overall_outcome: str
    next_step_markdown: str


@dataclass(frozen=True)
class RepoDocSurface:
    doc_id: str
    doc_path: str
    title: str
    surface_group: str
    bounded_role: str
    top_level_sections: tuple[str, ...]


@dataclass(frozen=True)
class TechniqueRecord:
    technique_dir: Path
    technique_path: Path
    id: str
    name: str
    domain: str
    kind: str
    status: str
    summary: str
    frontmatter: dict[str, Any]
    body: str
    sections: tuple[TechniqueSection, ...]
    checklists: tuple[TechniqueChecklist, ...]
    examples: tuple[TechniqueExample, ...]
    notes: tuple[TechniqueNote, ...]


@dataclass(frozen=True)
class IndexRow:
    section: str
    id: str
    name: str
    domain: str
    status: str
    summary: str


def fail(message: str) -> None:
    raise ValidationError(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def read_yaml(path: Path) -> Any:
    try:
        import yaml
    except ModuleNotFoundError:
        fail(f"{path}: PyYAML is required to read YAML config; install requirements-dev.txt")
    try:
        return yaml.safe_load(read_text(path))
    except yaml.YAMLError as exc:
        fail(f"{path}: invalid YAML: {exc}")


def load_kind_registry(repo_root: Path) -> dict[str, Any]:
    registry_path = repo_root / TECHNIQUE_KIND_REGISTRY_PATH
    if not registry_path.is_file():
        fail(f"{repo_root}: missing kind registry '{TECHNIQUE_KIND_REGISTRY_PATH}'")
    registry = read_yaml(registry_path)
    if not isinstance(registry, dict):
        fail(f"{registry_path}: registry payload must be a mapping")
    return registry


def load_family_scout(repo_root: Path) -> dict[str, Any]:
    scout_path = repo_root / TECHNIQUE_FAMILY_SCOUT_PATH
    if not scout_path.is_file():
        fail(f"{repo_root}: missing family scout '{TECHNIQUE_FAMILY_SCOUT_PATH}'")
    scout = read_yaml(scout_path)
    if not isinstance(scout, dict):
        fail(f"{scout_path}: family scout payload must be a mapping")
    return scout


def load_topology_axes_registry(repo_root: Path) -> dict[str, Any]:
    registry_path = repo_root / TECHNIQUE_TOPOLOGY_AXES_PATH
    if not registry_path.is_file():
        fail(f"{repo_root}: missing topology axis registry '{TECHNIQUE_TOPOLOGY_AXES_PATH}'")
    registry = read_yaml(registry_path)
    if not isinstance(registry, dict):
        fail(f"{registry_path}: topology axis registry payload must be a mapping")
    return registry


def load_kind_overlay(repo_root: Path) -> dict[str, Any]:
    overlay_path = repo_root / TECHNIQUE_KIND_OVERLAY_PATH
    if not overlay_path.is_file():
        fail(f"{repo_root}: missing kind overlay '{TECHNIQUE_KIND_OVERLAY_PATH}'")
    overlay = read_yaml(overlay_path)
    if not isinstance(overlay, dict):
        fail(f"{overlay_path}: kind overlay payload must be a mapping")
    return overlay


def split_frontmatter(technique_path: Path) -> tuple[str, str]:
    text = read_text(technique_path)
    match = FRONTMATTER_RE.match(text)
    if not match:
        fail(f"{technique_path}: missing YAML frontmatter block")
    return match.group(1), text[match.end() :]


def skip_blank_lines(lines: list[str], index: int) -> int:
    while index < len(lines) and not lines[index].strip():
        index += 1
    return index


def indentation(line: str, technique_path: Path) -> int:
    if "\t" in line[: len(line) - len(line.lstrip(" \t"))]:
        fail(f"{technique_path}: tabs are not supported in frontmatter indentation")
    return len(line) - len(line.lstrip(" "))


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if value == "[]":
        return []
    if value == "{}":
        return {}
    if value == "true":
        return True
    if value == "false":
        return False
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_block(
    lines: list[str], index: int, expected_indent: int, technique_path: Path
) -> tuple[Any, int]:
    index = skip_blank_lines(lines, index)
    if index >= len(lines):
        fail(f"{technique_path}: expected nested frontmatter block at indent {expected_indent}")

    current_indent = indentation(lines[index], technique_path)
    if current_indent != expected_indent:
        fail(
            f"{technique_path}: expected frontmatter indent {expected_indent}, found {current_indent}"
        )

    if lines[index][expected_indent:].startswith("- "):
        return parse_list(lines, index, expected_indent, technique_path)
    return parse_mapping(lines, index, expected_indent, technique_path)


def parse_mapping(
    lines: list[str], index: int, expected_indent: int, technique_path: Path
) -> tuple[dict[str, Any], int]:
    mapping: dict[str, Any] = {}

    while True:
        index = skip_blank_lines(lines, index)
        if index >= len(lines):
            break

        line = lines[index]
        current_indent = indentation(line, technique_path)
        if current_indent < expected_indent:
            break
        if current_indent != expected_indent:
            fail(
                f"{technique_path}: unexpected frontmatter indent {current_indent}, expected {expected_indent}"
            )

        text = line[expected_indent:]
        if text.startswith("- "):
            fail(f"{technique_path}: unexpected list item at indent {expected_indent}")
        if ":" not in text:
            fail(f"{technique_path}: malformed frontmatter line: {line!r}")

        key, rest = text.split(":", 1)
        key = key.strip()
        rest = rest.strip()
        if not key:
            fail(f"{technique_path}: empty frontmatter key in line: {line!r}")
        if key in mapping:
            fail(f"{technique_path}: duplicate frontmatter key '{key}'")

        index += 1
        if rest:
            mapping[key] = parse_scalar(rest)
            continue

        value, index = parse_block(lines, index, expected_indent + 2, technique_path)
        mapping[key] = value

    return mapping, index


def parse_list(
    lines: list[str], index: int, expected_indent: int, technique_path: Path
) -> tuple[list[Any], int]:
    items: list[Any] = []

    while True:
        index = skip_blank_lines(lines, index)
        if index >= len(lines):
            break

        line = lines[index]
        current_indent = indentation(line, technique_path)
        if current_indent < expected_indent:
            break
        if current_indent != expected_indent:
            fail(
                f"{technique_path}: unexpected frontmatter indent {current_indent}, expected {expected_indent}"
            )

        text = line[expected_indent:]
        if not text.startswith("- "):
            break

        content = text[2:].strip()
        index += 1

        if not content:
            value, index = parse_block(lines, index, expected_indent + 2, technique_path)
            items.append(value)
            continue

        if ":" in content:
            key, raw_rest = content.split(":", 1)
            key = key.strip()
            if raw_rest and not raw_rest.startswith(" "):
                items.append(parse_scalar(content))
                continue

            rest = raw_rest.strip()
            if not key:
                fail(f"{technique_path}: malformed inline mapping list item: {line!r}")

            item: dict[str, Any] = {}
            if rest:
                item[key] = parse_scalar(rest)
            else:
                value, index = parse_block(lines, index, expected_indent + 4, technique_path)
                item[key] = value

            while True:
                index = skip_blank_lines(lines, index)
                if index >= len(lines):
                    break

                nested_line = lines[index]
                nested_indent = indentation(nested_line, technique_path)
                if nested_indent < expected_indent + 2:
                    break
                if nested_indent != expected_indent + 2:
                    fail(
                        f"{technique_path}: unexpected list-mapping indent {nested_indent}, expected {expected_indent + 2}"
                    )

                nested_text = nested_line[expected_indent + 2 :]
                if nested_text.startswith("- "):
                    fail(
                        f"{technique_path}: nested list items are not supported inside mapping list items"
                    )
                if ":" not in nested_text:
                    fail(f"{technique_path}: malformed frontmatter line: {nested_line!r}")

                nested_key, nested_rest = nested_text.split(":", 1)
                nested_key = nested_key.strip()
                nested_rest = nested_rest.strip()
                if not nested_key:
                    fail(f"{technique_path}: empty nested frontmatter key")
                if nested_key in item:
                    fail(f"{technique_path}: duplicate nested frontmatter key '{nested_key}'")

                index += 1
                if nested_rest:
                    item[nested_key] = parse_scalar(nested_rest)
                else:
                    nested_value, index = parse_block(
                        lines, index, expected_indent + 4, technique_path
                    )
                    item[nested_key] = nested_value

            items.append(item)
            continue

        items.append(parse_scalar(content))

    return items, index


def parse_frontmatter(frontmatter: str, technique_path: Path) -> dict[str, Any]:
    lines = frontmatter.splitlines()
    parsed, index = parse_block(lines, 0, 0, technique_path)
    index = skip_blank_lines(lines, index)
    if index != len(lines):
        fail(f"{technique_path}: could not parse frontmatter completely")
    if not isinstance(parsed, dict):
        fail(f"{technique_path}: frontmatter must parse into an object")
    return parsed


def load_schema_store(repo_root: Path) -> dict[str, Any]:
    schemas_dir = repo_root / "schemas"
    if not schemas_dir.is_dir():
        fail(f"{repo_root}: missing schemas/ directory")

    store: dict[str, Any] = {}
    for schema_path in sorted(schemas_dir.glob("*.schema.json")):
        schema = read_json(schema_path)
        store[schema_path.name] = schema
        schema_id = schema.get("$id")
        if isinstance(schema_id, str) and schema_id:
            store[schema_id] = schema
    return store


def resolve_schema_ref(ref: str, schema_store: dict[str, Any]) -> Any:
    if ref not in schema_store:
        fail(f"schema reference '{ref}' is not available in schema store")
    return schema_store[ref]


def ensure_type(instance: Any, expected_type: str, instance_path: str) -> None:
    type_ok = {
        "object": isinstance(instance, dict),
        "array": isinstance(instance, list),
        "string": isinstance(instance, str),
        "integer": isinstance(instance, int) and not isinstance(instance, bool),
        "boolean": isinstance(instance, bool),
    }.get(expected_type)

    if type_ok is None:
        fail(f"{instance_path}: unsupported schema type '{expected_type}'")
    if not type_ok:
        fail(f"{instance_path}: expected {expected_type}, found {type(instance).__name__}")


def validate_schema_instance(
    instance: Any, schema: dict[str, Any], instance_path: str, schema_store: dict[str, Any]
) -> None:
    if "$ref" in schema:
        validate_schema_instance(
            instance, resolve_schema_ref(schema["$ref"], schema_store), instance_path, schema_store
        )
        return

    if "type" in schema:
        ensure_type(instance, schema["type"], instance_path)

    if "enum" in schema and instance not in schema["enum"]:
        allowed = ", ".join(repr(value) for value in schema["enum"])
        fail(f"{instance_path}: value {instance!r} is not in enum [{allowed}]")

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            fail(f"{instance_path}: string is shorter than minLength {schema['minLength']}")
        if "pattern" in schema and not re.fullmatch(schema["pattern"], instance):
            fail(f"{instance_path}: value {instance!r} does not match pattern {schema['pattern']}")

    if isinstance(instance, int) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            fail(f"{instance_path}: value {instance} is below minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            fail(f"{instance_path}: value {instance} is above maximum {schema['maximum']}")

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            fail(f"{instance_path}: array has fewer than {schema['minItems']} items")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            fail(f"{instance_path}: array has more than {schema['maxItems']} items")
        if "items" in schema:
            for item_index, item in enumerate(instance):
                validate_schema_instance(
                    item, schema["items"], f"{instance_path}[{item_index}]", schema_store
                )

    if isinstance(instance, dict):
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        for required_key in required:
            if required_key not in instance:
                fail(f"{instance_path}: missing required property '{required_key}'")

        if schema.get("additionalProperties") is False:
            unexpected = sorted(set(instance) - set(properties))
            if unexpected:
                fail(
                    f"{instance_path}: unexpected properties {', '.join(repr(key) for key in unexpected)}"
                )

        for key, value in instance.items():
            if key in properties:
                validate_schema_instance(
                    value, properties[key], f"{instance_path}.{key}", schema_store
                )


