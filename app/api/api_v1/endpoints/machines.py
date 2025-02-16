from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_machines():
    return {"test": "working"}
