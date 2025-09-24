"""
Command-line interface for the improved-fortnight package.
"""

import argparse
import sys
from typing import List, Optional

from . import __version__, greet, calculate


def main(argv: Optional[List[str]] = None) -> int:
    """
    Main entry point for the CLI.
    
    Args:
        argv: Command line arguments. If None, uses sys.argv.
        
    Returns:
        int: Exit code (0 for success, non-zero for error).
    """
    if argv is None:
        argv = sys.argv[1:]
    
    parser = argparse.ArgumentParser(
        description="A simple dummy Python package",
        prog="improved-fortnight"
    )
    parser.add_argument(
        "--version", 
        action="version", 
        version=f"%(prog)s {__version__}"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Greet command
    greet_parser = subparsers.add_parser("greet", help="Generate a greeting")
    greet_parser.add_argument(
        "name", 
        nargs="?", 
        default="World", 
        help="Name to greet (default: World)"
    )
    
    # Calculate command
    calc_parser = subparsers.add_parser("calc", help="Perform calculations")
    calc_parser.add_argument("x", type=float, help="First number")
    calc_parser.add_argument("y", type=float, help="Second number")
    calc_parser.add_argument(
        "operation", 
        choices=["add", "subtract", "multiply", "divide"],
        help="Operation to perform"
    )
    
    args = parser.parse_args(argv)
    
    if args.command == "greet":
        print(greet(args.name))
        return 0
    elif args.command == "calc":
        try:
            result = calculate(args.x, args.y, args.operation)
            print(f"Result: {result}")
            return 0
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())