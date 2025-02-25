from odmantic import Model, ObjectId
from typing import Optional


class Probe(Model):
    machine_id: ObjectId
    name: str
    units: Optional[str]
    severity: str
    description: Optional[str]
