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
    "docs/CANONICAL_RUBRIC.md",
    "docs/DOMAIN_MAP.md",
    "schemas/technique.schema.json",
    "schemas/evidence-note.schema.json",
    "schemas/relation.schema.json",
    "schemas/index-entry.schema.json",
    "scripts/build_catalog.py",
    "scripts/build_capsules.py",
    "scripts/build_section_manifest.py",
    "scripts/build_checklist_manifest.py",
    "scripts/build_example_manifest.py",
    "scripts/build_evidence_note_manifest.py",
    "scripts/build_github_review_template_manifest.py",
    "scripts/build_semantic_review_manifest.py",
    "scripts/build_shadow_review_manifest.py",
    "scripts/build_repo_doc_surface_manifest.py",
    "generated/technique_catalog.json",
    "generated/technique_catalog.min.json",
    "generated/technique_capsules.json",
    "generated/technique_capsules.min.json",
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
    "generated/repo_doc_surface_manifest.json",
    "generated/repo_doc_surface_manifest.min.json",
)
REQUIRED_SELECTION_FILES = (
    "docs/TECHNIQUE_SELECTION.md",
    "docs/SELECTION_PATTERNS.md",
    "docs/SHADOW_PATTERNS.md",
)
REQUIRED_KAG_SOURCE_READER_FILES = (
    "docs/TECHNIQUE_SECTIONS.md",
    "docs/TECHNIQUE_CHECKLISTS.md",
    "docs/TECHNIQUE_EXAMPLES.md",
    "docs/EVIDENCE_NOTE_SURFACES.md",
)
REQUIRED_CAPSULE_SURFACE_FILES = ("docs/TECHNIQUE_CAPSULES.md",)
REQUIRED_REPO_DOC_SURFACE_FILES = ("docs/REPO_DOC_SURFACES.md",)
SELECTION_REVIEW_DOCS = {
    "published_summary": "docs/PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md",
    "evaluation_chain": "docs/EVALUATION_CHAIN_SEMANTIC_REVIEW.md",
    "docs_boundary": "docs/DOCS_BOUNDARY_SEMANTIC_REVIEW.md",
    "intent_chain": "docs/INTENT_CHAIN_SEMANTIC_REVIEW.md",
    "instruction_surface": "docs/INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md",
    "skill_support": "docs/SKILL_SUPPORT_SEMANTIC_REVIEW.md",
}
WORKING_SET_SPECS = (
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
        "title": "Instruction-surface pair",
        "technique_ids": ("AOA-T-0012", "AOA-T-0013"),
        "review_doc": SELECTION_REVIEW_DOCS["instruction_surface"],
        "note": "Fragment-first composition into one generated context artifact plus single-source distribution to multiple agent-facing instruction surfaces.",
    },
    {
        "title": "Skill-support cluster",
        "technique_ids": ("AOA-T-0014", "AOA-T-0015", "AOA-T-0017", "AOA-T-0016"),
        "review_doc": SELECTION_REVIEW_DOCS["skill_support"],
        "note": "Bounded test-first slicing, contract-surface validation, invariant coverage broadening, and semantic scoping for recent skill-support techniques.",
    },
)
DOMAIN_START_SPECS = (
    {
        "domain": "agent-workflows",
        "lead_ids": ("AOA-T-0001",),
        "review_docs": (),
        "note": "Start with the canonical workflow contract, then add narrower chain helpers only when the path gets more specialized.",
    },
    {
        "domain": "docs",
        "lead_ids": ("AOA-T-0002", "AOA-T-0009", "AOA-T-0012"),
        "review_docs": (
            SELECTION_REVIEW_DOCS["docs_boundary"],
            SELECTION_REVIEW_DOCS["instruction_surface"],
        ),
        "note": "Start with the canonical document-role layout, then inspect the docs boundary pair or instruction-surface pair when generation and entrypoint discipline become the next bounded question.",
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
    "published_summary": "docs/PUBLISHED_SUMMARY_SHADOW_REVIEW.md",
    "evaluation_chain": "docs/EVALUATION_CHAIN_SHADOW_REVIEW.md",
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
    "contribution/policy",
    "walkthrough/context",
    "status/release",
)
REPO_DOC_SURFACE_GROUP_SPECS = (
    {
        "group": "entrypoint/map",
        "heading": "Entrypoint / Map",
        "note": "Open these first when the question is where to start or which public repo map should anchor the next read.",
    },
    {
        "group": "contribution/policy",
        "heading": "Contribution / Policy",
        "note": "Use these when the question is how to contribute safely, publicly, and within the repo's current review posture.",
    },
    {
        "group": "walkthrough/context",
        "heading": "Walkthrough / Context",
        "note": "Use this when you need one concrete end-to-end example of how a real practice became a published technique here.",
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
        "doc_ids": ("readme", "docs_readme", "technique_index"),
        "note": "Start with the root README, then use the docs map and technique index for bounded navigation.",
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
        "question": "Where do release flow and status history live?",
        "doc_ids": ("changelog", "docs_releasing"),
        "note": "Use CHANGELOG for current history and RELEASING for the bounded validation path behind public corpus updates.",
    },
)
REPO_DOC_SURFACE_SPECS = (
    {
        "doc_id": "readme",
        "doc_path": "README.md",
        "surface_group": "entrypoint/map",
        "bounded_role": "root entrypoint for repository purpose, scope, and first-read routing",
    },
    {
        "doc_id": "technique_index",
        "doc_path": "TECHNIQUE_INDEX.md",
        "surface_group": "entrypoint/map",
        "bounded_role": "public corpus map by status, technique id, and domain",
    },
    {
        "doc_id": "docs_readme",
        "doc_path": "docs/README.md",
        "surface_group": "entrypoint/map",
        "bounded_role": "docs-layer entrypoint for generated surfaces, guides, and recommended reading paths",
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
        "doc_id": "walkthrough",
        "doc_path": "WALKTHROUGH.md",
        "surface_group": "walkthrough/context",
        "bounded_role": "one end-to-end example of origin practice, publication, reuse, and why the repo stores techniques this way",
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
DOMAIN_VALUES = {"agent-workflows", "docs", "evaluation"}
DOMAIN_ORDER = ("agent-workflows", "docs", "evaluation")
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
SECTION_RE = re.compile(r"^## (.+)$", re.MULTILINE)
SUBSECTION_RE = re.compile(r"^### (.+)$", re.MULTILINE)
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
PUBLIC_HYGIENE_SCAN_DIRS = (".github", "docs", "generated", "techniques", "templates")
PUBLIC_HYGIENE_EXCLUDED_ROOT_FILES = {"TODO.md", "PLANS.md", "ROADMAP.md"}
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


def validate_frontmatter_schema(
    frontmatter: dict[str, Any], technique_path: Path, schema_store: dict[str, Any]
) -> None:
    schema = resolve_schema_ref("technique.schema.json", schema_store)
    validate_schema_instance(frontmatter, schema, str(technique_path), schema_store)


def normalize_section_markdown(raw_markdown: str) -> str:
    return raw_markdown.lstrip("\r\n").rstrip()


def parse_subsections(markdown: str) -> tuple[TechniqueSection, ...]:
    matches = list(SUBSECTION_RE.finditer(markdown))
    sections: list[TechniqueSection] = []

    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        sections.append(
            TechniqueSection(
                heading=match.group(1).strip(),
                markdown=normalize_section_markdown(markdown[start:end]),
            )
        )

    return tuple(sections)


def parse_sections(body: str) -> tuple[TechniqueSection, ...]:
    matches = list(SECTION_RE.finditer(body))
    sections: list[TechniqueSection] = []

    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        sections.append(
            TechniqueSection(
                heading=match.group(1).strip(),
                markdown=normalize_section_markdown(body[start:end]),
            )
        )

    return tuple(sections)


def normalize_plain_text(text: str) -> str:
    return WHITESPACE_RE.sub(" ", text).strip()


def markdown_line_to_plain_text(line: str) -> str:
    stripped = line.strip()
    if not stripped or stripped.startswith(("## ", "### ")):
        return ""
    if stripped.startswith("|") and stripped.endswith("|"):
        return ""

    stripped = LEADING_LIST_MARKER_RE.sub("", stripped)
    stripped = MARKDOWN_LINK_RE.sub(r"\1", stripped)
    stripped = INLINE_CODE_RE.sub(r"\1", stripped)
    stripped = stripped.replace("**", "").replace("*", "")
    return normalize_plain_text(stripped)


def markdown_to_plain_text(markdown: str) -> str:
    return normalize_plain_text(
        " ".join(
            plain_line
            for plain_line in (markdown_line_to_plain_text(line) for line in markdown.splitlines())
            if plain_line
        )
    )


def capsule_markdown_items(markdown: str) -> list[str]:
    items: list[str] = []
    for line in markdown.splitlines():
        if not LEADING_LIST_MARKER_RE.match(line.strip()):
            continue
        plain_item = markdown_line_to_plain_text(line)
        if plain_item:
            items.append(plain_item)
    return items


def first_sentence(markdown: str) -> str:
    plain_text = markdown_to_plain_text(markdown)
    if not plain_text:
        return ""
    return re.split(r"(?<=[.!?])\s+", plain_text, maxsplit=1)[0].strip()


def finalize_capsule_text(text: str, truncated: bool) -> str:
    compact = normalize_plain_text(text).rstrip(" .,;:")
    if not compact:
        return ""
    return compact + ("..." if truncated else ".")


def truncate_capsule_text(text: str, max_words: int) -> str:
    normalized = normalize_plain_text(text)
    if not normalized:
        return ""

    words = normalized.split()
    if len(words) <= max_words:
        return finalize_capsule_text(normalized, truncated=False)
    return finalize_capsule_text(" ".join(words[:max_words]), truncated=True)


def capsule_compare_text(text: str) -> str:
    comparable = normalize_plain_text(text.replace("...", "").rstrip("."))
    for prefix in DERIVED_CAPSULE_PREFIXES:
        if comparable.startswith(prefix):
            comparable = comparable[len(prefix) :]
            break
    return normalize_plain_text(comparable)


DERIVED_CAPSULE_PREFIXES = (
    "Intent: ",
    "Use when ",
    "Avoid when ",
    "Needs ",
    "Produces ",
    "Core contract: ",
    "Main risk: ",
    "Validate by checking ",
)


def ensure_derived_capsule_text(candidate: str, source_markdown: str, max_words: int) -> str:
    source_plain = markdown_to_plain_text(source_markdown)
    if not source_plain:
        return candidate
    if capsule_compare_text(candidate) != capsule_compare_text(source_plain):
        return candidate

    source_words = source_plain.split()
    if len(source_words) <= 1:
        return candidate

    forced_budget = max(1, min(max_words, len(source_words) - 1))
    for prefix in DERIVED_CAPSULE_PREFIXES:
        if candidate.startswith(prefix):
            prefix_word_count = len(prefix.rstrip(": ").split())
            source_budget = max(1, forced_budget - prefix_word_count)
            return f"{prefix}{truncate_capsule_text(source_plain, source_budget)}"
    return truncate_capsule_text(source_plain, forced_budget)


def join_with_or(items: list[str]) -> str:
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} or {items[1]}"
    return f"{', '.join(items[:-1])}, or {items[-1]}"


def join_with_semicolons(items: list[str]) -> str:
    return "; ".join(item for item in items if item)


def capsule_sections_by_heading(record: TechniqueRecord) -> dict[str, TechniqueSection]:
    sections_by_heading = {section.heading: section for section in record.sections}
    missing = [heading for heading in CAPSULE_SECTION_HEADINGS if heading not in sections_by_heading]
    if missing:
        expected = ", ".join(f"'## {heading}'" for heading in CAPSULE_SECTION_HEADINGS)
        actual = ", ".join(f"'## {heading}'" for heading in missing)
        fail(
            f"{record.technique_path}: capsule source requires sections [{expected}]; "
            f"missing [{actual}]"
        )
    return sections_by_heading


def capsule_bullets_or_sentence(markdown: str, fallback_count: int) -> list[str]:
    items = capsule_markdown_items(markdown)
    if items:
        return items[:fallback_count]
    sentence = first_sentence(markdown)
    return [sentence] if sentence else []


def summarize_capsule_intent(markdown: str) -> str:
    sentence = first_sentence(markdown)
    candidate = truncate_capsule_text(sentence, 14)
    return ensure_derived_capsule_text(candidate, markdown, 12)


def summarize_capsule_use_when(markdown: str) -> str:
    candidate = truncate_capsule_text(
        f"Use when {join_with_or(capsule_bullets_or_sentence(markdown, 2))}",
        20,
    )
    return ensure_derived_capsule_text(candidate, markdown, 16)


def summarize_capsule_do_not_use(markdown: str) -> str:
    candidate = truncate_capsule_text(
        f"Avoid when {join_with_or(capsule_bullets_or_sentence(markdown, 2))}",
        20,
    )
    return ensure_derived_capsule_text(candidate, markdown, 16)


def summarize_capsule_inputs(markdown: str) -> str:
    candidate = truncate_capsule_text(
        f"Needs {join_with_semicolons(capsule_bullets_or_sentence(markdown, 3))}",
        18,
    )
    return ensure_derived_capsule_text(candidate, markdown, 14)


def summarize_capsule_outputs(markdown: str) -> str:
    candidate = truncate_capsule_text(
        f"Produces {join_with_semicolons(capsule_bullets_or_sentence(markdown, 3))}",
        18,
    )
    return ensure_derived_capsule_text(candidate, markdown, 14)


def summarize_capsule_contract(markdown: str) -> str:
    candidate = truncate_capsule_text(
        f"Core contract: {join_with_semicolons(capsule_bullets_or_sentence(markdown, 2))}",
        20,
    )
    return ensure_derived_capsule_text(candidate, markdown, 16)


def summarize_capsule_risk(markdown: str) -> str:
    subsection_map = {section.heading: section.markdown for section in parse_subsections(markdown)}
    for heading in ("Failure modes", "Negative effects", "Misuse patterns"):
        subsection_markdown = subsection_map.get(heading)
        if not subsection_markdown:
            continue
        signals = capsule_bullets_or_sentence(subsection_markdown, 1)
        if signals:
            candidate = truncate_capsule_text(f"Main risk: {signals[0]}", 20)
            return ensure_derived_capsule_text(candidate, subsection_markdown, 16)

    candidate = truncate_capsule_text(f"Main risk: {first_sentence(markdown)}", 20)
    return ensure_derived_capsule_text(candidate, markdown, 16)


def summarize_capsule_validation(markdown: str) -> str:
    candidate = truncate_capsule_text(
        f"Validate by checking {join_with_semicolons(capsule_bullets_or_sentence(markdown, 3))}",
        22,
    )
    return ensure_derived_capsule_text(candidate, markdown, 18)


def validate_risks_markdown(risks_markdown: str, technique_path: Path) -> None:
    subsection_matches = list(SUBSECTION_RE.finditer(risks_markdown))
    if not subsection_matches:
        fail(
            f"{technique_path}: '## Risks' must include fixed '###' subsections for the "
            f"rich risks contract"
        )

    intro_markdown = normalize_section_markdown(risks_markdown[: subsection_matches[0].start()])
    if intro_markdown:
        fail(f"{technique_path}: '## Risks' must not include prose before its first '###' subsection")

    subsections = parse_subsections(risks_markdown)
    actual_headings = tuple(section.heading for section in subsections)
    if actual_headings != RISK_SUBSECTION_HEADINGS:
        expected = ", ".join(f"'### {heading}'" for heading in RISK_SUBSECTION_HEADINGS)
        actual = ", ".join(f"'### {heading}'" for heading in actual_headings) or "(none)"
        fail(
            f"{technique_path}: '## Risks' must use the fixed subsection order "
            f"[{expected}], found [{actual}]"
        )

    for subsection in subsections:
        if not subsection.markdown:
            fail(f"{technique_path}: risk subsection '### {subsection.heading}' must not be empty")


def validate_sections(body: str, technique_path: Path) -> tuple[TechniqueSection, ...]:
    sections = parse_sections(body)
    present_sections = [section.heading for section in sections]
    for required_section in REQUIRED_SECTIONS:
        if required_section not in present_sections:
            fail(f"{technique_path}: missing required section '## {required_section}'")

    lift_positions: list[int] = []
    for heading in SECTION_LIFT_HEADINGS:
        matches = [index for index, section in enumerate(sections) if section.heading == heading]
        if len(matches) != 1:
            fail(
                f"{technique_path}: lift section '## {heading}' must appear exactly once"
            )
        lift_positions.extend(matches)

    if lift_positions != sorted(lift_positions):
        actual_lift_order = [
            section.heading for section in sections if section.heading in SECTION_LIFT_HEADINGS
        ]
        expected = ", ".join(f"'## {heading}'" for heading in SECTION_LIFT_HEADINGS)
        actual = ", ".join(f"'## {heading}'" for heading in actual_lift_order)
        fail(
            f"{technique_path}: lift sections must stay in standard order [{expected}], "
            f"found [{actual}]"
        )

    actual_lift_order = [sections[index].heading for index in lift_positions]
    if tuple(actual_lift_order) != SECTION_LIFT_HEADINGS:
        expected = ", ".join(f"'## {heading}'" for heading in SECTION_LIFT_HEADINGS)
        actual = ", ".join(f"'## {heading}'" for heading in actual_lift_order)
        fail(
            f"{technique_path}: lift sections must stay in standard order [{expected}], "
            f"found [{actual}]"
        )

    risk_sections = [section for section in sections if section.heading == "Risks"]
    if len(risk_sections) != 1:
        fail(f"{technique_path}: '## Risks' must appear exactly once")
    validate_risks_markdown(risk_sections[0].markdown, technique_path)

    return sections


def validate_support_dirs(technique_dir: Path) -> None:
    for support_dir_name in REQUIRED_SUPPORT_DIRS:
        support_dir = technique_dir / support_dir_name
        if not support_dir.is_dir():
            fail(f"{technique_dir}: missing support directory '{support_dir_name}/'")
        markdown_files = sorted(support_dir.rglob("*.md"))
        if not markdown_files:
            fail(f"{technique_dir}: support directory '{support_dir_name}/' is empty")


def validate_support_references(body: str, technique_dir: Path, technique_path: Path) -> None:
    for relative_path in sorted(set(match.group(0) for match in SUPPORT_PATH_RE.finditer(body))):
        pure_path = PurePosixPath(relative_path)
        if not pure_path.parts or pure_path.parts[0] not in REQUIRED_SUPPORT_DIRS:
            fail(f"{technique_path}: referenced support path '{relative_path}' is not allowed")
        if any(part == ".." for part in pure_path.parts):
            fail(
                f"{technique_path}: referenced support path '{relative_path}' must stay inside the technique bundle"
            )

        target = technique_dir.joinpath(*pure_path.parts)
        if not target.is_file():
            fail(f"{technique_path}: referenced support path '{relative_path}' does not exist")


def normalize_intro_markdown(lines: list[str]) -> str:
    return "\n".join(lines).rstrip()


def parse_checklist_file(check_path: Path, repo_root: Path) -> TechniqueChecklist:
    lines = read_text(check_path).splitlines()
    nonblank_indexes = [index for index, line in enumerate(lines) if line.strip()]
    if not nonblank_indexes:
        fail(f"{check_path}: checklist file must start with a '# ' title and at least one item")

    title_index = nonblank_indexes[0]
    title_line = lines[title_index]
    if not title_line.startswith("# ") or title_line.startswith("##"):
        fail(f"{check_path}: first meaningful line must be a single '# ' title")

    title = title_line[2:].strip()
    if not title:
        fail(f"{check_path}: checklist title must not be empty")

    index = title_index + 1
    while index < len(lines) and not lines[index].strip():
        index += 1

    intro_lines: list[str] = []
    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.startswith("- "):
            break
        if line.startswith("#"):
            fail(f"{check_path}: headings after the checklist title are not supported")
        if line.startswith((" ", "\t")):
            fail(f"{check_path}: indented intro or wrapped checklist content is not supported")
        intro_lines.append(line)
        index += 1

    while index < len(lines) and not lines[index].strip():
        index += 1

    items: list[ChecklistItem] = []
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        if line.startswith("- "):
            item_text = line[2:].strip()
            if not item_text:
                fail(f"{check_path}: checklist items must not be empty")
            items.append(ChecklistItem(text=item_text))
            index += 1
            continue
        if line.startswith((" ", "\t")):
            fail(f"{check_path}: nested bullets or wrapped checklist items are not supported")
        if line.startswith("#"):
            fail(f"{check_path}: headings after the checklist title are not supported")
        fail(f"{check_path}: prose after checklist items is not supported")

    if not items:
        fail(f"{check_path}: checklist file must include at least one top-level '- ' item")

    return TechniqueChecklist(
        check_path=check_path.relative_to(repo_root).as_posix(),
        title=title,
        intro_markdown=normalize_intro_markdown(intro_lines),
        items=tuple(items),
    )


def parse_checklists(repo_root: Path, technique_dir: Path) -> tuple[TechniqueChecklist, ...]:
    checks_dir = technique_dir / "checks"
    checklist_paths = sorted(
        checks_dir.rglob("*.md"), key=lambda path: path.relative_to(repo_root).as_posix()
    )
    return tuple(parse_checklist_file(path, repo_root) for path in checklist_paths)


def parse_example_file(example_path: Path, repo_root: Path) -> TechniqueExample:
    lines = read_text(example_path).splitlines()
    nonblank_indexes = [index for index, line in enumerate(lines) if line.strip()]
    if not nonblank_indexes:
        fail(f"{example_path}: example file must start with a '# ' title")

    title_index = nonblank_indexes[0]
    title_line = lines[title_index]
    if not title_line.startswith("# ") or title_line.startswith("##"):
        fail(f"{example_path}: first meaningful line must be a single '# ' title")

    title = title_line[2:].strip()
    if not title:
        fail(f"{example_path}: example title must not be empty")

    body_markdown = normalize_section_markdown("\n".join(lines[title_index + 1 :]))
    return TechniqueExample(
        example_path=example_path.relative_to(repo_root).as_posix(),
        title=title,
        body_markdown=body_markdown,
    )


def parse_examples(repo_root: Path, technique_dir: Path) -> tuple[TechniqueExample, ...]:
    examples_dir = technique_dir / "examples"
    example_paths = sorted(
        examples_dir.rglob("*.md"), key=lambda path: path.relative_to(repo_root).as_posix()
    )
    return tuple(parse_example_file(path, repo_root) for path in example_paths)


def parse_titled_markdown_file(markdown_path: Path, kind_label: str) -> tuple[str, list[str], int]:
    lines = read_text(markdown_path).splitlines()
    nonblank_indexes = [index for index, line in enumerate(lines) if line.strip()]
    if not nonblank_indexes:
        fail(f"{markdown_path}: {kind_label} file must start with a '# ' title")

    title_index = nonblank_indexes[0]
    title_line = lines[title_index]
    if not title_line.startswith("# ") or title_line.startswith("##"):
        fail(f"{markdown_path}: first meaningful line must be a single '# ' title")

    title = title_line[2:].strip()
    if not title:
        fail(f"{markdown_path}: {kind_label} title must not be empty")

    return title, lines, title_index


def extract_top_level_section_headings(
    markdown_path: Path, lines: list[str], title_index: int
) -> tuple[str, ...]:
    top_level_sections = tuple(
        line[3:].strip() for line in lines[title_index + 1 :] if line.startswith("## ")
    )
    if not top_level_sections:
        fail(
            f"{markdown_path}: repo-doc source must include at least one top-level '## ' heading"
        )
    return top_level_sections


def split_typed_note_body(note_path: Path, body: str) -> tuple[str, tuple[TechniqueSection, ...]]:
    matches = list(SECTION_RE.finditer(body))
    if not matches:
        fail(f"{note_path}: typed note must include top-level '## ' sections")

    intro_markdown = normalize_section_markdown(body[: matches[0].start()])
    sections: list[TechniqueSection] = []

    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        sections.append(
            TechniqueSection(
                heading=match.group(1).strip(),
                markdown=normalize_section_markdown(body[start:end]),
            )
        )

    return intro_markdown, tuple(sections)


def top_level_meaningful_indexes(lines: list[str]) -> list[int]:
    return [
        index
        for index, line in enumerate(lines)
        if line.strip() and not line.startswith((" ", "\t"))
    ]


def normalize_indented_markdown(lines: list[str]) -> str:
    trimmed = list(lines)
    while trimmed and not trimmed[0].strip():
        trimmed.pop(0)
    while trimmed and not trimmed[-1].strip():
        trimmed.pop()

    if not trimmed:
        return ""

    indents = [
        len(line) - len(line.lstrip(" "))
        for line in trimmed
        if line.strip() and line.startswith(" ")
    ]
    min_indent = min(indents) if indents else 0

    normalized_lines: list[str] = []
    for line in trimmed:
        if min_indent and line.startswith(" " * min_indent):
            normalized_lines.append(line[min_indent:])
        else:
            normalized_lines.append(line)

    return "\n".join(normalized_lines).rstrip()


def field_value_markdown(first_value: str, continuation_lines: list[str]) -> str:
    continuation_markdown = normalize_indented_markdown(continuation_lines)
    if first_value and continuation_markdown:
        return f"{first_value}\n{continuation_markdown}"
    if continuation_markdown:
        return continuation_markdown
    return first_value


def item_text_markdown(first_text: str, continuation_lines: list[str]) -> str:
    continuation_markdown = normalize_indented_markdown(continuation_lines)
    if first_text and continuation_markdown:
        return f"{first_text}\n{continuation_markdown}"
    if continuation_markdown:
        return continuation_markdown
    return first_text


def parse_note_section_payload(
    note_path: Path, heading: str, section_markdown: str
) -> EvidenceNoteSection:
    lines = section_markdown.splitlines()
    top_level_indexes = top_level_meaningful_indexes(lines)
    top_level_lines = [lines[index] for index in top_level_indexes]
    key_value_matches = [NOTE_FIELD_RE.fullmatch(line) for line in top_level_lines]

    if top_level_lines and all(match is not None for match in key_value_matches):
        fields: list[NoteField] = []
        for order, start_index in enumerate(top_level_indexes, start=1):
            end_index = (
                top_level_indexes[order] if order < len(top_level_indexes) else len(lines)
            )
            chunk_lines = lines[start_index:end_index]
            match = NOTE_FIELD_RE.fullmatch(chunk_lines[0])
            if match is None:
                fail(f"{note_path}: section '{heading}' must keep key/value bullet structure")
            fields.append(
                NoteField(
                    key=match.group(1).strip(),
                    value_markdown=field_value_markdown(
                        match.group(2).rstrip(), chunk_lines[1:]
                    ),
                )
            )

        return EvidenceNoteSection(
            heading=heading,
            payload_type=NOTE_PAYLOAD_FIELDS,
            fields=tuple(fields),
            items=(),
            markdown="",
        )

    if top_level_lines and all(line.startswith("- ") for line in top_level_lines):
        items: list[NoteItem] = []
        for order, start_index in enumerate(top_level_indexes, start=1):
            end_index = (
                top_level_indexes[order] if order < len(top_level_indexes) else len(lines)
            )
            chunk_lines = lines[start_index:end_index]
            item_text = item_text_markdown(chunk_lines[0][2:].strip(), chunk_lines[1:])
            if not item_text:
                fail(f"{note_path}: section '{heading}' contains an empty bullet item")
            items.append(NoteItem(text=item_text))

        return EvidenceNoteSection(
            heading=heading,
            payload_type=NOTE_PAYLOAD_ITEMS,
            fields=(),
            items=tuple(items),
            markdown="",
        )

    return EvidenceNoteSection(
        heading=heading,
        payload_type=NOTE_PAYLOAD_MARKDOWN,
        fields=(),
        items=(),
        markdown=section_markdown,
    )


def parse_note_file(note_path: Path, repo_root: Path) -> TechniqueNote:
    title, lines, title_index = parse_titled_markdown_file(note_path, "note")
    note_path_str = note_path.relative_to(repo_root).as_posix()
    kind = expected_evidence_kind(note_path_str)
    body = "\n".join(lines[title_index + 1 :])

    if kind not in TYPED_NOTE_SECTION_SCOPES:
        return TechniqueNote(
            note_path=note_path_str,
            kind=kind,
            title=title,
            note_shape=NOTE_SHAPE_OPAQUE,
            intro_markdown="",
            sections=(),
            body_markdown=normalize_section_markdown(body),
        )

    expected_title = TYPED_NOTE_TITLES[kind]
    if title != expected_title:
        fail(f"{note_path}: typed note title must be '{expected_title}', found '{title}'")

    intro_markdown, parsed_sections = split_typed_note_body(note_path, body)
    actual_headings = tuple(section.heading for section in parsed_sections)
    expected_headings = TYPED_NOTE_SECTION_SCOPES[kind]
    if actual_headings != expected_headings:
        expected = ", ".join(f"'## {heading}'" for heading in expected_headings)
        actual = ", ".join(f"'## {heading}'" for heading in actual_headings) or "none"
        fail(
            f"{note_path}: typed note sections must stay in standard order [{expected}], "
            f"found [{actual}]"
        )

    sections = tuple(
        parse_note_section_payload(note_path, section.heading, section.markdown)
        for section in parsed_sections
    )
    return TechniqueNote(
        note_path=note_path_str,
        kind=kind,
        title=title,
        note_shape=NOTE_SHAPE_TYPED,
        intro_markdown=intro_markdown,
        sections=sections,
        body_markdown="",
    )


def parse_notes(repo_root: Path, technique_dir: Path) -> tuple[TechniqueNote, ...]:
    notes_dir = technique_dir / "notes"
    note_paths = sorted(notes_dir.rglob("*.md"), key=lambda path: path.relative_to(repo_root).as_posix())
    return tuple(parse_note_file(path, repo_root) for path in note_paths)


def split_optional_frontmatter(markdown_path: Path) -> tuple[str | None, str]:
    text = read_text(markdown_path)
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, text
    return match.group(1), text[match.end() :]


def review_template_scopes_payload() -> dict[str, Any]:
    return {
        spec["template_id"]: {
            "template_type": spec["template_type"],
            "section_scope": list(spec["section_scope"]),
        }
        for spec in GITHUB_REVIEW_TEMPLATE_SPECS
    }


def validate_issue_template_metadata(
    template_path: Path, metadata: dict[str, Any]
) -> dict[str, str]:
    if tuple(metadata.keys()) != REVIEW_TEMPLATE_METADATA_KEYS:
        fail(
            f"{template_path}: issue template metadata must use exact keys "
            f"{list(REVIEW_TEMPLATE_METADATA_KEYS)}"
        )

    validated: dict[str, str] = {}
    for key in REVIEW_TEMPLATE_METADATA_KEYS:
        value = metadata[key]
        if not isinstance(value, str) or not value.strip():
            fail(f"{template_path}: metadata field '{key}' must be a non-empty string")
        validated[key] = value
    return validated


def parse_review_template_sections(
    template_path: Path, body: str, expected_headings: tuple[str, ...]
) -> tuple[TechniqueSection, ...]:
    matches = list(SECTION_RE.finditer(body))
    if not matches:
        fail(f"{template_path}: template body must include top-level '## ' sections")
    if normalize_section_markdown(body[: matches[0].start()]) != "":
        fail(f"{template_path}: template body must start directly with its first '## ' section")

    sections = parse_sections(body)
    actual_headings = tuple(section.heading for section in sections)
    if actual_headings != expected_headings:
        expected = ", ".join(f"'## {heading}'" for heading in expected_headings)
        actual = ", ".join(f"'## {heading}'" for heading in actual_headings) or "none"
        fail(
            f"{template_path}: review-template sections must stay in standard order "
            f"[{expected}], found [{actual}]"
        )
    return sections


def parse_review_template_section_payload(
    template_path: Path,
    template_type: str,
    heading: str,
    section_markdown: str,
) -> ReviewTemplateSection:
    lines = section_markdown.splitlines()
    top_level_indexes = top_level_meaningful_indexes(lines)
    top_level_lines = [lines[index] for index in top_level_indexes]
    checkbox_matches = [TEMPLATE_CHECKBOX_RE.fullmatch(line) for line in top_level_lines]
    field_matches = [TEMPLATE_FIELD_RE.fullmatch(line) for line in top_level_lines]

    if top_level_lines and all(match is not None for match in checkbox_matches):
        checkboxes: list[ReviewTemplateCheckbox] = []
        for order, start_index in enumerate(top_level_indexes, start=1):
            end_index = (
                top_level_indexes[order] if order < len(top_level_indexes) else len(lines)
            )
            chunk_lines = lines[start_index:end_index]
            match = TEMPLATE_CHECKBOX_RE.fullmatch(chunk_lines[0])
            if match is None:
                fail(f"{template_path}: section '{heading}' must keep checkbox structure")
            text = item_text_markdown(match.group(2).strip(), chunk_lines[1:])
            if not text:
                fail(f"{template_path}: section '{heading}' contains an empty checkbox item")
            checkboxes.append(
                ReviewTemplateCheckbox(text=text, checked=match.group(1).lower() == "x")
            )

        return ReviewTemplateSection(
            heading=heading,
            payload_type=REVIEW_TEMPLATE_PAYLOAD_CHECKBOXES,
            fields=(),
            items=(),
            checkboxes=tuple(checkboxes),
            markdown="",
        )

    if (
        template_type == REVIEW_TEMPLATE_TYPE_ISSUE
        and top_level_lines
        and all(match is not None for match in field_matches)
    ):
        fields: list[ReviewTemplateField] = []
        for order, start_index in enumerate(top_level_indexes, start=1):
            end_index = (
                top_level_indexes[order] if order < len(top_level_indexes) else len(lines)
            )
            chunk_lines = lines[start_index:end_index]
            match = TEMPLATE_FIELD_RE.fullmatch(chunk_lines[0])
            if match is None:
                fail(f"{template_path}: section '{heading}' must keep field-bullet structure")
            key = match.group(1).strip()
            if not key:
                fail(f"{template_path}: section '{heading}' contains an empty field key")
            fields.append(
                ReviewTemplateField(
                    key=key,
                    value_markdown=field_value_markdown(match.group(2).rstrip(), chunk_lines[1:]),
                )
            )

        return ReviewTemplateSection(
            heading=heading,
            payload_type=REVIEW_TEMPLATE_PAYLOAD_FIELDS,
            fields=tuple(fields),
            items=(),
            checkboxes=(),
            markdown="",
        )

    if top_level_lines and all(line.startswith("- ") for line in top_level_lines):
        items: list[ReviewTemplateItem] = []
        for order, start_index in enumerate(top_level_indexes, start=1):
            end_index = (
                top_level_indexes[order] if order < len(top_level_indexes) else len(lines)
            )
            chunk_lines = lines[start_index:end_index]
            item_text = item_text_markdown(chunk_lines[0][2:].strip(), chunk_lines[1:])
            if not item_text:
                fail(f"{template_path}: section '{heading}' contains an empty item")
            items.append(ReviewTemplateItem(text=item_text))

        return ReviewTemplateSection(
            heading=heading,
            payload_type=REVIEW_TEMPLATE_PAYLOAD_ITEMS,
            fields=(),
            items=tuple(items),
            checkboxes=(),
            markdown="",
        )

    return ReviewTemplateSection(
        heading=heading,
        payload_type=REVIEW_TEMPLATE_PAYLOAD_MARKDOWN,
        fields=(),
        items=(),
        checkboxes=(),
        markdown=section_markdown,
    )


def parse_github_review_templates(repo_root: Path) -> tuple[GitHubReviewTemplate, ...]:
    templates: list[GitHubReviewTemplate] = []

    for spec in GITHUB_REVIEW_TEMPLATE_SPECS:
        template_path = repo_root / spec["template_path"]
        if not template_path.is_file():
            fail(f"{template_path}: missing required GitHub review template")

        raw_frontmatter, body = split_optional_frontmatter(template_path)
        template_type = spec["template_type"]
        metadata: dict[str, str] | None

        if template_type == REVIEW_TEMPLATE_TYPE_ISSUE:
            if raw_frontmatter is None:
                fail(f"{template_path}: issue template must start with YAML frontmatter")
            metadata = validate_issue_template_metadata(
                template_path, parse_frontmatter(raw_frontmatter, template_path)
            )
        else:
            if raw_frontmatter is not None:
                fail(f"{template_path}: pull request template must not use YAML frontmatter")
            metadata = None

        sections = parse_review_template_sections(template_path, body, spec["section_scope"])
        parsed_sections = tuple(
            parse_review_template_section_payload(
                template_path, template_type, section.heading, section.markdown
            )
            for section in sections
        )
        templates.append(
            GitHubReviewTemplate(
                template_id=spec["template_id"],
                template_path=template_path.relative_to(repo_root).as_posix(),
                template_type=template_type,
                metadata=metadata,
                sections=parsed_sections,
            )
        )

    return tuple(templates)


def semantic_review_id_from_path(review_path: Path) -> str:
    stem = review_path.stem
    suffix = "_SEMANTIC_REVIEW"
    if not stem.endswith(suffix):
        fail(f"{review_path}: semantic review filename must end with '{suffix}.md'")
    review_id = stem[: -len(suffix)].lower()
    if not review_id:
        fail(f"{review_path}: semantic review filename must include a non-empty review id")
    return review_id


def split_semantic_review_body(
    review_path: Path, body: str
) -> tuple[str, tuple[TechniqueSection, ...]]:
    matches = list(SECTION_RE.finditer(body))
    if not matches:
        fail(f"{review_path}: semantic review doc must include top-level '## ' sections")

    intro_markdown = normalize_section_markdown(body[: matches[0].start()])
    sections: list[TechniqueSection] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        sections.append(
            TechniqueSection(
                heading=match.group(1).strip(),
                markdown=normalize_section_markdown(body[start:end]),
            )
        )

    return intro_markdown, tuple(sections)


def extract_last_outcome(markdown: str) -> str | None:
    matches = list(re.finditer(r"Outcome:\s*(.+)", markdown))
    if not matches:
        return None
    return matches[-1].group(1).strip()


def parse_semantic_review_map_entries(
    review_path: Path, repo_root: Path, map_markdown: str
) -> tuple[SemanticReviewMapEntry, ...]:
    lines = [line.rstrip() for line in map_markdown.splitlines() if line.strip()]
    if len(lines) < 3:
        fail(f"{review_path}: semantic review map must include a header, divider, and one row")
    if lines[0] != SEMANTIC_REVIEW_MAP_HEADER:
        fail(
            f"{review_path}: semantic review map must start with exact header "
            f"'{SEMANTIC_REVIEW_MAP_HEADER}'"
        )
    if lines[1] != SEMANTIC_REVIEW_MAP_DIVIDER:
        fail(
            f"{review_path}: semantic review map must use exact divider "
            f"'{SEMANTIC_REVIEW_MAP_DIVIDER}'"
        )

    entries: list[SemanticReviewMapEntry] = []
    row_re = re.compile(r"^\| \[([A-Za-z0-9-]+)\]\(([^)]+)\) \| (.+) \|$")
    for row_order, line in enumerate(lines[2:], start=1):
        match = row_re.fullmatch(line)
        if match is None:
            fail(f"{review_path}: semantic review map row {row_order} is malformed")
        technique_id = match.group(1).strip()
        target = match.group(2).strip()
        current_role = match.group(3).strip()
        if not current_role:
            fail(f"{review_path}: semantic review map row {row_order} must include current role")

        resolved_target = review_path.parent.joinpath(*PurePosixPath(target).parts).resolve()
        try:
            technique_path = resolved_target.relative_to(repo_root.resolve()).as_posix()
        except ValueError:
            fail(
                f"{review_path}: semantic review map row {row_order} points outside the repo: "
                f"'{target}'"
            )
        if not resolved_target.is_file():
            fail(
                f"{review_path}: semantic review map row {row_order} points to missing file "
                f"'{target}'"
            )

        entries.append(
            SemanticReviewMapEntry(
                technique_id=technique_id,
                technique_path=technique_path,
                current_role=current_role,
            )
        )

    return tuple(entries)


def parse_semantic_review_seams(
    review_path: Path, seam_markdown: str
) -> tuple[SemanticReviewSeam, ...]:
    matches = list(SUBSECTION_RE.finditer(seam_markdown))
    if not matches:
        fail(f"{review_path}: semantic review '## Seam Review' must include '### ' subsections")

    intro = normalize_section_markdown(seam_markdown[: matches[0].start()])
    if intro:
        fail(f"{review_path}: semantic review '## Seam Review' must not include prose before seams")

    seams: list[SemanticReviewSeam] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(seam_markdown)
        heading = match.group(1).strip()
        body_markdown = normalize_section_markdown(seam_markdown[start:end])
        if not body_markdown:
            fail(f"{review_path}: semantic review seam '{heading}' must not be empty")

        lines = body_markdown.splitlines()
        nonblank_indexes = [line_index for line_index, line in enumerate(lines) if line.strip()]
        if not nonblank_indexes:
            fail(f"{review_path}: semantic review seam '{heading}' must contain a question")
        question_index = nonblank_indexes[0]
        question_line = lines[question_index].strip()
        if not question_line.startswith(SEMANTIC_REVIEW_QUESTION_PREFIX):
            fail(
                f"{review_path}: semantic review seam '{heading}' must start with "
                f"'{SEMANTIC_REVIEW_QUESTION_PREFIX}'"
            )
        question = question_line[len(SEMANTIC_REVIEW_QUESTION_PREFIX) :].strip()
        if not question:
            fail(f"{review_path}: semantic review seam '{heading}' question must not be empty")

        analysis_markdown = normalize_section_markdown("\n".join(lines[question_index + 1 :]))
        if not analysis_markdown:
            fail(f"{review_path}: semantic review seam '{heading}' must include analysis markdown")
        outcome = extract_last_outcome(analysis_markdown)
        if outcome is None:
            fail(
                f"{review_path}: semantic review seam '{heading}' must include an "
                f"'{SEMANTIC_REVIEW_OUTCOME_MARKER}' marker"
            )

        seams.append(
            SemanticReviewSeam(
                heading=heading,
                question=question,
                analysis_markdown=analysis_markdown,
                outcome=outcome,
            )
        )

    return tuple(seams)


def parse_semantic_review_findings(
    review_path: Path, findings_markdown: str
) -> tuple[tuple[SemanticReviewFinding, ...], str]:
    lines = findings_markdown.splitlines()
    top_level_indexes = top_level_meaningful_indexes(lines)
    if len(top_level_indexes) < 2:
        fail(
            f"{review_path}: semantic review '## Findings' must include bullet findings and "
            f"'{SEMANTIC_REVIEW_OVERALL_OUTCOME_PREFIX}'"
        )

    last_index = top_level_indexes[-1]
    overall_line = lines[last_index].strip()
    if not overall_line.startswith(SEMANTIC_REVIEW_OVERALL_OUTCOME_PREFIX):
        fail(
            f"{review_path}: semantic review '## Findings' must end with "
            f"'{SEMANTIC_REVIEW_OVERALL_OUTCOME_PREFIX}'"
        )
    overall_outcome = overall_line[len(SEMANTIC_REVIEW_OVERALL_OUTCOME_PREFIX) :].strip()
    if not overall_outcome:
        fail(f"{review_path}: semantic review overall outcome must not be empty")

    findings: list[SemanticReviewFinding] = []
    item_indexes = top_level_indexes[:-1]
    for order, start_index in enumerate(item_indexes, start=1):
        line = lines[start_index]
        if not line.startswith("- "):
            fail(
                f"{review_path}: semantic review findings must use top-level '- ' bullets before "
                f"the overall outcome"
            )
        end_index = item_indexes[order] if order < len(item_indexes) else last_index
        chunk_lines = lines[start_index:end_index]
        text = item_text_markdown(chunk_lines[0][2:].strip(), chunk_lines[1:])
        if not text:
            fail(f"{review_path}: semantic review finding {order} must not be empty")
        findings.append(SemanticReviewFinding(text=text))

    return tuple(findings), overall_outcome


def parse_semantic_review_file(review_path: Path, repo_root: Path) -> SemanticReview:
    title, lines, title_index = parse_titled_markdown_file(review_path, "semantic review")
    review_id = semantic_review_id_from_path(review_path)
    review_path_str = review_path.relative_to(repo_root).as_posix()
    body = "\n".join(lines[title_index + 1 :])

    intro_markdown, sections = split_semantic_review_body(review_path, body)
    if len(sections) < 4:
        fail(
            f"{review_path}: semantic review doc must include map, seam review, findings, and "
            f"next step sections"
        )

    headings = [section.heading for section in sections]
    if not headings[0].endswith(" Map"):
        fail(f"{review_path}: first semantic review section must end with ' Map'")
    if headings[1] != "Seam Review":
        fail(f"{review_path}: second semantic review section must be '## Seam Review'")
    if headings[-2] != "Findings":
        fail(f"{review_path}: penultimate semantic review section must be '## Findings'")
    if headings[-1] != "Next Step":
        fail(f"{review_path}: final semantic review section must be '## Next Step'")
    if headings.count("Findings") != 1:
        fail(f"{review_path}: semantic review doc must contain exactly one '## Findings'")
    if headings.count("Next Step") != 1:
        fail(f"{review_path}: semantic review doc must contain exactly one '## Next Step'")

    map_section = sections[0]
    seam_section = sections[1]
    context_sections = sections[2:-2]
    findings_section = sections[-2]
    next_step_section = sections[-1]

    map_entries = parse_semantic_review_map_entries(review_path, repo_root, map_section.markdown)
    seams = parse_semantic_review_seams(review_path, seam_section.markdown)
    context_notes = tuple(
        SemanticReviewContextNote(
            heading=section.heading,
            markdown=section.markdown,
            outcome=extract_last_outcome(section.markdown),
        )
        for section in context_sections
    )
    findings, overall_outcome = parse_semantic_review_findings(
        review_path, findings_section.markdown
    )

    return SemanticReview(
        review_id=review_id,
        review_path=review_path_str,
        title=title,
        intro_markdown=intro_markdown,
        map_heading=map_section.heading,
        map_entries=map_entries,
        seams=seams,
        context_notes=context_notes,
        findings=findings,
        overall_outcome=overall_outcome,
        next_step_markdown=next_step_section.markdown,
    )


def parse_semantic_reviews(repo_root: Path) -> tuple[SemanticReview, ...]:
    review_paths = sorted(
        (repo_root / "docs").glob("*_SEMANTIC_REVIEW.md"),
        key=lambda path: path.relative_to(repo_root).as_posix(),
    )
    return tuple(parse_semantic_review_file(path, repo_root) for path in review_paths)


def shadow_review_id_from_path(review_path: Path) -> str:
    stem = review_path.stem
    suffix = "_SHADOW_REVIEW"
    if not stem.endswith(suffix):
        fail(f"{review_path}: shadow review filename must end with '{suffix}.md'")
    review_id = stem[: -len(suffix)].lower()
    if not review_id:
        fail(f"{review_path}: shadow review filename must include a non-empty review id")
    return review_id


def parse_shadow_review_map_entries(
    review_path: Path, repo_root: Path, map_markdown: str
) -> tuple[ShadowReviewMapEntry, ...]:
    lines = [line.rstrip() for line in map_markdown.splitlines() if line.strip()]
    if len(lines) < 3:
        fail(f"{review_path}: shadow review map must include a header, divider, and one row")
    if lines[0] != SHADOW_REVIEW_MAP_HEADER:
        fail(
            f"{review_path}: shadow review map must start with exact header "
            f"'{SHADOW_REVIEW_MAP_HEADER}'"
        )
    if lines[1] != SHADOW_REVIEW_MAP_DIVIDER:
        fail(
            f"{review_path}: shadow review map must use exact divider "
            f"'{SHADOW_REVIEW_MAP_DIVIDER}'"
        )

    entries: list[ShadowReviewMapEntry] = []
    row_re = re.compile(r"^\| \[([A-Za-z0-9-]+)\]\(([^)]+)\) \| (.+) \| (.+) \|$")
    for row_order, line in enumerate(lines[2:], start=1):
        match = row_re.fullmatch(line)
        if match is None:
            fail(f"{review_path}: shadow review map row {row_order} is malformed")
        technique_id = match.group(1).strip()
        target = match.group(2).strip()
        current_role = match.group(3).strip()
        current_shadow_seam = match.group(4).strip()
        if not current_role:
            fail(f"{review_path}: shadow review map row {row_order} must include current role")
        if not current_shadow_seam:
            fail(
                f"{review_path}: shadow review map row {row_order} must include current shadow seam"
            )

        resolved_target = review_path.parent.joinpath(*PurePosixPath(target).parts).resolve()
        try:
            technique_path = resolved_target.relative_to(repo_root.resolve()).as_posix()
        except ValueError:
            fail(
                f"{review_path}: shadow review map row {row_order} points outside the repo: "
                f"'{target}'"
            )
        if not resolved_target.is_file():
            fail(
                f"{review_path}: shadow review map row {row_order} points to missing file "
                f"'{target}'"
            )

        entries.append(
            ShadowReviewMapEntry(
                technique_id=technique_id,
                technique_path=technique_path,
                current_role=current_role,
                current_shadow_seam=current_shadow_seam,
            )
        )

    return tuple(entries)


def parse_shadow_review_seams(
    review_path: Path, seam_markdown: str
) -> tuple[ShadowReviewSeam, ...]:
    matches = list(SUBSECTION_RE.finditer(seam_markdown))
    if not matches:
        fail(f"{review_path}: shadow review '## Seam Review' must include '### ' subsections")

    intro = normalize_section_markdown(seam_markdown[: matches[0].start()])
    if intro:
        fail(f"{review_path}: shadow review '## Seam Review' must not include prose before seams")

    seams: list[ShadowReviewSeam] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(seam_markdown)
        heading = match.group(1).strip()
        body_markdown = normalize_section_markdown(seam_markdown[start:end])
        if not body_markdown:
            fail(f"{review_path}: shadow review seam '{heading}' must not be empty")

        lines = body_markdown.splitlines()
        nonblank_indexes = [line_index for line_index, line in enumerate(lines) if line.strip()]
        if not nonblank_indexes:
            fail(f"{review_path}: shadow review seam '{heading}' must contain a question")
        question_index = nonblank_indexes[0]
        question_line = lines[question_index].strip()
        if not question_line.startswith(SHADOW_REVIEW_QUESTION_PREFIX):
            fail(
                f"{review_path}: shadow review seam '{heading}' must start with "
                f"'{SHADOW_REVIEW_QUESTION_PREFIX}'"
            )
        question = question_line[len(SHADOW_REVIEW_QUESTION_PREFIX) :].strip()
        if not question:
            fail(f"{review_path}: shadow review seam '{heading}' question must not be empty")

        analysis_markdown = normalize_section_markdown("\n".join(lines[question_index + 1 :]))
        if not analysis_markdown:
            fail(f"{review_path}: shadow review seam '{heading}' must include analysis markdown")
        outcome = extract_last_outcome(analysis_markdown)
        if outcome is None:
            fail(
                f"{review_path}: shadow review seam '{heading}' must include an "
                f"'{SHADOW_REVIEW_OUTCOME_MARKER}' marker"
            )

        seams.append(
            ShadowReviewSeam(
                heading=heading,
                question=question,
                analysis_markdown=analysis_markdown,
                outcome=outcome,
            )
        )

    return tuple(seams)


def parse_shadow_review_findings(
    review_path: Path, findings_markdown: str
) -> tuple[tuple[ShadowReviewFinding, ...], str]:
    lines = findings_markdown.splitlines()
    top_level_indexes = top_level_meaningful_indexes(lines)
    if len(top_level_indexes) < 2:
        fail(
            f"{review_path}: shadow review '## Findings' must include bullet findings and "
            f"'{SHADOW_REVIEW_OVERALL_OUTCOME_PREFIX}'"
        )

    last_index = top_level_indexes[-1]
    overall_line = lines[last_index].strip()
    if not overall_line.startswith(SHADOW_REVIEW_OVERALL_OUTCOME_PREFIX):
        fail(
            f"{review_path}: shadow review '## Findings' must end with "
            f"'{SHADOW_REVIEW_OVERALL_OUTCOME_PREFIX}'"
        )
    overall_outcome = overall_line[len(SHADOW_REVIEW_OVERALL_OUTCOME_PREFIX) :].strip()
    if not overall_outcome:
        fail(f"{review_path}: shadow review overall outcome must not be empty")

    findings: list[ShadowReviewFinding] = []
    item_indexes = top_level_indexes[:-1]
    for order, start_index in enumerate(item_indexes, start=1):
        line = lines[start_index]
        if not line.startswith("- "):
            fail(
                f"{review_path}: shadow review findings must use top-level '- ' bullets before "
                f"the overall outcome"
            )
        end_index = item_indexes[order] if order < len(item_indexes) else last_index
        chunk_lines = lines[start_index:end_index]
        text = item_text_markdown(chunk_lines[0][2:].strip(), chunk_lines[1:])
        if not text:
            fail(f"{review_path}: shadow review finding {order} must not be empty")
        findings.append(ShadowReviewFinding(text=text))

    return tuple(findings), overall_outcome


def parse_shadow_review_file(review_path: Path, repo_root: Path) -> ShadowReview:
    title, lines, title_index = parse_titled_markdown_file(review_path, "shadow review")
    review_id = shadow_review_id_from_path(review_path)
    review_path_str = review_path.relative_to(repo_root).as_posix()
    body = "\n".join(lines[title_index + 1 :])

    intro_markdown, sections = split_semantic_review_body(review_path, body)
    if len(sections) != 4:
        fail(
            f"{review_path}: shadow review doc must include exactly map, seam review, findings, "
            f"and next step sections"
        )

    headings = [section.heading for section in sections]
    if not headings[0].endswith(" Map"):
        fail(f"{review_path}: first shadow review section must end with ' Map'")
    if headings[1] != "Seam Review":
        fail(f"{review_path}: second shadow review section must be '## Seam Review'")
    if headings[2] != "Findings":
        fail(f"{review_path}: third shadow review section must be '## Findings'")
    if headings[3] != "Next Step":
        fail(f"{review_path}: final shadow review section must be '## Next Step'")

    map_section, seam_section, findings_section, next_step_section = sections
    map_entries = parse_shadow_review_map_entries(review_path, repo_root, map_section.markdown)
    seams = parse_shadow_review_seams(review_path, seam_section.markdown)
    findings, overall_outcome = parse_shadow_review_findings(review_path, findings_section.markdown)

    return ShadowReview(
        review_id=review_id,
        review_path=review_path_str,
        title=title,
        intro_markdown=intro_markdown,
        map_heading=map_section.heading,
        map_entries=map_entries,
        seams=seams,
        findings=findings,
        overall_outcome=overall_outcome,
        next_step_markdown=next_step_section.markdown,
    )


def parse_shadow_reviews(repo_root: Path) -> tuple[ShadowReview, ...]:
    review_paths = sorted(
        (repo_root / "docs").glob("*_SHADOW_REVIEW.md"),
        key=lambda path: path.relative_to(repo_root).as_posix(),
    )
    return tuple(parse_shadow_review_file(path, repo_root) for path in review_paths)


def validate_repo_doc_surface_specs(repo_root: Path) -> None:
    if len(REPO_DOC_SURFACE_SPECS) != 10:
        fail("REPO_DOC_SURFACE_SPECS must contain exactly the 10 authoritative docs/status files")
    if len(REPO_DOC_SURFACE_GROUP_SPECS) != len(REPO_DOC_SURFACE_GROUP_ORDER):
        fail("REPO_DOC_SURFACE_GROUP_SPECS must contain exactly one spec per surface group")

    seen_groups: set[str] = set()
    for spec in REPO_DOC_SURFACE_GROUP_SPECS:
        group = spec["group"]
        if group not in REPO_DOC_SURFACE_GROUP_ORDER:
            fail(f"REPO_DOC_SURFACE_GROUP_SPECS: unsupported group '{group}'")
        if group in seen_groups:
            fail(f"REPO_DOC_SURFACE_GROUP_SPECS: duplicate group '{group}'")
        seen_groups.add(group)
        if not spec["heading"].strip():
            fail(f"REPO_DOC_SURFACE_GROUP_SPECS[{group}]: heading must not be empty")
        if not spec["note"].strip():
            fail(f"REPO_DOC_SURFACE_GROUP_SPECS[{group}]: note must not be empty")

    if tuple(spec["group"] for spec in REPO_DOC_SURFACE_GROUP_SPECS) != REPO_DOC_SURFACE_GROUP_ORDER:
        fail("REPO_DOC_SURFACE_GROUP_SPECS must follow REPO_DOC_SURFACE_GROUP_ORDER")

    seen_doc_ids: set[str] = set()
    seen_doc_paths: set[str] = set()
    doc_ids = {spec["doc_id"] for spec in REPO_DOC_SURFACE_SPECS}

    for spec in REPO_DOC_SURFACE_SPECS:
        doc_id = spec["doc_id"]
        doc_path = spec["doc_path"]
        surface_group = spec["surface_group"]
        bounded_role = spec["bounded_role"]

        if doc_id in seen_doc_ids:
            fail(f"REPO_DOC_SURFACE_SPECS: duplicate doc_id '{doc_id}'")
        if doc_path in seen_doc_paths:
            fail(f"REPO_DOC_SURFACE_SPECS: duplicate doc_path '{doc_path}'")
        seen_doc_ids.add(doc_id)
        seen_doc_paths.add(doc_path)

        if surface_group not in seen_groups:
            fail(
                f"REPO_DOC_SURFACE_SPECS[{doc_id}]: surface_group '{surface_group}' must be declared in REPO_DOC_SURFACE_GROUP_SPECS"
            )
        if not bounded_role.strip():
            fail(f"REPO_DOC_SURFACE_SPECS[{doc_id}]: bounded_role must not be empty")

        target = repo_root / doc_path
        if not target.is_file():
            fail(f"REPO_DOC_SURFACE_SPECS[{doc_id}]: missing source doc '{doc_path}'")

    seen_questions: set[str] = set()
    for spec in REPO_DOC_NAVIGATION_SPECS:
        question = spec["question"]
        if question in seen_questions:
            fail(f"REPO_DOC_NAVIGATION_SPECS: duplicate question '{question}'")
        seen_questions.add(question)
        if not question.strip():
            fail("REPO_DOC_NAVIGATION_SPECS: question must not be empty")

        doc_id_list = tuple(spec["doc_ids"])
        if not doc_id_list:
            fail(f"REPO_DOC_NAVIGATION_SPECS[{question}]: doc_ids must not be empty")
        for doc_id in doc_id_list:
            if doc_id not in doc_ids:
                fail(f"REPO_DOC_NAVIGATION_SPECS[{question}]: unknown doc_id '{doc_id}'")
        if not spec["note"].strip():
            fail(f"REPO_DOC_NAVIGATION_SPECS[{question}]: note must not be empty")


def parse_repo_doc_surface_file(repo_root: Path, spec: dict[str, str]) -> RepoDocSurface:
    doc_path = repo_root / spec["doc_path"]
    title, lines, title_index = parse_titled_markdown_file(doc_path, "repo doc surface")
    return RepoDocSurface(
        doc_id=spec["doc_id"],
        doc_path=spec["doc_path"],
        title=title,
        surface_group=spec["surface_group"],
        bounded_role=spec["bounded_role"],
        top_level_sections=extract_top_level_section_headings(doc_path, lines, title_index),
    )


def parse_repo_doc_surfaces(repo_root: Path) -> tuple[RepoDocSurface, ...]:
    validate_repo_doc_surface_specs(repo_root)
    return tuple(parse_repo_doc_surface_file(repo_root, spec) for spec in REPO_DOC_SURFACE_SPECS)


def validate_selection_working_set_specs(repo_root: Path) -> None:
    reviews_by_path = {
        review.review_path: review for review in parse_semantic_reviews(repo_root)
    }

    for spec in WORKING_SET_SPECS:
        review_doc = spec["review_doc"]
        if review_doc not in reviews_by_path:
            fail(
                f"{Path(review_doc).name}: review-backed working set '{spec['title']}' points to a "
                f"missing semantic review doc"
            )

        actual_ids = tuple(entry.technique_id for entry in reviews_by_path[review_doc].map_entries)
        expected_ids = tuple(spec["technique_ids"])
        if actual_ids != expected_ids:
            fail(
                f"{Path(review_doc).name}: working set '{spec['title']}' must match semantic review "
                f"map entry order {expected_ids}, found {actual_ids}"
            )


def validate_shadow_working_set_specs(records: list[TechniqueRecord], repo_root: Path) -> None:
    records_by_id = {record.id: record for record in records}
    reviews_by_path = {
        review.review_path: review for review in parse_shadow_reviews(repo_root)
    }

    for spec in SHADOW_WORKING_SET_SPECS:
        review_doc = spec["review_doc"]
        if review_doc not in reviews_by_path:
            fail(
                f"{Path(review_doc).name}: review-backed shadow working set '{spec['title']}' points "
                f"to a missing shadow review doc"
            )

        technique_ids = tuple(spec["technique_ids"])
        if not technique_ids:
            fail(f"{Path(review_doc).name}: shadow working set '{spec['title']}' must not be empty")

        actual_ids = tuple(entry.technique_id for entry in reviews_by_path[review_doc].map_entries)
        if actual_ids != technique_ids:
            fail(
                f"{Path(review_doc).name}: shadow working set '{spec['title']}' must match shadow "
                f"review map entry order {technique_ids}, found {actual_ids}"
            )

        for technique_id in technique_ids:
            record = records_by_id.get(technique_id)
            if record is None:
                fail(
                    f"{Path(review_doc).name}: shadow working set '{spec['title']}' "
                    f"references unknown technique '{technique_id}'"
                )
            if record.status != "canonical":
                fail(
                    f"{Path(review_doc).name}: shadow working set '{spec['title']}' "
                    f"must stay canonical-only, found '{technique_id}' with status '{record.status}'"
                )
            if "adverse_effects_review" not in {note.kind for note in record.notes}:
                fail(
                    f"{Path(review_doc).name}: shadow working set '{spec['title']}' "
                    f"requires typed adverse-effects reviews for '{technique_id}'"
                )


def validate_shadow_question_specs(records: list[TechniqueRecord]) -> None:
    records_by_id = {record.id: record for record in records}
    shadow_targets = {
        technique_id
        for spec in SHADOW_WORKING_SET_SPECS
        for technique_id in spec["technique_ids"]
    }

    for spec in SHADOW_COMMON_QUESTION_SPECS:
        target_id = spec["target_id"]
        record = records_by_id.get(target_id)
        if record is None:
            fail(f"SHADOW_COMMON_QUESTION_SPECS: unknown target_id '{target_id}'")
        if record.status != "canonical":
            fail(f"SHADOW_COMMON_QUESTION_SPECS: target_id '{target_id}' must be canonical")
        if target_id not in shadow_targets:
            fail(
                f"SHADOW_COMMON_QUESTION_SPECS[{target_id}]: target must belong to a declared "
                "shadow working set"
            )


def validate_repo_doc_navigation_specs(repo_root: Path) -> None:
    validate_repo_doc_surface_specs(repo_root)
    surfaces_by_id = {
        surface.doc_id: surface for surface in parse_repo_doc_surfaces(repo_root)
    }

    for spec in REPO_DOC_NAVIGATION_SPECS:
        for doc_id in spec["doc_ids"]:
            if doc_id not in surfaces_by_id:
                fail(
                    f"REPO_DOC_NAVIGATION_SPECS[{spec['question']}]: doc_id '{doc_id}' is not present in parsed repo doc surfaces"
                )


def validate_selection_navigation_specs(records: list[TechniqueRecord], repo_root: Path) -> None:
    records_by_id = {record.id: record for record in records}
    reviews_by_path = {
        review.review_path: review for review in parse_semantic_reviews(repo_root)
    }

    if len(DOMAIN_START_SPECS) != len(DOMAIN_ORDER):
        fail("DOMAIN_START_SPECS must contain exactly one spec per domain")

    seen_domains: set[str] = set()
    domain_start_targets: dict[str, str] = {}
    for spec in DOMAIN_START_SPECS:
        domain = spec["domain"]
        if domain not in DOMAIN_VALUES:
            fail(f"DOMAIN_START_SPECS: unsupported domain '{domain}'")
        if domain in seen_domains:
            fail(f"DOMAIN_START_SPECS: duplicate domain '{domain}'")
        seen_domains.add(domain)

        lead_ids = tuple(spec["lead_ids"])
        if not lead_ids:
            fail(f"DOMAIN_START_SPECS[{domain}]: lead_ids must not be empty")
        domain_start_targets[domain] = lead_ids[0]

        for review_doc in spec.get("review_docs", ()):
            if review_doc not in reviews_by_path:
                fail(
                    f"DOMAIN_START_SPECS[{domain}]: review doc '{review_doc}' does not exist"
                )

        for technique_id in lead_ids:
            record = records_by_id.get(technique_id)
            if record is None:
                fail(f"DOMAIN_START_SPECS[{domain}]: unknown technique id '{technique_id}'")
            if record.status != "canonical":
                fail(
                    f"DOMAIN_START_SPECS[{domain}]: lead_id '{technique_id}' must be canonical"
                )
            if record.domain != domain:
                fail(
                    f"DOMAIN_START_SPECS[{domain}]: lead_id '{technique_id}' must belong to domain '{domain}'"
                )

    if set(domain_start_targets) != set(DOMAIN_ORDER):
        fail("DOMAIN_START_SPECS must cover every domain exactly once")

    for spec in COMMON_MOVE_SPECS:
        target_id = spec["target_id"]
        record = records_by_id.get(target_id)
        if record is None:
            fail(f"COMMON_MOVE_SPECS: unknown target_id '{target_id}'")
        if record.status != "canonical":
            fail(f"COMMON_MOVE_SPECS: target_id '{target_id}' must be canonical")

        basis_type = spec["basis_type"]
        if basis_type == COMMON_MOVE_BASIS_DIRECT_RELATION:
            anchor_ids = tuple(spec.get("anchor_ids", ()))
            if not anchor_ids:
                fail(
                    f"COMMON_MOVE_SPECS[{target_id}]: direct_relation moves require non-empty anchor_ids"
                )
            for anchor_id in anchor_ids:
                anchor = records_by_id.get(anchor_id)
                if anchor is None:
                    fail(f"COMMON_MOVE_SPECS[{target_id}]: unknown anchor_id '{anchor_id}'")
                direct_relation_found = any(
                    relation["target"] == target_id for relation in anchor.frontmatter["relations"]
                ) or any(
                    relation["target"] == anchor_id for relation in record.frontmatter["relations"]
                )
                if not direct_relation_found:
                    fail(
                        f"COMMON_MOVE_SPECS[{target_id}]: anchor_id '{anchor_id}' must have a direct relation with '{target_id}'"
                    )
            continue

        if basis_type == COMMON_MOVE_BASIS_DOMAIN_START:
            domain = spec.get("domain")
            if domain not in domain_start_targets:
                fail(
                    f"COMMON_MOVE_SPECS[{target_id}]: domain_start move requires a valid domain"
                )
            expected_target = domain_start_targets[domain]
            if target_id != expected_target:
                fail(
                    f"COMMON_MOVE_SPECS[{target_id}]: domain_start move for '{domain}' must point to '{expected_target}'"
                )
            continue

        fail(
            f"COMMON_MOVE_SPECS[{target_id}]: unsupported basis_type '{basis_type}'"
        )


def strip_allowlisted_public_urls(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        url = match.group(0)
        if url.startswith(PUBLIC_HYGIENE_ALLOWED_URL_PREFIXES):
            return ""
        return url

    return PUBLIC_HYGIENE_URL_RE.sub(replace, text)


def blocked_public_hygiene_patterns(text: str) -> tuple[str, ...]:
    candidate = strip_allowlisted_public_urls(text)
    matches = [
        description
        for description, pattern in PUBLIC_HYGIENE_BLOCKED_PATTERNS
        if pattern.search(candidate)
    ]
    return tuple(matches)


def iter_public_hygiene_paths(repo_root: Path) -> tuple[Path, ...]:
    paths: list[Path] = []

    root_files = sorted(
        path
        for path in repo_root.iterdir()
        if path.is_file()
        and path.suffix == ".md"
        and path.name not in PUBLIC_HYGIENE_EXCLUDED_ROOT_FILES
    )
    paths.extend(root_files)

    for relative_dir in PUBLIC_HYGIENE_SCAN_DIRS:
        base = repo_root / relative_dir
        if not base.exists():
            continue
        paths.extend(sorted(path for path in base.rglob("*") if path.is_file()))

    return tuple(sorted(paths, key=lambda path: path.relative_to(repo_root).as_posix()))


def validate_public_hygiene(repo_root: Path) -> None:
    for path in iter_public_hygiene_paths(repo_root):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue

        for line_number, line in enumerate(lines, start=1):
            matches = blocked_public_hygiene_patterns(line)
            if matches:
                blocked = ", ".join(matches)
                fail(f"{path}:{line_number}: public surface matches blocked pattern(s): {blocked}")


def validate_stage1_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_STAGE1_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required Stage 1 file '{relative_path}'")


def validate_selection_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_SELECTION_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required selection file '{relative_path}'")


def validate_kag_source_reader_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_KAG_SOURCE_READER_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required KAG source reader file '{relative_path}'")


def validate_capsule_surface_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_CAPSULE_SURFACE_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required capsule surface file '{relative_path}'")


def validate_repo_doc_surface_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_REPO_DOC_SURFACE_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required repo doc surface file '{relative_path}'")


def validate_technique_bundle(
    repo_root: Path, technique_dir: Path, expected_domain: str, schema_store: dict[str, Any]
) -> TechniqueRecord:
    technique_path = technique_dir / "TECHNIQUE.md"
    if not technique_path.is_file():
        fail(f"{technique_dir}: missing TECHNIQUE.md")

    validate_support_dirs(technique_dir)

    frontmatter_text, body = split_frontmatter(technique_path)
    frontmatter = parse_frontmatter(frontmatter_text, technique_path)
    validate_frontmatter_schema(frontmatter, technique_path, schema_store)
    sections = validate_sections(body, technique_path)
    checklists = parse_checklists(repo_root, technique_dir)
    examples = parse_examples(repo_root, technique_dir)
    notes = parse_notes(repo_root, technique_dir)
    validate_support_references(body, technique_dir, technique_path)

    if frontmatter["domain"] != expected_domain:
        fail(
            f"{technique_path}: frontmatter domain '{frontmatter['domain']}' does not match parent directory '{expected_domain}'"
        )

    return TechniqueRecord(
        technique_dir=technique_dir,
        technique_path=technique_path,
        id=frontmatter["id"],
        name=frontmatter["name"],
        domain=frontmatter["domain"],
        status=frontmatter["status"],
        summary=frontmatter["summary"],
        frontmatter=frontmatter,
        body=body,
        sections=sections,
        checklists=checklists,
        examples=examples,
        notes=notes,
    )


def collect_techniques(repo_root: Path, schema_store: dict[str, Any]) -> list[TechniqueRecord]:
    techniques_dir = repo_root / "techniques"
    if not techniques_dir.is_dir():
        fail(f"{repo_root}: missing techniques/ directory")

    records: list[TechniqueRecord] = []
    seen_ids: set[str] = set()

    for domain_dir in sorted(path for path in techniques_dir.iterdir() if path.is_dir()):
        if domain_dir.name not in DOMAIN_VALUES:
            fail(f"{domain_dir}: unsupported domain directory '{domain_dir.name}'")

        for technique_dir in sorted(path for path in domain_dir.iterdir() if path.is_dir()):
            record = validate_technique_bundle(repo_root, technique_dir, domain_dir.name, schema_store)
            if record.id in seen_ids:
                fail(f"duplicate technique id '{record.id}' at {record.technique_dir}")
            seen_ids.add(record.id)
            records.append(record)

    if not records:
        fail(f"{repo_root}: no technique bundles found under techniques/")

    return records


def parse_index_rows(index_path: Path) -> dict[str, list[IndexRow]]:
    rows_by_id: dict[str, list[IndexRow]] = {}
    current_section = ""

    for line in read_text(index_path).splitlines():
        if line.startswith("## "):
            current_section = line[3:].strip()
            continue

        if current_section not in SECTION_STATUS or not line.startswith("|"):
            continue

        cells = [cell.strip() for cell in line.strip().split("|")[1:-1]]
        if not cells:
            continue
        if cells[0] == "id":
            continue
        if all(re.fullmatch(r"-+", cell) for cell in cells):
            continue
        if all(cell == "-" for cell in cells):
            continue

        if current_section == "Deprecated techniques":
            if len(cells) != 4:
                fail(f"{index_path}: malformed row in deprecated table: {line}")
            row_id, name, _replacement, _note = cells
            if row_id == "-":
                continue
            row = IndexRow(
                section=current_section,
                id=row_id,
                name=name,
                domain="",
                status="deprecated",
                summary="",
            )
        else:
            if len(cells) != 5:
                fail(f"{index_path}: malformed row in {current_section}: {line}")
            row_id, name, domain, status, summary = cells
            if row_id == "-":
                continue
            row = IndexRow(
                section=current_section,
                id=row_id,
                name=name,
                domain=domain,
                status=status,
                summary=summary,
            )

        rows_by_id.setdefault(row.id, []).append(row)

    return rows_by_id


def validate_index(repo_root: Path, records: list[TechniqueRecord]) -> None:
    index_path = repo_root / "TECHNIQUE_INDEX.md"
    if not index_path.is_file():
        fail(f"{repo_root}: missing TECHNIQUE_INDEX.md")

    rows_by_id = parse_index_rows(index_path)
    records_by_id = {record.id: record for record in records}

    for row_id in rows_by_id:
        if row_id not in records_by_id:
            fail(f"{index_path}: index contains unknown technique id '{row_id}'")

    for record in records:
        rows = rows_by_id.get(record.id)
        if not rows:
            fail(f"{index_path}: missing row for technique '{record.id}'")
        if len(rows) != 1:
            fail(f"{index_path}: technique '{record.id}' appears more than once in the index")

        row = rows[0]
        expected_section = STATUS_SECTION[record.status]
        if row.section != expected_section:
            fail(
                f"{index_path}: technique '{record.id}' is in '{row.section}' but should be in '{expected_section}'"
            )

        if row.name != record.name:
            fail(
                f"{index_path}: technique '{record.id}' name mismatch: index='{row.name}' technique='{record.name}'"
            )

        if record.status in {"canonical", "promoted"}:
            if row.domain != record.domain:
                fail(
                    f"{index_path}: technique '{record.id}' domain mismatch: index='{row.domain}' technique='{record.domain}'"
                )
            if row.status != record.status:
                fail(
                    f"{index_path}: technique '{record.id}' status mismatch: index='{row.status}' technique='{record.status}'"
                )
            if row.summary != record.summary:
                fail(
                    f"{index_path}: technique '{record.id}' summary mismatch between index and frontmatter"
                )


def expected_evidence_kind(relative_path: str) -> str:
    return EVIDENCE_KIND_BY_NAME.get(Path(relative_path).name, "support_note")


def validate_evidence(records: list[TechniqueRecord]) -> None:
    for record in records:
        notes_dir = record.technique_dir / "notes"
        actual_note_paths = sorted(
            path.relative_to(record.technique_dir).as_posix()
            for path in notes_dir.rglob("*.md")
        )
        evidence_items = record.frontmatter["evidence"]
        evidence_paths = [item["path"] for item in evidence_items]

        if sorted(evidence_paths) != actual_note_paths:
            fail(
                f"{record.technique_path}: evidence paths do not match notes/ contents: "
                f"frontmatter={sorted(evidence_paths)} notes={actual_note_paths}"
            )

        if len(set(evidence_paths)) != len(evidence_paths):
            fail(f"{record.technique_path}: evidence paths must be unique")

        has_adverse_effects_review = ADVERSE_EFFECTS_REVIEW_PATH in actual_note_paths
        if record.status == "canonical":
            if not has_adverse_effects_review:
                fail(
                    f"{record.technique_path}: canonical techniques must include "
                    f"'{ADVERSE_EFFECTS_REVIEW_PATH}'"
                )
        elif has_adverse_effects_review:
            fail(
                f"{record.technique_path}: only canonical techniques may include "
                f"'{ADVERSE_EFFECTS_REVIEW_PATH}'"
            )

        for item in evidence_items:
            expected_kind = expected_evidence_kind(item["path"])
            if item["kind"] != expected_kind:
                fail(
                    f"{record.technique_path}: evidence '{item['path']}' must use kind '{expected_kind}', "
                    f"found '{item['kind']}'"
                )


def validate_relations(records: list[TechniqueRecord]) -> None:
    known_ids = {record.id for record in records}
    for record in records:
        seen_pairs: set[tuple[str, str]] = set()
        for relation in record.frontmatter["relations"]:
            pair = (relation["type"], relation["target"])
            if relation["target"] == record.id:
                fail(f"{record.technique_path}: relation '{relation['type']}' cannot target itself")
            if relation["target"] not in known_ids:
                fail(
                    f"{record.technique_path}: relation target '{relation['target']}' does not exist"
                )
            if pair in seen_pairs:
                fail(
                    f"{record.technique_path}: duplicate relation '{relation['type']}' -> '{relation['target']}'"
                )
            seen_pairs.add(pair)


def full_catalog_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    frontmatter = record.frontmatter
    return {
        "id": frontmatter["id"],
        "name": frontmatter["name"],
        "domain": frontmatter["domain"],
        "status": frontmatter["status"],
        "summary": frontmatter["summary"],
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
        "origin": frontmatter["origin"],
        "owners": frontmatter["owners"],
        "tags": frontmatter["tags"],
        "maturity_score": frontmatter["maturity_score"],
        "rigor_level": frontmatter["rigor_level"],
        "reversibility": frontmatter["reversibility"],
        "review_required": frontmatter["review_required"],
        "validation_strength": frontmatter["validation_strength"],
        "public_safety_reviewed_at": frontmatter["public_safety_reviewed_at"],
        "export_ready": frontmatter["export_ready"],
        "relations": frontmatter["relations"],
        "evidence": frontmatter["evidence"],
    }


def min_catalog_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    frontmatter = record.frontmatter
    return {
        "id": frontmatter["id"],
        "name": frontmatter["name"],
        "domain": frontmatter["domain"],
        "status": frontmatter["status"],
        "summary": frontmatter["summary"],
        "maturity_score": frontmatter["maturity_score"],
        "rigor_level": frontmatter["rigor_level"],
        "reversibility": frontmatter["reversibility"],
        "review_required": frontmatter["review_required"],
        "validation_strength": frontmatter["validation_strength"],
        "export_ready": frontmatter["export_ready"],
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
    }


def full_capsule_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    sections_by_heading = capsule_sections_by_heading(record)
    capsule_entry = {
        "id": record.id,
        "name": record.name,
        "summary": record.summary,
        "one_line_intent": summarize_capsule_intent(sections_by_heading["Intent"].markdown),
        "use_when_short": summarize_capsule_use_when(sections_by_heading["When to use"].markdown),
        "do_not_use_short": summarize_capsule_do_not_use(
            sections_by_heading["When not to use"].markdown
        ),
        "inputs_short": summarize_capsule_inputs(sections_by_heading["Inputs"].markdown),
        "outputs_short": summarize_capsule_outputs(sections_by_heading["Outputs"].markdown),
        "core_contract_short": summarize_capsule_contract(sections_by_heading["Contracts"].markdown),
        "main_risk_short": summarize_capsule_risk(sections_by_heading["Risks"].markdown),
        "validation_short": summarize_capsule_validation(sections_by_heading["Validation"].markdown),
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
    }

    for key in (
        "one_line_intent",
        "use_when_short",
        "do_not_use_short",
        "inputs_short",
        "outputs_short",
        "core_contract_short",
        "main_risk_short",
        "validation_short",
    ):
        if not capsule_entry[key]:
            fail(f"{record.technique_path}: capsule field '{key}' must not be empty")

    return capsule_entry


def full_section_manifest_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    sections_by_heading = {section.heading: section for section in record.sections}
    return {
        "id": record.id,
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
        "sections": [
            {
                "heading": heading,
                "order": order,
                "markdown": sections_by_heading[heading].markdown,
            }
            for order, heading in enumerate(SECTION_LIFT_HEADINGS, start=1)
        ],
    }


def project_min_section_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "section_scope": full_manifest["section_scope"],
        "techniques": [
            {
                "id": technique["id"],
                "technique_path": technique["technique_path"],
                "sections": [
                    {
                        "heading": section["heading"],
                        "order": section["order"],
                    }
                    for section in technique["sections"]
                ],
            }
            for technique in full_manifest["techniques"]
        ],
    }


def full_checklist_manifest_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    return {
        "id": record.id,
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
        "checklists": [
            {
                "check_path": checklist.check_path,
                "title": checklist.title,
                "intro_markdown": checklist.intro_markdown,
                "items": [
                    {
                        "order": order,
                        "text": item.text,
                    }
                    for order, item in enumerate(checklist.items, start=1)
                ],
            }
            for checklist in record.checklists
        ],
    }


def project_min_checklist_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "techniques": [
            {
                "id": technique["id"],
                "technique_path": technique["technique_path"],
                "checklists": [
                    {
                        "check_path": checklist["check_path"],
                        "title": checklist["title"],
                        "item_count": len(checklist["items"]),
                        "items": [
                            {
                                "order": item["order"],
                            }
                            for item in checklist["items"]
                        ],
                    }
                    for checklist in technique["checklists"]
                ],
            }
            for technique in full_manifest["techniques"]
        ],
    }


def full_example_manifest_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    return {
        "id": record.id,
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
        "examples": [
            {
                "example_path": example.example_path,
                "title": example.title,
                "body_markdown": example.body_markdown,
            }
            for example in record.examples
        ],
    }


def project_min_example_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "techniques": [
            {
                "id": technique["id"],
                "technique_path": technique["technique_path"],
                "examples": [
                    {
                        "example_path": example["example_path"],
                        "title": example["title"],
                        "body_present": example["body_markdown"] != "",
                    }
                    for example in technique["examples"]
                ],
            }
            for technique in full_manifest["techniques"]
        ],
    }


