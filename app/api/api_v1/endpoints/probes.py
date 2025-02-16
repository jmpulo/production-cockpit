from fastapi import APIRouter, Depends
from odmantic.session import AIOSession
from odmantic import ObjectId
from api.api_v1 import deps
import schemas
import models
import crud

router = APIRouter()


@router.get("/", response_model=schemas.Probe)
async def get_probe(
    db: AIOSession = Depends(deps.get_db),
    *,
    id: ObjectId,
    probe_db: models.Probe = Depends(deps.get_probe)
):
    return probe_db


@router.put("/{id}", response_model=schemas.Probe)
async def update_probe(
    db: AIOSession = Depends(deps.get_db),
    *,
    id: ObjectId,
    update_obj: schemas.ProbeUpdate,
    probe_db: models.Probe = Depends(deps.get_probe)
):
    return await crud.probe.update(db, db_obj=probe_db, obj_in=update_obj)


@router.delete("/{id}", response_model=schemas.Probe)
async def delete_probe(
    db: AIOSession = Depends(deps.get_db),
    *,
    id: ObjectId,
    probe_db: models.Probe = Depends(deps.get_probe)
):
    return await crud.probe.remove(db, db_obj=probe_db)
