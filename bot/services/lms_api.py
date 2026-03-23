"""LMS API client service.

This service handles all HTTP requests to the LMS backend with Bearer token authentication.
"""

import os
from pathlib import Path

import httpx
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuration for the LMS API client."""

    lms_api_base_url: str = "http://localhost:42002"
    lms_api_key: str = ""

    class Config:
        # Look for .env.bot.secret in the project root (parent of bot/)
        env_file = str(Path(__file__).parent.parent.parent / ".env.bot.secret")
        env_file_encoding = "utf-8"
        # Ignore extra fields in the .env file (e.g., BOT_TOKEN, LLM_*)
        extra = "ignore"


class LMSAPIClient:
    """Client for the LMS backend API."""

    def __init__(self, settings: Settings | None = None):
        """Initialize the API client.

        Args:
            settings: Configuration settings. If None, loads from environment.
        """
        self.settings = settings or Settings()
        self.base_url = self.settings.lms_api_base_url.rstrip("/")
        self.api_key = self.settings.lms_api_key

    def _get_headers(self) -> dict[str, str]:
        """Get headers for API requests with Bearer token."""
        return {"Authorization": f"Bearer {self.api_key}"}

    def get_items(self) -> list[dict]:
        """Fetch all items (labs and tasks) from the backend.

        Returns:
            List of items with their metadata.

        Raises:
            httpx.RequestError: If the request fails.
        """
        url = f"{self.base_url}/items/"
        with httpx.Client() as client:
            response = client.get(url, headers=self._get_headers())
            response.raise_for_status()
            return response.json()

    def get_health(self) -> dict:
        """Check backend health status.

        Returns:
            Health status information.

        Raises:
            httpx.RequestError: If the request fails.
        """
        # Use /items/ as a health check endpoint
        url = f"{self.base_url}/items/"
        with httpx.Client() as client:
            response = client.get(url, headers=self._get_headers())
            response.raise_for_status()
            return {"status": "healthy", "items_count": len(response.json())}

    def get_scores(self, lab: str) -> dict:
        """Get scores for a specific lab.

        Args:
            lab: Lab identifier (e.g., "lab-04").

        Returns:
            Score data for the lab.

        Raises:
            httpx.RequestError: If the request fails.
        """
        url = f"{self.base_url}/analytics/pass-rates"
        params = {"lab": lab}
        with httpx.Client() as client:
            response = client.get(url, headers=self._get_headers(), params=params)
            response.raise_for_status()
            return response.json()


# Global client instance for use in handlers
_lms_client: LMSAPIClient | None = None


def get_lms_client() -> LMSAPIClient:
    """Get or create the global LMS API client instance."""
    global _lms_client
    if _lms_client is None:
        _lms_client = LMSAPIClient()
    return _lms_client