def typed_note_scopes_payload() -> dict[str, Any]:
    return {
        kind: {
            "title": TYPED_NOTE_TITLES[kind],
            "section_scope": list(TYPED_NOTE_SECTION_SCOPES[kind]),
        }
        for kind in TYPED_NOTE_KIND_ORDER
    }


def full_note_section_payload(section: EvidenceNoteSection, order: int) -> dict[str, Any]:
    payload = {
        "heading": section.heading,
        "order": order,
        "payload_type": section.payload_type,
    }
    if section.payload_type == NOTE_PAYLOAD_FIELDS:
        payload["fields"] = [
            {
                "order": field_order,
                "key": field.key,
                "value_markdown": field.value_markdown,
            }
            for field_order, field in enumerate(section.fields, start=1)
        ]
    elif section.payload_type == NOTE_PAYLOAD_ITEMS:
        payload["items"] = [
            {
                "order": item_order,
                "text": item.text,
            }
            for item_order, item in enumerate(section.items, start=1)
        ]
    else:
        payload["markdown"] = section.markdown
    return payload


def full_evidence_note_manifest_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    return {
        "id": record.id,
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
        "notes": [
            {
                "note_path": note.note_path,
                "kind": note.kind,
                "title": note.title,
                "note_shape": note.note_shape,
                **(
                    {
                        "intro_markdown": note.intro_markdown,
                        "sections": [
                            full_note_section_payload(section, order)
                            for order, section in enumerate(note.sections, start=1)
                        ],
                    }
                    if note.note_shape == NOTE_SHAPE_TYPED
                    else {"body_markdown": note.body_markdown}
                ),
            }
            for note in record.notes
        ],
    }


