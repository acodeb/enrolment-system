import models
from app.db import schema
from sqlalchemy.orm import Session


class Student:
    def __init__(self, student: schema.Student, db: Session):
        self.student = models.Student(
            first_name=student.first_name,
            last_name=student.last_name,
            phone_number=student.phone_number,
            nationality=student.nationality,
            gender=student.gender,
        )
        self._db = db

    def create_student(self):
        self._db.add(self.student)
        self._db.commit()
        self._db.refresh(self.student)

    def modify_student(self):
        # self._db.get()