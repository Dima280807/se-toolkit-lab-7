"""Services for the LMS Telegram bot.

Services are reusable components that handle external dependencies:
- LMS API client for backend communication
- LLM client for natural language understanding (Task 3)
"""

from .lms_api import LMSAPIClient, get_lms_client

__all__ = [
    "LMSAPIClient",
    "get_lms_client",
]
