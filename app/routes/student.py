from app.db.models import Student
from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.db.connection import engine
from typing import List


router = APIRouter(prefix="/student")


@router.post("/", response_model=Student)
def post(student: Student):
    with Session(engine) as session:
        db_student = Student.from_orm(student)
        session.add(db_student)
        session.commit()
        session.refresh(db_student)
        return db_student


@router.get("/", response_model=List[Student])
def list():
    with Session(engine) as session:
        return session.exec(select(Student)).all()


@router.get("/{id}", response_model=Student)
def get(id: int):
    with Session(engine) as session:
        student = session.get(Student, id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student


@router.put("/", response_model=Student)
def update(student: Student):
    with Session(engine) as session:
        db_student = session.get(Student, student.id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        db_student.first_name = student.first_name
        db_student.last_name = student.last_name
        db_student.phone_number = student.phone_number
        db_student.nationality = student.nationality
        db_student.gender = student.gender
        session.add(db_student)
        session.commit()
        session.refresh(db_student)
        return db_student
