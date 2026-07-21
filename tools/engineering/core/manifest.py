import json
import datetime
from ..core import git, repository, approval
import os

def generate(sprint_id, artifacts, root):
    # Retrieve the authoritative sprint from the approval file
    approval_file = os.path.join(root, "review", "current", "technical-lead-approval.md")
    approval_data = approval.parse(approval_file)
    
    # Extract structured metadata
    # Expected format:
    # # Sprint
    # **Sprint:** <eng_sprint>
    #
    # Supporting Product Sprint: **<product_sprint> (<status>)**
    sprint_full = approval_data.get("Sprint", "Unknown").strip()
    
    # Parse structured data
    eng_sprint = "Unknown"
    product_sprint = "Unknown"
    product_status = "Unknown"
    
    lines = sprint_full.splitlines()
    for line in lines:
        if "**Sprint:**" in line:
            eng_sprint = line.split("**Sprint:**")[1].strip().replace("*", "")
        elif "Supporting Product Sprint:" in line:
            # Format: Supporting Product Sprint: **<product_sprint> (<status>)**
            content = line.split("Supporting Product Sprint:")[1].strip().replace("*", "")
            if "(" in content and ")" in content:
                product_sprint = content.split("(")[0].strip()
                product_status = content.split("(")[1].split(")")[0].strip()
    
    # Validate against passed sprint_id (which is full markdown)
    if sprint_full.replace("*", "").strip() != sprint_id.replace("*", "").strip():
        raise ValueError(f"CRITICAL: Sprint metadata mismatch!")

    return {
        "sprint_metadata": {
            "engineering_sprint": eng_sprint,
            "product_sprint": product_sprint,
            "product_status": product_status
        },
        "timestamp": datetime.datetime.now().isoformat(),
        "branch": git.get_branch(),
        "commit": git.get_commit(),
        "artifacts": artifacts
    }

def save(manifest, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
