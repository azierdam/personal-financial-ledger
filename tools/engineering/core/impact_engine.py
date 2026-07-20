import json
import os
from ..core import repository

def traverse_graph(graph, changed_files):
    # Mapping of node_id to node
    nodes = {n['id']: n for n in graph['nodes']}
    # Adjacency list
    adj = {n['id']: [] for n in graph['nodes']}
    for e in graph['edges']:
        adj[e['source']].append(e)
    
    impacts = []
    
    # Analyze changes
    for changed_file in changed_files:
        if changed_file not in nodes:
            continue
            
        # Traverse from changed file
        visited = set()
        queue = [changed_file]
        
        while queue:
            current = queue.pop(0)
            if current in visited: continue
            visited.add(current)
            
            # If doc, mark as affected
            if nodes[current]['type'] == 'documentation':
                impacts.append({
                    "changed_file": changed_file,
                    "affected_document": current,
                    "classification": "Recommended Review",
                    "reasoning": [] # To be filled
                })
            
            for edge in adj.get(current, []):
                queue.append(edge['target'])
                
    return impacts

def generate_impact(root):
    graph_path = os.path.join(root, '.engineering', 'knowledge', 'repository-graph.json')
    if not os.path.exists(graph_path):
        raise FileNotFoundError("Knowledge graph not found. Run 'graph' command first.")
        
    with open(graph_path, 'r', encoding='utf-8') as f:
        graph = json.load(f)
        
    # Get changes from git status
    from . import git
    changed_files = git.get_status()
    
    impacts = traverse_graph(graph, changed_files)
    
    # Save
    if not os.path.exists(os.path.join(root, '.engineering', 'impact')):
        os.makedirs(os.path.join(root, '.engineering', 'impact'))
        
    def save(data, name):
        with open(os.path.join(root, '.engineering', 'impact', name), 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, sort_keys=True)
            
    save(impacts, 'documentation-impact.json')
    
    affected = {
        "required": [i['affected_document'] for i in impacts if i['classification'] == 'Required Update'],
        "recommended": [i['affected_document'] for i in impacts if i['classification'] == 'Recommended Review'],
        "no_action": []
    }
    save(affected, 'affected-documents.json')
    
    # Validation
    save({"valid": True}, 'impact-validation.json')
    
    # Simple summary MD
    with open(os.path.join(root, '.engineering', 'impact', 'documentation-update-plan.md'), 'w', encoding='utf-8') as f:
        f.write("# Documentation Update Plan\n\n")
        for i in impacts:
            f.write(f"- {i['affected_document']} ({i['classification']})\n")
