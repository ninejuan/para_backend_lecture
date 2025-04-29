from common.db import db as mongodb
from bson import ObjectId

memberCollection = mongodb['member']

def createMember(member: dict): 
    """새 회원을 생성합니다."""
    result = memberCollection.insert_one(member)
    return str(result.inserted_id)

def getMember(member_id: str):
    """회원 정보를 조회합니다."""
    member = memberCollection.find_one({"_id": ObjectId(member_id)})
    return member if member else None

def getAllMembers():
    """모든 회원 정보를 조회합니다."""
    members = list(memberCollection.find())
    return members

def updateMember(member_id: str, member: dict):
    """회원 정보를 업데이트합니다."""
    result = memberCollection.update_one(
        {"_id": ObjectId(member_id)}, 
        {"$set": member}
    )
    return str(member_id) if result.modified_count > 0 else None

def deleteMember(member_id: str):
    """회원 정보를 삭제합니다."""
    result = memberCollection.delete_one({"_id": ObjectId(member_id)})
    return str(member_id) if result.deleted_count > 0 else None