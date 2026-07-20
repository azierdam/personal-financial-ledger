import os
import zipfile
import shutil
from . import manifest

REQUIRED_ARTIFACTS = [
    "technical-lead-approval.md",
    "implementation-summary.md",
    "validation.md",
    "checklist.md",
    "architecture-notes.md",
    "changed-files.md",
    "self-review.md",
    "gemini-handover.md"
]

PROFILES = {
    "chatgpt": [
        "technical-lead-approval.md",
        "implementation-summary.md",
        "validation.md",
        "checklist.md",
        "architecture-notes.md",
        "changed-files.md",
        "self-review.md",
        "gemini-handover.md"
    ]
}

def package(profile, sprint_id, root):
    if profile not in PROFILES:
        raise ValueError(f"Unknown packaging profile: {profile}")
        
    artifacts = PROFILES[profile]
    
    # Validation
    missing = []
    for art in artifacts:
        # Search for artifacts in 'review/current/' or 'review/artifacts/'
        path = None
        if os.path.exists(os.path.join(root, "review", "current", art)):
            path = os.path.join(root, "review", "current", art)
        elif os.path.exists(os.path.join(root, "review", "artifacts", art)):
            path = os.path.join(root, "review", "artifacts", art)
        
        if not path:
            missing.append(art)
    
    if missing:
        raise FileNotFoundError(f"Missing required artifacts: {', '.join(missing)}")
        
    # Packaging
    package_dir = os.path.join(root, ".temp", "packaging")
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    os.makedirs(package_dir)
    
    for art in artifacts:
        src = None
        if os.path.exists(os.path.join(root, "review", "current", art)):
            src = os.path.join(root, "review", "current", art)
        else:
            src = os.path.join(root, "review", "artifacts", art)
        shutil.copy2(src, os.path.join(package_dir, art))
        
    # Manifest
    manifest_data = manifest.generate(sprint_id, artifacts)
    manifest.save(manifest_data, os.path.join(package_dir, "manifest.json"))
    
    # Zip
    zip_path = os.path.join(root, "review", f"review-package-{profile}.zip")
    shutil.make_archive(zip_path.replace(".zip", ""), 'zip', package_dir)
    
    return zip_path
