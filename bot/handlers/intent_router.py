"""Intent router for natural language queries.

This module uses an LLM to understand user intent and route to the appropriate tool.
"""

import json

from services.llm_client import get_llm_client
from services.tools import get_tools, execute_tool


# System prompt that tells the LLM how to behave
SYSTEM_PROMPT = """You are an assistant for a Learning Management System (LMS) Telegram bot.

Your job is to understand what the user wants and call the appropriate tool to help them.

Available tools:
- get_health: Check if the backend is running and healthy
- get_labs: List all available labs
- get_scores: Get scores/pass rates for a specific lab (requires lab parameter like "lab-04")

When the user asks about:
- System status, health, if service is working → call get_health
- Available labs, what labs exist, lab list → call get_labs  
- Scores, pass rates, performance for a lab → call get_scores with the lab name

If the user's query doesn't match any tool, respond with a helpful message suggesting what you can help with.

Always be concise and friendly. Format your responses clearly.
"""


def handle_natural_language(query: str) -> str:
    """Process a natural language query using the LLM.

    Args:
        query: The user's message text.

    Returns:
        The bot's response text.
    """
    try:
        llm = get_llm_client()
        tools = get_tools()

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ]

        # Call LLM with tools
        response = llm.chat(messages, tools=tools)

        # Check if LLM wants to call a tool
        choice = response.get("choices", [{}])[0]
        message = choice.get("message", {})
        tool_calls = message.get("tool_calls", [])

        if tool_calls:
            # LLM wants to call a tool
            tool_call = tool_calls[0]
            function = tool_call.get("function", {})
            tool_name = function.get("name", "")
            tool_args = {}

            # Parse arguments if present
            args_str = function.get("arguments", "{}")
            try:
                tool_args = json.loads(args_str) if args_str else {}
            except json.JSONDecodeError:
                tool_args = {}

            # Execute the tool
            result = execute_tool(tool_name, tool_args)
            return result

        else:
            # No tool call — return LLM's direct response
            content = message.get("content", "I'm not sure how to help with that. Try asking about labs, scores, or system health.")
            return content

    except ValueError as e:
        # LLM not configured
        return f"LLM not configured: {e}. Try using slash commands like /help, /labs, /scores."
    except Exception as e:
        return f"Error processing query: {e}. Try using slash commands like /help, /labs, /scores."
