"""Tool definitions for LLM intent routing.

Each tool represents an action the bot can take. The LLM uses these descriptions
to decide which tool to call based on user intent.
"""

from services.lms_api import get_lms_client


def get_tools() -> list[dict]:
    """Return the list of available tools for the LLM.

    Returns:
        List of tool definitions in OpenAI function calling format.
    """
    return [
        {
            "type": "function",
            "function": {
                "name": "get_health",
                "description": "Check if the LMS backend is healthy and running. Use this when the user asks about system status, health, or if the service is working.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_labs",
                "description": "List all available labs in the LMS. Use this when the user asks about available labs, what labs exist, or wants to see the lab list.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_scores",
                "description": "Get per-task pass rates and scores for a specific lab. Use this when the user asks about scores, pass rates, or performance for a lab.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lab": {
                            "type": "string",
                            "description": "Lab identifier (e.g., 'lab-01', 'lab-04'). Must be in format 'lab-XX' where XX is a number.",
                        },
                    },
                    "required": ["lab"],
                },
            },
        },
    ]


def execute_tool(name: str, arguments: dict) -> str:
    """Execute a tool by name with the given arguments.

    Args:
        name: The tool name (e.g., 'get_health', 'get_labs', 'get_scores').
        arguments: The tool arguments as a dict.

    Returns:
        The tool's result as a formatted string.

    Raises:
        ValueError: If the tool name is unknown.
    """
    import httpx
    from services.lms_api import get_lms_client

    if name == "get_health":
        try:
            client = get_lms_client()
            health = client.get_health()
            return f"Backend status: healthy (items: {health['items_count']})"
        except ValueError as e:
            return f"Configuration error: {e}"
        except httpx.ConnectError as e:
            return f"Backend unreachable: connection refused"
        except httpx.HTTPStatusError as e:
            return f"Backend error: HTTP {e.response.status_code}"
        except Exception as e:
            return f"Backend error: {e}"

    elif name == "get_labs":
        try:
            client = get_lms_client()
            items = client.get_items()
            labs = [item for item in items if item.get("type") == "lab"]
            if not labs:
                return "No labs available."
            lab_list = "\n".join([f"- {lab['title']}" for lab in labs])
            return f"Available labs:\n{lab_list}"
        except ValueError as e:
            return f"Configuration error: {e}"
        except httpx.ConnectError as e:
            return f"Failed to connect to backend"
        except Exception as e:
            return f"Failed to fetch labs: {e}"

    elif name == "get_scores":
        lab = arguments.get("lab")
        if not lab:
            return "Usage: Please specify a lab (e.g., 'lab-04')"

        try:
            client = get_lms_client()
            scores = client.get_scores(lab)
            if not scores:
                return f"No scores found for {lab}."
            score_lines = []
            for item in scores:
                task_name = item.get("task", "Unknown")
                avg_score = item.get("avg_score", 0)
                attempts = item.get("attempts", 0)
                score_lines.append(f"- {task_name}: {avg_score:.1f}% ({attempts} attempts)")
            return f"Scores for {lab}:\n" + "\n".join(score_lines)
        except ValueError as e:
            return f"Configuration error: {e}"
        except httpx.ConnectError as e:
            return f"Failed to connect to backend"
        except Exception as e:
            return f"Failed to fetch scores: {e}"

    else:
        raise ValueError(f"Unknown tool: {name}")
