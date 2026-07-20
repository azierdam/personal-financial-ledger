import os
import sys
from . import doctor, context, prompt
from ..core import output, repository

def run(agent):
    root = repository.get_root()
    current_dir = os.path.join(root, "review", "current")
    
    if not os.path.exists(current_dir):
        os.makedirs(current_dir)
        print(f"Created directory: {current_dir}")

    print("\n--- Working File Generation ---")

    # 1. Doctor
    try:
        doctor.run()
    except SystemExit as e:
        if e.code != 0:
            sys.exit(e.code)
    except Exception as e:
        output.error(f"Doctor failed: {e}")
        sys.exit(1)

    # 2. Context
    try:
        print("Regenerating working file: .context.md")
        context.run()
    except SystemExit as e:
        if e.code != 0:
            sys.exit(e.code)
    except Exception as e:
        output.error(f"Context generation failed: {e}")
        sys.exit(1)

    # 3. Prompt
    try:
        print("Regenerating working file: .prompt.md")
        prompt.run(agent)
    except SystemExit as e:
        if e.code != 0:
            sys.exit(e.code)
    except Exception as e:
        output.error(f"Prompt generation failed: {e}")
        sys.exit(1)

    # Success summary
    print("\n--- Preparation Complete ---")
    print("Working files (.context.md, .prompt.md) regenerated.")
    print("Engineering workspace prepared.")
