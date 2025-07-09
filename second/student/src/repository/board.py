from pydantic import BaseModel, Field
import uuid
import datetime as dt

class Article(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="게시글 ID")
    title: str = Field(..., description="게시글 제목", examples=["[25] PARA ANN 수업자료"])
    content: str = Field(..., description="게시글 내용", examples=["2025년도 PARA ANN 수업자료"])
    createdAt: dt.datetime = Field(default_factory=dt.datetime.now, description="게시글 작성 시간")

