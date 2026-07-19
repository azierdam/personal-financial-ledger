# Engineering CLI

A lightweight internal developer tool for PFL engineering tasks.

## Commands
- `python -m tools.engineering doctor`: Validate repository environment.
- `python -m tools.engineering context`: Generate repository context in `.context.md`.
- `python -m tools.engineering prompt gemini`: Generate engineering prompt template in `.prompt.md`.

## Architecture
- `core/`: Generic, reusable modules (repository, filesystem, git, etc.).
- `commands/`: Specific task implementations.
- `templates/`: Templates for artifact generation.
