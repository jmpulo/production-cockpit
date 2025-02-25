from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

client = AsyncIOMotorClient(host=settings.MONGODB_DSN)

engine = AIOEngine(client=client, database=settings.MONGODB_DB)
