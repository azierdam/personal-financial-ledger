# Engineering CLI

A lightweight internal developer tool for PFL engineering tasks.

## Commands
- `python -m tools.engineering doctor`: Validate repository environment.
- `python -m tools.engineering context`: Generate repository context in `.context.md`.
- `python -m tools.engineering prompt gemini`: Generate implementation prompt from `review/current/technical-lead-approval.md` in `.prompt.md`.
- `python -m tools.engineering prepare gemini`: Orchestrate environment validation, context generation, and prompt generation in a single command.

## Prompt Workflow
The `prompt` command automatically generates an implementation prompt based on the approved Technical Lead specification:
1. Ensure the Technical Lead approval document exists at `review/current/technical-lead-approval.md`.
2. Run `python -m tools.engineering prompt gemini`.
3. The CLI will parse the approval document and generate a clean `.prompt.md` file for Gemini.

## VS Code Tasks

You can run these tasks from VS Code using `Terminal → Run Task...`:

- **Engineering: Doctor**: Validate repository environment.
- **Engineering: Context**: Generate repository context.
- **Engineering: Prompt (Gemini)**: Generate engineering prompt.
- **Engineering: Prepare Gemini**: Executes the `prepare gemini` workflow.

## Architecture
- `core/`: Generic, reusable modules (repository, filesystem, git, approval parsing, etc.).
- `commands/`: Specific task implementations.
- `templates/`: Templates for artifact generation.
