import os
import json
import hashlib
import re
from ..core import repository

# Mapping for artifact type based on directory
ARTIFACT_TYPE_MAP = {
    'docs': 'documentation',
    'src': 'source',
    'test': 'test',
    'review': 'artifact',
    'tools': 'tooling',
    'templates': 'template',
    'archive': 'archive'
}

# Mapping for language based on extension
LANGUAGE_MAP = {
    '.gs': 'Google Apps Script',
    '.py': 'Python',
    '.md': 'Markdown',
    '.json': 'JSON',
    '.html': 'HTML',
    '.js': 'JavaScript',
    '.zip': 'Binary'
}

def get_sha256(full_path):
    sha256 = hashlib.sha256()
    with open(full_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def get_file_metadata(root, path):
    full_path = os.path.join(root, path)
    stat = os.stat(full_path)
    
    parts = path.split('/')
    directory = '/'.join(parts[:-1]) if len(parts) > 1 else ''
    
    return {
        "relative_path": path,
        "directory": directory,
        "file_name": os.path.basename(path),
        "extension": os.path.splitext(path)[1],
        "language": LANGUAGE_MAP.get(os.path.splitext(path)[1], 'unknown'),
        "artifact_type": ARTIFACT_TYPE_MAP.get(parts[0], 'other'),
        "size": stat.st_size,
        "sha256": get_sha256(full_path),
        "generated": path in ['.context.md', '.prompt.md'],
        "exists": True,
        "last_modified": str(stat.st_mtime),
        "references": [],
        "referenced_by": []
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
    return sorted(files, key=lambda x: x['relative_path'])

def detect_duplicates(files):
    # Priority: 1. SHA256, 2. Filename
    sha_map = {}
    name_map = {}
    duplicates = []
    
    for f in files:
        sha = f['sha256']
        name = f['file_name']
        
        # Check SHA duplicate
        if sha in sha_map:
            duplicates.append({"reason": "SHA256 identical", "files": [sha_map[sha], f['relative_path']]})
        else:
            sha_map[sha] = f['relative_path']
            
        # Check Name duplicate (excluding known non-duplicates)
        if name in name_map:
            duplicates.append({"reason": "Same filename", "files": [name_map[name], f['relative_path']]})
        else:
            name_map[name] = f['relative_path']
            
    return duplicates

def map_dependencies(root, files):
    dep_map = {}
    for f in files:
        full_path = os.path.join(root, f['relative_path'])
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f_obj:
            content = f_obj.read()
            deps = re.findall(r'(?:import|include)\s+[\'"]?([^\s\'"]+)', content)
            deps += re.findall(r'\[.*?\]\((.*?)\)', content)
            dep_map[f['relative_path']] = sorted(list(set(deps)))
    return dep_map

def detect_stale(root, files, dep_map):
    stale = []
    for path, deps in dep_map.items():
        for dep in deps:
            if dep.startswith(('../', './')):
                target = os.path.normpath(os.path.join(os.path.dirname(path), dep))
                if not os.path.exists(os.path.join(root, target)):
                    stale.append({"path": path, "reason": "broken relative path", "reference": dep})
    return stale

def audit():
    root = repository.get_root()
    if not os.path.exists(os.path.join(root, '.engineering')):
        os.makedirs(os.path.join(root, '.engineering'))
        
    files = scan_repo(root)
    
    def save(data, name):
        with open(os.path.join(root, '.engineering', name), 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, sort_keys=True)
            
    save(files, 'repository-audit.json')
    save(detect_duplicates(files), 'duplicate-docs.json')
    
    dep_map = map_dependencies(root, files)
    save(dep_map, 'dependency-map.json')
    
    save(detect_stale(root, files, dep_map), 'stale-docs.json')
    
    docs = [f for f in files if f['artifact_type'] == 'documentation']
    save(docs, 'documentation-inventory.json')
