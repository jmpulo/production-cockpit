from odmantic.session import AIOSession
from odmantic import ObjectId
from typing import AsyncGenerator
from db.engine import engine
from fastapi import Depends, HTTPException, status
from interfaces import Machine
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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Machine {id} does not exist"
        )
    return machine_db


async def get_probe(db: AIOSession = Depends(get_db), *, id: ObjectId) -> models.Probe:
    probe_db = await crud.probe.get(db, id=id)
    if not probe_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Probe {id} does not exist"
        )
    return probe_db


async def get_machine_iface(
    machine_db: models.Machine = Depends(get_machine),
) -> Machine:
    return Machine(machine_db)


async def get_metric(
    db: AIOSession = Depends(get_db), *, id: ObjectId
) -> models.Metric:
    metric_db = await crud.metric.get(db, id=id)
    if not metric_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Metric {id} does not exist"
        )
    return metric_db
