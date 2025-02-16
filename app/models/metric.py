from odmantic import Model, ObjectId
from typing import Union


class Metric(Model):
    probe_id: ObjectId
    value: Union[float, int, str]
