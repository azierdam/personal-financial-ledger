import json
import datetime
from ..core import git, repository

def generate(sprint_id, artifacts):
    return {
        "sprint": sprint_id,
        "timestamp": datetime.datetime.now().isoformat(),
        "branch": git.get_branch(),
        "commit": git.get_commit(),
        "artifacts": artifacts
    }

def save(manifest, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
