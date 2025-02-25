from pydantic import BaseModel
from odmantic import ObjectId
from typing import Optional
from typing import Union


class MetricBase(BaseModel):
    probe_id: Optional[ObjectId] = None
    probe_name: Optional[str] = None
    value: Optional[Union[float, int, str]] = None


class MetricCreate(MetricBase):
    probe_name: str
    value: Union[float, int, str]


class MetricUpdate(MetricBase):
    pass


class MetricInDBBase(MetricBase):
    id: ObjectId


class Metric(MetricInDBBase):
    pass
