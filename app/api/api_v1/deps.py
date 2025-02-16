from odmantic.session import AIOSession
from odmantic import ObjectId
from typing import AsyncGenerator
from db.engine import engine
from fastapi import Depends, HTTPException, status
import models
import crud


async def get_db() -> AsyncGenerator[AIOSession, None]:
    async with engine.session() as session:
        yield session


async def get_machine(
    db: AIOSession = Depends(get_db), *, id: ObjectId
) -> models.Machine:
    machine_db = await crud.machine.get(db, id=id)
    if not machine_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return machine_db
