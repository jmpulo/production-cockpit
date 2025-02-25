from fastapi import APIRouter, Depends, HTTPException, status
from odmantic.session import AIOSession
from odmantic import ObjectId
from api.api_v1 import deps
from interfaces import Machine
from errors import ProbeDuplicated
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
    machine_int: Machine = Depends(deps.get_machine_iface)
):

    return await machine_int.delete(db)


@router.post(
    "/{id}/probe",
    response_model=schemas.Probe,
    description="Adds a new probe to an existing machine",
)
async def add_probe_to_machine(
    db: AIOSession = Depends(deps.get_db),
    *,
    id: ObjectId,
    new_probe: schemas.ProbeCreate,
    machine_int: Machine = Depends(deps.get_machine_iface)
):

    try:
        return await machine_int.add_probe(db, probe=new_probe)
    except ProbeDuplicated as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.get(
    "/{id}/probe",
    response_model=schemas.MachineProbes,
    description="Retrieves all the probes of a machine",
)
async def get_machine_probes(
    db: AIOSession = Depends(deps.get_db),
    *,
    id: ObjectId,
    machine_db: models.Machine = Depends(deps.get_machine)
):
    probes_db = await crud.probe.get_by_machine_id(db, machine_id=id)
    machine = schemas.MachineProbes(**machine_db.model_dump())
    machine.probes = probes_db

    return machine


@router.post("/{id}/metric", response_model=schemas.Metric)
async def add_metric(
    db: AIOSession = Depends(deps.get_db),
    *,
    id: ObjectId,
    machine_iface: Machine = Depends(deps.get_machine_iface),
    new_metric: schemas.MetricCreate
):
    return await machine_iface.add_metric(db, metric=new_metric)
