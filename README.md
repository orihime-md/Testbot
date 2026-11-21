# Student bot

Sends a congrats image on /start with a Join button and an Add channel button.
Only the owner can add channels. Each added channel becomes a new Join button.

## Setup
1. Create a bot with @BotFather and copy the token.
2. Set environment variables:
   - `BOT_TOKEN` = the token
   - `OWNER_USERNAME` = your Telegram username without @
3. `pip install -r requirements.txt`
4. `python main.py`

## Deploy on Render
Create a **Background Worker** (not a Web Service), connect the repo, then:
- Build command: `pip install -r requirements.txt`
- Start command: `python main.py`
- Add `BOT_TOKEN` and `OWNER_USERNAME` in the Environment tab.

Note: added channels are saved to `channels.json` on the server. Render can clear that file on redeploy, so re-add channels after a redeploy.
