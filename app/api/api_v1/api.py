from fastapi import APIRouter
from .endpoints import machines

api_router = APIRouter()


api_router.include_router(machines.router, prefix="/machine", tags=["Machines"])
