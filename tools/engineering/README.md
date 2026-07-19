# Engineering CLI

A lightweight internal developer tool for PFL engineering tasks.

## Commands
- `python -m tools.engineering doctor`: Validate repository environment.
- `python -m tools.engineering context`: Generate repository context in `.context.md`.
- `python -m tools.engineering prompt gemini`: Generate engineering prompt template in `.prompt.md`.
- `python -m tools.engineering prepare gemini`: Orchestrate environment validation, context generation, and prompt generation in a single command. This is the recommended command to run before asking Gemini to implement a new feature.

## VS Code Tasks

You can run these tasks from VS Code using `Terminal → Run Task...`:

- **Engineering: Doctor**: Validate repository environment.
- **Engineering: Context**: Generate repository context.
- **Engineering: Prompt (Gemini)**: Generate engineering prompt template.
- **Engineering: Prepare Gemini**: Executes the `prepare gemini` workflow to validate and generate prompt files.

## Architecture
- `core/`: Generic, reusable modules (repository, filesystem, git, etc.).
- `commands/`: Specific task implementations.
- `templates/`: Templates for artifact generation.
