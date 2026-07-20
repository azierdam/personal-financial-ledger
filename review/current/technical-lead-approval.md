# Sprint

Engineering CLI – Git Branch Slugification

# Objective

Fix Engineering CLI branch generation so that feature branch names derived from the Sprint section always produce valid Git branch names.

# Scope

- Investigate current branch generation.
- Implement deterministic branch slugification.
- Replace spaces with hyphens.
- Convert to lowercase.
- Replace Unicode dashes with standard hyphens.
- Remove unsupported Git branch characters.
- Collapse repeated hyphens.
- Trim leading and trailing separators.
- Preserve deterministic output.
- Update documentation.
- Add automated tests for branch generation.

# Constraints

- Preserve existing Engineering CLI workflow.
- Do not modify the approval parser.
- Do not modify context generation.
- Do not modify package generation.
- Keep implementation simple.
- Do not introduce new dependencies.

# Acceptance Criteria

The sprint is complete when:

- Sprint titles always produce valid Git branch names.
- Unicode punctuation is normalized.
- Spaces are converted to hyphens.
- Invalid Git characters are removed.
- Existing workflows remain backward compatible.
- Automated tests cover representative sprint titles.
- Documentation is updated.

# Deliverables

- Implementation Summary
- Validation Results
- Updated Documentation
- Git Status
- Recommended Commit Message

# Conventional Commit

fix(cli): sanitize generated git branch names

# Stop Condition

Stop after implementation.

Generate the Engineering Review Package using:

python -m tools.engineering package chatgpt

Do not perform repository finalization.

Wait for Technical Lead review.