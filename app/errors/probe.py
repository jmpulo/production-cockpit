from .base import CockpitException


class ProbeException(CockpitException):
    pass


class ProbeDuplicated(ProbeException):
    pass
