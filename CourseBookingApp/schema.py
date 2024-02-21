from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    convenor: str


class CourseCreate(CourseBase):
    pass

class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    course_id: int

    class Config:
        orm_mode = True

class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True