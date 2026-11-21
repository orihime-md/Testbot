import json
import os

CHANNELS_FILE = "channels.json"


def load_channels():
    """Returns the list of channel links the owner has added."""
    if not os.path.exists(CHANNELS_FILE):
        return []
    with open(CHANNELS_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_channels(channels):
    with open(CHANNELS_FILE, "w", encoding="utf-8") as f:
        json.dump(channels, f)
