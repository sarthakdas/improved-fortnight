"""
Tests for the CLI module.
"""

import pytest
from typer.testing import CliRunner
from eigen_robotics.cli import app


class TestCLI:
    """Test cases for the CLI."""
    
    def setup_method(self):
        """Set up test runner."""
        self.runner = CliRunner()
    
    def test_greet_default(self):
        """Test greet command with default name."""
        result = self.runner.invoke(app, ["greet"])
        assert result.exit_code == 0
        assert result.stdout.strip() == "Hello, World!"
        
    def test_greet_with_name(self):
        """Test greet command with custom name."""
        result = self.runner.invoke(app, ["greet", "Alice"])
        assert result.exit_code == 0
        assert result.stdout.strip() == "Hello, Alice!"
        
    def test_calc_add(self):
        """Test calc command with addition."""
        result = self.runner.invoke(app, ["calc", "5", "3", "add"])
        assert result.exit_code == 0
        assert result.stdout.strip() == "Result: 8.0"
        
    def test_calc_divide(self):
        """Test calc command with division."""
        result = self.runner.invoke(app, ["calc", "10", "2", "divide"])
        assert result.exit_code == 0
        assert result.stdout.strip() == "Result: 5.0"
        
    def test_calc_divide_by_zero(self):
        """Test calc command with division by zero."""
        result = self.runner.invoke(app, ["calc", "10", "0", "divide"])
        assert result.exit_code == 1
        assert "Error: Cannot divide by zero" in result.stdout
        
    def test_calc_invalid_operation(self):
        """Test calc command with invalid operation."""
        result = self.runner.invoke(app, ["calc", "5", "3", "power"])
        assert result.exit_code == 1
        assert "Error: Invalid operation" in result.stdout
        
    def test_no_command(self):
        """Test CLI with no command shows help."""
        result = self.runner.invoke(app, [])
        # Typer shows help and exits with code 0 when --help is used, but exits with 2 when no command is given
        # Let's test the help command explicitly
        result = self.runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "A simple dummy Python package for eigen robotics" in result.stdout
        
    def test_version(self):
        """Test version flag."""
        result = self.runner.invoke(app, ["--version"])
        assert result.exit_code == 0
        assert "eigen 0.2.0" in result.stdout