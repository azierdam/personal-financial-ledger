# Engineering Workflow v2.1

## Engineering Lifecycle
1. **Technical Lead Approval**: Technical Lead creates `review/current/technical-lead-approval.md` (Implementation Specification).
2. **Engineering CLI (`prepare`)**: Automates workspace setup based on `approval.md` (Branch management, Context, Prompt).
3. **Gemini Implementation**: Implementation based on `.prompt.md`.
4. **Technical Lead Review**: Technical Lead reviews implementation and creates `technical-lead-review.md`.
5. **Authorization**: Technical Lead review authorizes Post-Approval Actions (Git commit, merge).
6. **Finalization**: Repository synchronized with `main`.

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
