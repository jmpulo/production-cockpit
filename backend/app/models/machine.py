from odmantic import Model
from typing import Optional


class Machine(Model):
    name: str
    reference: Optional[str]
