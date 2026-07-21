import os
import sys
from ..core import repository, packaging, approval, output

def run(profile):
    root = repository.get_root()
    # Path: E:\Reiza\Projects\AI\PersonalFinance\review\current\technical-lead-approval.md
    approval_file = os.path.join(root, "review", "current", "technical-lead-approval.md") 

    if not os.path.exists(approval_file):
        output.error("Technical Lead approval not found.")
        sys.exit(1)

    try:
        sections = approval.parse(approval_file)
        # Authoritative source: technical-lead-approval.md
        authoritative_sprint = sections.get("Sprint", "Unknown").strip()
        
        # Use authoritative source as sprint_id
        sprint_id = authoritative_sprint
        
        print(f"DEBUG: Using Authoritative Sprint ID: {sprint_id}")
    except Exception as e:
        output.error(f"Failed to parse approval for sprint ID: {e}")
        sys.exit(1)

    try:
        # Pass the authoritative sprint_id
        zip_path = packaging.package(profile, sprint_id, root)
        print(f"\nSuccessfully generated review package: {zip_path}")
    except FileNotFoundError as e:
        output.error(f"Missing required artifacts:\n\n{e}")
        sys.exit(1)
    except Exception as e:
        output.error(f"Packaging failed: {e}")
        sys.exit(1)
