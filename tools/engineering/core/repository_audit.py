import os
import json
import hashlib
import re
from ..core import repository

def get_file_metadata(root, path):
    full_path = os.path.join(root, path)
    stat = os.stat(full_path)
    return {
        "path": path,
        "category": path.split('/')[0] if '/' in path else 'root',
        "extension": os.path.splitext(path)[1],
        "size": stat.st_size,
        "generated": path in ['.context.md', '.prompt.md'],
        "last_modified": str(stat.st_mtime),
        "exists": True
    }

def scan_repo(root):
    files = []
    ignore = ['.git', '.engineering', '__pycache__', '.temp']
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ignore]
        for f in filenames:
            if f == '.gitignore': continue
            rel_path = os.path.relpath(os.path.join(dirpath, f), root).replace('\\', '/')
            files.append(get_file_metadata(root, rel_path))
    return sorted(files, key=lambda x: x['path'])

def detect_duplicates(files):
    hashes = {}
    duplicates = []
    for f in files:
        # Simple filename+size duplicate detection
        key = f"{os.path.basename(f['path'])}_{f['size']}"
        if key in hashes:
            duplicates.append({"file1": hashes[key], "file2": f['path']})
        else:
            hashes[key] = f['path']
    return duplicates

def map_dependencies(root, files):
    dep_map = {}
    for f in files:
        full_path = os.path.join(root, f['path'])
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f_obj:
            content = f_obj.read()
            # Factual dependencies: imports, includes, links
            deps = re.findall(r'(?:import|include)\s+[\'"]?([^\s\'"]+)', content)
            deps += re.findall(r'\[.*?\]\((.*?)\)', content)
            dep_map[f['path']] = sorted(list(set(deps)))
    return dep_map

def detect_stale(root, files, dep_map):
    stale = []
    for path, deps in dep_map.items():
        for dep in deps:
            # Check if relative reference exists
            if dep.startswith(('../', './')):
                target = os.path.normpath(os.path.join(os.path.dirname(path), dep))
                if not os.path.exists(os.path.join(root, target)):
                    stale.append({"path": path, "broken_reference": dep})
    return stale

def audit():
    root = repository.get_root()
    if not os.path.exists(os.path.join(root, '.engineering')):
        os.makedirs(os.path.join(root, '.engineering'))
        
    files = scan_repo(root)
    
    # Generate and save JSONs deterministically
    def save(data, name):
        with open(os.path.join(root, '.engineering', name), 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, sort_keys=True)
            
    save(files, 'repository-audit.json')
    save(detect_duplicates(files), 'duplicate-docs.json')
    
    dep_map = map_dependencies(root, files)
    save(dep_map, 'dependency-map.json')
    
    save(detect_stale(root, files, dep_map), 'stale-docs.json')
    
    # Doc inventory (subset of audit)
    docs = [f for f in files if f['category'] == 'docs']
    save(docs, 'documentation-inventory.json')
