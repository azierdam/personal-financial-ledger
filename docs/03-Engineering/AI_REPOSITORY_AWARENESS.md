# AI Repository Awareness

## Definition
Repository-aware engineering means that the AI must actively query and understand the context of the current project before proposing or executing any task.

## Mandatory Repository Analysis Sequence
Repository Analysis
↓
Read START_HERE.md
↓
Read README.md
↓
Read docs/INDEX.md
↓
Read engineering standards
↓
Read architecture
↓
Read affected modules
↓
Identify reusable objects
↓
Identify dependencies
↓
Implement
↓
Self Review

Repository analysis MUST occur before implementation.

## Inspection Requirements
Before starting any implementation, the AI must inspect:
- **Repository Structure:** Understand where files reside and how the project is organized.
- **Documentation:** Review `docs/` and `archive/planning-artifacts/` to align with the project's vision and requirements.
- **Architecture:** Understand the domain model and system flow.
- **Existing Code:** Analyze related services, repositories, and adapters to follow existing patterns.
- **Naming Conventions:** Adopt existing naming styles for files, classes, and variables.
- **Reusable Components:** Identify and leverage existing utilities.

## Constraints
- Repository awareness is essential but does not override established architectural decisions.
- If existing code or documentation is unclear, the AI must ask for clarification before proceeding.
