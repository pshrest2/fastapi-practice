from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)

    items = relationship("Item", back_populates="owner")
