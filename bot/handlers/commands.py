"""Command handlers with real LMS backend integration.

Handlers call the LMS API service and format responses for users.
Errors are handled gracefully with user-friendly messages.
"""

import httpx

from services.lms_api import get_lms_client


def handle_start() -> str:
    """Handle /start command — welcome message."""
    return "Welcome to the LMS Bot! Use /help to see available commands."


def handle_help() -> str:
    """Handle /help command — list all available commands."""
    return """Available commands:
/start — Welcome message
/help — Show this help message
/health — Check backend system status
/labs — List available labs
/scores <lab> — Show scores for a specific lab"""


def handle_health() -> str:
    """Handle /health command — backend status check."""
    try:
        client = get_lms_client()
        health = client.get_health()
        return f"Backend status: healthy (items: {health['items_count']})"
    except httpx.ConnectError as e:
        return f"Backend status: unhealthy — connection refused ({e})"
    except httpx.HTTPStatusError as e:
        return f"Backend status: unhealthy — HTTP error {e.response.status_code}"
    except httpx.RequestError as e:
        return f"Backend status: unhealthy — {e}"
    except Exception as e:
        return f"Backend status: unhealthy — unexpected error: {e}"


def handle_labs() -> str:
    """Handle /labs command — list available labs."""
    try:
        client = get_lms_client()
        items = client.get_items()
        labs = [item for item in items if item.get("type") == "lab"]
        if not labs:
            return "No labs available."
        lab_list = "\n".join([f"- {lab['title']}" for lab in labs])
        return f"Available labs:\n{lab_list}"
    except httpx.ConnectError as e:
        return f"Failed to fetch labs — connection refused ({e})"
    except httpx.HTTPStatusError as e:
        return f"Failed to fetch labs — HTTP error {e.response.status_code}"
    except httpx.RequestError as e:
        return f"Failed to fetch labs — {e}"
    except Exception as e:
        return f"Failed to fetch labs — unexpected error: {e}"


def handle_scores(lab: str | None = None) -> str:
    """Handle /scores command — show scores for a lab.

    Args:
        lab: Lab identifier (e.g., "lab-04"). If None, shows usage message.
    """
    if lab is None:
        return "Usage: /scores <lab> (e.g., /scores lab-04)"

    try:
        client = get_lms_client()
        scores = client.get_scores(lab)
        if not scores:
            return f"No scores found for {lab}."
        # Format scores as a list of task names with percentages
        score_lines = []
        for task_name, percentage in scores.items():
            score_lines.append(f"- {task_name}: {percentage:.1f}%")
        return f"Scores for {lab}:\n" + "\n".join(score_lines)
    except httpx.ConnectError as e:
        return f"Failed to fetch scores — connection refused ({e})"
    except httpx.HTTPStatusError as e:
        return f"Failed to fetch scores — HTTP error {e.response.status_code}"
    except httpx.RequestError as e:
        return f"Failed to fetch scores — {e}"
    except Exception as e:
        return f"Failed to fetch scores — unexpected error: {e}"