def project_min_evidence_note_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "typed_note_scopes": full_manifest["typed_note_scopes"],
        "techniques": [
            {
                "id": technique["id"],
                "technique_path": technique["technique_path"],
                "notes": [
                    {
                        "note_path": note["note_path"],
                        "kind": note["kind"],
                        "title": note["title"],
                        "note_shape": note["note_shape"],
                        **(
                            {
                                "intro_present": note["intro_markdown"] != "",
                                "sections": [
                                    {
                                        "heading": section["heading"],
                                        "order": section["order"],
                                        "payload_type": section["payload_type"],
                                        **(
                                            {
                                                "fields": [
                                                    {
                                                        "order": field["order"],
                                                        "key": field["key"],
                                                    }
                                                    for field in section["fields"]
                                                ]
                                            }
                                            if section["payload_type"] == NOTE_PAYLOAD_FIELDS
                                            else {}
                                        ),
                                        **(
                                            {
                                                "items": [
                                                    {
                                                        "order": item["order"],
                                                    }
                                                    for item in section["items"]
                                                ]
                                            }
                                            if section["payload_type"] == NOTE_PAYLOAD_ITEMS
                                            else {}
                                        ),
                                        **(
                                            {"markdown_present": section["markdown"] != ""}
                                            if section["payload_type"] == NOTE_PAYLOAD_MARKDOWN
                                            else {}
                                        ),
                                    }
                                    for section in note["sections"]
                                ],
                            }
                            if note["note_shape"] == NOTE_SHAPE_TYPED
                            else {"body_present": note["body_markdown"] != ""}
                        ),
                    }
                    for note in technique["notes"]
                ],
            }
            for technique in full_manifest["techniques"]
        ],
    }


