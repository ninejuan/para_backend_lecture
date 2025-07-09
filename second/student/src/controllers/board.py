from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
import services.board as boardService
from repository.board import Article

load_dotenv()

router = APIRouter(
    prefix="/board"
)

@router.post('/create')
async def create(article: Article):
    try:
        board_id = boardService.create_board(article.model_dump())
        return {"message": "게시글 생성 성공", "id": board_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/get/all')
async def getAll():
    try:
        boards = boardService.get_all_boards()
        return { "boards": boards }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/get/{board_id}')
async def getArticle(board_id):
    try:
        board = boardService.get_board(board_id)
        return { "board": board }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put('/update/{board_id}')
async def updateArticle(board_id, article: Article):
    try:
        updated = boardService.update_board(board_id, article.model_dump())
        return { "message": "게시글 업데이트 성공", "updated": updated }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete('/delete/{board_id}')
async def deleteArticle(board_id):
    try:
        deleted = boardService.delete_board(board_id)
        return { "message": "게시글 삭제 성공", "deleted": deleted }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))