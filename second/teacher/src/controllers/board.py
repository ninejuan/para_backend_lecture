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
        return {"message": "게시글이 생성되었습니다.", "board_id": board_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/get/all')
async def getAll():
    try:
        boards = boardService.get_all_boards()
        return {"boards": boards}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/get/{board_id}')
async def getArticle(board_id: str):
    try:
        board = boardService.get_board(board_id)
        if not board:
            raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
        return board
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put('/update/{board_id}')
async def updateArticle(board_id: str, article: Article):
    try:
        updated_id = boardService.update_board(board_id, article.model_dump())
        if not updated_id:
            raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
        return {"message": "게시글이 수정되었습니다.", "board_id": updated_id}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete('/delete/{board_id}')
async def deleteArticle(board_id: str):
    try:
        deleted_id = boardService.delete_board(board_id)
        if not deleted_id:
            raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
        return {"message": "게시글이 삭제되었습니다.", "board_id": deleted_id}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))