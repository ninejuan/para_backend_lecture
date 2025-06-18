from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
import services.board as boardService
from repository.board import Article

load_dotenv()

router = APIRouter(
    prefix="/search"
)

@router.get('/article')
async def search_article(
    keyword: str,
    page: int = 1,
    limit: int = 10
):
    if not keyword:
        raise HTTPException(status_code=400, detail="Keyword is required")

    articles = await boardService.search_article(keyword, page, limit)
    total_count = await boardService.count_articles(keyword)

    return {
        "articles": articles,
        "total_count": total_count,
        "page": page,
        "limit": limit
    }