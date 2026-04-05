# Fork changelog (claw-code-cheap-deepseek)

Track **your** releases on top of **upstream** Claw Code.

## Template (copy per sync)

```text
## YYYY-MM-DD — sync upstream

- Upstream: instructkr/claw-code @ <commit-sha or tag>
- Fork changes: (none | listed)
- Tests: cargo test --workspace
- Notes: (conflicts resolved in …)
```

## History

### 2026-04-06 — sync upstream

- Upstream: `instructkr/claw-code` @ `f7321ca05d095b3682f35cdcee6bcdfd37b30a2e` (`upstream/main` at fetch time)
- Fork changes: merged `README.md` (fork-first); `rust/crates/api/src/providers/mod.rs` — upstream `model_token_limit` + DeepSeek `ModelTokenLimit` (8192 / 128k); `rust/crates/rusty-claude-cli/src/main.rs` — combined `api` imports (`oauth_token_is_expired` + fork `ProviderClient` / `detect_provider_kind` / `provider_max_tokens`)
- Tests: `cargo test --workspace` (run after build)
- Notes: conflicts in `README.md`, `mod.rs`, `main.rs`

- _Add entries after each `merge`/`rebase` from `upstream/main`._
