import subprocess
import re
import unicodedata

def get_branch():
    return subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()

def get_commit():
    return subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()

def get_diff():
    # Show diff against main
    try:
        return subprocess.check_output(["git", "diff", "main"]).decode().strip()
    except subprocess.CalledProcessError:
        return ""

def checkout(branch):
    subprocess.check_call(["git", "checkout", branch])

def pull():
    subprocess.check_call(["git", "pull"])

def create_branch(branch):
    subprocess.check_call(["git", "checkout", "-b", branch])

def branch_exists(branch):
    return subprocess.call(["git", "show-ref", "--verify", f"refs/heads/{branch}"]) == 0

def slugify_branch_name(name):
    # Normalize unicode
    slug = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
    
    # Lowercase
    slug = slug.lower()
    
    # Replace all non-alphanumeric with hyphens
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    
    # Collapse hyphens
    slug = re.sub(r'-+', '-', slug)
    
    # Trim separators
    slug = slug.strip('-')
    
    return slug
