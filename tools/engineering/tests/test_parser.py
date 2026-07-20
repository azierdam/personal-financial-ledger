from ..core import approval
import os

def test_parse_success():
    # Setup test file
    with open("test_success.md", "w", encoding="utf-8") as f:
        f.write("# Sprint\nValue\n# Objective\nValue\n# Scope\nValue\n# Constraints\nValue\n# Acceptance Criteria\nValue\n# Deliverables\nValue\n# Conventional Commit\nValue\n# Stop Condition\nValue")
    
    data = approval.parse("test_success.md")
    assert data["Sprint"] == "Value"
    
    os.remove("test_success.md")
    print("Test parse success passed!")

def test_parse_missing_section():
    # Setup test file
    with open("test_missing.md", "w", encoding="utf-8") as f:
        f.write("# Sprint\nValue")
    
    try:
        approval.parse("test_missing.md")
    except ValueError as e:
        assert "Missing required section" in str(e)
        print("Test parse missing section passed!")
    
    os.remove("test_missing.md")

if __name__ == "__main__":
    test_parse_success()
    test_parse_missing_section()
