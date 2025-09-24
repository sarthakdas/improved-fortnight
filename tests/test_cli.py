"""
Tests for the CLI module.
"""

import pytest
from eigen_robotics.cli import main


class TestCLI:
    """Test cases for the CLI."""
    
    def test_greet_default(self, capsys):
        """Test greet command with default name."""
        result = main(["greet"])
        captured = capsys.readouterr()
        assert result == 0
        assert captured.out.strip() == "Hello, World!"
        
    def test_greet_with_name(self, capsys):
        """Test greet command with custom name."""
        result = main(["greet", "Alice"])
        captured = capsys.readouterr()
        assert result == 0
        assert captured.out.strip() == "Hello, Alice!"
        
    def test_calc_add(self, capsys):
        """Test calc command with addition."""
        result = main(["calc", "5", "3", "add"])
        captured = capsys.readouterr()
        assert result == 0
        assert captured.out.strip() == "Result: 8.0"
        
    def test_calc_divide(self, capsys):
        """Test calc command with division."""
        result = main(["calc", "10", "2", "divide"])
        captured = capsys.readouterr()
        assert result == 0
        assert captured.out.strip() == "Result: 5.0"
        
    def test_calc_divide_by_zero(self, capsys):
        """Test calc command with division by zero."""
        result = main(["calc", "10", "0", "divide"])
        captured = capsys.readouterr()
        assert result == 1
        assert "Error: Cannot divide by zero" in captured.err
        
    def test_no_command(self, capsys):
        """Test CLI with no command shows help."""
        result = main([])
        captured = capsys.readouterr()
        assert result == 1
        assert "usage:" in captured.out
        
    def test_version(self, capsys):
        """Test version flag."""
        with pytest.raises(SystemExit) as exc_info:
            main(["--version"])
        assert exc_info.value.code == 0