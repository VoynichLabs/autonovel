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
    Falls back through AUTONOVEL_FALLBACK_CHAIN on failure.

    Primary: AUTONOVEL_PROVIDER + AUTONOVEL_WRITER_MODEL (or model arg)
    Fallback: AUTONOVEL_FALLBACK_CHAIN (comma-separated list of
              "provider:model" pairs, e.g.
              "openrouter:x-ai/grok-4.1-fast,openrouter:minimax/minimax-m2.7")
    """
    provider = os.environ.get("AUTONOVEL_PROVIDER", "anthropic-key")
    resolved_model = _get_model(model)

    attempts = [{"provider": provider, "model": resolved_model}]

    # Build fallback chain from env
    fallback_env = os.environ.get("AUTONOVEL_FALLBACK_CHAIN", "")
    if fallback_env:
        for entry in fallback_env.split(","):
            entry = entry.strip()
            if ":" in entry:
                fb_provider, fb_model = entry.split(":", 1)
                attempts.append({"provider": fb_provider.strip(), "model": fb_model.strip()})

    last_error = None
    for attempt in attempts:
        p = attempt["provider"]
        m = attempt["model"]
        try:
            if p == "anthropic-key":
                return _call_anthropic_key(prompt, system, max_tokens, m)
            elif p == "anthropic-oauth":
                return _call_anthropic_oauth(prompt, system, max_tokens, m)
            elif p == "openrouter":
                return _call_openrouter(prompt, system, max_tokens, m)
            else:
                raise ValueError(f"Unknown provider: {p!r}")
        except Exception as e:
            print(f"[api_client] {p}:{m} failed: {e} — trying next fallback...")
            last_error = e

    raise RuntimeError(f"All providers failed. Last error: {last_error}")
