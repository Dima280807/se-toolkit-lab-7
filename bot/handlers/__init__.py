"""Command handlers for the LMS Telegram bot.

Handlers are pure functions that take a command string and return a text response.
They don't depend on Telegram — same logic works from --test mode, unit tests, or Telegram.
"""

from .commands import (
    handle_start,
    handle_help,
    handle_health,
    handle_labs,
    handle_scores,
)
from .intent_router import handle_natural_language

__all__ = [
    "handle_start",
    "handle_help",
    "handle_health",
    "handle_labs",
    "handle_scores",
    "handle_natural_language",
]
