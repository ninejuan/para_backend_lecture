from common.db import db as mongodb
boardCollection = mongodb['board']

# from common.client import client as mongo_client
# db = mongo_client['board']

def create_board(board: dict):
    """새 게시글을 생성합니다."""
    result = boardCollection.insert_one(board)
    return str(result.inserted_id)

def get_board(board_id: str):
    """게시글을 ID로 조회합니다."""
    result = boardCollection.find_one({
        "id": board_id
    })
    return result

def get_all_boards():
    """모든 게시글을 조회합니다."""
    boards = []
    for board in boardCollection.find({}):
        board['id'] = str(board['id'])
        board.pop("_id", None)
        boards.append(board)
    return boards

def update_board(board_id: str, board: dict):
    """게시글을 업데이트합니다."""
    result = boardCollection.update_one(
        {"id": board_id},
        {"$set": board}
    )
    return result.modified_count > 0

def delete_board(board_id: str):
    """게시글을 삭제합니다."""
    result = boardCollection.delete_one({
        "id": board_id
    })
    return result.deleted_count > 0