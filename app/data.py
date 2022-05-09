from db.models import ClassModel, Student
from sqlmodel import Session
from app.db.connection import engine, create_db_and_tables, drop_db


def create_data():
    with Session(engine) as session:
        student = Student(
            first_name="John",
            last_name="Doe",
            phone_number=1234567890,
            nationality="usa",
            gender="male",
        )
        session.add(student)
        student = Student(
            first_name="Jane",
            last_name="Doe",
            phone_number=1111111111,
            nationality="usa",
            gender="female",
        )
        session.add(student)

        session.add(ClassModel(name="math", semester=1))
        session.add(ClassModel(name="science", semester=2))
        session.add(ClassModel(name="english", semester=1))
        session.add(ClassModel(name="french", semester=2))
        session.commit()


if __name__ == "__main__":
    drop_db()
    create_db_and_tables()
    create_data()
