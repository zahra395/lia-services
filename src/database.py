from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings
from src.models.models import Product


async def connect_database():
    client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
    await init_beanie(database=client[settings.MONGO_DATABASE], document_models=[Product])
