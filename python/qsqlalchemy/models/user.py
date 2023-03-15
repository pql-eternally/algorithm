from datetime import datetime
from typing import Optional, List

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from qcore.core.mysql import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(32), nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(32))
    nickname: Mapped[Optional[str]] = mapped_column(String(64))
    created_at: Mapped[datetime] = mapped_column(insert_default=datetime.utcnow())
    updated_at: Mapped[datetime] = mapped_column(insert_default=datetime.utcnow())
    addresses: Mapped[List["Address"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
