from common.db import db as mongodb
boardCollection = mongodb['board']

def get_board(board_id: str):
    """게시글을 ID로 조회합니다."""
    board = boardCollection.find_one({"_id": board_id})
    return board if board else None

def create_board(board: dict):
    """새 게시글을 생성합니다."""
    result = boardCollection.insert_one(board)
    return result.inserted_id

def get_all_boards():
    """모든 게시글을 조회합니다."""
    return list(boardCollection.find())

def update_board(board_id: str, board: dict):
    """게시글을 업데이트합니다."""
    result = boardCollection.update_one(
        {"_id": board_id}, 
        {"$set": board}
    )
    return board_id if result.modified_count > 0 else None

def delete_board(board_id: str):
    """게시글을 삭제합니다."""
    result = boardCollection.delete_one({"_id": board_id})
    return board_id if result.deleted_count > 0 else None