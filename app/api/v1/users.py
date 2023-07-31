from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()


class User(BaseModel):
    name: str
    username: str


users_db = [User(name="John Doe", username="jdoe")]


@router.get("/")
async def get_users() -> list[User]:
    return users_db
