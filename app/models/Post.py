from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

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
  votes = relationship("Vote", cascade="all,delete")
  vote_count = column_property(
    select([func.count(Vote.id)]).where(Vote.post_id == id)
  )
  #above dynamic property same as following SQL query 
  #SELECT COUNT(votes.id) AS vote_count FROM votes WHERE votes.post_id = 1;

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