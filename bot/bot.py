#!/usr/bin/env python3
"""LMS Telegram Bot entry point.

Usage:
    uv run bot.py              # Run as Telegram bot
    uv run bot.py --test "/start"  # Test mode: print response to stdout
"""

import argparse
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from handlers import (
    handle_start,
    handle_help,
    handle_health,
    handle_labs,
    handle_scores,
)


def parse_command(test_input: str) -> tuple[str, str | None]:
    """Parse a command string into command name and argument.
    
    Args:
        test_input: The command string (e.g., "/start", "/scores lab-04")
    
    Returns:
        Tuple of (command_name, argument_or_none)
    """
    parts = test_input.strip().split(maxsplit=1)
    command = parts[0].lstrip("/")
    arg = parts[1] if len(parts) > 1 else None
    return command, arg


def run_test_mode(test_input: str) -> str:
    """Run a command in test mode and return the response.
    
    Args:
        test_input: The command to test (e.g., "/start", "/help")
    
    Returns:
        The handler's text response
    
    Raises:
        ValueError: If the command is not recognized
    """
    command, arg = parse_command(test_input)
    
    handlers = {
        "start": lambda: handle_start(),
        "help": lambda: handle_help(),
        "health": lambda: handle_health(),
        "labs": lambda: handle_labs(),
        "scores": lambda: handle_scores(arg),
    }
    
    if command not in handlers:
        raise ValueError(f"Unknown command: /{command}")
    
    return handlers[command]()


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="LMS Telegram Bot",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Test mode examples:
  uv run bot.py --test "/start"
  uv run bot.py --test "/help"
  uv run bot.py --test "/health"
  uv run bot.py --test "/labs"
  uv run bot.py --test "/scores lab-04"
""",
    )
    parser.add_argument(
        "--test",
        metavar="COMMAND",
        help="Run a command in test mode (prints response to stdout)",
    )
    
    args = parser.parse_args()
    
    if args.test:
        # Test mode: run command and print response
        try:
            response = run_test_mode(args.test)
            print(response)
            sys.exit(0)
        except ValueError as e:
            # Unknown command — return helpful message, not a crash
            print(f"Unknown command. Available commands: /start, /help, /health, /labs, /scores")
            sys.exit(0)
        except Exception as e:
            print(f"Unexpected error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Telegram bot mode (to be implemented in Task 2)
        print("Telegram bot mode not yet implemented. Use --test for testing.")
        print("Example: uv run bot.py --test '/start'")
        sys.exit(0)


if __name__ == "__main__":
    main()
