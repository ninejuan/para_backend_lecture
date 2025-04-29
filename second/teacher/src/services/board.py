from common.db import db as mongodb
from bson import ObjectId

boardCollection = mongodb['board']

def create_board(board: dict):
    """새 게시글을 생성합니다."""
    result = boardCollection.insert_one(board)
    return str(result.inserted_id)

def get_all_boards():
    """모든 게시글을 조회합니다."""
    boards = list(boardCollection.find())
    for board in boards:
        board['id'] = str(board['id'])
    return boards

def get_board(board_id: str):
    """게시글을 ID로 조회합니다."""
    board = boardCollection.find_one({"id": board_id})
    if board:
        board['id'] = str(board['id'])
    return board if board else None

def update_board(board_id: str, board: dict):
    """게시글을 업데이트합니다."""
    result = boardCollection.update_one(
        {"id": board_id}, 
        {"$set": board}
    )
    return str(board_id) if result.modified_count > 0 else None

def delete_board(board_id: str):
    """게시글을 삭제합니다."""
    result = boardCollection.delete_one({"id": board_id})
    return str(board_id) if result.deleted_count > 0 else None