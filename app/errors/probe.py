from .base import CockpitException


class ProbeException(CockpitException):
    pass


class ProbeDuplicated(ProbeException):
    pass


class ProbeNotExist(ProbeException):
    pass
