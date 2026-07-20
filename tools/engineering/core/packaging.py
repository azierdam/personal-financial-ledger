import os
import zipfile
import shutil
import json
from . import manifest

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

    # Collect artifacts
    missing = []
    for art in required:
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
