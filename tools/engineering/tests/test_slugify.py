from ..core import git

def test_slugify():
    test_cases = {
        "feature/d1.3-create-transaction": "feature-d1-3-create-transaction",
        "feature/engineering cli – git branch slugification-create-transaction": "feature-engineering-cli-git-branch-slugification-create-transaction",
        "Sprint 1.0 / UI": "sprint-1-0-ui",
        "  Spaces  ": "spaces",
        "---Hyphens---": "hyphens",
        "Unicode_Test_é": "unicode-test-e"
    }
    
    for input_str, expected in test_cases.items():
        result = git.slugify_branch_name(input_str)
        assert result == expected, f"Failed: '{input_str}' -> '{result}' (expected '{expected}')"
        print(f"Passed: '{input_str}' -> '{result}'")

if __name__ == "__main__":
    test_slugify()
