import os
import shutil
import json
import sys
from . import manifest, approval, review_generator, output

def package(profile, sprint_id, root):
    contract_path = os.path.join(root, ".engineering", "contracts", "engineering-package-contract.json")
    with open(contract_path, 'r', encoding='utf-8') as f:
        contract = json.load(f)

    # Load context for generators
    audit_path = os.path.join(root, '.engineering', 'repository-audit.json')
    with open(audit_path, 'r', encoding='utf-8') as f:
        audit_data = json.load(f)
        
    manifest_path = os.path.join(root, '.engineering', 'manifest', 'execution-manifest.json')
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest_data = json.load(f)

    required = contract.get("required_deliverables", [])
    optional = contract.get("optional_deliverables", [])
    all_allowed = required + optional
    
    # Validation
    package_dir = os.path.join(root, ".temp", "packaging")
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    os.makedirs(package_dir)

    # Generate Content (all critical review artifacts are generated dynamically)
    generated_content = {
        "implementation-summary.md": review_generator.generate_summary(root, sprint_id, audit_data, manifest_data),
        "validation.md": review_generator.generate_validation(root, manifest_data),
        "self-review.md": review_generator.generate_self_review(root, manifest_data),
        "gemini-handover.md": review_generator.generate_handover(root, manifest_data),
        "architecture-notes.md": review_generator.generate_architecture(root),
        "changed-files.md": review_generator.generate_changed_files(root)
    }

    for art, content in generated_content.items():
        with open(os.path.join(package_dir, art), 'w', encoding='utf-8') as f:
            f.write(content)

    packaged_files = list(generated_content.keys())

    # Collect other artifacts (copy if exist)
    for art in all_allowed:
        if art in generated_content: continue
        
        found = False
        for search_dir in ["review/current", "review/artifacts"]:
            src = os.path.join(root, search_dir, art)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(package_dir, art))
                packaged_files.append(art)
                found = True
                break
        
        # Enforce requirement for 'required' artifacts
        if not found and art in required:
            raise FileNotFoundError(f"Missing required deliverable: {art}")

    # Double check: ensure every file in package_dir exists before zipping (fails loud)
    for file_name in packaged_files:
        target_file = os.path.join(package_dir, file_name)
        if not os.path.exists(target_file):
            raise FileNotFoundError(f"Validation failed: Packaged file {file_name} does not exist.")

    # Manifest (Only contains files actually written to package_dir)
    try:
        manifest_data = manifest.generate(sprint_id, sorted(packaged_files), root)
    except ValueError as e:
        output.error(f"Manifest generation failed: {e}")
        sys.exit(1)
        
    manifest.save(manifest_data, os.path.join(package_dir, "manifest.json"))
    
    # Zip
    zip_path = os.path.join(root, "review", f"review-package-{profile}.zip")
    shutil.make_archive(zip_path.replace(".zip", ""), 'zip', package_dir)
    
    return zip_path
