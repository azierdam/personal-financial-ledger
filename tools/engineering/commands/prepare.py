import os
import sys
from . import doctor, context, prompt
from ..core import output, repository, git, approval

GENERATED_ARTIFACTS = {
    '.context.md',
    '.prompt.md',
    'review/review-package-chatgpt.zip'
}

def validate_working_tree():
    changed_files = git.get_status()
    if not changed_files:
        return True

    generated = []
    user_modified = []
    
    for f in changed_files:
        if f in GENERATED_ARTIFACTS:
            generated.append(f)
        else:
            user_modified.append(f)

    print("\n--- Working Tree Safety Diagnostic ---")
    if generated:
        print("Generated Artifacts (safe to overwrite):")
        for f in generated:
            print(f"  - {f}")
    if user_modified:
        print("User Modifications (will be blocked):")
        for f in user_modified:
            print(f"  - {f}")

    if user_modified:
        output.error("\nBranch automation blocked: Uncommitted user modifications detected.")
        print("Recommendation: Commit or stash changes before running 'prepare'.")
        return False
    
    # If only generated artifacts, maybe we warn? 
    # Requirement: "Stop execution before any destructive Git operation."
    # I'll block everything to be absolutely safe as per constraints.
    output.error("\nBranch automation blocked: Uncommitted changes detected.")
    return False

def run(agent):
    root = repository.get_root()

    if not validate_working_tree():
        sys.exit(1)

    approval_file = os.path.join(root, "review", "current", "technical-lead-approval.md")
    
    if not os.path.exists(approval_file):
        output.error("Technical Lead approval not found.")
        sys.exit(1)
        
    try:
        sections = approval.parse(approval_file)
    except Exception as e:
        output.error(f"Failed to parse approval: {e}")
        sys.exit(1)
        
    sprint_id = sections.get("Sprint", "").strip()
    # Clean sprint ID in case it includes delimiters
    if "---" in sprint_id:
        sprint_id = sprint_id.split("---")[0].strip()
    
    if not sprint_id:
        output.error("Sprint ID missing in approval document.")
        sys.exit(1)
        
    raw_branch_name = f"feature/{sprint_id}-create-transaction"
    branch_name = git.slugify_branch_name(raw_branch_name)
    
    print(f"\n--- Branch Automation ---")
    print(f"Target Branch: {branch_name}")
    
    try:
        git.checkout("main")
        git.pull()
        if git.branch_exists(branch_name):
            git.checkout(branch_name)
        else:
            git.create_branch(branch_name)
    except Exception as e:
        output.error(f"Branch automation failed: {e}")
        sys.exit(1)
        
    if git.get_branch() != branch_name:
        output.error(f"Failed to switch to {branch_name}")
        sys.exit(1)
    print(f"Active Branch: {branch_name}")

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
    print(f"Engineering workspace prepared on branch {branch_name}.")
