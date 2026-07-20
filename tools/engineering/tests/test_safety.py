from tools.engineering.commands import prepare
from unittest.mock import patch

def test_validate_working_tree_clean():
    with patch('tools.engineering.commands.prepare.git.get_status') as mock_status:
        mock_status.return_value = []
        assert prepare.validate_working_tree() == True
        print("Test clean passed")

def test_validate_working_tree_dirty_user_modified():
    with patch('tools.engineering.commands.prepare.git.get_status') as mock_status:
        mock_status.return_value = ["src/app/WebApp.gs"]
        # Output will print, so just assert return value
        with patch('sys.exit') as mock_exit:
            assert prepare.validate_working_tree() == False
            print("Test dirty passed")

if __name__ == "__main__":
    test_validate_working_tree_clean()
    test_validate_working_tree_dirty_user_modified()
