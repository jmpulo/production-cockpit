from pydantic import BaseModel
from odmantic import ObjectId
from typing import Optional


class MachineBase(BaseModel):
    name: Optional[str] = None
    reference: Optional[str] = None


class MachineCreate(MachineBase):
    name: str


class MachineUpdate(MachineBase):
    pass


class MachineInDBBase(MachineBase):
    id: ObjectId


class Machine(MachineInDBBase):
    pass
