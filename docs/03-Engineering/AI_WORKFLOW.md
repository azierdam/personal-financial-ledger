# AI Workflow

## Engineering Lifecycle
1.  **Planning:** Human and Technical Lead align on the objective and scope.
2.  **Repository Analysis:** Implementation AI maps the task against existing architecture and code.
3.  **Implementation:** AI implements the solution in an isolated manner, adhering to standards.
4.  **Self Review:** AI verifies implementation against requirements and standards.
5.  **Engineering Handover Package:** AI creates the mandatory handover package.
6.  **ChatGPT Review:** Technical Lead validates the implementation.
7.  **Technical Lead Response:** Technical Lead approves or requests changes.
8.  **Human Approval:** Product Owner reviews and accepts the changes.
9.  **Git:** Human Developer executes Git commands to incorporate approved changes.
10. **Merge:** Changes merged into main.

## Engineering Handover Package (Mandatory)
Every sprint must produce a complete engineering record in `review/artifacts/`.
This replaces the "Review Package" concept.

Required artifacts:
- `repository-analysis.md` (when applicable)
- `implementation-plan.md` (when applicable)
- `implementation-summary.md`
- `architecture-notes.md`
- `self-review.md`
- `gemini-handover.md` (Mandatory)
- `validation.md`
- `test-results.md`
- `changed-files.md`
- `commit-message.txt`
- `checklist.md`
- `technical-lead-response.md` (Placeholder)

## Repository Artifact Policy

The repository is the only persistent workspace.

Any artifact that is intended for review, reuse, or version control must be written inside the repository (specifically `review/artifacts/` or `review/snapshots/`).

Do not leave implementation plans, reports, review packages, or documentation in temporary directories, cache folders, or Gemini CLI working folders.

Temporary directories may be used internally during execution but must never become the canonical location of project artifacts.

## Responsibilities
- **Implementation AI:** Analyzes, implements, tests, and packages.
- **Technical Lead:** Validates architecture and implementation quality.
- **Human Developer:** Approves and commits changes.

## Completion Criteria
- Implementation satisfies requirements.
- Automated tests pass.
- Documentation is synchronized.
- Engineering Handover Package is generated and committed.
