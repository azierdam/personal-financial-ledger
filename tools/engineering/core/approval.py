import os

def parse(file_path):
    if not os.path.exists(file_path):
        return None
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    sections = {}
    parts = content.split("## ")
    
    for part in parts[1:]:
        lines = part.splitlines()
        header = lines[0].strip()
        body = "\n".join(lines[1:]).strip()
        if body:
            sections[header] = body
            
    return sections
