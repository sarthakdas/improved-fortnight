"""
Utility functions for the improved-fortnight package.
"""


def greet(name: str = "World") -> str:
    """
    Generate a greeting message.
    
    Args:
        name (str): Name to greet. Defaults to "World".
        
    Returns:
        str: A greeting message.
        
    Example:
        >>> greet("Alice")
        'Hello, Alice!'
        >>> greet()
        'Hello, World!'
    """
    return f"Hello, {name}!"


def calculate(x: float, y: float, operation: str = "add") -> float:
    """
    Perform basic mathematical operations.
    
    Args:
        x (float): First number.
        y (float): Second number.
        operation (str): Operation to perform. Options: 'add', 'subtract', 'multiply', 'divide'.
        
    Returns:
        float: Result of the calculation.
        
    Raises:
        ValueError: If operation is not supported or division by zero.
        
    Example:
        >>> calculate(5, 3, "add")
        8.0
        >>> calculate(10, 2, "divide")
        5.0
    """
    if operation == "add":
        return float(x + y)
    elif operation == "subtract":
        return float(x - y)
    elif operation == "multiply":
        return float(x * y)
    elif operation == "divide":
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return float(x / y)
    else:
        raise ValueError(f"Unsupported operation: {operation}")