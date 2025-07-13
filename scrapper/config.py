# scraper/config.py
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_ID = int(os.getenv("TELEGRAM_API_ID"))
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
CHANNELS = [
    "https://t.me/lobelia4cosmetics",
    "https://t.me/tikvahpharma",
    "https://t.me/chemed_et",
]
DATA_DIR = "data/raw/telegram_messages"
LOG_FILE = "logs/scraper.log"
