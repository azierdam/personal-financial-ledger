# Engineering Workflow

## Engineering Lifecycle
1. **Feature Request**
2. **Technical Lead**: Creates `review/current/technical-lead-approval.md` (Approval Template)
3. **Engineering CLI**: `prepare` (Parses approval, automates branch/context/prompt)
4. **Gemini CLI**: Implementation
5. **Technical Lead**: Reviews implementation, creates `technical-lead-review.md` (Review Document)
6. **Authorization**: Technical Lead Review authorizes Post-Approval Actions
7. **Validation & Git Commit**
8. **Merge**

## Technical Lead Documents
1. `technical-lead-approval.md`
   - Parsed by Engineering CLI (Machine Contract).
   - Authorizes implementation.
2. `technical-lead-review.md`
   - Authored manually by Technical Lead after implementation.
   - Authorizes repository synchronization/next steps.

## Responsibilities
- **Implementation AI**: Analyzes, implements, tests, and packages.
- **Technical Lead**: Approves architecture (`approval.md`) and validates quality (`review.md`).
- **Human Developer**: Approves and commits changes.

## Engineering Principles
- Simple solutions, incremental changes, reusable components.

## Scope Guardrails
- Strictly enforce task scope. No unrelated refactoring.
