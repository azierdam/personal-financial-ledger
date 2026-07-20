import os
from ..core import repository, filesystem, git, markdown

def run():
    root = repository.get_root()
    
    # Priority 1: Artifacts
    artifacts_dir = os.path.join(root, "review", "artifacts")
    required_artifacts = ["implementation-summary.md", "validation.md", "gemini-handover.md"]
    found_artifacts = [a for a in required_artifacts if os.path.exists(os.path.join(artifacts_dir, a))]
    
    if len(found_artifacts) >= 2:
        print("Context Source: ✓ Existing Engineering Artifacts")
        content = "Context derived from existing artifacts.\n\n"
        for art in found_artifacts:
            with open(os.path.join(artifacts_dir, art), 'r', encoding='utf-8') as f:
                content += f"## {art}\n{f.read()}\n\n"
        _save_context(content)
        return

    # Priority 2: Delta (Git Diff)
    try:
        diff = git.get_diff()
        if diff:
            print("Context Source: ✓ Incremental Context Delta")
            content = "Context derived from git diff since last sprint:\n\n"
            content += f"```diff\n{diff}\n```\n"
            _save_context(content)
            return
    except Exception:
        pass

    # Priority 3: Repository Analysis
    print("Context Source: ✓ Repository Analysis")
    branch = git.get_branch()
    files = filesystem.scan_files(root)
    content = f"Branch: {branch}\n\n"
    content += markdown.section("File Tree", markdown.list_to_md(files[:50]))
    _save_context(content)

def _save_context(content):
    with open(".context.md", "w", encoding='utf-8') as f:
        f.write(content)
    print("Generated .context.md")
