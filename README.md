# improved-fortnight

A simple template for a dummy Python package that demonstrates best practices for Python package development.

## Features

- Basic utility functions (greet and calculate)
- Command-line interface
- Comprehensive test suite using pytest
- Modern packaging with pyproject.toml
- Type hints and documentation
- Example usage script

## Installation

### Development Installation

```bash
# Clone the repository
git clone https://github.com/sarthakdas/improved-fortnight.git
cd improved-fortnight

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### From Source

```bash
pip install .
```

## Usage

### As a Library

```python
from improved_fortnight import greet, calculate

# Greeting
print(greet())           # Hello, World!
print(greet("Alice"))    # Hello, Alice!

# Calculations
result = calculate(5, 3, "add")        # 8.0
result = calculate(10, 2, "divide")    # 5.0
result = calculate(4, 7, "multiply")   # 28.0
result = calculate(15, 5, "subtract")  # 10.0
```

### Command Line Interface

```bash
# Greet someone
improved-fortnight greet
improved-fortnight greet Alice

# Perform calculations
improved-fortnight calc 5 3 add
improved-fortnight calc 10 2 divide
improved-fortnight calc 4 7 multiply
improved-fortnight calc 15 5 subtract

# Show version
improved-fortnight --version
```

### Running the Example

```bash
python example.py
```

## Development

### Running Tests

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=improved_fortnight --cov-report=term-missing
```

### Code Quality

```bash
# Format code
black improved_fortnight/ tests/

# Lint code
flake8 improved_fortnight/ tests/

# Type checking
mypy improved_fortnight/
```

## Project Structure

```
improved-fortnight/
├── improved_fortnight/          # Main package directory
│   ├── __init__.py             # Package initialization
│   ├── utils.py                # Core utility functions
│   └── cli.py                  # Command-line interface
├── tests/                      # Test suite
│   ├── __init__.py
│   ├── test_utils.py           # Tests for utils module
│   └── test_cli.py             # Tests for CLI module
├── example.py                  # Usage example script
├── pyproject.toml              # Modern Python packaging configuration
├── README.md                   # This file
└── .gitignore                  # Git ignore rules
```

## License

MIT License - feel free to use this template for your own projects!

## Contributing

This is a template repository. Feel free to fork it and adapt it for your needs!