from typing import Optional

from sqlalchemy.orm import Session

from app.repos.base_repo import BaseRepo
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserRepo(BaseRepo[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def authenticate(self, db: Session, *, email: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None

        return user


user = UserRepo(User)
