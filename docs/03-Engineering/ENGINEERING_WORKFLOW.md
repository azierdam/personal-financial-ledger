# Engineering Workflow v2.1

## Engineering Lifecycle
1. **Technical Lead Approval**: Technical Lead creates `review/current/technical-lead-approval.md`.
2. **Phase 1: Repository Preparation (`setup`)**: Engineering CLI automates Git branch management (checkout, pull, branch creation) based on `approval.md`.
3. **Phase 2: Working File Generation (`prepare`)**: Engineering CLI regenerates workspace artifacts (`.context.md`, `.prompt.md`) on the feature branch.
4. **Gemini Implementation**: Implementation based on `.prompt.md`.
5. **Technical Lead Review**: Technical Lead reviews implementation and creates `technical-lead-review.md`.
6. **Authorization**: Technical Lead review authorizes Post-Approval Actions (Git commit, merge).
7. **Finalization**: Repository synchronized with `main`.

## Artifact Ownership

| Artifact | Owner | Purpose |
| :--- | :--- | :--- |
| `technical-lead-approval.md` | Technical Lead | Machine Contract (Implementation Spec) |
| `technical-lead-review.md` | Technical Lead | Authorization (Review/Post-Approval) |
| `.context.md` | Engineering CLI | Gemini context |
| `.prompt.md` | Engineering CLI | Gemini implementation prompt |
| Handover Artifacts | Gemini | Review/Validation (Summary, Val, Git Status, etc.) |

## Scope Guardrails
- Strictly enforce task scope. No unrelated refactoring.
- Engineering CLI automates, Technical Lead decides.
