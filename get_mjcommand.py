from os import getenv

Url_mjCommand=getenv("MJCOMMAND_HOST")&"/"&getenv("DISCORD_API_VER")&"/applications/"&getenv("MJAPP_ID")&"/commands"
