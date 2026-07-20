import os
import sys
from ..core import repository, packaging, approval, output

def run(profile):
    root = repository.get_root()
    approval_file = os.path.join(root, "review", "current", "technical-lead-approval.md")
    
    if not os.path.exists(approval_file):
        output.error("Technical Lead approval not found.")
        sys.exit(1)
        
    try:
        sections = approval.parse(approval_file)
        sprint_id = sections.get("Sprint", "Unknown").strip()
    except Exception as e:
        output.error(f"Failed to parse approval for sprint ID: {e}")
        sys.exit(1)
        
    try:
        zip_path = packaging.package(profile, sprint_id, root)
        print(f"\nSuccessfully generated review package: {zip_path}")
    except FileNotFoundError as e:
        output.error(f"Missing required artifacts:\n\n{e}")
        sys.exit(1)
    except Exception as e:
        output.error(f"Packaging failed: {e}")
        sys.exit(1)
