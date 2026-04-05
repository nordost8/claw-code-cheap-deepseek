# Claw Code — cheap DeepSeek setup

This fork is **adapted to run well with cheap [DeepSeek](https://www.deepseek.com/)** using **`DEEPSEEK_API_KEY`** and OpenAI-compatible endpoints. You can still use Anthropic or other providers if your build supports them.

## Suggested GitHub repository name

Publish this fork as:

### **`claw-code-cheap-deepseek`**

That name states clearly: **Claw Code**, tuned for **cheap DeepSeek**.  
Suggested **About** line on GitHub:

> Claw Code CLI fork — cheap DeepSeek (`DEEPSEEK_API_KEY`), OpenAI-compatible. Use with Ductor `claw` provider.

## Prerequisites

- **Rust** + `cargo`
- **DeepSeek API key** ([platform](https://platform.deepseek.com/))

## Environment

Copy examples and edit (never commit real keys):

```bash
cp .env.example .env
# or use claw.env.example as a reference
```

Minimum for **cheap DeepSeek**:

```bash
export DEEPSEEK_API_KEY=sk-...
```

Optional overrides (if your build reads them):

```bash
# DEEPSEEK_API_BASE=https://api.deepseek.com/v1
# DEEPSEEK_MODEL=deepseek-chat
```

Load from project root when developing; for production, put the same variables in the environment of your shell or service.

## Build the `claw` binary

```bash
cd rust
cargo build --release
```

Binary: **`rust/target/release/claw`**.

Install on your `PATH`, for example:

```bash
ln -sf "$(pwd)/target/release/claw" ~/.local/bin/claw
```

## Quick test (DeepSeek)

```bash
cd rust
DEEPSEEK_API_KEY=sk-... ./target/release/claw --output-format json --model deepseek-chat prompt "Reply with one word: ok"
```

You should get JSON with a `message` field.

## Models (cheap DeepSeek)

Typical IDs:

- **`deepseek-chat`** — default cheap chat model  
- **`deepseek-reasoner`** — reasoning variant  

Exact names depend on this repo’s CLI; check `claw --help` or project docs.

## Companion: Telegram bot

To control this CLI from Telegram, use the **Ductor** fork with the `claw` provider (suggested name **`ductor-claw-code`**). See its **`SETUP.md`**.

## Syncing from upstream

See **[docs/UPSTREAM_SYNC.md](docs/UPSTREAM_SYNC.md)** for branch model, which files are “fork-owned”, and merge vs rebase. Quick fetch + reminder:

```bash
./scripts/sync-upstream.sh
git merge upstream/main   # or: git rebase upstream/main
```

Log each sync in **`CHANGELOG_FORK.md`**.

## GitHub publish

See **`GITHUB_SETUP.md`**.

---

## Українською

**Рекомендована назва репозиторія на GitHub (англійською): `claw-code-cheap-deepseek`** — одразу видно, що це Claw під **дешевий DeepSeek**.

Що зробити: встановити **Rust**, скопіювати **`.env.example` → `.env`**, додати **`DEEPSEEK_API_KEY`**, зібрати **`cd rust && cargo build --release`**, покласти **`claw`** у **`PATH`**. Перевірка — одна команда `prompt` з `--model deepseek-chat` (див. розділ **Quick test** вище).

Для бота в Telegram — другий репо **`ductor-claw-code`**, там свій **`SETUP.md`**.

Публікація на GitHub — **`GITHUB_SETUP.md`**.
