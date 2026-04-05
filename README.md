# claw-code-cheap-deepseek

Fork of **[Claw Code](https://github.com/instructkr/claw-code)** (upstream: `instructkr/claw-code`) tuned for **[DeepSeek](https://www.deepseek.com/)** via **`DEEPSEEK_API_KEY`**. Anthropic / OpenAI / xAI шляхи лишаються там, де їх підтримує апстрім.

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

```bash
cd rust
cargo build --workspace
./target/debug/claw --help
```

## Ліцензія

Як у апстрімі (див. [LICENSE](LICENSE) у дереві).