def full_review_template_section_payload(section: ReviewTemplateSection, order: int) -> dict[str, Any]:
    payload = {
        "heading": section.heading,
        "order": order,
        "payload_type": section.payload_type,
    }
    if section.payload_type == REVIEW_TEMPLATE_PAYLOAD_FIELDS:
        payload["fields"] = [
            {
                "order": field_order,
                "key": field.key,
                "value_markdown": field.value_markdown,
            }
            for field_order, field in enumerate(section.fields, start=1)
        ]
    elif section.payload_type == REVIEW_TEMPLATE_PAYLOAD_ITEMS:
        payload["items"] = [
            {
                "order": item_order,
                "text": item.text,
            }
            for item_order, item in enumerate(section.items, start=1)
        ]
    elif section.payload_type == REVIEW_TEMPLATE_PAYLOAD_CHECKBOXES:
        payload["checkboxes"] = [
            {
                "order": checkbox_order,
                "text": checkbox.text,
                "checked": checkbox.checked,
            }
            for checkbox_order, checkbox in enumerate(section.checkboxes, start=1)
        ]
    else:
        payload["markdown"] = section.markdown
    return payload


def full_github_review_template_manifest_entry(template: GitHubReviewTemplate) -> dict[str, Any]:
    payload = {
        "template_id": template.template_id,
        "template_path": template.template_path,
        "template_type": template.template_type,
        "sections": [
            full_review_template_section_payload(section, order)
            for order, section in enumerate(template.sections, start=1)
        ],
    }
    if template.metadata is not None:
        payload["metadata"] = {key: template.metadata[key] for key in REVIEW_TEMPLATE_METADATA_KEYS}
    return payload


