# claw-code-cheap-deepseek

Fork of upstream **Claw Code** with **DeepSeek (OpenAI-compatible) support** (`deepseek-chat`, `deepseek-reasoner`) via **`DEEPSEEK_API_KEY`**.

- **Upstream**: `https://github.com/instructkr/claw-code`
- **Telegram bot (Ductor)**: `https://github.com/nordost8/ductor-claw-code`
- **Ecosystem map**: [`ECOSYSTEM.md`](./ECOSYSTEM.md)

If you **don't need DeepSeek**, prefer upstream.

## Швидкий приклад CLI

```bash
export DEEPSEEK_API_KEY=sk-...   # див. SETUP.md
cd /path/to/your/repo
claw --model deepseek-chat --permission-mode workspace-write prompt \
  "Create a small Python script using Pillow that draws the Ukrainian flag (blue over yellow), write ua_flag.png, run it, and confirm the file exists."
```

Для Telegram: **[nordost8/ductor-claw-code](https://github.com/nordost8/ductor-claw-code)**.

| Документ | Призначення |
|----------|-------------|
| **[SETUP.md](SETUP.md)** | Збірка, env, smoke test |
| **[USAGE.md](USAGE.md)** | Поточний CLI, сесії, parity (з апстріму) |
| **[docs/UPSTREAM_SYNC.md](docs/UPSTREAM_SYNC.md)** | Як мерджити апстрім |
| **[CHANGELOG_FORK.md](CHANGELOG_FORK.md)** | Лог синків |

## Що змінилося в апстримі (огляд)

Після останнього merge з `upstream/main`: канонічна реалізація в **`rust/`**, здоров’я — **`claw doctor`**, деталі — **`rust/README.md`**, **`PARITY.md`**, **`ROADMAP.md`**, контейнерний флоу — **`docs/container.md`**.

Швидкий старт з сорцу:

> [!NOTE]
> [!WARNING]
> **`cargo install claw-code` installs the wrong thing.** The `claw-code` crate on crates.io is a deprecated stub that places `claw-code-deprecated.exe` — not `claw`. Running it only prints `"claw-code has been renamed to agent-code"`. **Do not use `cargo install claw-code`.** Either build from source (this repo) or install the upstream binary:
> ```bash
> cargo install agent-code   # upstream binary — installs 'agent.exe' (Windows) / 'agent' (Unix), NOT 'agent-code'
> ```
> This repo (`ultraworkers/claw-code`) is **build-from-source only** — follow the steps below.

```bash
# 1. Clone and build
git clone https://github.com/ultraworkers/claw-code
cd claw-code/rust
cargo build --workspace
./target/debug/claw --help

# 2. Set your API key
export ANTHROPIC_API_KEY="sk-ant-..."
# or DeepSeek:
export DEEPSEEK_API_KEY="sk-..."

# 3. Verify everything is wired correctly
./target/debug/claw doctor

# 4. Run a prompt
./target/debug/claw prompt "say hello"
```

## Документація

- `USAGE.md` — команди CLI, auth, сесії, конфіг, parity harness
- `rust/README.md` — структура Rust workspace та деталі CLI
- `ROADMAP.md` — активний roadmap

## Ліцензія

Як у апстрімі (див. `LICENSE` у дереві).
