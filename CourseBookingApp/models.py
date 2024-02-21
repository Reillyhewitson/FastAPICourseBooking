from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    convenor = Column(String, index=True)

    students = relationship("User", back_populates="course")

Base.metadata.create_all(bind=engine)