def project_min_github_review_template_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "template_scopes": full_manifest["template_scopes"],
        "templates": [
            {
                "template_id": template["template_id"],
                "template_path": template["template_path"],
                "template_type": template["template_type"],
                **({"metadata": template["metadata"]} if "metadata" in template else {}),
                "sections": [
                    {
                        "heading": section["heading"],
                        "order": section["order"],
                        "payload_type": section["payload_type"],
                        **(
                            {
                                "fields": [
                                    {
                                        "order": field["order"],
                                        "key": field["key"],
                                    }
                                    for field in section["fields"]
                                ]
                            }
                            if section["payload_type"] == REVIEW_TEMPLATE_PAYLOAD_FIELDS
                            else {}
                        ),
                        **(
                            {
                                "items": [
                                    {
                                        "order": item["order"],
                                    }
                                    for item in section["items"]
                                ]
                            }
                            if section["payload_type"] == REVIEW_TEMPLATE_PAYLOAD_ITEMS
                            else {}
                        ),
                        **(
                            {
                                "checkboxes": [
                                    {
                                        "order": checkbox["order"],
                                        "checked": checkbox["checked"],
                                    }
                                    for checkbox in section["checkboxes"]
                                ]
                            }
                            if section["payload_type"] == REVIEW_TEMPLATE_PAYLOAD_CHECKBOXES
                            else {}
                        ),
                        **(
                            {"markdown_present": section["markdown"] != ""}
                            if section["payload_type"] == REVIEW_TEMPLATE_PAYLOAD_MARKDOWN
                            else {}
                        ),
                    }
                    for section in template["sections"]
                ],
            }
            for template in full_manifest["templates"]
        ],
    }


def semantic_review_scope_payload() -> dict[str, Any]:
    return {
        "map": {
            "first_section_suffix": "Map",
            "table_header": ["technique", "current role"],
        },
        "seams": {
            "section_heading": "Seam Review",
            "subsection_level": "###",
            "question_prefix": SEMANTIC_REVIEW_QUESTION_PREFIX,
            "outcome_marker": SEMANTIC_REVIEW_OUTCOME_MARKER,
        },
        "findings": {
            "section_heading": "Findings",
            "overall_outcome_prefix": SEMANTIC_REVIEW_OVERALL_OUTCOME_PREFIX,
        },
        "next_step": {
            "section_heading": "Next Step",
        },
    }


def shadow_review_scope_payload() -> dict[str, Any]:
    return {
        "map": {
            "first_section_suffix": "Map",
            "table_header": ["technique", "current role", "current shadow seam"],
        },
        "seams": {
            "section_heading": "Seam Review",
            "subsection_level": "###",
            "question_prefix": SHADOW_REVIEW_QUESTION_PREFIX,
            "outcome_marker": SHADOW_REVIEW_OUTCOME_MARKER,
        },
        "findings": {
            "section_heading": "Findings",
            "overall_outcome_prefix": SHADOW_REVIEW_OVERALL_OUTCOME_PREFIX,
        },
        "next_step": {
            "section_heading": "Next Step",
        },
    }


def repo_doc_surface_groups_payload() -> list[dict[str, str]]:
    return [
        {
            "group": spec["group"],
            "heading": spec["heading"],
            "note": spec["note"],
        }
        for spec in REPO_DOC_SURFACE_GROUP_SPECS
    ]


def full_semantic_review_manifest_entry(review: SemanticReview) -> dict[str, Any]:
    return {
        "review_id": review.review_id,
        "review_path": review.review_path,
        "title": review.title,
        "intro_markdown": review.intro_markdown,
        "map_heading": review.map_heading,
        "map_entries": [
            {
                "order": order,
                "technique_id": entry.technique_id,
                "technique_path": entry.technique_path,
                "current_role": entry.current_role,
            }
            for order, entry in enumerate(review.map_entries, start=1)
        ],
        "seams": [
            {
                "heading": seam.heading,
                "order": order,
                "question": seam.question,
                "analysis_markdown": seam.analysis_markdown,
                "outcome": seam.outcome,
            }
            for order, seam in enumerate(review.seams, start=1)
        ],
        "context_notes": [
            {
                "heading": note.heading,
                "order": order,
                "markdown": note.markdown,
                "outcome": note.outcome,
            }
            for order, note in enumerate(review.context_notes, start=1)
        ],
        "findings": [
            {
                "order": order,
                "text": finding.text,
            }
            for order, finding in enumerate(review.findings, start=1)
        ],
        "overall_outcome": review.overall_outcome,
        "next_step_markdown": review.next_step_markdown,
    }


