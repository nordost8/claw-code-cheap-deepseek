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

### 2026-04-06 — DeepSeek as first-class `ProviderKind`

- `ProviderKind::DeepSeek`, `ProviderClient::DeepSeek`, registry aliases: `deepseek-chat`, `deepseek-reasoner`, `ds-chat`, `reasoner`, `r1`.
- `model_token_limit` / preflight: per [DeepSeek Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing) — 128K context both models; max output 8K (chat) / 64K (reasoner).

### 2026-04-06 — sync upstream

- Upstream: `instructkr/claw-code` @ `f7321ca05d095b3682f35cdcee6bcdfd37b30a2e` (`upstream/main` at fetch time)
- Fork changes: merged `README.md` (fork-first); `rust/crates/api/src/providers/mod.rs` — upstream `model_token_limit` + DeepSeek `ModelTokenLimit` (8192 / 128k); `rust/crates/rusty-claude-cli/src/main.rs` — combined `api` imports (`oauth_token_is_expired` + fork `ProviderClient` / `detect_provider_kind` / `provider_max_tokens`)
- Tests: `cargo test --workspace` (run after build)
- Notes: conflicts in `README.md`, `mod.rs`, `main.rs`

### 2026-04-06 — sync upstream (Anthropic count_tokens preflight)

- Upstream: `instructkr/claw-code` @ `be561bfdeb92fce7011938e748ee20051460d6a4` (`upstream/main` at fetch time)
- Fork changes: resolved `rust/crates/rusty-claude-cli/src/main.rs` — kept `ProviderBackedRuntimeClient` + upstream `format_user_visible_api_error` / `format_context_window_blocked_error`; updated `push_output_block` calls for thinking summary; `rust/crates/api/tests/client_integration.rs` + `mock_parity_harness.rs` — expect `POST /v1/messages/count_tokens` preflight (integration test + mock parity harness)
- Tests: `cargo test --workspace`
- Notes: conflict in `main.rs` around provider runtime vs error helpers

- _Add entries after each `merge`/`rebase` from `upstream/main`._
