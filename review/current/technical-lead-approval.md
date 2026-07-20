# Sprint
D1.7

# Objective
Improve the Engineering CLI so that it validates the working tree before branch automation and provides actionable diagnostics instead of raw Git failures.

# Scope
- Detect working tree status before any Git checkout.
- Classify modified files into:
    - Generated artifacts
    - User modifications
- Display a clear diagnostic report.
- Explain why branch automation is blocked.
- Recommend appropriate user actions.
- Stop execution before any destructive Git operation.
- Update documentation describing the Working Tree Safety workflow.
- Add automated tests covering representative scenarios.

# Constraints
- Preserve backward compatibility.
- Do not modify approval parser.
- Do not modify context generation.
- Do not modify package generation.
- Do not automatically stash/discard/commit changes.
- Keep implementation simple and maintainable.

# Acceptance Criteria
- Working tree validation occurs before branch automation.
- Generated artifacts are identified separately from user modifications.
- Git errors are replaced by Engineering CLI diagnostics.
- Users receive clear recovery instructions.
- No automatic modification of the working tree occurs.
- Existing workflows remain backward compatible.
- Documentation is synchronized.
- Automated tests cover representative working tree scenarios.

# Deliverables
- Implementation Summary
- Validation Results
- Updated Documentation
- Git Status
- Recommended Commit Message

# Conventional Commit
feat(cli): add working tree safety validation

# Stop Condition
Stop after implementation.
