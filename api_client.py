#!/usr/bin/env python3
"""
Unified API client for autonovel.

Supports three providers via AUTONOVEL_PROVIDER env var:
  anthropic-key   (default) — direct Anthropic API with ANTHROPIC_API_KEY
  anthropic-oauth            — Anthropic API with OAuth token from ~/.openclaw/secrets.json
  openrouter                 — OpenRouter with OPENROUTER_API_KEY

Public API:
  call_model(prompt, system="", max_tokens=4000, model=None) -> str
"""
import json
import os
from pathlib import Path

import httpx

_TIMEOUT = 300

_DEFAULT_MODEL = "claude-haiku-4-5"


def _get_model(model_arg):
    if model_arg:
        return model_arg
    return os.environ.get("AUTONOVEL_WRITER_MODEL", _DEFAULT_MODEL)


def _call_anthropic_key(prompt, system, max_tokens, model):
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system:
        payload["system"] = system
    resp = httpx.post(
        "https://api.anthropic.com/v1/messages",
        headers=headers,
        json=payload,
        timeout=_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()["content"][0]["text"]


def _call_anthropic_oauth(prompt, system, max_tokens, model):
    secrets_path = Path("~/.openclaw/secrets.json").expanduser()
    with open(secrets_path) as f:
        secrets = json.load(f)
    token = secrets["anthropic"]["oauthToken"]
    headers = {
        "Authorization": f"Bearer {token}",
        "anthropic-beta": "oauth-2025-04-20",
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system:
        payload["system"] = system
    resp = httpx.post(
        "https://api.anthropic.com/v1/messages",
        headers=headers,
        json=payload,
        timeout=_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()["content"][0]["text"]


def _call_openrouter(prompt, system, max_tokens, model):
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com/VoynichLabs/autonovel",
        "X-Title": "autonovel",
        "content-type": "application/json",
    }
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": messages,
    }
    resp = httpx.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def call_model(prompt, system="", max_tokens=4000, model=None):
    """
    Call the configured LLM provider and return the response text.

    Args:
        prompt:     User message content.
        system:     Optional system prompt.
        max_tokens: Maximum tokens to generate (default 4000).
        model:      Model name; overrides AUTONOVEL_WRITER_MODEL env var.

    Returns:
        Response text as a string.
    """
    provider = os.environ.get("AUTONOVEL_PROVIDER", "anthropic-key")
    resolved_model = _get_model(model)

    if provider == "anthropic-key":
        return _call_anthropic_key(prompt, system, max_tokens, resolved_model)
    elif provider == "anthropic-oauth":
        return _call_anthropic_oauth(prompt, system, max_tokens, resolved_model)
    elif provider == "openrouter":
        return _call_openrouter(prompt, system, max_tokens, resolved_model)
    else:
        raise ValueError(
            f"Unknown AUTONOVEL_PROVIDER: {provider!r}. "
            "Expected: anthropic-key, anthropic-oauth, openrouter"
        )
