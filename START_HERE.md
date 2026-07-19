# START HERE

Welcome to the Personal Financial Ledger (PFL) repository.

This document provides the quickest way to understand the project before making any changes.

---

# Repository Purpose

PFL is a production-oriented personal finance application built around:

* Google Sheets
* Google Apps Script
* Telegram
* AI-assisted software engineering

The repository prioritizes simplicity, maintainability, and long-term extensibility.

---

# First Steps

Before making any changes:

1. Read `README.md`.
2. Review the documentation in `docs/`.
3. Ensure your local repository is synchronized with `main`.
4. Create a new feature or chore branch.
5. Implement one focused task at a time.

---

# Active Directories

```text
docs/
src/
scripts/
test/
assets/
```

These directories contain the active project assets.

---

# Archived Planning Artifacts

Planning documents from earlier engineering phases have been moved to:

```text
archive/planning-artifacts/
```

They are retained for historical reference and should not be treated as the authoritative implementation source unless explicitly referenced.

---

# Development Principles

* Keep solutions simple.
* Prefer modular components.
* Avoid unnecessary dependencies.
* Maintain backward compatibility where practical.
* Update documentation alongside implementation.
* Validate changes before committing.

---

# Git Workflow

```text
main
 ├── chore/*
 ├── feature/*
 └── fix/*
```

Never develop directly on `main`.

---

# Current Priority

Current repository objective:

**Repository Cleanup & Synchronization**

After cleanup is complete, development will continue with the Expense Transaction Flow and subsequent production milestones.

---

# Need More Information?

Refer to the documentation under the `docs/` directory for detailed project information and implementation guidance.

---

## AI Engineering

This repository follows the AI Engineering Playbook. AI contributors MUST complete repository analysis before implementation.

### Recommended Reading Order
1. START_HERE.md
2. README.md
3. docs/INDEX.md
4. docs/03-Engineering/AI_ENGINEERING_CONSTITUTION.md
5. docs/03-Engineering/AI_WORKFLOW.md
6. docs/03-Engineering/AI_IMPLEMENTATION_STANDARD.md
7. docs/03-Engineering/AI_REPOSITORY_AWARENESS.md
8. docs/03-Engineering/AI_CHECKLIST.md
9. docs/01-Architecture/
10. Relevant source code
11. Current implementation task