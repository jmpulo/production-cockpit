from .base import CRUDBase
import schemas
import models


class CRUDMetric(CRUDBase[models.Metric, schemas.MetricCreate, schemas.MetricUpdate]):
    pass


metric = CRUDMetric(models.Metric)
