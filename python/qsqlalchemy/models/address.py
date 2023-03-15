from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from qcore.core.mysql import BaseModel


class Address(BaseModel):
    __tablename__ = "address"

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("user.id"))
    email_address: Mapped[str] = mapped_column(String(32))
    created_at: Mapped[datetime] = mapped_column(insert_default=datetime.utcnow())
    updated_at: Mapped[datetime] = mapped_column(insert_default=datetime.utcnow())

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
