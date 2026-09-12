# Outlaw X Music — Railway Deployment

## Deploy
1. Push the contents of this folder to the root of a GitHub repository.
2. Railway → New Project → Deploy from GitHub Repo → select the repository.
3. Railway will detect the Dockerfile automatically.
4. Add the required environment variables in the Railway service's Variables tab.
5. Deploy. This is a background Telegram bot; no HTTP port is required.

## Required variables
- `API_ID`
- `API_HASH`
- `BOT_TOKEN`
- `LOGGER_ID`
- `MONGO_URL`
- `OWNER_ID`
- `SESSION`

Optional:
- `SESSION2`
- `SESSION3`

Branding defaults are already included in `config.py` and `sample.env`.

Do not commit real bot tokens, API secrets, MongoDB credentials, or session strings.
