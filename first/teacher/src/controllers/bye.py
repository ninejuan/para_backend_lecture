from fastapi import APIRouter
import services.bye as byeService

router = APIRouter(
    prefix='/bye'
)

@router.get('/')
def bye():
    return byeService.getBye()
