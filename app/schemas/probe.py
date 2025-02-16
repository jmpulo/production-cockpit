from pydantic import BaseModel
from odmantic import ObjectId
from typing import Optional
from typing import Literal, ClassVar
from .metric import Metric


class ProbeBase(BaseModel):
    machine_id: Optional[ObjectId] = None
    name: Optional[str] = None
    units: Optional[str] = None
    severity: Optional[Literal["low", "medium", "high"]] = None
    description: Optional[str] = None


class ProbeCreate(ProbeBase):
    name: str
    severity: Literal["low", "medium", "high"] = "low"


class ProbeUpdate(ProbeBase):
    pass


class ProbeInDBBase(ProbeBase):
    id: ObjectId


class Probe(ProbeInDBBase):
    machine_id: ClassVar[ObjectId]


class ProbeMetrics(Probe):
    metrics: list[Metric]
