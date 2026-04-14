# Ecosystem

This repository is a **fork** of upstream Claw Code with **DeepSeek (OpenAI-compatible) support**.

## Repositories

- **Upstream core**: `instructkr/claw-code`
- **This fork (DeepSeek-first)**: `nordost8/claw-code-cheap-deepseek`
- **Telegram bot orchestration (Ductor)**: `nordost8/ductor-claw-code`

## When to use what

- Use **upstream** if you don't need DeepSeek routing (`DEEPSEEK_API_KEY`) and prefer the canonical source.
- Use **this fork** if you want:
  - `deepseek-chat` / `deepseek-reasoner` model ids
  - `DEEPSEEK_API_KEY` auth and `DEEPSEEK_API_BASE` override (defaults to `https://api.deepseek.com/v1`)
- Use **`ductor-claw-code`** if you want to run the agent as a Telegram bot (it calls the `claw` CLI).

