# scraper/scraper.py
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest
import json
import asyncio
import logging

from .config import TELEGRAM_API_ID, TELEGRAM_API_HASH, CHANNELS, LOG_FILE
from .utils import create_output_path, init_logger

init_logger(LOG_FILE)

async def fetch_messages(client, channel_url):
    try:
        entity = await client.get_entity(channel_url)
        history = await client(GetHistoryRequest(
            peer=entity,
            limit=500,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0
        ))

        messages = []
        for msg in history.messages:
            messages.append(msg.to_dict())

        output_path = create_output_path(channel_url)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)

        logging.info(f"Scraped {len(messages)} messages from {channel_url}")
    except FloodWaitError as e:
        logging.warning(f"Rate limited. Waiting {e.seconds} seconds.")
        await asyncio.sleep(e.seconds)
    except Exception as e:
        logging.error(f"Error scraping {channel_url}: {str(e)}")

async def main():
    async with TelegramClient('anon', TELEGRAM_API_ID, TELEGRAM_API_HASH) as client:
        tasks = [fetch_messages(client, url) for url in CHANNELS]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
