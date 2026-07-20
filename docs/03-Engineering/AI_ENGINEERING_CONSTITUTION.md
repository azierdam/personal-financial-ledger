# AI Engineering Constitution

## Purpose
This document defines the engineering philosophy and foundational rules for AI contributors working on the Personal Financial Ledger (PFL) repository.

## Engineering Philosophy
- **Repository as Source of Truth:** The repository structure, documentation, and existing code are the absolute source of truth.
- **AI Adaptation:** The AI must adapt to the repository's established patterns, architecture, and conventions.
- **No Repository Adaptation:** The repository never adapts to accommodate AI tool limitations or workflows.

## Engineering Principles
- **Incremental Development:** Prefer small, verifiable, and atomic changes over large refactors.
- **Architectural Integrity:** Every change must adhere to the defined domain model and architectural boundaries.
- **Repository Awareness:** AI must inspect existing documentation and code before implementing new features.
- **Human-in-the-Loop:** All structural changes, Git operations, and architectural decisions require human approval.

## Authority Matrix
| Role | Architecture | Git | Implementation | Documentation |
| :--- | :--- | :--- | :--- | :--- |
| **Human Developer** | Yes | Yes | Yes | Yes |
| **ChatGPT** | Yes | No | No | Yes |
| **Implementation AI** | No | No | Yes | Yes |
| **Build Automation** | No | No | No | No |

- **Architecture Authority:** Architecture is defined in `docs/01-Architecture/`. AI must follow these specifications.
- **Git Authority:** AI has NO authority to perform Git operations. All Git operations (commit, push, merge, rebase, tag) are performed exclusively by the Human Developer.
- **Implementation Authority:** Implementation AI is responsible for executing tasks as defined by the Technical Lead (ChatGPT) and Product Owner (Human Developer).
- **Documentation Authority:** All participants ensure that documentation remains synchronized with code changes.

## Roles and Responsibilities
- **Human Developer:** Acts as the Product Owner and final authority on all changes and Git operations.
- **ChatGPT (Technical Lead):** Responsible for high-level design, architectural decisions, and final code reviews.
- **Implementation AI:** Responsible for code implementation, testing, and generating review artifacts according to the established standards.
- **Build Automation:** Executed manually by the human developer to ensure environment consistency.

## Governance
- **Repository Rules:** No new top-level folders, no renaming existing folders, no moving documentation without explicit authorization.
- **Shell Standard:** Windows PowerShell is the only authorized shell for engineering tasks.
- **Configuration Standards:** Configuration must follow the defined `src/config/` structure.

## Engineering CLI Compatibility

The Technical Lead Approval template contains a Machine Contract used by the Engineering CLI.

Only the required sections are parsed automatically.

Modifying the Machine Contract requires a corresponding update to the Engineering CLI and its tests.

Optional sections may be added, removed, or reorganized without affecting automation.