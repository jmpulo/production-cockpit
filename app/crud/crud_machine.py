from .base import CRUDBase
import schemas
import models


class CRUDMachine(
    CRUDBase[models.Machine, schemas.MachineCreate, schemas.MachineUpdate]
):
    pass


machine = CRUDMachine(models.Machine)
