import os
import zipfile
import shutil
import json
from . import manifest, approval

def generate_structured_summary(root, sprint_id):
    approval_file = os.path.join(root, "review", "current", "technical-lead-approval.md")
    approval_data = approval.parse(approval_file) if os.path.exists(approval_file) else {}
    
    # Simple extraction of components
    summary = f"# Engineering Review Summary\n\n"
    summary += f"## Milestone\n{sprint_id}\n\n"
    summary += f"## Objective\n{approval_data.get('Objective', 'N/A')}\n\n"
    summary += f"## Tasks\n(See approved-findings.json)\n\n"
    summary += f"## Deliverables\n(See manifest.json)\n\n"
    summary += f"## Changed Files\n(See repository-audit.json)\n\n"
    summary += f"## Validation Evidence\n(See validation.md)\n\n"
    summary += f"## Known Limitations\n(See self-review.md)\n\n"
    summary += f"## Next Milestone\n(See technical-lead-review.md)\n\n"
    
    return summary

def package(profile, sprint_id, root):
    contract_path = os.path.join(root, ".engineering", "contracts", "engineering-package-contract.json")
    with open(contract_path, 'r', encoding='utf-8') as f:
        contract = json.load(f)

    required = contract.get("required_deliverables", [])
    optional = contract.get("optional_deliverables", [])
    all_allowed = required + optional
    
    # Validation
    package_dir = os.path.join(root, ".temp", "packaging")
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    os.makedirs(package_dir)

    # Generate Structured Summary
    structured_summary = generate_structured_summary(root, sprint_id)
    with open(os.path.join(package_dir, "implementation-summary.md"), 'w', encoding='utf-8') as f:
        f.write(structured_summary)

    # Collect artifacts (copy others)
    missing = []
    for art in required:
        if art == "implementation-summary.md": continue
        found = False
        for search_dir in ["review/current", "review/artifacts"]:
            src = os.path.join(root, search_dir, art)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(package_dir, art))
                found = True
                break
        if not found:
            missing.append(art)
    
    if missing:
        raise FileNotFoundError(f"Missing required deliverables: {', '.join(missing)}")
    
    # Copy optional if exist
    for art in optional:
        if art == "implementation-summary.md": continue
        for search_dir in ["review/current", "review/artifacts"]:
            src = os.path.join(root, search_dir, art)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(package_dir, art))
                break

    # Manifest
    manifest_data = manifest.generate(sprint_id, all_allowed)
    manifest.save(manifest_data, os.path.join(package_dir, "manifest.json"))
    
    # Zip
    zip_path = os.path.join(root, "review", f"review-package-{profile}.zip")
    shutil.make_archive(zip_path.replace(".zip", ""), 'zip', package_dir)
    
    return zip_path
