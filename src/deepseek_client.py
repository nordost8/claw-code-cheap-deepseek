"""OpenAI-compatible chat completions against DeepSeek (stdlib only)."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any


DEFAULT_DEEPSEEK_BASE = 'https://api.deepseek.com/v1'
DEFAULT_MODEL = 'deepseek-chat'


def _resolve_api_key(explicit: str | None) -> str:
    key = (explicit or os.environ.get('DEEPSEEK_API_KEY') or '').strip()
    return key


def chat_completion(
    messages: list[dict[str, str]],
    *,
    api_key: str | None = None,
    model: str | None = None,
    base_url: str | None = None,
    timeout: float = 120.0,
) -> tuple[str, dict[str, Any]]:
    """POST /v1/chat/completions. Returns (assistant_text, raw_json)."""
    key = _resolve_api_key(api_key)
    if not key:
        raise ValueError('DEEPSEEK_API_KEY is not set. Export it in the environment before running.')
    resolved_model = (model or os.environ.get('DEEPSEEK_MODEL') or DEFAULT_MODEL).strip()
    root = (base_url or os.environ.get('DEEPSEEK_API_BASE') or DEFAULT_DEEPSEEK_BASE).rstrip('/')
    url = f'{root}/chat/completions'
    payload = json.dumps(
        {
            'model': resolved_model,
            'messages': messages,
            'temperature': 0.7,
        }
    ).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=payload,
        method='POST',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {key}',
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        raise ValueError(f'DeepSeek HTTP {e.code}: {body[:800]}') from e
    except urllib.error.URLError as e:
        raise ValueError(f'DeepSeek request failed: {e}') from e

    choices = raw.get('choices') or []
    if not choices:
        raise ValueError(f'DeepSeek response missing choices: {raw!r:.500}')
    message = choices[0].get('message') or {}
    content = message.get('content')
    if not isinstance(content, str) or not content.strip():
        raise ValueError(f'DeepSeek empty content: {raw!r:.500}')
    return content.strip(), raw


def simple_prompt(
    user_text: str,
    *,
    system: str | None = None,
    api_key: str | None = None,
    model: str | None = None,
    base_url: str | None = None,
) -> str:
    messages: list[dict[str, str]] = []
    if system:
        messages.append({'role': 'system', 'content': system})
    messages.append({'role': 'user', 'content': user_text})
    text, _ = chat_completion(messages, api_key=api_key, model=model, base_url=base_url)
    return text
