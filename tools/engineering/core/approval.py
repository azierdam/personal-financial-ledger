import os

# Updated to match the current template
REQUIRED_SECTIONS = [
    "Sprint",
    "Objective",
    "Scope",
    "Constraints",
    "Acceptance Criteria",
    "Deliverables",
    "Conventional Commit",
    "Stop Condition",
]

def parse(file_path):
    if not os.path.exists(file_path):
        return None
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    sections = {}
    # The template uses '# ' for sections
    # Split by '# ' to isolate sections
    parts = content.split("# ")
    
    for part in parts[1:]:
        lines = part.splitlines()
        header = lines[0].strip()
        body = "\n".join(lines[1:]).strip()
        # Keep body even if empty to handle potential edge cases, 
        # but the logic expects non-empty bodies for parsing logic.
        sections[header] = body
            
    # Validate required sections
    for section in REQUIRED_SECTIONS:
        if section not in sections:
            raise ValueError(f"Missing required section: {section}")
            
    return sections
