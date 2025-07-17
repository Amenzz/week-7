from fastapi import FastAPI
import crud

app = FastAPI()

@app.get("/api/reports/top-products")
async def top_products(limit: int = 10):
    return await crud.get_top_products(limit)

@app.get("/api/channels/{channel_name}/activity")
async def channel_activity(channel_name: str):
    return await crud.get_channel_activity(channel_name)

@app.get("/api/search/messages")
async def search_messages(query: str):
    return await crud.search_messages(query)
