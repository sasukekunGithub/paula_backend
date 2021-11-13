from fastapi import FastAPI
from pydantic import BaseModel

# app is an instance of FastAPI
app = FastAPI()


class Baby(BaseModel):
    isBabyThere: bool = "false"
    admin_email: str = ""
    babyName: str = ""
    babyWeight: str = ""
    babySize: str = ""
    babyBirthdate: str = ""


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/krinksbaby", response_model=Baby)
async def get_is_baby_there():
    baby = Baby()
    return baby

