import os

# Set these in Render's Environment tab (or in a local .env file).
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "").lstrip("@").lower()  # your Telegram username, no @

JOIN_URL = "https://t.me/Boltix_labs"
