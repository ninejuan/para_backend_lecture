import os, uvicorn, dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from controllers.member import router as memberController


dotenv.load_dotenv()

app = FastAPI(
    title="PARA Member Homework",
    description="PARA 2차시 부원정보 CRUD 구현 과제",
    version="dev",
    docs_url="/api-docs"
)

# CORS 코드를 채워봅시다.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def thisisroot():
    return 'Hello this is para backend homework answer file'

app.include_router(memberController)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)