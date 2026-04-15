# Upstream sync architecture (claw-code-cheap-deepseek)

This fork stays **on top of** the main Claw Code tree (`instructkr/claw-code` or your chosen upstream). The goal is to **pull upstream often** and re-apply only a **small, documented surface** of changes.

## Remotes

| Remote     | Typical URL                              | Role                          |
|-----------|-------------------------------------------|-------------------------------|
| `upstream` | `https://github.com/instructkr/claw-code.git` | Official / main Claw line     |
| `origin`   | your `claw-code-cheap-deepseek` repo     | Your publish + collaboration  |

```bash
git remote -v
# upstream → instructkr/claw-code
# origin   → YOUR_USER/claw-code-cheap-deepseek
```

## Branch model (recommended)

- **`main`** — your fork: upstream + DeepSeek / cheap-model patches. This is what you push to `origin`.
- Optional **`upstream-vanilla`** (or tag only) — fast-forward only to `upstream/main` when you want a clean diff:  
  `git fetch upstream && git branch -f upstream-vanilla upstream/main`

**Merge vs rebase**

| Strategy | Pros | Cons |
|----------|------|------|
| **`git merge upstream/main`** into `main` | Preserves history; safe for shared `main` | Merge commits |
| **`git rebase main` onto `upstream/main`** | Linear history | Rewrites SHAs; avoid if others clone your `main` |

For a solo maintainer, **rebase** is fine. For collaborators, prefer **merge**.

## Patch surface (what this fork “owns”)

When upstream updates, expect conflicts mainly here:

| Area | Files | Notes |
|------|--------|--------|
| OpenAI-compat / providers | `rust/crates/api/src/providers/mod.rs`, `openai_compat.rs` | Provider registration |
| HTTP client glue | `rust/crates/api/src/client.rs` | Small diffs possible |
| CLI entry | `rust/crates/rusty-claude-cli/src/main.rs` | **High churn** — upstream often touches |
| Python port | `src/main.py`, `src/deepseek_client.py` | Parallel to Rust; merge carefully |
| Tests | `tests/test_deepseek_client.py` | Usually low conflict |
| Docs / examples | `SETUP.md`, `GITHUB_SETUP.md`, `README.md` (banner), `.env.example`, `claw.env.example` | Keep fork docs |
| Ignore rules | `.gitignore` | Never commit sessions again |

**Rule of thumb:** take **upstream** for structure and refactors; re-apply **fork-only** behaviour (DeepSeek defaults, env keys, flags) in these files.

## Sync procedure

1. Commit or stash local WIP.
2. `git fetch upstream`
3. Either:
   - `git merge upstream/main`, or
   - `git rebase upstream/main`
4. Resolve conflicts file-by-file using the table above.
5. `cd rust && cargo test --workspace` (or minimal `cargo build --release`).
6. Smoke: `DEEPSEEK_API_KEY=... ./target/release/claw --output-format json --model deepseek-chat prompt "ping"`
7. Commit merge/rebase result; push `origin main`.
8. Note upstream commit or tag in **`CHANGELOG_FORK.md`**.

Helper (prints safe next step):

```bash
./scripts/sync-upstream.sh
```

## If upstream changes the CLI contract

If `claw prompt` / JSON shape / flags change, **Ductor’s** `claw_provider.py` (sibling repo `ductor-claw-code`) may need a matching update. See that repo’s `docs/UPSTREAM_SYNC.md`.
