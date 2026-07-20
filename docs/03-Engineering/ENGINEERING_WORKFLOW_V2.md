# Engineering Workflow v2.1 (Canonical)

## 1. Lifecycle
Repository Audit -> Knowledge Graph -> Impact Analysis -> Execution Manifest -> Prompt Generation -> Implementation -> Review -> Approval -> Finalization -> Release.

## 2. Principle
The Engineering CLI is a deterministic, artifact-driven orchestrator. No AI reasoning is performed within the CLI. It transforms repository facts into planning contracts.

## 3. Artifact Roles
- **Input Contracts**: Technical Lead Approval (Requirements).
- **Derived Knowledge**: Audit, Graph, Impact, Manifest (The "Knowledge Chain").
- **Execution**: Prompts & Implementation (Derived from manifest).
- **Review**: Review Package (Derived from contract).
- **Authorization**: Technical Lead Review (Manual approval).
