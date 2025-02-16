from pydantic import BaseModel
from odmantic import ObjectId
from typing import Optional
from typing import Union, ClassVar


class MetricBase(BaseModel):
    probe_id: Optional[ObjectId] = None
    value: Optional[Union[float, int, str]] = None


class MetricCreate(MetricBase):
    probe_name: Optional[str]
    value: Union[float, int, str]


class MetricUpdate(MetricBase):
    pass


class MetricInDBBase(MetricBase):
    id: ObjectId


class Metric(MetricInDBBase):
    probe_id: ClassVar[ObjectId]
