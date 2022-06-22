from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Post(Base):
  __tablename__ = "posts"
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  user_id = Column(Integer, ForeignKey("users.id"))
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  user = relationship("User")

  # Query will appear as follows
  # {
  # "id": 1,
  # "title": "How to Learn Python",
  # "user_id": 2,
  # "user": {
  #   "id": 2,
  #   "username": "lernantino"
  # }
  # }