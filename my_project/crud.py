from sqlalchemy.future import select
from models import Message, Detection
from database import SessionLocal

async def get_top_products(limit: int):
    async with SessionLocal() as session:
        result = await session.execute(
            f"""
            SELECT detected_object_class, COUNT(*) AS frequency
            FROM fct_image_detections
            GROUP BY detected_object_class
            ORDER BY frequency DESC
            LIMIT {limit}
            """
        )
        return result.fetchall()

async def get_channel_activity(channel_name: str):
    async with SessionLocal() as session:
        result = await session.execute(
            f"""
            SELECT DATE_TRUNC('day', timestamp) as day, COUNT(*) as posts
            FROM fct_messages
            WHERE channel = '{channel_name}'
            GROUP BY day
            ORDER BY day
            """
        )
        return result.fetchall()

async def search_messages(query: str):
    async with SessionLocal() as session:
        result = await session.execute(
            f"""
            SELECT * FROM fct_messages
            WHERE content ILIKE '%{query}%'
            LIMIT 100
            """
        )
        return result.fetchall()
