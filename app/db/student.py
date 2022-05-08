from . import get_db, Student
from app import schema
from sqlalchemy.orm import Session


def create(student: schema.Student, db: Session):
    db_user = Student(
        first_name=student.first_name,
        last_name=student.last_name,
        phone_number=student.phone_number,
        nationality=student.nationality,
        gender=student.gender,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
