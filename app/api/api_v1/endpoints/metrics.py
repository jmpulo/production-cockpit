from fastapi import APIRouter, Depends
from odmantic.session import AIOSession
from odmantic import ObjectId
from api.api_v1 import deps
import schemas
import models
import crud

router = APIRouter()


@router.get("/{id}", response_model=models.Metric)
async def get_metric(
    db: AIOSession = Depends(deps.get_db),
    *,
    id: ObjectId,
    metric_db=Depends(deps.get_metric)
):
    return metric_db


@router.put("/{id}", response_model=models.Metric)
async def update_metric(
    db: AIOSession = Depends(deps.get_db),
    *,
    id: ObjectId,
    update_obj: schemas.MetricUpdate,
    metric_db: models.Metric = Depends(deps.get_metric)
):
    return await crud.metric.update(db, db_obj=metric_db, obj_in=update_obj)


@router.delete("/{id}", response_model=models.Metric)
async def delete_metric(
    db: AIOSession = Depends(deps.get_db),
    *,
    id: ObjectId,
    metric_db: models.Metric = Depends(deps.get_metric)
):
    return await crud.metric.remove(db, db_obj=metric_db)
