import models
import crud
import schemas
from odmantic.session import AIOSession
from errors import ProbeDuplicated


class Machine:
    def __init__(self, model: models.Machine):
        self._model = model

    async def add_probe(
        self, db: AIOSession, *, probe: schemas.ProbeCreate
    ) -> models.Probe:
        probe.machine_id = self._model.id
        probe_db = await crud.probe.get_probe_in_machine(
            db, machine_id=probe.machine_id, probe_name=probe.name
        )
        if probe_db is not None:
            raise ProbeDuplicated("Probe name already exists")

        return await crud.probe.create(db, obj_in=probe)

    async def delete(self, db: AIOSession) -> models.Machine:
        machine_db = await crud.machine.remove(db, db_obj=self._model)
        await crud.probe.remove_by_machine_id(db, machine_id=machine_db.id)
        return machine_db

    # todo finish method to add metric to probe
    async def add_metric(
        self, db: AIOSession, *, metric: schemas.MetricCreate
    ) -> models.Metric:
        probe_db = await crud.probe.get_probe_in_machine(
            db, machine_id=self._model.id, probe_name=metric.probe_name
        )
