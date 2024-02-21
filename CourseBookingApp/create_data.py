from database import engine
import models, schema
from sqlalchemy.orm import Session

with Session(bind=engine) as session:
    course1 = models.Courses(id= 0, title="Biology",  convenor="Jim Smith")
    course2 = models.Courses(id = 1, title="Maths",convenor="Jack Jones")

    student1 = models.User(name="Test test", course_id = 0)
    student2 = models.User(name="not test", course_id = 0)

    session.add_all([course1, course2])
    session.commit()