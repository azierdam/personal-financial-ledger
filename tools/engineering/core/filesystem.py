import os

def scan_files(root, ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', 'dist', 'build', '.temp'}
    
    tree = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        for f in filenames:
            tree.append(os.path.relpath(os.path.join(dirpath, f), root))
    return tree
