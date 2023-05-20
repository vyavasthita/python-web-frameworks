from fastapi import FastAPI
import uvicorn
from config import settings

app = FastAPI()


@app.get("/")
async def home():
    return {'name': 'Raja Sharma'}


if __name__ == '__main__':
    uvicorn.run("main:app", host=settings.api_host, port=settings.api_port, reload=True)