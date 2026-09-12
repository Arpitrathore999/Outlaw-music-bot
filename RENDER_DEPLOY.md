# Outlaw X Music — Render Deployment

1. Upload the contents of this repository to GitHub.
2. In Render, choose **New → Blueprint** and select the GitHub repository.
3. Render will read `render.yaml` and create the Background Worker.
4. Fill the secret environment variables marked `sync: false`:
   - `API_ID`
   - `API_HASH`
   - `BOT_TOKEN`
   - `LOGGER_ID`
   - `MONGO_URL`
   - `OWNER_ID`
   - `SESSION`
   - `SESSION2` / `SESSION3` (optional)
5. Deploy and check the worker logs.

The project uses the included Dockerfile, which provides the runtime dependencies required by the music bot.
