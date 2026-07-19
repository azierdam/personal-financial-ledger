import os
from ..core import repository, filesystem, git, markdown

def run():
    root = repository.get_root()
    branch = git.get_branch()
    files = filesystem.scan_files(root)
    
    content = f"Branch: {branch}\n\n"
    content += markdown.section("File Tree", markdown.list_to_md(files[:50])) # Limit for conciseness
    
    with open(".context.md", "w") as f:
        f.write(content)
    print("Generated .context.md")
