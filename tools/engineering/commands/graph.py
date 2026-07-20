from ..core import repository, knowledge_graph

def run():
    print("\n--- Knowledge Graph Engine ---")
    root = repository.get_root()
    knowledge_graph.generate_graph(root)
    print("Graph generation complete. Reports saved to .engineering/knowledge/")
