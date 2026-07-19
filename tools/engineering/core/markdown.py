def section(header, content):
    return f"## {header}\n\n{content}\n\n"

def list_to_md(items):
    return "\n".join([f"- {item}" for item in items])
