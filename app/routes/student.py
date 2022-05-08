from app.db import get_db
from app.db.student import create
from app.schema import Student
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


routes = APIRouter(prefix="/student")


@routes.post("/", response_model=Student)
def create_student(student: Student, db: Session = Depends(get_db)):
    create(student, db)
