from fastapi import APIRouter
import services.hello as helloService

router = APIRouter(
    prefix="/hello"
)
# router = APIRouter()

@router.get('/sungho')
def return_sungho():
    return helloService.return_sungho()