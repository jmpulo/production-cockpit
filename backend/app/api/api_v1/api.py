from fastapi import APIRouter
from .endpoints import machines, probes, metrics

api_router = APIRouter()


api_router.include_router(machines.router, prefix="/machine", tags=["Machines"])
api_router.include_router(probes.router, prefix="/probe", tags=["Probes"])
api_router.include_router(metrics.router, prefix="/metric", tags=["Metrics"])