def full_shadow_review_manifest_entry(review: ShadowReview) -> dict[str, Any]:
    return {
        "review_id": review.review_id,
        "review_path": review.review_path,
        "title": review.title,
        "intro_markdown": review.intro_markdown,
        "map_heading": review.map_heading,
        "map_entries": [
            {
                "order": order,
                "technique_id": entry.technique_id,
                "technique_path": entry.technique_path,
                "current_role": entry.current_role,
                "current_shadow_seam": entry.current_shadow_seam,
            }
            for order, entry in enumerate(review.map_entries, start=1)
        ],
        "seams": [
            {
                "heading": seam.heading,
                "order": order,
                "question": seam.question,
                "analysis_markdown": seam.analysis_markdown,
                "outcome": seam.outcome,
            }
            for order, seam in enumerate(review.seams, start=1)
        ],
        "findings": [
            {
                "order": order,
                "text": finding.text,
            }
            for order, finding in enumerate(review.findings, start=1)
        ],
        "overall_outcome": review.overall_outcome,
        "next_step_markdown": review.next_step_markdown,
    }


def project_min_semantic_review_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "review_scope": full_manifest["review_scope"],
        "reviews": [
            {
                "review_id": review["review_id"],
                "review_path": review["review_path"],
                "title": review["title"],
                "intro_present": review["intro_markdown"] != "",
                "map_heading": review["map_heading"],
                "map_entries": [
                    {
                        "order": entry["order"],
                        "technique_id": entry["technique_id"],
                        "technique_path": entry["technique_path"],
                    }
                    for entry in review["map_entries"]
                ],
                "seams": [
                    {
                        "heading": seam["heading"],
                        "order": seam["order"],
                        "question_present": seam["question"] != "",
                        "outcome": seam["outcome"],
                    }
                    for seam in review["seams"]
                ],
                "context_notes": [
                    {
                        "heading": note["heading"],
                        "order": note["order"],
                        "outcome_present": note["outcome"] is not None,
                        **({"outcome": note["outcome"]} if note["outcome"] is not None else {}),
                    }
                    for note in review["context_notes"]
                ],
                "finding_count": len(review["findings"]),
                "overall_outcome": review["overall_outcome"],
                "next_step_present": review["next_step_markdown"] != "",
            }
            for review in full_manifest["reviews"]
        ],
    }


def project_min_shadow_review_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "review_scope": full_manifest["review_scope"],
        "reviews": [
            {
                "review_id": review["review_id"],
                "review_path": review["review_path"],
                "title": review["title"],
                "intro_present": review["intro_markdown"] != "",
                "map_heading": review["map_heading"],
                "map_entries": [
                    {
                        "order": entry["order"],
                        "technique_id": entry["technique_id"],
                        "technique_path": entry["technique_path"],
                    }
                    for entry in review["map_entries"]
                ],
                "seams": [
                    {
                        "heading": seam["heading"],
                        "order": seam["order"],
                        "question_present": seam["question"] != "",
                        "outcome": seam["outcome"],
                    }
                    for seam in review["seams"]
                ],
                "finding_count": len(review["findings"]),
                "overall_outcome": review["overall_outcome"],
                "next_step_present": review["next_step_markdown"] != "",
            }
            for review in full_manifest["reviews"]
        ],
    }


def full_repo_doc_surface_manifest_entry(surface: RepoDocSurface) -> dict[str, Any]:
    return {
        "doc_id": surface.doc_id,
        "doc_path": surface.doc_path,
        "title": surface.title,
        "surface_group": surface.surface_group,
        "bounded_role": surface.bounded_role,
        "top_level_sections": list(surface.top_level_sections),
    }


def project_min_repo_doc_surface_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "docs": [
            {
                "doc_id": doc["doc_id"],
                "doc_path": doc["doc_path"],
                "title": doc["title"],
                "surface_group": doc["surface_group"],
                "bounded_role": doc["bounded_role"],
                "top_level_sections": doc["top_level_sections"],
            }
            for doc in full_manifest["docs"]
        ],
    }


def build_catalog_payloads(
    repo_root: Path, records: list[TechniqueRecord]
) -> tuple[dict[str, Any], dict[str, Any]]:
    sorted_records = sorted(records, key=lambda record: record.id)
    full_catalog = {
        "catalog_version": 1,
        "source_of_truth": "markdown-frontmatter-v2",
        "techniques": [full_catalog_entry(repo_root, record) for record in sorted_records],
    }
    min_catalog = {
        "catalog_version": 1,
        "source_of_truth": "markdown-frontmatter-v2",
        "techniques": [min_catalog_entry(repo_root, record) for record in sorted_records],
    }
    return full_catalog, min_catalog


def build_capsule_payload(repo_root: Path, records: list[TechniqueRecord]) -> dict[str, Any]:
    sorted_records = sorted(records, key=lambda record: record.id)
    return {
        "capsule_version": CAPSULE_VERSION,
        "source_of_truth": CAPSULE_SOURCE_OF_TRUTH,
        "techniques": [full_capsule_entry(repo_root, record) for record in sorted_records],
    }


def project_min_capsule_payload(full_payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "capsule_version": full_payload["capsule_version"],
        "source_of_truth": full_payload["source_of_truth"],
        "techniques": [
            {key: entry[key] for key in CAPSULE_MIN_FIELDS} for entry in full_payload["techniques"]
        ],
    }


def build_capsule_payloads(
    repo_root: Path, records: list[TechniqueRecord]
) -> tuple[dict[str, Any], dict[str, Any]]:
    full_payload = build_capsule_payload(repo_root, records)
    return full_payload, project_min_capsule_payload(full_payload)


def build_section_manifest_payloads(
    repo_root: Path, records: list[TechniqueRecord]
) -> tuple[dict[str, Any], dict[str, Any]]:
    sorted_records = sorted(records, key=lambda record: record.id)
    full_manifest = {
        "manifest_version": SECTION_MANIFEST_VERSION,
        "source_of_truth": SECTION_MANIFEST_SOURCE_OF_TRUTH,
        "section_scope": list(SECTION_LIFT_HEADINGS),
        "techniques": [full_section_manifest_entry(repo_root, record) for record in sorted_records],
    }
    return full_manifest, project_min_section_manifest(full_manifest)


def build_checklist_manifest_payloads(
    repo_root: Path, records: list[TechniqueRecord]
) -> tuple[dict[str, Any], dict[str, Any]]:
    sorted_records = sorted(records, key=lambda record: record.id)
    full_manifest = {
        "manifest_version": CHECKLIST_MANIFEST_VERSION,
        "source_of_truth": CHECKLIST_MANIFEST_SOURCE_OF_TRUTH,
        "techniques": [full_checklist_manifest_entry(repo_root, record) for record in sorted_records],
    }
    return full_manifest, project_min_checklist_manifest(full_manifest)


def build_example_manifest_payloads(
    repo_root: Path, records: list[TechniqueRecord]
) -> tuple[dict[str, Any], dict[str, Any]]:
    sorted_records = sorted(records, key=lambda record: record.id)
    full_manifest = {
        "manifest_version": EXAMPLE_MANIFEST_VERSION,
        "source_of_truth": EXAMPLE_MANIFEST_SOURCE_OF_TRUTH,
        "techniques": [full_example_manifest_entry(repo_root, record) for record in sorted_records],
    }
    return full_manifest, project_min_example_manifest(full_manifest)


def build_evidence_note_manifest_payloads(
    repo_root: Path, records: list[TechniqueRecord]
) -> tuple[dict[str, Any], dict[str, Any]]:
    sorted_records = sorted(records, key=lambda record: record.id)
    full_manifest = {
        "manifest_version": EVIDENCE_NOTE_MANIFEST_VERSION,
        "source_of_truth": EVIDENCE_NOTE_MANIFEST_SOURCE_OF_TRUTH,
        "typed_note_scopes": typed_note_scopes_payload(),
        "techniques": [
            full_evidence_note_manifest_entry(repo_root, record) for record in sorted_records
        ],
    }
    return full_manifest, project_min_evidence_note_manifest(full_manifest)


def build_github_review_template_manifest_payloads(
    repo_root: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    templates = parse_github_review_templates(repo_root)
    full_manifest = {
        "manifest_version": GITHUB_REVIEW_TEMPLATE_MANIFEST_VERSION,
        "source_of_truth": GITHUB_REVIEW_TEMPLATE_MANIFEST_SOURCE_OF_TRUTH,
        "template_scopes": review_template_scopes_payload(),
        "templates": [
            full_github_review_template_manifest_entry(template) for template in templates
        ],
    }
    return full_manifest, project_min_github_review_template_manifest(full_manifest)


def build_semantic_review_manifest_payloads(
    repo_root: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    reviews = parse_semantic_reviews(repo_root)
    full_manifest = {
        "manifest_version": SEMANTIC_REVIEW_MANIFEST_VERSION,
        "source_of_truth": SEMANTIC_REVIEW_MANIFEST_SOURCE_OF_TRUTH,
        "review_scope": semantic_review_scope_payload(),
        "reviews": [full_semantic_review_manifest_entry(review) for review in reviews],
    }
    return full_manifest, project_min_semantic_review_manifest(full_manifest)


def build_shadow_review_manifest_payloads(
    repo_root: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    reviews = parse_shadow_reviews(repo_root)
    full_manifest = {
        "manifest_version": SHADOW_REVIEW_MANIFEST_VERSION,
        "source_of_truth": SHADOW_REVIEW_MANIFEST_SOURCE_OF_TRUTH,
        "review_scope": shadow_review_scope_payload(),
        "reviews": [full_shadow_review_manifest_entry(review) for review in reviews],
    }
    return full_manifest, project_min_shadow_review_manifest(full_manifest)


def build_repo_doc_surface_manifest_payloads(
    repo_root: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    surfaces = parse_repo_doc_surfaces(repo_root)
    full_manifest = {
        "manifest_version": REPO_DOC_SURFACE_MANIFEST_VERSION,
        "source_of_truth": REPO_DOC_SURFACE_MANIFEST_SOURCE_OF_TRUTH,
        "surface_groups": repo_doc_surface_groups_payload(),
        "docs": [full_repo_doc_surface_manifest_entry(surface) for surface in surfaces],
    }
    return full_manifest, project_min_repo_doc_surface_manifest(full_manifest)


def selection_technique_link(entry: dict[str, Any]) -> str:
    return f"[{entry['id']}](../{entry['technique_path']})"


def record_technique_link(repo_root: Path, record: TechniqueRecord) -> str:
    technique_path = record.technique_path.relative_to(repo_root).as_posix()
    return f"[{record.id}](../{technique_path})"


def strip_display_prefix(text: str, prefix: str) -> str:
    if text.startswith(prefix):
        return text[len(prefix) :]
    return text


def capsule_status_rank(status: str) -> int:
    if status == "canonical":
        return 0
    if status == "promoted":
        return 1
    return 2


def escape_markdown_table_cell(value: str) -> str:
    flattened = re.sub(r"\s*\r?\n\s*", " ", value).strip()
    return flattened.replace("|", r"\|")


def record_sort_key(record: TechniqueRecord) -> tuple[int, int, str, str]:
    if record.domain in DOMAIN_ORDER:
        domain_rank = DOMAIN_ORDER.index(record.domain)
    else:
        domain_rank = len(DOMAIN_ORDER)
    return (domain_rank, capsule_status_rank(record.status), record.status, record.id)


def docs_relative_link(target_path: str) -> str:
    target = PurePosixPath(target_path)
    if target.parts[:1] == ("docs",):
        return PurePosixPath(*target.parts[1:]).as_posix()
    return PurePosixPath("..", *target.parts).as_posix()


def repo_doc_surface_link(surface: RepoDocSurface) -> str:
    return f"[{surface.title}]({docs_relative_link(surface.doc_path)}) (`{surface.doc_path}`)"


def relation_summary(entry: dict[str, Any], entries_by_id: dict[str, dict[str, Any]]) -> str:
    grouped: dict[str, list[str]] = {}
    for relation_type in RELATION_TYPE_ORDER:
        grouped[relation_type] = []

    for relation in entry.get("relations", []):
        target = entries_by_id[relation["target"]]
        grouped[relation["type"]].append(selection_technique_link(target))

    parts: list[str] = []
    for relation_type in RELATION_TYPE_ORDER:
        targets = grouped[relation_type]
        if targets:
            parts.append(f"`{relation_type}` " + ", ".join(targets))
    return "; ".join(parts) if parts else "none"


def note_by_kind(record: TechniqueRecord, kind: str) -> TechniqueNote:
    for note in record.notes:
        if note.kind == kind:
            return note
    fail(f"{record.technique_path}: missing required note kind '{kind}'")


def note_section_by_heading(note: TechniqueNote, heading: str) -> EvidenceNoteSection:
    for section in note.sections:
        if section.heading == heading:
            return section
    fail(f"{note.note_path}: missing required section '{heading}'")


def note_field_value(section: EvidenceNoteSection, key: str, note_path: str) -> str:
    for field in section.fields:
        if field.key == key:
            return field.value_markdown
    fail(f"{note_path}: section '{section.heading}' must include field '{key}'")


def shadow_note_summary(record: TechniqueRecord) -> dict[str, str]:
    note = note_by_kind(record, "adverse_effects_review")
    review_focus = note_section_by_heading(note, "Review focus")
    failure_modes = note_section_by_heading(note, "Failure modes")
    if not failure_modes.items:
        fail(f"{note.note_path}: section 'Failure modes' must include at least one bullet")
    return {
        "current_role": note_field_value(review_focus, "current role", note.note_path),
        "watch_seam": note_field_value(review_focus, "current watch seam", note.note_path),
        "main_failure_mode": failure_modes.items[0].text,
        "note_path": note.note_path,
    }


def technique_source_link(repo_root: Path, record: TechniqueRecord) -> str:
    return f"[TECHNIQUE.md]({docs_relative_link(record.technique_path.relative_to(repo_root).as_posix())})"


def note_kind_title(kind: str) -> str:
    if kind in TYPED_NOTE_TITLES:
        return TYPED_NOTE_TITLES[kind]
    if kind == "support_note":
        return "Support Note"
    return kind.replace("_", " ").title()


def typed_note_scope_signal(kind: str) -> str:
    headings = TYPED_NOTE_SECTION_SCOPES[kind]
    heading_list = ", ".join(f"`{heading}`" for heading in headings)
    return f"`{len(headings)}` fixed sections: {heading_list}"


def note_routing_signal(note: TechniqueNote) -> str:
    if note.note_shape == NOTE_SHAPE_TYPED:
        return f"`{len(note.sections)}` typed sections"
    return "`body_markdown` only"


def build_section_reader_markdown(repo_root: Path, records: list[TechniqueRecord]) -> str:
    sorted_records = sorted(records, key=record_sort_key)
    lines = [
        "# Technique Sections",
        "",
        "This file is generated from authoritative `TECHNIQUE.md` bundles plus the current section manifest payload.",
        "Do not edit it by hand; run `python scripts/build_section_manifest.py`.",
        "",
        "Use this surface when you need one bounded answer to which techniques expose a given lifted section heading without opening every bundle first.",
        "",
        "This surface is heading-first. It stays bounded to exactly `SECTION_LIFT_HEADINGS`, preserves their fixed order, and only exposes technique, section order, and source routing. It does not dump section markdown, invent section IDs, or act like search or graph behavior.",
        "",
        "See also:",
        "- [Technique Section Lift Guide](TECHNIQUE_SECTION_LIFT_GUIDE.md)",
        "- [Full section manifest](../generated/technique_section_manifest.json)",
        "- [Min section manifest](../generated/technique_section_manifest.min.json)",
        "- [Documentation Map](README.md)",
        "- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)",
        "",
        "## Section Scope",
        "",
        "| order | heading | bounded role |",
        "|---|---|---|",
    ]

    for order, heading in enumerate(SECTION_LIFT_HEADINGS, start=1):
        lines.append(
            f"| `{order}` | `{heading}` | Lift the authored `{heading}` section into heading-first routing only. |"
        )

    lines.append("")

    for heading in SECTION_LIFT_HEADINGS:
        lines.extend(
            [
                f"## `{heading}`",
                "",
                "| technique | domain | status | section order | source |",
                "|---|---|---|---|---|",
            ]
        )

        for record in sorted_records:
            section_order = next(
                (order for order, section in enumerate(record.sections, start=1) if section.heading == heading),
                None,
            )
            if section_order is None:
                fail(f"{record.technique_path}: missing required lifted section '{heading}'")

            lines.append(
                "| "
                f"{record_technique_link(repo_root, record)} - {escape_markdown_table_cell(record.name)} | "
                f"`{record.domain}` | "
                f"`{record.status}` | "
                f"`{section_order}` | "
                f"{technique_source_link(repo_root, record)} |"
            )

        lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            "- The meaning remains in the authored `TECHNIQUE.md` bundles.",
            "- This surface is for section routing and lookup only.",
            "- This surface does not become section scoring, a section-ID layer, or search or graph behavior.",
            "",
        ]
    )
    return "\n".join(lines)


def build_checklist_reader_markdown(repo_root: Path, records: list[TechniqueRecord]) -> str:
    lines = [
        "# Technique Checklists",
        "",
        "This file is generated from authoritative `TECHNIQUE.md` bundles plus the current checklist manifest payload.",
        "Do not edit it by hand; run `python scripts/build_checklist_manifest.py`.",
        "",
        "Use this surface when you want a bounded checklist inventory by domain and technique without opening each bundle first.",
        "",
        "This surface stays domain-first and technique-first. It preserves checklist title, intro-presence, item count, check path, and source routing, including techniques that publish more than one checklist.",
        "",
        "See also:",
        "- [Technique Checklist Lift Guide](TECHNIQUE_CHECKLIST_LIFT_GUIDE.md)",
        "- [Full checklist manifest](../generated/technique_checklist_manifest.json)",
        "- [Min checklist manifest](../generated/technique_checklist_manifest.min.json)",
        "- [Documentation Map](README.md)",
        "- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)",
        "",
    ]

    for domain in DOMAIN_ORDER:
        domain_records = sorted(
            [record for record in records if record.domain == domain],
            key=record_sort_key,
        )
        if not domain_records:
            continue

        lines.extend([f"## `{domain}`", ""])
        for record in domain_records:
            lines.extend(
                [
                    f"### {record_technique_link(repo_root, record)} - {record.name} (`{record.status}`)",
                    "",
                ]
            )

            if not record.checklists:
                lines.extend(["_No checklists currently published._", ""])
                continue

            lines.extend(
                [
                    "| checklist | intro | items | check path | source |",
                    "|---|---|---|---|---|",
                ]
            )
            for checklist in record.checklists:
                intro_signal = "present" if checklist.intro_markdown else "absent"
                lines.append(
                    "| "
                    f"{escape_markdown_table_cell(checklist.title)} | "
                    f"`{intro_signal}` | "
                    f"`{len(checklist.items)}` | "
                    f"`{checklist.check_path}` | "
                    f"{technique_source_link(repo_root, record)} |"
                )

            lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            "- The meaning remains in the authored checklist files and source bundles.",
            "- This surface is derived validation knowledge only.",
            "- This surface does not become executable policy, hard-gate semantics, or scoring.",
            "",
        ]
    )
    return "\n".join(lines)


