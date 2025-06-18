import os, uvicorn, dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

dotenv.load_dotenv()

app = FastAPI(
    title="PARA BE Lecture",
    description="PARA BE Lecture",
    version="dev",
    docs_url="/api-docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def thisisroot():
    return 'Hello this is para backend second lecture'

app.include_router(boardController)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)