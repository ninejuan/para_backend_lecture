from fastapi import APIRouter, HTTPException
import services.member as memberService
from repository.member import Member

router = APIRouter(
    prefix="/member"
)

@router.post('/create')
async def create(member: Member):
    try:
        member_id = memberService.create_member(member.model_dump())
        return {"message": "회원이 생성되었습니다.", "member_id": member_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get('/get/all')
async def getAll():
    try:
        members = memberService.get_all_members()
        return {"members": members}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/get/{member_id}')
async def getMember(member_id: str):
    try:
        member = memberService.get_member(member_id)
        if not member:
            raise HTTPException(status_code=404, detail="회원을 찾을 수 없습니다.")
        return member
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put('/update/{member_id}')
async def updateMember(member_id: str, member: Member):
    try:
        updated_id = memberService.update_member(member_id, member.model_dump())
        if not updated_id:
            raise HTTPException(status_code=404, detail="회원을 찾을 수 없습니다.")
        return {"message": "회원이 수정되었습니다.", "member_id": updated_id}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete('/delete/{member_id}')
async def deleteMember(member_id: str):
    try:
        deleted_id = memberService.delete_member(member_id)
        if not deleted_id:
            raise HTTPException(status_code=404, detail="회원을 찾을 수 없습니다.")
        return {"message": "회원이 삭제되었습니다.", "member_id": deleted_id}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))