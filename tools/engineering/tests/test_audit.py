from tools.engineering.core import repository_audit
import os
import shutil
from unittest.mock import patch

def test_audit_flow():
    # Setup: use a temporary root
    root = "test_root"
    os.makedirs(os.path.join(root, "docs"))
    with open(os.path.join(root, "docs", "test.md"), "w") as f:
        f.write("test")
    
    # Run audit with mocked root
    with patch('tools.engineering.core.repository.get_root', return_value=root):
        repository_audit.audit()
    
    # Assert
    assert os.path.exists(os.path.join(root, ".engineering", "repository-audit.json"))
    assert os.path.exists(os.path.join(root, ".engineering", "documentation-inventory.json"))
    
    # Cleanup
    shutil.rmtree(root)
    print("Integration audit test passed!")

if __name__ == "__main__":
    test_audit_flow()
