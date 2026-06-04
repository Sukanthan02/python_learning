from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), uniq
<truncated 563 bytes>