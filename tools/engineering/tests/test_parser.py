from ..core import approval
import os
import pytest

def test_parse_success():
    # Setup test file
    with open("test_success.md", "w", encoding="utf-8") as f:
        f.write("# Sprint\nD1.4\n# Objective\nObjectiveText\n# Scope\nScopeText\n# Constraints\nConstraintsText\n# Acceptance Criteria\nAcceptanceText\n# Deliverables\nDeliverablesText\n# Conventional Commit\nCommitText\n# Stop Condition\nStopText")
    
    data = approval.parse("test_success.md")
    assert data["Sprint"] == "D1.4"
    assert data["Objective"] == "ObjectiveText"
    
    os.remove("test_success.md")
    print("Test parse success passed!")

def test_parse_success_with_optional():
    # Setup test file
    with open("test_success_opt.md", "w", encoding="utf-8") as f:
        f.write("# OptionalSection\nOptionalBody\n# Sprint\nD1.4\n# Objective\nObjectiveText\n# Scope\nScopeText\n# Constraints\nConstraintsText\n# Acceptance Criteria\nAcceptanceText\n# Deliverables\nDeliverablesText\n# Conventional Commit\nCommitText\n# Stop Condition\nStopText\n# AnotherOptional\nAnotherBody")
    
    data = approval.parse("test_success_opt.md")
    assert "OptionalSection" not in data
    assert data["Sprint"] == "D1.4"
    
    os.remove("test_success_opt.md")
    print("Test parse success with optional passed!")

def test_parse_missing_required():
    # Setup test file
    with open("test_missing.md", "w", encoding="utf-8") as f:
        f.write("# Sprint\nD1.4")
    
    try:
        approval.parse("test_missing.md")
    except ValueError as e:
        assert "Missing or empty required section" in str(e)
        print("Test parse missing required section passed!")
    
    os.remove("test_missing.md")

if __name__ == "__main__":
    test_parse_success()
    test_parse_success_with_optional()
    test_parse_missing_required()
