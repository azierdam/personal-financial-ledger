import subprocess

def get_branch():
    return subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()

def get_commit():
    return subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
