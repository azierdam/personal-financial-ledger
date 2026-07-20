from ..core import repository, cleanup_engine

def run():
    print("\n--- Repository Cleanup Engine ---")
    root = repository.get_root()
    cleanup_engine.execute_cleanup(root)
    print("Cleanup complete. Results saved to .engineering/cleanup/")
