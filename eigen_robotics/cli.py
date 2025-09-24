"""
Command-line interface for the eigen_robotics package.
"""

import sys
from typing import Optional

import typer

from . import __version__, greet, calculate


app = typer.Typer(help="A simple dummy Python package for eigen robotics")


def version_callback(value: bool):
    if value:
        typer.echo(f"eigen {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback, help="Show version and exit"
    )
):
    """
    Main entry point for the eigen CLI.
    """
    pass


@app.command("greet")
def greet_cmd(name: str = typer.Argument("World", help="Name to greet")):
    """Generate a greeting."""
    result = greet(name)
    typer.echo(result)


@app.command("calc")
def calc_cmd(
    x: float = typer.Argument(..., help="First number"),
    y: float = typer.Argument(..., help="Second number"),
    operation: str = typer.Argument(
        ..., help="Operation to perform (add, subtract, multiply, divide)"
    )
):
    """Perform calculations."""
    valid_operations = ["add", "subtract", "multiply", "divide"]
    if operation not in valid_operations:
        typer.echo(f"Error: Invalid operation. Choose from: {', '.join(valid_operations)}", err=True)
        raise typer.Exit(1)
    
    try:
        result = calculate(x, y, operation)
        typer.echo(f"Result: {result}")
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


def main_wrapper():
    """Wrapper function for the CLI entry point."""
    return app()


if __name__ == "__main__":
    app()