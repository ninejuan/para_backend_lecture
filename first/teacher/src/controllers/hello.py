from fastapi import APIRouter
import services.hello as helloService

router = APIRouter(
    prefix='/hello'
)

@router.get('/')
def hello():
    return helloService.getHello()
