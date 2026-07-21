
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
print(f"REQUIRED_SECTIONS: {REQUIRED_SECTIONS}")

def parse(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    sections = {}
    current_section = None
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Look for section headers formatted as '# Section Name'
        if stripped.startswith("# "):
            header = stripped[2:].strip()
            print(f"Found header: '{header}' at line {i}")
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
            print(f"Missing or empty required section: {section}")
        else:
            print(f"Found section: {section} (len: {len(final_sections[section])})")
            
    return final_sections

parse('review/current/technical-lead-approval.md')
