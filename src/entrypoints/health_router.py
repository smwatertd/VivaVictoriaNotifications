from entrypoints.schemas import HealthSchema

from fastapi import APIRouter


router = APIRouter()


@router.get('/health')
def check_health() -> HealthSchema:
    return HealthSchema(status='ok')
