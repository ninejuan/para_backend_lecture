from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
import services.board as boardService
from repository.board import Article

load_dotenv()

router = APIRouter(
    prefix="/board"
)

@router.post('/create')
async def create():
    try:
        return {}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/get/all')
async def getAll():
    try:
        return {}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/get/')
async def getArticle():
    try:
        return {}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put('/update/')
async def updateArticle():
    try:
        return {}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete('/delete/')
async def deleteArticle():
    try:
        return {}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))