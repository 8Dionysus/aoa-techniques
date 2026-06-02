from __future__ import annotations

import sys
from pathlib import Path

SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from validate_repo_fixtures import *


class ValidateRepoPublicHygieneTests(unittest.TestCase):
    def test_public_hygiene_allows_public_github_urls(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            docs_dir = repo_root / "docs"
            docs_dir.mkdir(parents=True)
            (docs_dir / "provenance.md").write_text(
                "Source: https://github.com/example/public-technique\n",
                encoding="utf-8",
            )

            validate_repo.validate_public_hygiene(repo_root)

    def test_public_hygiene_rejects_blocked_patterns_on_scanned_surfaces(self) -> None:
        blocked_cases = (
            "D:\\private-repo\\docs\\secret.md",
            "/Users/alice/private-notes.md",
            "See http://localhost:3000/status for details.",
            "Loopback host 127.0.0.1 should not appear here.",
            "ghp_exampletokenvalue",
            "gho_exampletokenvalue",
            "AKIAEXAMPLEKEY",
            "BEGIN OPENSSH PRIVATE KEY",
        )

        for blocked_text in blocked_cases:
            with self.subTest(blocked_text=blocked_text):
                with TemporaryDirectory() as temp_dir:
                    repo_root = Path(temp_dir)
                    docs_dir = repo_root / "docs"
                    docs_dir.mkdir(parents=True)
                    (docs_dir / "public.md").write_text(blocked_text + "\n", encoding="utf-8")

                    with self.assertRaises(validate_repo.ValidationError):
                        validate_repo.validate_public_hygiene(repo_root)

    def test_public_hygiene_rejects_internal_host_suffix_urls(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            docs_dir = repo_root / "docs"
            docs_dir.mkdir(parents=True)
            (docs_dir / "public.md").write_text(
                "See https://grafana.internal/dashboard for details.\n",
                encoding="utf-8",
            )

            with self.assertRaises(validate_repo.ValidationError):
                validate_repo.validate_public_hygiene(repo_root)

    def test_public_hygiene_rejects_rfc1918_urls(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            docs_dir = repo_root / "docs"
            docs_dir.mkdir(parents=True)
            (docs_dir / "public.md").write_text(
                "See https://10.0.0.5/status for details.\n",
                encoding="utf-8",
            )

            with self.assertRaises(validate_repo.ValidationError):
                validate_repo.validate_public_hygiene(repo_root)

    def test_public_hygiene_scans_root_non_markdown_files(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            (repo_root / "PUBLIC.txt").write_text(
                "See https://router.corp/status for details.\n",
                encoding="utf-8",
            )

            with self.assertRaises(validate_repo.ValidationError):
                validate_repo.validate_public_hygiene(repo_root)

    def test_canonical_readiness_notes_do_not_use_windows_absolute_paths(self) -> None:
        note_paths = [
            REPO_ROOT
            / "techniques"
            / "proof"
            / "published-summary"
            / "latest-alias-plus-history-copy"
            / "notes"
            / "canonical-readiness.md",
            REPO_ROOT
            / "techniques"
            / "proof"
            / "published-summary"
            / "published-summary-remediation-snapshot"
            / "notes"
            / "canonical-readiness.md",
            REPO_ROOT
            / "techniques"
            / "proof"
            / "published-summary"
            / "required-vs-optional-source-rendering"
            / "notes"
            / "canonical-readiness.md",
            REPO_ROOT
            / "techniques"
            / "proof"
            / "published-summary"
            / "telemetry-integrity-snapshot"
            / "notes"
            / "canonical-readiness.md",
        ]

        for note_path in note_paths:
            content = note_path.read_text(encoding="utf-8")
            self.assertNotIn("D:\\", content)
            self.assertIn("atm10-agent/docs/", content)

    def test_root_readme_surfaces_concrete_bundle_and_routes_validation_to_agents(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8")

        self.assertIn(
            "techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md",
            readme,
        )
        self.assertIn("../AGENTS.md#validation", start_here)
        self.assertIn("RELEASING.md", start_here)
        for command in (
            "python scripts/validate_repo.py",
            "python scripts/run_tests.py",
            "python scripts/release_check.py",
            "git status -sb",
        ):
            with self.subTest(command=command):
                self.assertNotIn(command, start_here)
        self.assertLess(
            readme.index("techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md"),
            readme.index("docs/README.md"),
        )

    def test_root_readme_does_not_duplicate_github_native_or_validation_surfaces(
        self,
    ) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

        for duplicate_heading in (
            "## License",
            "## Validation",
            "## Root Surfaces",
        ):
            with self.subTest(heading=duplicate_heading):
                self.assertNotIn(duplicate_heading, readme)

        for command in (
            "python scripts/validate_repo.py",
            "python scripts/run_tests.py",
            "python scripts/release_check.py",
            "git status -sb",
        ):
            with self.subTest(command=command):
                self.assertNotIn(command, readme)

        self.assertNotIn("CODE_OF_CONDUCT.md", readme)
        self.assertNotIn("SECURITY.md", readme)
        self.assertNotIn("CONTRIBUTING.md", readme)
        self.assertNotIn("LICENSE", readme)
        self.assertIn("AGENTS.md", readme)

    def test_public_route_surfaces_use_active_links_for_concrete_targets(
        self,
    ) -> None:
        surfaces = {
            "README.md": (REPO_ROOT / "README.md").read_text(encoding="utf-8"),
            "ROADMAP.md": (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8"),
            "AGENTS.md": (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8"),
            "docs/ROOT_SURFACE_LAW.md": (
                REPO_ROOT / "docs" / "ROOT_SURFACE_LAW.md"
            ).read_text(encoding="utf-8"),
        }
        concrete_route_targets = (
            "docs/START_HERE.md",
            "docs/TECHNIQUE_ATOM_CONTRACT.md",
            "docs/TECHNIQUE_TOPOLOGY_CONTRACT.md",
            "docs/TECHNIQUE_TREE_CONTRACT.md",
            "docs/ROOT_SURFACE_LAW.md",
            "TECHNIQUE_INDEX.md",
        )

        for surface_name, surface in surfaces.items():
            for target in concrete_route_targets:
                with self.subTest(surface=surface_name, target=target):
                    self.assertNotIn(f"`{target}`", surface)

        self.assertIn("[TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md)", surfaces["README.md"])
        self.assertIn("[TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md)", surfaces["ROADMAP.md"])
        self.assertIn("[TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md)", surfaces["AGENTS.md"])
        self.assertIn("[README](../README.md)", surfaces["docs/ROOT_SURFACE_LAW.md"])

    def test_public_route_surface_links_resolve(self) -> None:
        link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        surfaces = (
            "README.md",
            "ROADMAP.md",
            "AGENTS.md",
            "CHANGELOG.md",
            "docs/ROOT_SURFACE_LAW.md",
            "docs/readers/repo/REPO_DOC_SURFACES.md",
            "docs/decisions/AOA-TECH-D-0053-root-md-surface-slimming.md",
        )

        for relative_path in surfaces:
            path = REPO_ROOT / relative_path
            for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                for target in link_pattern.findall(line):
                    if (
                        "://" in target
                        or target.startswith("#")
                        or target.startswith("mailto:")
                    ):
                        continue
                    target_path = target.split("#", 1)[0]
                    if not target_path:
                        continue
                    with self.subTest(surface=relative_path, line=line_number, target=target):
                        self.assertTrue((path.parent / target_path).exists())


if __name__ == "__main__":
    unittest.main()
