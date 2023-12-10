from os import getenv
from pathlib import Path

from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parent.parent

dotenv_path = Path(ROOT_DIR, "config", ".env")
load_dotenv(dotenv_path)

bot_token = getenv("BOT_TOKEN")
admin1 = getenv("ADMIN1")
