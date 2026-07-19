import os
import sys
from ..core import repository, output

def run():
    root = repository.get_root()
    if not root:
        output.error("Not a git repository.")
        sys.exit(1)
    
    output.success(f"Repository root: {root}")
    
    required = ["README.md", "GEMINI.md", "appsscript.json"]
    missing = [f for f in required if not os.path.exists(os.path.join(root, f))]
    
    if missing:
        output.error(f"Missing files: {', '.join(missing)}")
        sys.exit(1)
        
    output.success("Environment valid.")
    sys.exit(0)
