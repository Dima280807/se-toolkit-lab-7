"""LLM API client service.

This service handles all HTTP requests to the LLM API for intent classification.
"""

import json
from pathlib import Path

import httpx
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuration for the LLM API client."""

    llm_api_base_url: str = ""
    llm_api_key: str = ""
    llm_api_model: str = "coder-model"

    class Config:
        # Look for .env.bot.secret in the project root (parent of bot/)
        env_file = str(Path(__file__).parent.parent.parent / ".env.bot.secret")
        env_file_encoding = "utf-8"
        # Ignore extra fields in the .env file (e.g., BOT_TOKEN, LMS_*)
        extra = "ignore"


class LLMClient:
    """Client for the LLM API."""

    def __init__(self, settings: Settings | None = None):
        """Initialize the LLM client.

        Args:
            settings: Configuration settings. If None, loads from environment.
        """
        self.settings = settings or Settings()
        self.base_url = self.settings.llm_api_base_url.rstrip("/") if self.settings.llm_api_base_url else ""
        self.api_key = self.settings.llm_api_key
        self.model = self.settings.llm_api_model

    def chat(self, messages: list[dict], tools: list[dict] | None = None) -> dict:
        """Send a chat request to the LLM API.

        Args:
            messages: List of message dicts with 'role' and 'content'.
            tools: Optional list of tool definitions for function calling.

        Returns:
            LLM response as a dict.

        Raises:
            ValueError: If LLM API is not configured.
            httpx.RequestError: If the request fails.
        """
        if not self.base_url or not self.api_key:
            raise ValueError(
                "LLM API is not configured. "
                "Make sure .env.bot.secret contains LLM_API_BASE_URL and LLM_API_KEY"
            )

        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.model,
            "messages": messages,
        }

        if tools:
            payload["tools"] = tools
            payload["tool_choice"] = "auto"

        with httpx.Client() as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()


# Global client instance for use in handlers
_llm_client: LLMClient | None = None


def get_llm_client() -> LLMClient:
    """Get or create the global LLM API client instance."""
    global _llm_client
    if _llm_client is None:
        _llm_client = LLMClient()
    return _llm_client