def build_example_reader_markdown(repo_root: Path, records: list[TechniqueRecord]) -> str:
    lines = [
        "# Technique Examples",
        "",
        "This file is generated from authoritative `TECHNIQUE.md` bundles plus the current example manifest payload.",
        "Do not edit it by hand; run `python scripts/build_example_manifest.py`.",
        "",
        "Use this surface when you want a bounded example inventory by domain and technique without opening every example body first.",
        "",
        "This surface preserves example title, example path, body-presence, and source routing only. It does not inline full example bodies into the generated reader surface.",
        "",
        "See also:",
        "- [Technique Example Lift Guide](TECHNIQUE_EXAMPLE_LIFT_GUIDE.md)",
        "- [Full example manifest](../generated/technique_example_manifest.json)",
        "- [Min example manifest](../generated/technique_example_manifest.min.json)",
        "- [Documentation Map](README.md)",
        "- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)",
        "",
    ]

    for domain in DOMAIN_ORDER:
        domain_records = sorted(
            [record for record in records if record.domain == domain],
            key=record_sort_key,
        )
        if not domain_records:
            continue

        lines.extend([f"## `{domain}`", ""])
        for record in domain_records:
            lines.extend(
                [
                    f"### {record_technique_link(repo_root, record)} - {record.name} (`{record.status}`)",
                    "",
                ]
            )

            if not record.examples:
                lines.extend(["_No examples currently published._", ""])
                continue

            lines.extend(
                [
                    "| example | body | example path | source |",
                    "|---|---|---|---|",
                ]
            )
            for example in record.examples:
                body_signal = "present" if example.body_markdown else "absent"
                lines.append(
                    "| "
                    f"{escape_markdown_table_cell(example.title)} | "
                    f"`{body_signal}` | "
                    f"`{example.example_path}` | "
                    f"{technique_source_link(repo_root, record)} |"
                )

            lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            "- The meaning remains in the authored example files and source bundles.",
            "- This surface is derived example knowledge only.",
            "- This surface does not become scenario graphs, executable tests, or richer step extraction.",
            "",
        ]
    )
    return "\n".join(lines)


def build_evidence_note_reader_markdown(repo_root: Path, records: list[TechniqueRecord]) -> str:
    notes_by_kind: dict[str, list[tuple[TechniqueRecord, TechniqueNote]]] = {}
    for record in sorted(records, key=record_sort_key):
        for note in record.notes:
            notes_by_kind.setdefault(note.kind, []).append((record, note))

    known_kind_order = list(TYPED_NOTE_KIND_ORDER) + ["support_note"]
    ordered_kinds = [kind for kind in known_kind_order if kind in notes_by_kind]
    ordered_kinds.extend(sorted(kind for kind in notes_by_kind if kind not in known_kind_order))

    lines = [
        "# Evidence Note Surfaces",
        "",
        "This file is generated from authoritative evidence-note markdown plus the current evidence note manifest payload.",
        "Do not edit it by hand; run `python scripts/build_evidence_note_manifest.py`.",
        "",
        "Use this surface when you need note-kind routing, note-shape awareness, or a bounded inventory of supporting note surfaces without flattening note prose into one reader layer.",
        "",
        "This surface is note-scope first. It only exposes note kind, title, note path, note shape, owning technique, and bounded routing signals such as fixed section scopes or opaque-body handling. It does not flatten note prose, review arguments, or caution language into the reader.",
        "",
        "See also:",
        "- [Evidence Note Provenance Guide](EVIDENCE_NOTE_PROVENANCE_GUIDE.md)",
        "- [Full evidence note manifest](../generated/technique_evidence_note_manifest.json)",
        "- [Min evidence note manifest](../generated/technique_evidence_note_manifest.min.json)",
        "- [Documentation Map](README.md)",
        "- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)",
        "",
        "## Note Scope",
        "",
        "| note kind | title | note shape | routing signal | entries |",
        "|---|---|---|---|---|",
    ]

    for kind in ordered_kinds:
        if kind in TYPED_NOTE_SECTION_SCOPES:
            note_shape = NOTE_SHAPE_TYPED
            routing_signal = typed_note_scope_signal(kind)
        else:
            note_shape = NOTE_SHAPE_OPAQUE
            routing_signal = "opaque note body only"

        lines.append(
            "| "
            f"`{kind}` | "
            f"{escape_markdown_table_cell(note_kind_title(kind))} | "
            f"`{note_shape}` | "
            f"{escape_markdown_table_cell(routing_signal)} | "
            f"`{len(notes_by_kind[kind])}` |"
        )

    lines.append("")

    for kind in ordered_kinds:
        lines.extend(
            [
                f"## `{kind}` - {note_kind_title(kind)}",
                "",
                "| title | note shape | routing signal | owning technique | note path | source |",
                "|---|---|---|---|---|---|",
            ]
        )

        for record, note in notes_by_kind[kind]:
            lines.append(
                "| "
                f"{escape_markdown_table_cell(note.title)} | "
                f"`{note.note_shape}` | "
                f"{escape_markdown_table_cell(note_routing_signal(note))} | "
                f"{record_technique_link(repo_root, record)} | "
                f"`{note.note_path}` | "
                f"[Note]({docs_relative_link(note.note_path)}) |"
            )

        lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            "- The meaning remains in the authored note markdown.",
            "- This surface is derived provenance and routing knowledge only.",
            "- `adverse_effects_review` stays a typed note role, not generated caution policy or a machine-readable caution verdict engine.",
            "- This surface does not flatten note prose, review arguments, or support-note bodies into one merged reader layer.",
            "",
        ]
    )
    return "\n".join(lines)


def build_capsule_markdown(repo_root: Path, records: list[TechniqueRecord]) -> str:
    records_by_id = {record.id: record for record in records}
    full_payload = build_capsule_payload(repo_root, records)
    entries_by_domain: dict[str, list[tuple[TechniqueRecord, dict[str, Any]]]] = {
        domain: [] for domain in DOMAIN_ORDER
    }

    for entry in full_payload["techniques"]:
        record = records_by_id[entry["id"]]
        entries_by_domain[record.domain].append((record, entry))

    lines = [
        "# Technique Capsules",
        "",
        "This file is generated from authoritative `TECHNIQUE.md` bundles plus the current local capsule payload.",
        "Do not edit it by hand; run `python scripts/build_capsules.py`.",
        "",
        "Use this surface when one bounded local runtime card is enough to orient on a technique without opening selection, review, or manifest layers first.",
        "",
        "Capsules are derived local runtime cards for lookup only. They are not the source of truth and they do not replace the authored technique bundles.",
        "",
        "See also:",
        "- [Technique Capsule Guide](TECHNIQUE_CAPSULE_GUIDE.md)",
        "- [Full capsule JSON](../generated/technique_capsules.json)",
        "- [Min capsule JSON](../generated/technique_capsules.min.json)",
        "- [Documentation Map](README.md)",
        "",
    ]

    for domain in DOMAIN_ORDER:
        lines.extend([f"## `{domain}`", ""])
        ordered_entries = sorted(
            entries_by_domain[domain],
            key=lambda item: (capsule_status_rank(item[0].status), item[0].status, item[0].id),
        )

        for record, entry in ordered_entries:
            lines.extend(
                [
                    f"### {record_technique_link(repo_root, record)} - {entry['name']} (`{record.status}`)",
                    "",
                    f"- Summary: {entry['summary']}",
                    f"- Intent: {entry['one_line_intent']}",
                    f"- Use when: {strip_display_prefix(entry['use_when_short'], 'Use when ')}",
                    f"- Avoid when: {strip_display_prefix(entry['do_not_use_short'], 'Avoid when ')}",
                    f"- Needs: {strip_display_prefix(entry['inputs_short'], 'Needs ')}",
                    f"- Produces: {strip_display_prefix(entry['outputs_short'], 'Produces ')}",
                    f"- Core contract: {strip_display_prefix(entry['core_contract_short'], 'Core contract: ')}",
                    f"- Main risk: {strip_display_prefix(entry['main_risk_short'], 'Main risk: ')}",
                    f"- Validate by: {strip_display_prefix(entry['validation_short'], 'Validate by checking ')}",
                    f"- Source: [TECHNIQUE.md](../{entry['technique_path']})",
                    "",
                ]
            )

    lines.extend(
        [
            "## Boundaries",
            "",
            "- The source of meaning stays in the authored `TECHNIQUE.md` bundles.",
            "- Capsules stay local runtime lookup aids only; they are not KAG/source-lift surfaces and they do not replace the full bundle.",
            "- This surface is not selection, scoring, or policy routing.",
            "",
        ]
    )

    return "\n".join(lines)


def build_selection_surface_markdown(full_catalog: dict[str, Any]) -> str:
    entries = list(full_catalog["techniques"])
    entries_by_id = {entry["id"]: entry for entry in entries}
    canonical_by_domain: dict[str, list[dict[str, Any]]] = {domain: [] for domain in DOMAIN_ORDER}
    entries_by_domain: dict[str, list[dict[str, Any]]] = {domain: [] for domain in DOMAIN_ORDER}

    for entry in entries:
        domain = entry["domain"]
        entries_by_domain[domain].append(entry)
        if entry["status"] == "canonical":
            canonical_by_domain[domain].append(entry)

    export_ready_true = sum(1 for entry in entries if entry["export_ready"])
    total_entries = len(entries)
    evaluation_starters = canonical_by_domain["evaluation"]

    lines = [
        "# Technique Selection",
        "",
        "This file is generated from `../generated/technique_catalog.json` and the authoritative markdown frontmatter.",
        "Do not edit it by hand; run `python scripts/build_catalog.py`.",
        "",
        "Use this surface to make one bounded choice:",
        "1. narrow by `domain` first",
        "2. prefer `canonical` techniques for default use",
        "3. use `validation_strength` as an evidence-breadth signal",
        "4. use direct `relations` as adjacency hints, not graph traversal",
        "",
        "See also:",
        "- [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md)",
        "- [CANONICAL_RUBRIC](CANONICAL_RUBRIC.md)",
        "- [Full catalog JSON](../generated/technique_catalog.json)",
        "- [Min catalog JSON](../generated/technique_catalog.min.json)",
        "",
        "## Quick Questions",
        "",
        "### I need an evaluation pattern. Where do I start?",
        "",
        "| technique | validation | summary |",
        "|---|---|---|",
    ]

    for entry in evaluation_starters:
        lines.append(
            "| "
            f"{selection_technique_link(entry)} | "
            f"`{entry['validation_strength']}` | "
            f"{escape_markdown_table_cell(entry['summary'])} |"
        )

    lines.extend(
        [
            "",
            "### What are the current canonical defaults by domain?",
            "",
            "| domain | canonical defaults |",
            "|---|---|",
        ]
    )

    for domain in DOMAIN_ORDER:
        defaults = ", ".join(selection_technique_link(entry) for entry in canonical_by_domain[domain])
        lines.append(f"| `{domain}` | {defaults or '-'} |")

    lines.extend(
        [
            "",
            "### If I choose one technique, what nearby techniques usually go with it?",
            "",
        ]
    )

    for entry in entries:
        lines.append(f"- {selection_technique_link(entry)}: {relation_summary(entry, entries_by_id)}")

    lines.extend(["", "## Browse By Domain", ""])

    for domain in DOMAIN_ORDER:
        lines.extend(
            [
                f"### `{domain}`",
                "",
                "| technique | status | validation | rigor | summary |",
                "|---|---|---|---|---|",
            ]
        )
        for entry in entries_by_domain[domain]:
            lines.append(
                "| "
                f"{selection_technique_link(entry)} | "
                f"`{entry['status']}` | "
                f"`{entry['validation_strength']}` | "
                f"`{entry['rigor_level']}` | "
                f"{escape_markdown_table_cell(entry['summary'])} |"
            )
        lines.append("")

    lines.extend(
        [
            "## Current Catalog Audit",
            "",
            f"- `export_ready` is currently `true` for {export_ready_true}/{total_entries} techniques.",
            "- For the current corpus, that uniform `true` is intentional: every tracked bundle is considered safe for Stage 1 catalog publication.",
            "- Treat `export_ready` as the current Stage 1 catalog-publication safety floor, not as a meaningful selector yet.",
            "- A future `export_ready: false` should mean one bounded thing only: the markdown bundle may still exist, but structured catalog publication would currently overstate its safety, trustworthiness, or stability.",
            "",
        ]
    )

    return "\n".join(lines)


def build_shadow_patterns_markdown(repo_root: Path, records: list[TechniqueRecord]) -> str:
    records_by_id = {record.id: record for record in records}
    review_doc_names = [Path(spec["review_doc"]).name for spec in SHADOW_WORKING_SET_SPECS]

    lines = [
        "# Shadow Patterns",
        "",
        "This file is generated from authoritative `TECHNIQUE.md` bundles plus typed canonical `adverse_effects_review` notes.",
        "Do not edit it by hand; run `python scripts/build_catalog.py`.",
        "",
        "Use this surface when the main question is not which technique to choose, but where a canonical technique can quietly make the system worse and which watch seam to inspect first.",
        "",
        "This surface is canonical-only. It stays bounded to authored markdown, typed adverse-effects notes, review-backed working sets, and validator-backed prompts. It does not do scoring, policy routing, or generated caution metadata.",
        "",
        "See also:",
        "- [Technique Shadow Guide](TECHNIQUE_SHADOW_GUIDE.md)",
        "- [Risk And Negative-Effect Lift Guide](RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md)",
        *[f"- [{name}]({name})" for name in review_doc_names],
        "",
        "## Working Sets",
        "",
    ]

    for spec in SHADOW_WORKING_SET_SPECS:
        linked_techniques = ", ".join(
            record_technique_link(repo_root, records_by_id[technique_id])
            for technique_id in spec["technique_ids"]
        )
        review_doc_name = Path(spec["review_doc"]).name
        lines.extend(
            [
                f"### {spec['title']}",
                "",
                f"- Techniques: {linked_techniques}",
                f"- Review: [{review_doc_name}]({review_doc_name})",
                f"- Why grouped: {spec['note']}",
                "",
                "| technique | current role | watch seam | main failure mode | note |",
                "|---|---|---|---|---|",
            ]
        )

        for technique_id in spec["technique_ids"]:
            record = records_by_id[technique_id]
            summary = shadow_note_summary(record)
            lines.append(
                "| "
                f"{record_technique_link(repo_root, record)} | "
                f"{escape_markdown_table_cell(summary['current_role'])} | "
                f"{escape_markdown_table_cell(summary['watch_seam'])} | "
                f"{escape_markdown_table_cell(summary['main_failure_mode'])} | "
                f"[Adverse Effects Review](../{summary['note_path']}) |"
            )

        lines.append("")

    lines.extend(
        [
            "## Common Shadow Questions",
            "",
            "| question | inspect first | why |",
            "|---|---|---|",
        ]
    )

    for spec in SHADOW_COMMON_QUESTION_SPECS:
        record = records_by_id[spec["target_id"]]
        lines.append(
            "| "
            f"{escape_markdown_table_cell(spec['prompt'])} | "
            f"{record_technique_link(repo_root, record)} | "
            f"{escape_markdown_table_cell(spec['note'])} |"
        )

    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- The source of meaning stays in the full technique bundle and its typed adverse-effects review note.",
            "- This surface is a bounded lookup aid for canonical watch seams, not a permission to skip `TECHNIQUE.md`.",
            "- If a question needs scoring, policy tiers, or machine-readable caution exports, that is a later wave.",
            "",
        ]
    )

    return "\n".join(lines)


def build_repo_doc_surfaces_markdown(repo_root: Path) -> str:
    surfaces = parse_repo_doc_surfaces(repo_root)
    surfaces_by_id = {surface.doc_id: surface for surface in surfaces}
    surfaces_by_group: dict[str, list[RepoDocSurface]] = {
        group: [] for group in REPO_DOC_SURFACE_GROUP_ORDER
    }

    for surface in surfaces:
        surfaces_by_group[surface.surface_group].append(surface)

    group_specs = {spec["group"]: spec for spec in REPO_DOC_SURFACE_GROUP_SPECS}

    lines = [
        "# Repo Doc Surfaces",
        "",
        "This file is generated from the authoritative public docs/status layer only.",
        "Do not edit it by hand; run `python scripts/build_repo_doc_surface_manifest.py`.",
        "",
        "Use this surface when the main question is which public repo doc to open next for orientation, contribution rules, public-safety expectations, or release/status context.",
        "",
        "It stays bounded to the current authored docs/status source set. It excludes local planning files such as `TODO.md`, `PLANS.md`, and `ROADMAP.md`, plus deeper guide/review docs that belong to later waves.",
        "",
        "See also:",
        "- [Repo Doc Surface Lift Guide](REPO_DOC_SURFACE_LIFT_GUIDE.md)",
        "- [Full repo doc surface manifest](../generated/repo_doc_surface_manifest.json)",
        "- [Documentation Map](README.md)",
        "- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)",
        "",
        "## Quick Navigation",
        "",
        "| question | open | why |",
        "|---|---|---|",
    ]

    for spec in REPO_DOC_NAVIGATION_SPECS:
        open_docs = ", ".join(
            repo_doc_surface_link(surfaces_by_id[doc_id]) for doc_id in spec["doc_ids"]
        )
        lines.append(
            "| "
            f"{escape_markdown_table_cell(spec['question'])} | "
            f"{open_docs} | "
            f"{escape_markdown_table_cell(spec['note'])} |"
        )

    lines.append("")

    for group in REPO_DOC_SURFACE_GROUP_ORDER:
        group_spec = group_specs[group]
        lines.extend(
            [
                f"## {group_spec['heading']}",
                "",
                group_spec["note"],
                "",
                "| doc | bounded role | top-level sections |",
                "|---|---|---|",
            ]
        )

        for surface in surfaces_by_group[group]:
            sections_markdown = ", ".join(f"`{heading}`" for heading in surface.top_level_sections)
            lines.append(
                "| "
                f"{repo_doc_surface_link(surface)} | "
                f"{escape_markdown_table_cell(surface.bounded_role)} | "
                f"{escape_markdown_table_cell(sections_markdown)} |"
            )

        lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            "- The source of meaning stays in the authored docs themselves.",
            "- The bounded source set is exactly the 10 authoritative public docs/status files named in `REPO_DOC_SURFACE_LIFT_GUIDE.md`.",
            "- This surface and its manifest are routing aids only. They do not become a new source of truth or a status-policy engine.",
            "",
        ]
    )

    return "\n".join(lines)


