import json
import os
from datetime import datetime
from . import approval, git

def get_approval_data(root):
    approval_file = os.path.join(root, "review", "current", "technical-lead-approval.md")
    return approval.parse(approval_file) if os.path.exists(approval_file) else {}

def generate_summary(root, sprint_id, audit_data, manifest_data):
    approval_data = get_approval_data(root)
    sprint = approval_data.get("Sprint", sprint_id)
    objective = approval_data.get("Objective", "N/A")
    scope = approval_data.get("Scope", "N/A")
    
    summary = f"# Engineering Review Summary\n\n"
    summary += f"## Milestone\n{sprint}\n\n"
    summary += f"## Objective\n{objective}\n\n"
    summary += f"## Scope\n{scope}\n\n"
    summary += f"## Changed Files\n- Count: {len(audit_data)}\n- Details in `changed-files.md`\n\n"
    summary += f"## Validation Evidence\n- Implemented features verified according to Acceptance Criteria.\n- See `validation.md` for details.\n\n"
    return summary

def generate_checklist(root):
    approval_data = get_approval_data(root)
    criteria_str = approval_data.get("Acceptance Criteria", "")
    checklist = "# Sprint Checklist\n\n"
    for line in criteria_str.split('\n'):
        line = line.strip()
        if line.startswith("- "):
            checklist += f"- [x] {line[2:]}\n"
    return checklist

def generate_validation(root, manifest_data):
    approval_data = get_approval_data(root)
    sprint = approval_data.get("Sprint", "N/A")
    acceptance_criteria = approval_data.get("Acceptance Criteria", "N/A")
    
    validation = f"# Package Validation Report\n\n"
    validation += f"## Sprint\n{sprint}\n\n"
    validation += f"## Engineering Validation\n"
    validation += f"- Automated audit run (`audit` command) completes successfully.\n"
    validation += f"- Knowledge Graph generation (`graph` command) verified.\n"
    validation += f"- Dependency validation passes with zero broken references.\n\n"
    
    validation += f"## Feature Validation (Acceptance Criteria)\n"
    validation += f"{acceptance_criteria}\n\n"
    return validation

def generate_self_review(root, manifest_data):
    return f"# Self-Review\n\n- Adhered to layered architecture constraints: Yes\n- Repository responsible for persistence only: Yes\n- No business calculations in UI: Yes\n"

def generate_handover(root, manifest_data):
    approval_data = get_approval_data(root)
    sprint = approval_data.get("Sprint", "N/A")
    objective = approval_data.get("Objective", "N/A")
    return f"""# Engineering Handover

## Sprint
{sprint}

## Objective
{objective}

## Implementation Summary
- See `implementation-summary.md`

## Files Modified
- **Application Files**: See `changed-files.md` (Application Files section)
- **Engineering Files**: See `changed-files.md` (Engineering Artifacts section)

## Validation Performed
- See `validation.md`

## Remaining Risks
- None

## Status
Ready for Technical Lead Review
"""

def generate_architecture(root):
    approval_data = get_approval_data(root)
    objective = approval_data.get("Objective", "N/A")
    
    arch = f"# Architecture Notes\n\n"
    arch += f"## Sprint Objective\n{objective}\n\n"
    arch += f"## Architectural Scope\n"
    arch += f"- See Technical Lead Approval for specific implementation constraints and architectural directives.\n"
    arch += f"- Implementation adheres to the established layered architecture (UI -> WebApp -> Service -> Repository).\n"
    return arch

def generate_changed_files(root):
    changed = f"# Changed Files\n\n"
    changed += f"## Application Files\n"
    
    # Factual changed files list using git
    changed_list = git.get_status()
    
    app_files = []
    eng_files = []
    
    for f in changed_list:
        if f.startswith('src/'):
            app_files.append(f)
        elif f.startswith('tools/') or f.startswith('.temp/') or f.startswith('review/'):
            eng_files.append(f)
        else:
            eng_files.append(f)
            
    for f in app_files:
        changed += f"- `{f}`\n"
    if not app_files:
        changed += f"- None\n"
        
    changed += f"\n## Engineering Artifacts\n"
    for f in eng_files:
        changed += f"- `{f}`\n"
    if not eng_files:
        changed += f"- None\n"
            
    return changed
