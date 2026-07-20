from ..core import approval
import os

def test_parse_approval():
    # Create a temporary file for testing
    test_file = "test_approval.md"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("## Objective\n\nTest Objective\n\n## Scope\n\nTest Scope")
    
    data = approval.parse(test_file)
    assert data["Objective"] == "Test Objective"
    assert data["Scope"] == "Test Scope"
    
    os.remove(test_file)
    print("Test passed!")

if __name__ == "__main__":
    test_parse_approval()
