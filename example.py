#!/usr/bin/env python3
"""
Example usage of the eigen_roboticspython -m pip install --upgrade build twine package.
"""

from eigen_robotics import greet, calculate, __version__


def main():
    """Demonstrate the package functionality."""
    print(f"eigen_robotics v{__version__}")
    print("=" * 40)
    
    # Demonstrate greet function
    print("\n1. Greeting Examples:")
    print(f"   {greet()}")
    print(f"   {greet('Alice')}")
    print(f"   {greet('Python Developer')}")
    
    # Demonstrate calculate function
    print("\n2. Calculation Examples:")
    operations = [
        (10, 5, "add"),
        (10, 5, "subtract"),
        (10, 5, "multiply"),
        (10, 5, "divide"),
    ]
    
    for x, y, op in operations:
        try:
            result = calculate(x, y, op)
            print(f"   {x} {op} {y} = {result}")
        except ValueError as e:
            print(f"   Error: {e}")
    
    # Demonstrate error handling
    print("\n3. Error Handling:")
    try:
        calculate(10, 0, "divide")
    except ValueError as e:
        print(f"   Division by zero: {e}")
    
    try:
        calculate(5, 3, "power")
    except ValueError as e:
        print(f"   Unsupported operation: {e}")


if __name__ == "__main__":
    main()