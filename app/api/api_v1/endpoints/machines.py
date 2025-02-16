from fastapi import APIRouter, Depends
from odmantic.session import AIOSession
from api.api_v1 import deps
import schemas
import crud

router = APIRouter()


@router.get("/", response_model=list[schemas.Machine])
async def get_machines(db: AIOSession = Depends(deps.get_db)):
    return await crud.machine.get_multi(db)


@router.post("/", response_model=schemas.Machine)
async def create_machine(
    db: AIOSession = Depends(deps.get_db), *, new_machine: schemas.MachineCreate
):
    return await crud.machine.create(db, obj_in=new_machine)
