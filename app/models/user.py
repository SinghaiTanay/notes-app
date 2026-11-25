from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Integer, String, func
from app.db.session import Base


class User(Base):
    __tablename__='users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String)
    hashed_password: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    entries = relationship(
    "Entry",
    back_populates="user",
    cascade="all, delete-orphan",
    passive_deletes=True
)
