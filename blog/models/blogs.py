from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from blog.database import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    creator_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="blogs")
