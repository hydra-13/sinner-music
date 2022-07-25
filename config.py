## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Umk")
API_ID = int(getenv("API_ID", "13561314"))
API_HASH = getenv("API_HASH", "271beccf04bacef8caf3d4bf6e4c7f24")
OWNER_NAME = getenv("OWNER_NAME", "𝓐𝓷𝓮𝓼𝓽𝓱𝓮𝓼𝓲𝓪✿્᭄͜͡")
OWNER_USERNAME = getenv("OWNER_USERNAME", "HornyBitch169")
ALIVE_NAME = getenv("ALIVE_NAME", "sugarXmusic")
BOT_USERNAME = getenv("SugarBabyXbot")
ASSISTANT_NAME = getenv("HornyBitch169")
GROUP_SUPPORT = getenv("alterbasecam")
UPDATES_CHANNEL = getenv("xproject13")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1172673317").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
