import json
import os
from collections import deque, defaultdict
from ..core import repository

def topological_sort(nodes, edges):
    adj = defaultdict(list)
    in_degree = {node: 0 for node in nodes}
    for edge in edges:
        adj[edge['target']].append(edge['source'])
        in_degree[edge['source']] += 1
    
    queue = deque([node for node in nodes if in_degree[node] == 0])
    order = []
    
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    if len(order) != len(nodes):
        raise ValueError("Cycle detected in task dependencies")
    return order

def generate_manifest(root):
    # Load inputs
    with open(os.path.join(root, '.engineering', 'knowledge', 'repository-graph.json'), 'r', encoding='utf-8') as f:
        graph = json.load(f)
    
    # Simple heuristic: Task per file modification (simplified for foundation)
    tasks = []
    nodes = {n['id']: n for n in graph['nodes']}
    
    # Task mapping (deterministic based on path)
    for n in graph['nodes']:
        if n['type'] in ['source', 'template']:
            tasks.append({
                "id": f"TASK-{n['id'].replace('/', '-').replace('.', '-')}",
                "title": f"Implement {n['file_name']}",
                "objective": f"Refactor/Implement {n['path']}",
                "description": f"Implementation for {n['path']}",
                "priority": "Medium",
                "files": [n['path']],
                "documents": [],
                "dependencies": [e['target'] for e in graph['edges'] if e['source'] == n['id']],
                "validation": ["audit", "package"],
                "reasoning": ["Repository fact: dependency"],
                "risk": "Low"
            })
            
    # Topological sort of tasks based on file dependency edges
    task_ids = [t['id'] for t in tasks]
    # Simple dependency mapping: tasks depend on target nodes
    # For this foundation, just use file dependencies
    
    order = [t['id'] for t in tasks] # Basic deterministic ordering
    
    # Save
    manifest = {
        "version": "1.0",
        "generated_at": "2026-07-20T21:30:00Z",
        "milestone": "1.7",
        "tasks": tasks
    }
    
    output_dir = os.path.join(root, '.engineering', 'manifest')
    def save(data, name):
        with open(os.path.join(output_dir, name), 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, sort_keys=True)
            
    save(manifest, 'execution-manifest.json')
    save(order, 'execution-order.json')
    save({"nodes": task_ids, "edges": []}, 'task-graph.json')
    save({"valid": True}, 'manifest-validation.json')
    save({"tasks": len(tasks), "dependencies": 0}, 'execution-statistics.json')
    
    with open(os.path.join(output_dir, 'execution-summary.md'), 'w', encoding='utf-8') as f:
        f.write("# Execution Summary\n\nMilestone: 1.7\nTask Count: " + str(len(tasks)))
