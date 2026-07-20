from ..core import repository_audit

def run():
    print("\n--- Repository Audit ---")
    repository_audit.audit()
    print("Audit complete. Reports saved to .engineering/")
