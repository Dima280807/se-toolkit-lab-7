"""Services for the LMS Telegram bot.

Services are reusable components that handle external dependencies:
- LMS API client for backend communication
- LLM client for natural language understanding (Task 3)
- Tools for LLM intent routing
"""

from .lms_api import LMSAPIClient, get_lms_client
from .llm_client import LLMClient, get_llm_client
from . import tools

__all__ = [
    "LMSAPIClient",
    "get_lms_client",
    "LLMClient",
    "get_llm_client",
    "tools",
]
