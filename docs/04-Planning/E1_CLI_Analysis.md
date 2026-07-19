# Repository Analysis: Engineering Sprint E1 — Engineering CLI

## 1. Assessment
The repository currently lacks standardized, automated engineering task support. Development relies on manually executed, fragmented scripts (`scripts/doctor.js`, etc.) or manual documentation checks.

## 2. Architecture Review
The new engineering CLI will be implemented in Python (Standard Library) to ensure zero dependencies, high portability, and low maintenance overhead, keeping it strictly separate from the PFL production codebase (Apps Script).
- **Core Abstractions**: `Repository` (locator), `Filesystem` (scanner), `Git` (subprocess wrapper), `Markdown` (renderer), `Output` (formatting).
- **Commands**: `doctor` (validation), `context` (compilation), `prompt` (prompt generation).
- **Independence**: The tool will not depend on `clasp` or Apps Script directly; it orchestrates the environment, not the runtime.

## 3. Risks
- Python environment dependency on developer machines (Mitigation: Standard library only).
- Maintenance of the tool itself (Mitigation: strict scope limit, no frameworks, simple architecture).

## 4. Acceptance Criteria
- [ ] `doctor` command detects repo root and required files.
- [ ] `context` command generates `.context.md` covering repo structure.
- [ ] `prompt gemini` generates compliant `.prompt.md`.
- [ ] CLI runs via `python -m tools.engineering`.
- [ ] No production PFL code modified.
