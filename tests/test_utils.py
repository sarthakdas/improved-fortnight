"""
Tests for the utils module.
"""

import pytest
from eigen_robotics.utils import greet, calculate


class TestGreet:
    """Test cases for the greet function."""
    
    def test_greet_default(self):
        """Test greet with default argument."""
        result = greet()
        assert result == "Hello, World!"
        
    def test_greet_with_name(self):
        """Test greet with custom name."""
        result = greet("Alice")
        assert result == "Hello, Alice!"
        
    def test_greet_with_empty_string(self):
        """Test greet with empty string."""
        result = greet("")
        assert result == "Hello, !"


class TestCalculate:
    """Test cases for the calculate function."""
    
    def test_add(self):
        """Test addition."""
        result = calculate(5, 3, "add")
        assert result == 8.0
        
    def test_subtract(self):
        """Test subtraction."""
        result = calculate(10, 4, "subtract")
        assert result == 6.0
        
    def test_multiply(self):
        """Test multiplication."""
        result = calculate(6, 7, "multiply")
        assert result == 42.0
        
    def test_divide(self):
        """Test division."""
        result = calculate(15, 3, "divide")
        assert result == 5.0
        
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculate(10, 0, "divide")
            
    def test_unsupported_operation(self):
        """Test unsupported operation raises ValueError."""
        with pytest.raises(ValueError, match="Unsupported operation: power"):
            calculate(2, 3, "power")
            
    def test_default_operation(self):
        """Test default operation (add)."""
        result = calculate(5, 3)
        assert result == 8.0
        
    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = calculate(-5, 3, "add")
        assert result == -2.0
        
    def test_float_numbers(self):
        """Test with float numbers."""
        result = calculate(2.5, 1.5, "multiply")
        assert result == 3.75