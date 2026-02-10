import os

import dotenv

dotenv.load_dotenv()

DEBUG = os.getenv("DEBUG", False)
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
POSTGRES_URL = os.getenv("POSTGRES_URL", "")
