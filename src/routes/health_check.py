from fastapi import APIRouter

from src.schemas.health_check_schema import HealthCheckResponse

router = APIRouter()


@router.get(
    path='/healthcheck', 
    status_code=200,
    response_model=HealthCheckResponse, 
    tags=['Health Check'], 
    description='Is API alive ?'
)
def health_check():
    return HealthCheckResponse()
