"""Command handlers returning placeholder responses.

Task 2 will connect these to the real LMS backend.
"""


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
    """Handle /health command — backend status check.
    
    Task 2: Will call GET /health on the LMS backend.
    """
    return "Backend status: OK (placeholder)"


def handle_labs() -> str:
    """Handle /labs command — list available labs.
    
    Task 2: Will call GET /items on the LMS backend.
    """
    return "Available labs: (placeholder — will fetch from backend)"


def handle_scores(lab: str | None = None) -> str:
    """Handle /scores command — show scores for a lab.
    
    Task 2: Will call GET /analytics/{lab} on the LMS backend.
    
    Args:
        lab: Lab identifier (e.g., "lab-04"). If None, shows general scores info.
    """
    if lab is None:
        return "Usage: /scores <lab> (e.g., /scores lab-04)"
    return f"Scores for {lab}: (placeholder — will fetch from backend)"
