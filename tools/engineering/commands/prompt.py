import os
from ..core import repository, filesystem, markdown

def run(agent):
    root = repository.get_root()
    files = filesystem.scan_files(root)
    
    # Simple prompt generation
    prompt = "# Engineering Task\n\n"
    prompt += "Objective: [Insert Objective Here]\n\n"
    prompt += "Implementation Rules:\n"
    prompt += "- Follow repository standards.\n"
    prompt += "- Implement ONLY the requested feature.\n"
    prompt += "- Do not refactor unrelated code.\n\n"
    prompt += markdown.section("Repository Structure", markdown.list_to_md(files[:50]))
    
    with open(".prompt.md", "w") as f:
        f.write(prompt)
    print(f"Generated .prompt.md for {agent}")
