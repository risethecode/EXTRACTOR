"""
from os import getenv


API_ID = int(getenv("API_ID", "22518279"))
API_HASH = getenv("API_HASH", "61e5cc94bc5e6318643707054e54caf4")
BOT_TOKEN = getenv("BOT_TOKEN", "8006527414:AAEZvtQy5aWXrnRxBi_vaVTUg2f-tQLoMXc")
OWNER_ID = int(getenv("OWNER_ID", "8500852075"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "502980590").split()))
MONGO_URL = "mongodb+srv://<sandeepsharma786>:<Sandeep786>@cluster0.xz78w44.mongodb.net")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003828380273"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1003533276261"))

"""
#




# --------------M----------------------------------

import os
import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("APP_ID", 22518279))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "8500852075"))
# ------------------X------------------------------
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "502980590").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003828380273"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003533276261"))
