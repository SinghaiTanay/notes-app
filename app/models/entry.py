import enum
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Integer, String, Text, func, ForeignKey, Enum
from app.db.session import Base

class EntryType(enum.Enum):
    note = "note"
    journal = "journal"
    todo = "todo"

class Entry(Base):
    __tablename__='entries'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer,ForeignKey('users.id',ondelete="CASCADE"),nullable=False)
    type: Mapped[EntryType] = mapped_column(Enum(EntryType),nullable=False)
    title: Mapped[str|None] = mapped_column(String(255),nullable=True)
    content: Mapped[str|None] = mapped_column(Text,nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now(),nullable=False)
    user = relationship("User",back_populates="entries")