# Implementation Plan: Engineering Sprint E1 — Engineering CLI

## Objective
Build a lightweight, Python-based CLI (`tools/engineering/`) to automate repository doctoring, context compilation, and prompt generation.

## Key Changes
- `tools/engineering/`: Core modules, commands, templates, entry point.
- `docs/03-Engineering/Development_Environment.md`: Update to include CLI usage.

## Implementation Steps
1. Create core modules: `repository.py`, `filesystem.py`, `git.py`, `markdown.py`, `output.py`.
2. Create templates: `context.md`, `prompt.md`.
3. Implement commands: `doctor.py`, `context.py`, `prompt.py`.
4. Create entry point: `__main__.py` and `__init__.py`.
5. Create `README.md` for tool usage.
6. Validation: Ensure commands execute via `python -m tools.engineering`.

## Verification
- Run `python -m tools.engineering doctor` to verify setup.
- Run `python -m tools.engineering context` and verify `.context.md` existence and content.
- Run `python -m tools.engineering prompt gemini` and verify `.prompt.md` existence and content.
