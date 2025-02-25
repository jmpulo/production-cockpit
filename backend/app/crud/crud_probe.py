import models.probe
from .base import CRUDBase
from odmantic.session import AIOSession
from odmantic import ObjectId
import schemas
import models


class CRUDProbe(CRUDBase[models.Probe, schemas.ProbeCreate, schemas.ProbeUpdate]):
    async def get_probe_in_machine(
        self, db: AIOSession, machine_id: ObjectId, probe_name: str
    ) -> models.Probe | None:

        return await db.find_one(
            self.model,
            self.model.machine_id == machine_id,
            self.model.name == probe_name,
        )

    async def get_by_machine_id(
        self, db: AIOSession, *, machine_id: ObjectId
    ) -> list[models.Probe]:
        return await db.find(self.model, self.model.machine_id == machine_id)

    async def remove_by_machine_id(
        self, db: AIOSession, *, machine_id: ObjectId
    ) -> None:
        orphan_probes = await db.find(self.model, self.model.machine_id == machine_id)

        for probe in orphan_probes:
            await db.delete(probe)


probe = CRUDProbe(models.Probe)
