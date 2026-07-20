import os
from ..core import repository, filesystem, git, markdown, approval

def run():
    root = repository.get_root()
    
    # Priority 1: Artifacts
    artifacts_dir = os.path.join(root, "review", "artifacts")
    required_artifacts = ["implementation-summary.md", "validation.md", "gemini-handover.md"]
    found_artifacts = [a for a in required_artifacts if os.path.exists(os.path.join(artifacts_dir, a))]
    
    if len(found_artifacts) >= 2:
        print("Context Source: ✓ Existing Engineering Artifacts")
        _generate_briefing(root, "Context derived from existing artifacts.", found_artifacts)
        return

    # Priority 2: Delta (Git Diff)
    try:
        diff = git.get_diff()
        if diff:
            print("Context Source: ✓ Incremental Context Delta")
            _generate_briefing(root, f"Context derived from git diff:\n\n```diff\n{diff}\n```\n")
            return
    except Exception:
        pass

    # Priority 3: Repository Analysis
    print("Context Source: ✓ Repository Analysis")
    _generate_briefing(root, "Context derived from full repository analysis.")

def _get_file_content(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return "N/A"

def _generate_briefing(root, source_info, artifacts=None):
    approval_file = os.path.join(root, "review", "current", "technical-lead-approval.md")
    approval_data = approval.parse(approval_file) if os.path.exists(approval_file) else {}

    content = f"# Technical Lead Briefing\n\n## Source\n{source_info}\n\n"
    content += f"## Current Sprint\n{approval_data.get('Sprint', 'N/A')}\n\n"
    content += f"## Repository Status\nBranch: {git.get_branch()}\nCommit: {git.get_commit()}\n\n"
    content += f"## Last Approved Architecture\n{_get_file_content(os.path.join(root, 'docs', '01-Architecture', 'Domain_Model.md'))}\n\n"
    content += f"## Completed Since Last Sprint\n{_get_file_content(os.path.join(root, 'docs', 'project', 'CHANGELOG.md'))}\n\n"
    content += f"## Outstanding Work\n{_get_file_content(os.path.join(root, 'docs', 'project', 'BACKLOG.md'))}\n\n"
    content += f"## Dependencies\n{_get_file_content(os.path.join(root, 'package.json'))}\n\n"
    content += f"## Known Risks\n{_get_file_content(os.path.join(root, 'docs', 'project', 'PROJECT_STATUS.md'))}\n\n"
    content += f"## Recommended Next Sprint\n{_get_file_content(os.path.join(root, 'docs', 'project', 'ROADMAP.md'))}\n\n"
    
    if artifacts:
        content += "## Relevant Engineering Artifacts\n"
        for art in artifacts:
            content += f"- {art}\n"
        content += "\n"

    _save_context(content)

def _save_context(content):
    with open(".context.md", "w", encoding='utf-8') as f:
        f.write(content)
    print("Generated .context.md")
