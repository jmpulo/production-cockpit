from fastapi import APIRouter, Depends, HTTPException, status
from odmantic.session import AIOSession
from odmantic import ObjectId
from api.api_v1 import deps
import schemas
import models
import crud

router = APIRouter()


@router.post("/", response_model=schemas.Machine)
async def create_machine(
    db: AIOSession = Depends(deps.get_db), *, new_machine: schemas.MachineCreate
):
    return await crud.machine.create(db, obj_in=new_machine)


@router.get(
    "/",
    response_model=list[schemas.Machine],
    description="Returns a list with all the existing machines",
)
async def get_machines(db: AIOSession = Depends(deps.get_db)):
    return await crud.machine.get_multi(db)


@router.get(
    "/{id}",
    response_model=schemas.Machine,
    description="Return a specific machine by id if exists",
)
async def get_machine(db: AIOSession = Depends(deps.get_db), *, id: ObjectId):
    machine_db = await crud.machine.get(db, id=id)
    if not machine_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return machine_db


@router.put(
    "/{id}", response_model=schemas.Machine, description="Updates a machine if exists"
)
async def update_machine(
    db: AIOSession = Depends(deps.get_db),
    *,
    id: ObjectId,
    machine_update: schemas.MachineUpdate,
    machine_db: models.Machine = Depends(deps.get_machine)
):
    return await crud.machine.update(db, db_obj=machine_db, obj_in=machine_update)


@router.delete(
    "/{id}", response_model=schemas.Machine, description="Removes an existing machine"
)
async def delete_machine(
    db: AIOSession = Depends(deps.get_db),
    *,
    id: ObjectId,
    machine_db: models.Machine = Depends(deps.get_machine)
):
    return await crud.machine.remove(db, db_obj=machine_db)