def build_selection_patterns_markdown(full_catalog: dict[str, Any]) -> str:
    entries = list(full_catalog["techniques"])
    entries_by_id = {entry["id"]: entry for entry in entries}
    canonical_by_domain: dict[str, list[dict[str, Any]]] = {domain: [] for domain in DOMAIN_ORDER}

    for entry in entries:
        if entry["status"] == "canonical":
            canonical_by_domain[entry["domain"]].append(entry)
    domain_specs = {spec["domain"]: spec for spec in DOMAIN_START_SPECS}

    lines = [
        "# Selection Patterns",
        "",
        "This file is generated from `../generated/technique_catalog.json`, current direct `relations`, validator-backed navigation specs, and review-backed working sets.",
        "Do not edit it by hand; run `python scripts/build_catalog.py`.",
        "",
        "Use this surface when the flat adjacency list in `TECHNIQUE_SELECTION.md` is not enough and you want one bounded answer to:",
        '- "What nearby technique should I inspect next, and why?"',
        "",
        "This surface uses direct relation navigation, validator-backed starting points and common moves, and review-backed clusters only. It does not do graph search, scoring, or multi-hop reasoning.",
        "",
        "See also:",
        "- [Technique Selection](TECHNIQUE_SELECTION.md)",
        "- [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md)",
        "- [Full catalog JSON](../generated/technique_catalog.json)",
        "",
        "## Starting Points",
        "",
        "| domain | canonical defaults | start here |",
        "|---|---|---|",
    ]

    for domain in DOMAIN_ORDER:
        defaults = ", ".join(selection_technique_link(entry) for entry in canonical_by_domain[domain])
        spec = domain_specs[domain]
        lines.append(
            f"| `{domain}` | {defaults or '-'} | {escape_markdown_table_cell(spec['note'])} |"
        )

    lines.extend(["", "## Working Sets", ""])

    for spec in WORKING_SET_SPECS:
        linked_techniques = ", ".join(
            selection_technique_link(entries_by_id[technique_id]) for technique_id in spec["technique_ids"]
        )
        review_doc_name = Path(spec["review_doc"]).name
        lines.extend(
            [
                f"### {spec['title']}",
                "",
                f"- Techniques: {linked_techniques}",
                f"- Review: [{review_doc_name}]({review_doc_name})",
                f"- Why grouped: {spec['note']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Common Moves",
            "",
            "| situation | inspect next | why |",
            "|---|---|---|",
        ]
    )

    for spec in COMMON_MOVE_SPECS:
        lines.append(
            "| "
            f"{escape_markdown_table_cell(spec['prompt'])} | "
            f"{selection_technique_link(entries_by_id[spec['target_id']])} | "
            f"{escape_markdown_table_cell(spec['note'])} |"
        )

    lines.extend(
        [
            "",
            "## Relation Notes",
            "",
            "- `requires` means one technique usually depends on another contract already existing.",
            "- `complements` means two techniques commonly strengthen each other without collapsing into one pattern.",
            "- `used_together_for` means the pair commonly appears in the same operating path, even if one does not strictly depend on the other.",
            "- `shares_contract_with` means neighboring techniques rely on the same bounded contract but still do different work.",
            "- This surface uses direct relation hints only. It does not do graph traversal, ranking, or multi-hop inference.",
            "",
        ]
    )

    return "\n".join(lines)


def write_json_file(path: Path, payload: Any, compact: bool) -> None:
    if compact:
        encoded = json.dumps(payload, ensure_ascii=True, separators=(",", ":"))
    else:
        encoded = json.dumps(payload, ensure_ascii=True, indent=2)
    path.write_text(encoded + "\n", encoding="utf-8")


def write_text_file(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def validate_catalogs(repo_root: Path, records: list[TechniqueRecord], schema_store: dict[str, Any]) -> None:
    full_path = repo_root / "generated" / "technique_catalog.json"
    min_path = repo_root / "generated" / "technique_catalog.min.json"

    expected_full, expected_min = build_catalog_payloads(repo_root, records)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated catalog is out of date; run 'python scripts/build_catalog.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated min catalog is out of date; run 'python scripts/build_catalog.py'"
        )

    min_schema = resolve_schema_ref("index-entry.schema.json", schema_store)
    for index, entry in enumerate(actual_min["techniques"]):
        validate_schema_instance(entry, min_schema, f"{min_path}[{index}]", schema_store)

    projected_min = [
        {
            key: entry[key]
            for key in (
                "id",
                "name",
                "domain",
                "status",
                "summary",
                "maturity_score",
                "rigor_level",
                "reversibility",
                "review_required",
                "validation_strength",
                "export_ready",
                "technique_path",
            )
        }
        for entry in actual_full["techniques"]
    ]
    if projected_min != actual_min["techniques"]:
        fail(f"{min_path}: min catalog must stay a projection of the full catalog")


def validate_capsules(repo_root: Path, records: list[TechniqueRecord]) -> None:
    path = repo_root / "generated" / "technique_capsules.json"
    min_path = repo_root / "generated" / "technique_capsules.min.json"
    reader_path = repo_root / "docs" / "TECHNIQUE_CAPSULES.md"
    expected_full, expected_min = build_capsule_payloads(repo_root, records)
    expected_reader = build_capsule_markdown(repo_root, records)
    actual = read_json(path)
    actual_min = read_json(min_path)
    actual_reader = read_text(reader_path)

    if actual != expected_full:
        fail(f"{path}: generated capsules are out of date; run 'python scripts/build_capsules.py'")
    if actual_min != expected_min:
        fail(f"{min_path}: generated min capsules are out of date; run 'python scripts/build_capsules.py'")
    if actual_reader != expected_reader:
        fail(
            f"{reader_path}: generated capsule reader surface is out of date; "
            "run 'python scripts/build_capsules.py'"
        )

    projected_min = project_min_capsule_payload(actual)
    if projected_min != actual_min:
        fail(f"{min_path}: min capsules must stay a projection of the full capsule payload")

    catalog = read_json(repo_root / "generated" / "technique_catalog.json")
    capsule_alignment = [
        (entry["id"], entry["name"], entry["summary"], entry["technique_path"])
        for entry in actual["techniques"]
    ]
    catalog_alignment = [
        (entry["id"], entry["name"], entry["summary"], entry["technique_path"])
        for entry in catalog["techniques"]
    ]
    if capsule_alignment != catalog_alignment:
        fail(f"{path}: capsule entries must stay 1:1 aligned with generated/technique_catalog.json")


def validate_section_manifests(repo_root: Path, records: list[TechniqueRecord]) -> None:
    full_path = repo_root / "generated" / "technique_section_manifest.json"
    min_path = repo_root / "generated" / "technique_section_manifest.min.json"
    reader_path = repo_root / "docs" / "TECHNIQUE_SECTIONS.md"

    expected_full, expected_min = build_section_manifest_payloads(repo_root, records)
    expected_reader = build_section_reader_markdown(repo_root, records)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)
    actual_reader = read_text(reader_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated section manifest is out of date; "
            f"run 'python scripts/build_section_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated section min manifest is out of date; "
            f"run 'python scripts/build_section_manifest.py'"
        )
    if actual_reader != expected_reader:
        fail(
            f"{reader_path}: generated section reader surface is out of date; "
            "run 'python scripts/build_section_manifest.py'"
        )

    projected_min = project_min_section_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min section manifest must stay a projection of the full manifest")


def validate_checklist_manifests(repo_root: Path, records: list[TechniqueRecord]) -> None:
    full_path = repo_root / "generated" / "technique_checklist_manifest.json"
    min_path = repo_root / "generated" / "technique_checklist_manifest.min.json"
    reader_path = repo_root / "docs" / "TECHNIQUE_CHECKLISTS.md"

    expected_full, expected_min = build_checklist_manifest_payloads(repo_root, records)
    expected_reader = build_checklist_reader_markdown(repo_root, records)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)
    actual_reader = read_text(reader_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated checklist manifest is out of date; "
            f"run 'python scripts/build_checklist_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated checklist min manifest is out of date; "
            f"run 'python scripts/build_checklist_manifest.py'"
        )
    if actual_reader != expected_reader:
        fail(
            f"{reader_path}: generated checklist reader surface is out of date; "
            "run 'python scripts/build_checklist_manifest.py'"
        )

    projected_min = project_min_checklist_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min checklist manifest must stay a projection of the full manifest")


def validate_example_manifests(repo_root: Path, records: list[TechniqueRecord]) -> None:
    full_path = repo_root / "generated" / "technique_example_manifest.json"
    min_path = repo_root / "generated" / "technique_example_manifest.min.json"
    reader_path = repo_root / "docs" / "TECHNIQUE_EXAMPLES.md"

    expected_full, expected_min = build_example_manifest_payloads(repo_root, records)
    expected_reader = build_example_reader_markdown(repo_root, records)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)
    actual_reader = read_text(reader_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated example manifest is out of date; "
            f"run 'python scripts/build_example_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated example min manifest is out of date; "
            f"run 'python scripts/build_example_manifest.py'"
        )
    if actual_reader != expected_reader:
        fail(
            f"{reader_path}: generated example reader surface is out of date; "
            "run 'python scripts/build_example_manifest.py'"
        )

    projected_min = project_min_example_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min example manifest must stay a projection of the full manifest")


def validate_evidence_note_manifests(repo_root: Path, records: list[TechniqueRecord]) -> None:
    full_path = repo_root / "generated" / "technique_evidence_note_manifest.json"
    min_path = repo_root / "generated" / "technique_evidence_note_manifest.min.json"
    reader_path = repo_root / "docs" / "EVIDENCE_NOTE_SURFACES.md"

    expected_full, expected_min = build_evidence_note_manifest_payloads(repo_root, records)
    expected_reader = build_evidence_note_reader_markdown(repo_root, records)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)
    actual_reader = read_text(reader_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated evidence note manifest is out of date; "
            f"run 'python scripts/build_evidence_note_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated evidence note min manifest is out of date; "
            f"run 'python scripts/build_evidence_note_manifest.py'"
        )
    if actual_reader != expected_reader:
        fail(
            f"{reader_path}: generated evidence note reader surface is out of date; "
            "run 'python scripts/build_evidence_note_manifest.py'"
        )

    projected_min = project_min_evidence_note_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min evidence note manifest must stay a projection of the full manifest")


def validate_github_review_template_manifests(repo_root: Path) -> None:
    full_path = repo_root / "generated" / "github_review_template_manifest.json"
    min_path = repo_root / "generated" / "github_review_template_manifest.min.json"

    expected_full, expected_min = build_github_review_template_manifest_payloads(repo_root)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated GitHub review template manifest is out of date; "
            f"run 'python scripts/build_github_review_template_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated GitHub review template min manifest is out of date; "
            f"run 'python scripts/build_github_review_template_manifest.py'"
        )

    projected_min = project_min_github_review_template_manifest(actual_full)
    if projected_min != actual_min:
        fail(
            f"{min_path}: min GitHub review template manifest must stay a projection of the full manifest"
        )


def validate_semantic_review_manifests(repo_root: Path) -> None:
    full_path = repo_root / "generated" / "semantic_review_manifest.json"
    min_path = repo_root / "generated" / "semantic_review_manifest.min.json"

    expected_full, expected_min = build_semantic_review_manifest_payloads(repo_root)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated semantic review manifest is out of date; "
            f"run 'python scripts/build_semantic_review_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated semantic review min manifest is out of date; "
            f"run 'python scripts/build_semantic_review_manifest.py'"
        )

    projected_min = project_min_semantic_review_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min semantic review manifest must stay a projection of the full manifest")


def validate_shadow_review_manifests(repo_root: Path) -> None:
    full_path = repo_root / "generated" / "shadow_review_manifest.json"
    min_path = repo_root / "generated" / "shadow_review_manifest.min.json"

    expected_full, expected_min = build_shadow_review_manifest_payloads(repo_root)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated shadow review manifest is out of date; "
            f"run 'python scripts/build_shadow_review_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated shadow review min manifest is out of date; "
            f"run 'python scripts/build_shadow_review_manifest.py'"
        )

    projected_min = project_min_shadow_review_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min shadow review manifest must stay a projection of the full manifest")


def validate_repo_doc_surface_manifests(repo_root: Path) -> None:
    full_path = repo_root / "generated" / "repo_doc_surface_manifest.json"
    min_path = repo_root / "generated" / "repo_doc_surface_manifest.min.json"

    expected_full, expected_min = build_repo_doc_surface_manifest_payloads(repo_root)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated repo doc surface manifest is out of date; "
            f"run 'python scripts/build_repo_doc_surface_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated repo doc surface min manifest is out of date; "
            f"run 'python scripts/build_repo_doc_surface_manifest.py'"
        )

    projected_min = project_min_repo_doc_surface_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min repo doc surface manifest must stay a projection of the full manifest")


def validate_selection_surface(repo_root: Path, records: list[TechniqueRecord]) -> None:
    selection_path = repo_root / "docs" / "TECHNIQUE_SELECTION.md"
    patterns_path = repo_root / "docs" / "SELECTION_PATTERNS.md"
    shadow_path = repo_root / "docs" / "SHADOW_PATTERNS.md"
    full_path = repo_root / "generated" / "technique_catalog.json"

    validate_selection_working_set_specs(repo_root)
    validate_shadow_working_set_specs(records, repo_root)
    validate_shadow_question_specs(records)

    full_catalog = read_json(full_path)
    expected = build_selection_surface_markdown(full_catalog)
    expected_patterns = build_selection_patterns_markdown(full_catalog)
    expected_shadow = build_shadow_patterns_markdown(repo_root, records)
    actual = read_text(selection_path)
    actual_patterns = read_text(patterns_path)
    actual_shadow = read_text(shadow_path)

    if actual != expected:
        fail(
            f"{selection_path}: generated selection surface is out of date; run 'python scripts/build_catalog.py'"
        )
    if actual_patterns != expected_patterns:
        fail(
            f"{patterns_path}: generated selection patterns surface is out of date; run 'python scripts/build_catalog.py'"
        )
    if actual_shadow != expected_shadow:
        fail(
            f"{shadow_path}: generated shadow patterns surface is out of date; run 'python scripts/build_catalog.py'"
        )


def validate_repo_doc_surface_reader(repo_root: Path) -> None:
    reader_path = repo_root / "docs" / "REPO_DOC_SURFACES.md"
    expected = build_repo_doc_surfaces_markdown(repo_root)
    actual = read_text(reader_path)

    if actual != expected:
        fail(
            f"{reader_path}: generated repo doc surface is out of date; run "
            "'python scripts/build_repo_doc_surface_manifest.py'"
        )


def validate_repo(repo_root: Path) -> None:
    validate_stage1_files(repo_root)
    validate_selection_files(repo_root)
    validate_kag_source_reader_files(repo_root)
    validate_capsule_surface_files(repo_root)
    validate_repo_doc_surface_files(repo_root)
    schema_store = load_schema_store(repo_root)
    records = collect_techniques(repo_root, schema_store)
    validate_selection_navigation_specs(records, repo_root)
    validate_repo_doc_navigation_specs(repo_root)
    validate_index(repo_root, records)
    validate_evidence(records)
    validate_relations(records)
    validate_catalogs(repo_root, records, schema_store)
    validate_capsules(repo_root, records)
    validate_section_manifests(repo_root, records)
    validate_checklist_manifests(repo_root, records)
    validate_example_manifests(repo_root, records)
    validate_evidence_note_manifests(repo_root, records)
    validate_github_review_template_manifests(repo_root)
    validate_semantic_review_manifests(repo_root)
    validate_shadow_review_manifests(repo_root)
    validate_repo_doc_surface_manifests(repo_root)
    validate_selection_surface(repo_root, records)
    validate_repo_doc_surface_reader(repo_root)
    validate_public_hygiene(repo_root)

    canonical_count = sum(1 for record in records if record.status == "canonical")
    promoted_count = sum(1 for record in records if record.status == "promoted")
    deprecated_count = sum(1 for record in records if record.status == "deprecated")

    print(
        f"[ok] validated {len(records)} technique bundles "
        f"({canonical_count} canonical, {promoted_count} promoted, {deprecated_count} deprecated)"
    )
    print("[ok] validated TECHNIQUE_INDEX.md structure and parity")
    print("[ok] validated frontmatter-v2 schema, evidence coverage, and relations")
    print("[ok] validated generated catalog parity")
    print("[ok] validated generated capsule parity and reader surface")
    print("[ok] validated generated section manifest parity and reader surface")
    print("[ok] validated generated checklist manifest parity and reader surface")
    print("[ok] validated generated example manifest parity and reader surface")
    print("[ok] validated generated evidence note manifest parity and reader surface")
    print("[ok] validated generated GitHub review template manifest parity")
    print("[ok] validated generated semantic review manifest parity")
    print("[ok] validated generated shadow review manifest parity")
    print("[ok] validated generated repo doc surface manifest parity")
    print("[ok] validated generated selection and shadow surface parity")
    print("[ok] validated generated repo doc surface parity")
    print("[ok] validated selection navigation specs, repo doc routing specs, review-backed working sets, shadow specs, and bounded public hygiene")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    try:
        validate_repo(repo_root)
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
