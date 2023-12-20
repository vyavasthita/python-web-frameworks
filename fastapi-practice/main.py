from fastapi import FastAPI, UploadFile, Depends
import uvicorn
from config import settings
from routers.user import user_router
from pydantic import BaseModel
from enum import IntEnum


app = FastAPI()

app.include_router(user_router)


class Age(IntEnum):
    CHILD = 10
    YOUTH = 25
    ELDER = 50

class User(BaseModel):
    name: str
    city: str
    
async def get_name():
    return 'Raja'

@app.post("/home/{designation}")
async def home(designation: str, user: User, age: Age):
    return {'designation': designation, 'name': user.name, 'city': user.city}


if __name__ == '__main__':
    uvicorn.run("main:app", host=settings.api_host, port=settings.api_port, reload=True)