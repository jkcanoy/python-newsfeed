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
  #deleting a post will delete all associated comments
  comments = relationship("Comment", cascade="all,delete")

  # Query will appear as follows
  # {
  #   "id": 1,
  #   "title": "How to Learn Python",
  #   "user_id": 2,
  #   "user": {
  #     "id": 2,
  #     "username": "lernantino"
  #  },
  #  "comments": [
  #    {
  #      "id": 1,
  #      "comment_text": "Great article!",
  #      "post_id": 1,
  #      "user_id": 3,
  #      "user": {
  #        "id": 3,
  #        "username": "someone_else" // comment author
  #      }
  #     }
  #    ]
  #  }