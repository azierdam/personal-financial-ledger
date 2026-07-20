import os
import sys
from ..core import repository, filesystem, markdown, approval

def run(agent):
    root = repository.get_root()
    approval_file = os.path.join(root, "review", "current", "technical-lead-approval.md")
    
    if not os.path.exists(approval_file):
        print("Technical Lead approval not found.")
        print("Expected:")
        print("review/current/technical-lead-approval.md")
        sys.exit(1)
        
    sections = approval.parse(approval_file)
    
    prompt = f"# Implementation Task: {sections.get('Objective', 'N/A')}\n\n"
    prompt += f"## Sprint / Milestone\n{sections.get('Sprint / Milestone', 'N/A')}\n\n"
    prompt += f"## Scope\n{sections.get('Scope', 'N/A')}\n\n"
    prompt += f"## Constraints\n{sections.get('Constraints', 'N/A')}\n\n"
    prompt += f"## Acceptance Criteria\n{sections.get('Acceptance Criteria', 'N/A')}\n\n"
    prompt += f"## Required Deliverables\n{sections.get('Required Deliverables', 'N/A')}\n\n"
    prompt += f"## Validation Requirements\n{sections.get('Validation Requirements', 'N/A')}\n\n"
    prompt += f"## Conventional Commit\n{sections.get('Conventional Commit', 'N/A')}\n\n"
    prompt += f"## Stop Condition\n{sections.get('Stop Condition', 'N/A')}\n\n"
    
    prompt += markdown.section("Repository Structure", markdown.list_to_md(filesystem.scan_files(root)[:50]))
    
    with open(".prompt.md", "w") as f:
        f.write(prompt)
    print(f"Generated .prompt.md for {agent}")
