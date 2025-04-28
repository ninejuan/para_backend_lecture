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

# CORS 코드를 채워봅시다.
app.add_middleware()

@app.get('/')
def thisisroot():
    return 'Hello this is para backend first lecture'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)