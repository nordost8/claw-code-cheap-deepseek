# Підключення до GitHub (форк Claw Code)

Зараз після підготовки:

- **`upstream`** → канонічне джерело, з якого ти тягнеш оновлення (наприклад `https://github.com/instructkr/claw-code.git`).

Створи **свій** репозиторій на GitHub і додай його як `origin`:

```bash
cd /home/nordost/Projects/claw-code
git remote add origin https://github.com/YOUR_USER/YOUR_CLAW_FORK.git
git push -u origin main
```

Якщо раніше `origin` вказував на instructkr — перед цим:

```bash
git remote rename origin upstream
git remote add origin https://github.com/YOUR_USER/YOUR_CLAW_FORK.git
git push -u origin main
```

Синхронізація з апстрімом:

```bash
git fetch upstream
git merge upstream/main
```

## Що в цьому клоні змінено (орієнтир)

- Інтеграція **DeepSeek** та сумісних провайдерів (див. зміни в `rust/crates/api/`, `src/`, приклади `.env.example` / `claw.env.example`).

Не коміть файл **`.env`** — там ключі API.
