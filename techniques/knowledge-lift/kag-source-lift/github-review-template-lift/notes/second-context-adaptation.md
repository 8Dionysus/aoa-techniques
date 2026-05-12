# Second Context Adaptation

## Technique
- id: AOA-T-0047
- name: github-review-template-lift

## Target project
- name: GitHub issue and pull request templates
- public source repository: `github/docs`
- observed surfaces:
  - `content/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates.md`
  - `content/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository.md`
  - `content/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository.md`

## What changed
- intake lift: authored issue templates and pull request templates become contributor-facing intake surfaces in GitHub's issue chooser, rendered issue forms, and pull request body.
- source boundary: template files live in the repository or organization account, and their availability depends on committed source placement such as `.github/ISSUE_TEMPLATE` or `.github/PULL_REQUEST_TEMPLATE`.
- review boundary: the template layer shapes what contributors provide; it does not decide triage, approval, review outcome, or workflow state.
- adaptation fit: this closes the first non-origin template-intake consumer for the bundle's bounded source-lift contract.

## What stayed invariant
- authored templates remain the prompt source.
- the downstream surface is an intake reader or form, not a verdict engine.
- issue forms may structure inputs, but the result remains an issue body or pull request body for later human or workflow review.
- template chooser behavior supports routing to the right prompt shape without turning the manifest or UI into policy.

## Risks introduced by adaptation
- platform-native forms can tempt maintainers to treat structured intake as triage or approval logic.
- generic issue templates are too broad unless the template-to-intake boundary stays visible.
- pull request templates can be ordinary prompts; they count here only because GitHub exposes them as default contributor intake surfaces while source templates remain authored files.

## Evidence
- GitHub's issue-template documentation describes templates on the default branch under `.github/ISSUE_TEMPLATE` and a template chooser for new issues.
- GitHub issue forms convert configured form inputs into a standard Markdown issue comment while keeping the form schema in repository-owned template files.
- GitHub pull request templates automatically populate the pull request body from committed template files, including `.github/PULL_REQUEST_TEMPLATE`.

## Result
- first second-context adaptation recorded
- keep `AOA-T-0047` promoted until canonical review has a stronger review-specific intake consumer or manifest beyond platform-native template rendering
