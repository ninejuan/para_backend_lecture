from pydantic import BaseModel, Field
import uuid
import datetime as dt

class Member(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="회원ID")
    name: str = Field(..., description="회원의 이름입니다.", examples=["이주안"])
    introduction: str = Field(..., description="회원의 자기소개입니다.", examples=["안녕하세요, 백엔드 개발자 이주안입니다."])
    department: str = Field(..., description="회원의 소속입니다.", examples=["소프트웨어과"])
    generation: int = Field(..., description="회원의 기수입니다.", examples=[120])
    createdAt: dt.datetime = Field(default_factory=dt.datetime.now, description="생성 시각")