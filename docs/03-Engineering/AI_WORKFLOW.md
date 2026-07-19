# AI Workflow

## Engineering Lifecycle
1.  **Planning:** Human and Technical Lead align on the objective and scope.
2.  **Repository Analysis:** Implementation AI maps the task against existing architecture and code.
3.  **Implementation:** AI implements the solution in a isolated manner, adhering to standards.
4.  **Self Review:** AI verifies implementation against requirements and standards.
5.  **Review Package:** AI creates a temporary review package.
6.  **ChatGPT Review:** Technical Lead validates the implementation.
7.  **Human Approval:** Product Owner reviews and accepts the changes.
8.  **Git:** Human Developer executes Git commands to incorporate approved changes.

## Repository Artifact Policy

The repository is the only persistent workspace.

Any artifact that is intended for review, reuse, or version control must be written inside the repository.

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
- Review package is generated successfully.
