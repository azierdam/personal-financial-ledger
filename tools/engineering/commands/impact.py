from ..core import repository, impact_engine

def run():
    print("\n--- Documentation Impact Engine ---")
    root = repository.get_root()
    impact_engine.generate_impact(root)
    print("Impact analysis complete. Reports saved to .engineering/impact/")
