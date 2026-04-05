# claw-code-cheap-deepseek

## Example (CLI)

Same class of work as in Telegram, but from the terminal:

```bash
export DEEPSEEK_API_KEY=sk-...   # see SETUP.md
cd /path/to/your/repo
claw --model deepseek-chat --permission-mode workspace-write prompt \
  "Create a small Python script using Pillow that draws the Ukrainian flag (blue over yellow), write ua_flag.png, run it, and confirm the file exists."
```

**Agent:** plans steps, writes the script, runs it in the workspace, and returns a **text result** (paths, stdout). For chat + file delivery, pair with **[Ductor Claw Code](https://github.com/nordost8/ductor-claw-code)** on Telegram.

Illustrative — tools and sandboxing follow your Claw build and flags (`--dangerously-skip-permissions`, Docker, etc.).

---

**Fork of [Claw Code](https://github.com/instructkr/claw-code)** tuned for **cheap [DeepSeek](https://www.deepseek.com/)** via **`DEEPSEEK_API_KEY`**. Anthropic / OpenAI / xAI paths remain available where upstream supports them.

## Quick links

| Doc | Purpose |
|-----|---------|
| **[SETUP.md](SETUP.md)** | Build, env, smoke test |
| **[docs/UPSTREAM_SYNC.md](docs/UPSTREAM_SYNC.md)** | Merge from main Claw repo, conflict map |
| **[CHANGELOG_FORK.md](CHANGELOG_FORK.md)** | Log each upstream sync |
| **[GITHUB_SETUP.md](GITHUB_SETUP.md)** | Remotes |

**Telegram stack:** [nordost8/ductor-claw-code](https://github.com/nordost8/ductor-claw-code)

## Upstream (vanilla Claw Code)

Full history, layout, ecosystem:

**[instructkr/claw-code — README (main)](https://github.com/instructkr/claw-code/blob/main/README.md)**

This fork tracks `upstream` = `https://github.com/instructkr/claw-code.git`. Sync: `./scripts/sync-upstream.sh` then merge/rebase.

## License

Same as upstream (see [LICENSE](LICENSE) if present in tree).
