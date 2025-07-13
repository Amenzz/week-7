# scraper/utils.py
import os
from datetime import datetime
import logging

def init_logger(log_file):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
    )

def create_output_path(channel_username):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    channel_clean = channel_username.replace("https://t.me/", "").replace("/", "_")
    dir_path = os.path.join("data", "raw", "telegram_messages", today)
    os.makedirs(dir_path, exist_ok=True)
    return os.path.join(dir_path, f"{channel_clean}.json")
