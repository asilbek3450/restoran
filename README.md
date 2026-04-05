# Lazzat Restaurant

Django-based restaurant site with menu browsing, contact flow, table reservations, Telegram alerts, and a custom admin panel.

## Local setup

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Copy environment variables:

```bash
cp .env.example .env
```

3. Run migrations and start the project:

```bash
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py runserver
```

## Telegram setup

Set these values in `.env` or Railway variables:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_ADMIN_CHAT_ID`

Contact messages and reservation requests will be sent to the configured bot chat.

## Railway deployment

Recommended environment variables:

- `DEBUG=False`
- `SECRET_KEY=<strong-random-value>`
- `ALLOWED_HOSTS=<your-railway-domain>`
- `CSRF_TRUSTED_ORIGINS=https://<your-railway-domain>`
- `DATABASE_URL=<railway-postgres-url>`
- `KITCHEN_ADMIN_USER=<admin-login>`
- `KITCHEN_ADMIN_PASS=<admin-password>`
- `TELEGRAM_BOT_TOKEN=<bot-token>`
- `TELEGRAM_ADMIN_CHAT_ID=<chat-id>`

Build steps:

```bash
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic --noinput
```

Start command:

```bash
gunicorn restaurant.wsgi --log-file -
```

## Important note

Uploaded media files are stored on the local filesystem. For long-term production usage on Railway, attach a persistent volume or move media storage to S3/Cloudinary.
# retoran
