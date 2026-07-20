from ..core import repository, manifest_engine

def run():
    print("\n--- Execution Manifest Engine ---")
    root = repository.get_root()
    manifest_engine.generate_manifest(root)
    print("Manifest generation complete. Reports saved to .engineering/manifest/")
