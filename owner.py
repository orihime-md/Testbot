from config import OWNER_USERNAME


def is_owner(user):
    return bool(user and user.username and OWNER_USERNAME and user.username.lower() == OWNER_USERNAME)
