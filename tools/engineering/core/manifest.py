import json
import datetime
from ..core import git, repository, approval
import os

def generate(sprint_id, artifacts, root):
    # Retrieve the authoritative sprint from the approval file
    approval_file = os.path.join(root, "review", "current", "technical-lead-approval.md")
    approval_data = approval.parse(approval_file)
    authoritative_sprint = approval_data.get("Sprint", "Unknown").strip()
    
    # Compare with passed sprint_id
    # If they conflict, fail immediately as required
    if authoritative_sprint.replace("*", "").strip() != sprint_id.replace("*", "").strip():
        raise ValueError(f"CRITICAL: Sprint metadata mismatch! Authoritative: '{authoritative_sprint}', CLI passed: '{sprint_id}'")

    return {
        "sprint": authoritative_sprint,
        "timestamp": datetime.datetime.now().isoformat(),
        "branch": git.get_branch(),
        "commit": git.get_commit(),
        "artifacts": artifacts
    }

def save(manifest, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
