from typing import Any, List
from app import repos, models, schemas
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
async def get_users(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    users = repos.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=schemas.User)
async def create_user(
    user_in: schemas.UserCreate, db: Session = Depends(deps.get_db)
) -> Any:
    user = repos.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400, detail="The user with this email already exists."
        )
    user = repos.user.create(db=db, obj_in=user_in)
    return user
