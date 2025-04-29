from pydantic import BaseModel, Field
import uuid
import datetime as dt

class Article(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="게시글의 ID입니다.")
    title: str = Field(..., description="게시글의 제목입니다.", examples=["[25] PARA ANN 수업자료"])
    content: str = Field(..., description="게시글의 내용입니다.", examples=["PARA 인공신경망 수업자료입니다."])
    createdAt: dt.datetime = Field(default_factory=dt.datetime.now, description="게시글이 생성된 시간입니다.")
