# Development Plan: Telegram Bot for LMS

## Overview

This document outlines the development plan for building a Telegram bot that provides a chat interface to the Learning Management System (LMS) backend. The bot will allow users to check system health, browse available labs, view scores, and ask questions in natural language using an LLM-powered intent router.

## Task 1: Scaffold and Test Mode

The foundation of the bot is a testable architecture where handlers are pure functions that don't depend on Telegram. This allows testing via `--test` mode without needing a Telegram connection. The entry point (`bot.py`) will parse command-line arguments and call handlers directly. Handlers will return simple text responses (placeholders initially). Configuration loading from `.env.bot.secret` will be implemented to support both test and production modes.

## Task 2: Backend Integration

Once the scaffold is working, handlers will be connected to the real LMS backend. An API client service will handle HTTP requests with Bearer token authentication. Each slash command (`/health`, `/labs`, `/scores`) will call the corresponding backend endpoint. Error handling will ensure that backend failures produce user-friendly messages rather than crashes. The test mode will continue to work, now returning real data from the backend.

## Task 3: Intent-Based Natural Language Routing

The bot will understand plain text queries using an LLM. Tool descriptions will be created for each backend endpoint, allowing the LLM to decide which API call to make based on user intent. The intent router will parse LLM responses and execute the appropriate tool. This enables queries like "what labs are available?" or "show me my score for lab-04" without requiring slash commands.

## Task 4: Containerization and Deployment

The bot will be containerized with a Dockerfile and added as a service in `docker-compose.yml`. Environment variables will be managed through `.env.bot.secret` on the VM. Documentation will cover deployment steps, troubleshooting, and maintenance. The bot will run alongside the existing backend and PostgreSQL services.

## Architecture Decisions

- **Handler separation**: Handlers are pure functions taking a command string and returning text. This enables testing without Telegram.
- **Configuration via environment**: Secrets (bot token, API keys) are loaded from environment files, not hardcoded.
- **Service layer**: API clients (LMS backend, LLM) are isolated in a `services/` directory for reusability.
- **Test-first development**: Every feature is verified in `--test` mode before Telegram deployment.
