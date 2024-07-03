# tests/test_cli.py

import unittest
from click.testing import CliRunner
from random_quote.cli import main  # Ensure this import path matches your project structure

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_main_with_author(self):
        result = self.runner.invoke(main, ['--author', 'Albert Einstein'])
        self.assertEqual(result.exit_code, 0)  # Update the expected exit code if necessary

    def test_main_without_author(self):
        result = self.runner.invoke(main)
        self.assertEqual(result.exit_code, 0)  # Ensure the default exit code is correct

if __name__ == '__main__':
    unittest.main()

