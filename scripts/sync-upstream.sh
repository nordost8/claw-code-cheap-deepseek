#!/usr/bin/env bash
# Safe helper: fetch upstream and print merge/rebase commands (does not modify branches).
set -euo pipefail
UPSTREAM_REMOTE="${UPSTREAM_REMOTE:-upstream}"
UPSTREAM_BRANCH="${UPSTREAM_BRANCH:-main}"

if ! git remote get-url "$UPSTREAM_REMOTE" &>/dev/null; then
  echo "No remote '$UPSTREAM_REMOTE'. Add it, e.g.:"
  echo "  git remote add upstream https://github.com/instructkr/claw-code.git"
  exit 1
fi

git fetch "$UPSTREAM_REMOTE"
echo "Fetched $UPSTREAM_REMOTE."
echo ""
echo "Current branch: $(git branch --show-current)"
echo ""
echo "Integrate upstream into your branch (pick one):"
echo "  git merge ${UPSTREAM_REMOTE}/${UPSTREAM_BRANCH}"
echo "  # or linear history:"
echo "  git rebase ${UPSTREAM_REMOTE}/${UPSTREAM_BRANCH}"
echo ""
echo "Then: cd rust && cargo build --release && cargo test --workspace"
echo "Docs: docs/UPSTREAM_SYNC.md"
