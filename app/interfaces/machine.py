import models
import crud
import schemas
from odmantic.session import AIOSession
from errors import ProbeDuplicated, ProbeNotExist


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

    async def get_probe(
        self, db: AIOSession, *, probe_name: str
    ) -> models.Probe | None:
        return await crud.probe.get_probe_in_machine(
            db, machine_id=self._model.id, probe_name=probe_name
        )

    async def delete(self, db: AIOSession) -> models.Machine:
        machine_db = await crud.machine.remove(db, db_obj=self._model)
        await crud.probe.remove_by_machine_id(db, machine_id=machine_db.id)
        return machine_db

    async def add_metric(
        self, db: AIOSession, *, metric: schemas.MetricCreate
    ) -> models.Metric:
        probe_db = await self.get_probe(db, probe_name=metric.probe_name)
        if not probe_db:
            raise ProbeNotExist(
                f"Probe {metric.probe_name} does not exist in machine {self._model.name}"
            )
        metric.probe_id = probe_db.id
        return await crud.metric.create(db, obj_in=metric)
