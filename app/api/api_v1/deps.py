from odmantic.session import AIOSession
from typing import AsyncGenerator
from db.engine import engine


async def get_db() -> AsyncGenerator[AIOSession, None]:
    async with engine.session() as session:
        yield session
