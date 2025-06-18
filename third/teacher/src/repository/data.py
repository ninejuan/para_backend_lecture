from pydantic import BaseModel, Field
import uuid
import datetime as dt

# vectordb 실습용 db야. vector 값을 담을 수 있어야 해.
class Data(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    vector: list[float]
    created_at: dt.datetime = Field(default_factory=dt.datetime.utcnow)
    updated_at: dt.datetime = Field(default_factory=dt.datetime.utcnow)

    class Config:
        schema_extra = {
            "example": {
                "name": "example",
                "vector": [0.1, 0.2, 0.3],
            }
        }