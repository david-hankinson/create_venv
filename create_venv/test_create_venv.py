import unittest
from unittest.mock import patch
import subprocess

from create_venv import create_venv

class TestCreateVenv(unittest.TestCase):
    @patch('builtins.input', return_value='my_venv')
    @patch('subprocess.run')
    def test_create_venv_with_custom_name(self, mock_run, mock_input):
        create_venv()
        
        mock_input.assert_called_once_with("Enter the name of the virtual environment (default: .venv): ")
        mock_run.assert_called_once_with(["python3", "-m", "venv", "my_venv"])
        
if __name__ == '__main__':
    unittest.main()