from common.db import db as mongodb
boardCollection = mongodb['board']

def get_board(board_id: str):
    """게시글을 ID로 조회합니다."""

def create_board(board: dict):
    """새 게시글을 생성합니다."""

def get_all_boards():
    """모든 게시글을 조회합니다."""

def update_board(board_id: str, board: dict):
    """게시글을 업데이트합니다."""

def delete_board(board_id: str):
    """게시글을 삭제합니다."""