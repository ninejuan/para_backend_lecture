import os
from common.db import db as mongodb

memberCollection = mongodb[os.getenv('DB_COLLECTION')]

def createMember(member: dict): 
    """새 부원 정보를 생성합니다."""
    result = memberCollection.insert_one(member)
    return str(result.inserted_id)

def getMember(member_id: str):
    """부원 정보를 조회합니다."""
    member = memberCollection.find_one({"id": member_id})
    return member if member else None

def getAllMembers():
    """모든 부원 정보를 조회합니다."""
    members = list(memberCollection.find())
    return members

def updateMember(member_id: str, member: dict):
    """부원 정보를 업데이트합니다."""
    result = memberCollection.update_one(
        {"id": member_id}, 
        {"$set": member}
    )
    return str(member_id) if result.modified_count > 0 else None

def deleteMember(member_id: str):
    """부원 정보를 삭제합니다."""
    result = memberCollection.delete_one({"id": member_id})
    return str(member_id) if result.deleted_count > 0 else None