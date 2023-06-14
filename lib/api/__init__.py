from os import getenv

from exceptions import MissRequiredVariable

GUILD_ID = getenv("GUILD_ID")
CHANNEL_ID = getenv("CHANNEL_ID")
USER_TOKEN = getenv("USER_TOKEN")
CALLBACK_URL = getenv("CALLBACK_URL")
MJBOT_ID = int(getenv("MJBOT_ID"))
MJAPP_ID = getenv("MJAPP_ID")

if not all([GUILD_ID, CHANNEL_ID, USER_TOKEN]):
    raise MissRequiredVariable("Missing required environment variable: [GUILD_ID, CHANNEL_ID, USER_TOKEN]")
