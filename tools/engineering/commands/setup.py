import os
import sys
from ..core import output, repository, git, approval

def run():
    root = repository.get_root()
    
    # 1. Validate Approval
    approval_file = os.path.join(root, "review", "current", "technical-lead-approval.md")
    
    if not os.path.exists(approval_file):
        output.error("Technical Lead approval not found.")
        sys.exit(1)
        
    try:
        sections = approval.parse(approval_file)
    except Exception as e:
        output.error(f"Failed to parse approval: {e}")
        sys.exit(1)
        
    # 2. Extract Sprint ID
    sprint_id = sections.get("Sprint", "").strip()
    if "---" in sprint_id:
        sprint_id = sprint_id.split("---")[0].strip()
    
    if not sprint_id:
        output.error("Sprint ID missing in approval document.")
        sys.exit(1)
        
    # 3. Branch Automation
    raw_branch_name = f"feature/{sprint_id}-create-transaction"
    branch_name = git.slugify_branch_name(raw_branch_name)
    
    print(f"\n--- Branch Automation ---")
    print(f"Target Branch: {branch_name}")
    
    # Safety Check: Check working tree
    changed_files = git.get_status()
    if changed_files:
        output.error("\nBranch automation blocked: Uncommitted user modifications detected.")
        print("Recommendation: Commit or stash changes before running 'setup'.")
        sys.exit(1)
    
    try:
        git.checkout("main")
        git.pull()
        if git.branch_exists(branch_name):
            git.checkout(branch_name)
        else:
            git.create_branch(branch_name)
    except Exception as e:
        output.error(f"Branch automation failed: {e}")
        sys.exit(1)
        
    if git.get_branch() != branch_name:
        output.error(f"Failed to switch to {branch_name}")
        sys.exit(1)
    print(f"Active Branch: {branch_name}")
