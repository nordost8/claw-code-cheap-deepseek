# Publish on GitHub

## Suggested repository name (English)

### **`claw-code-cheap-deepseek`**

Use this name so it is obvious this fork targets **cheap DeepSeek** (`DEEPSEEK_API_KEY`) with **Claw Code**.

Full build + env + test steps: **[SETUP.md](SETUP.md)** (English + Українською).

## Remotes in this clone

- **`upstream`** → `https://github.com/instructkr/claw-code.git` (or your chosen upstream)

## First push

Create an **empty** repo named **`claw-code-cheap-deepseek`** on GitHub, then:

```bash
cd /path/to/claw-code
git remote add origin https://github.com/YOUR_USER/claw-code-cheap-deepseek.git
git push -u origin main
```

If you already renamed the old `origin` to `upstream` (as in this workspace):

```bash
git remote add origin https://github.com/YOUR_USER/claw-code-cheap-deepseek.git
git push -u origin main
```

## Sync from upstream

```bash
git fetch upstream
git merge upstream/main
```

Never commit **`.env`** — API keys must stay local.

---

## Публікація на GitHub (українською)

**Рекомендована назва репозиторія (англійською): `claw-code-cheap-deepseek`** — зрозуміло, що це Claw під **дешевий DeepSeek**.

Повна інструкція: **[SETUP.md](SETUP.md)**.

Додай **`origin`** на свій порожній репо й **`git push -u origin main`**. Для оновлень з апстріму: `git fetch upstream` і merge. Файл **`.env`** не комітити.
