import sys

def success(message):
    print(f"✅ {message}")

def error(message):
    print(f"❌ {message}", file=sys.stderr)

def info(message):
    print(f"ℹ️ {message}")
