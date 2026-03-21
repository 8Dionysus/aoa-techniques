# Concrete Local-First Session History

Scenario: a repository wants its CLI agent sessions to stay inspectable after each terminal run.

1. Launch the coding agent through one wrapper that saves each session locally.
2. Write each session to `.specstory/history/` with a stable project-scoped path.
3. Keep the saved session readable as a versioned artifact even when optional cloud sync is disabled.
4. Run summaries or organization tools on top of that history later, instead of treating those tools as the source of truth.
5. Keep repository instructions and decisions in authored docs, not in the captured transcript itself.

This preserves session knowledge as history without widening into memory substrate or instruction policy.
