from sqlalchemy import Column, Integer, String, Text, DateTime, func
from .database import Base

class Post(Base):
    __tablename__ = "posts_db"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    likes = Column(Integer, default=0)
    created_time = Column(DateTime(timezone=True), server_default=func.now())
