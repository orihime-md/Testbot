import re

_CHANNEL_PATTERN = re.compile(r"^(?:https?://)?(?:t\.me/|telegram\.me/)?@?([A-Za-z][A-Za-z0-9_]{4,})/?$")


def parse_channel_link(text):
    """Accepts @name, t.me/name or https://t.me/name. Returns a full link, or None if it isn't one."""
    match = _CHANNEL_PATTERN.match((text or "").strip())
    if not match:
        return None
    return f"https://t.me/{match.group(1)}"
