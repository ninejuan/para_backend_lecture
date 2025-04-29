from fastapi import APIRouter
from dotenv import load_dotenv
import services.board as boardService

load_dotenv()

router = APIRouter(
    prefix="/board"
)

@router.post('/create')
async def create():
    return ''

@router.get('/get/all')
async def getAll():
    return ''

@router.get('/get/:id')
async def getArticle():
    return ''

@router.put('/update')
async def updateArticle():
    return ''

@router.delete('/delete')
async def deleteArticle():
    return ''