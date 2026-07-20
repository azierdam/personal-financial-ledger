import os

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
        lines = f.readlines()
    
    sections = {}
    current_section = None
    
    for line in lines:
        stripped = line.strip()
        # Look for section headers formatted as '# Section Name'
        if stripped.startswith("# "):
            header = stripped[2:].strip()
            if header in REQUIRED_SECTIONS:
                current_section = header
                sections[current_section] = []
            else:
                # Ignore optional or unknown sections
                current_section = None
        elif current_section:
            sections[current_section].append(stripped)
            
    # Format results
    final_sections = {}
    for k, v in sections.items():
        final_sections[k] = "\n".join(v).strip()
            
    # Validate required sections
    for section in REQUIRED_SECTIONS:
        if section not in final_sections or not final_sections[section]:
            raise ValueError(f"Missing or empty required section: {section}")
            
    return final_sections
