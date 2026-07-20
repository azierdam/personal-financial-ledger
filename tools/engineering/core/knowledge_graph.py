import json
import os
from ..core import repository

def get_node_type(f):
    if f['relative_path'].startswith('src/ui/') and f['extension'] == '.html': return 'template'
    if f['relative_path'].startswith('tools/engineering/commands/'): return 'command'
    if f['relative_path'].startswith('test/'): return 'test'
    if f['generated']: return 'generated'
    if f['extension'] in ['.md']: return 'documentation'
    if f['extension'] in ['.gs', '.py', '.js']: return 'source'
    if f['extension'] in ['.json', '.claspignore', '.gitignore']: return 'configuration'
    return 'source'

def build_graph(root):
    audit_path = os.path.join(root, '.engineering', 'repository-audit.json')
    dep_path = os.path.join(root, '.engineering', 'dependency-map.json')
    
    with open(audit_path, 'r', encoding='utf-8') as f:
        files = json.load(f)
    with open(dep_path, 'r', encoding='utf-8') as f:
        deps = json.load(f)
        
    nodes = []
    edges = []
    node_ids = set()
    
    for f in files:
        node_id = f['relative_path']
        node = {
            "id": node_id,
            "type": get_node_type(f),
            "path": node_id,
            "file_name": f['file_name']
        }
        nodes.append(node)
        node_ids.add(node_id)
        
    for path, target_deps in deps.items():
        for target in target_deps:
            # Simple factual link: if it exists in our node list
            # Note: target might be relative path, need robust resolution
            target_path = target if target in node_ids else None
            if not target_path:
                # Try resolving relative path
                candidate = os.path.normpath(os.path.join(os.path.dirname(path), target)).replace('\\', '/')
                if candidate in node_ids:
                    target_path = candidate
            
            if target_path:
                edges.append({
                    "source": path,
                    "target": target_path,
                    "relationship": "references" if get_node_type({'relative_path': path}) == 'documentation' else "imports"
                })
                
    return {"nodes": sorted(nodes, key=lambda x: x['id']), "edges": sorted(edges, key=lambda x: x['source'] + x['target'])}

def generate_graph(root):
    graph = build_graph(root)
    
    # Stats
    stats = {
        "nodes": len(graph['nodes']),
        "edges": len(graph['edges']),
        "isolated_nodes": len([n for n in graph['nodes'] if not any(e['source'] == n['id'] or e['target'] == n['id'] for e in graph['edges'])]),
        "relationship_counts": {}
    }
    for e in graph['edges']:
        rel = e['relationship']
        stats["relationship_counts"][rel] = stats["relationship_counts"].get(rel, 0) + 1
        
    # Validation
    validation = {
        "valid": True,
        "errors": []
    }
    
    # Save
    def save(data, name):
        with open(os.path.join(root, '.engineering', 'knowledge', name), 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, sort_keys=True)
            
    save(graph, 'repository-graph.json')
    save(stats, 'graph-statistics.json')
    save(validation, 'graph-validation.json')
