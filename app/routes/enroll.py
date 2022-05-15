from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query, Response
from sqlmodel import Session, select, or_
from sqlalchemy import func
from app.db.connection import engine
from app.db.models import Enroll, Semester, Student

router = APIRouter(prefix="/enroll")


@router.post("/student/{student_id}/semester/{semester_id}", status_code=201)
def post(student_id: int, semester_id: int, class_name: str, credits: int):
    with Session(engine) as session:
        student = session.exec(select(Student).where(Student.id == student_id)).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        semester = session.exec(
            select(Semester).where(Semester.id == semester_id)
        ).first()
        if not semester:
            raise HTTPException(status_code=404, detail="Semester not found")

        class_exists = session.exec(
            select(Enroll).where(
                Enroll.semester_id != semester_id, Enroll.class_name == class_name
            )
        ).first()
        if class_exists:
            raise HTTPException(
                status_code=400, detail="Class cannot exists in this semester"
            )

        enroll_exists = session.exec(
            select(Enroll).where(
                Enroll.student_id == student_id,
                Enroll.semester_id == semester_id,
                Enroll.class_name == class_name,
            )
        ).first()

        if enroll_exists:
            raise HTTPException(status_code=400, detail="Enrollment already exists")

        enroll = Enroll(
            student=student, semester=semester, class_name=class_name, credits=credits
        )
        session.add(enroll)
        session.commit()


@router.get("/student/{student_id}/semester/{semester_id}")
def get_classes(student_id: int, semester_id: int):
    with Session(engine) as session:
        enroll = session.exec(
            select(Enroll).where(
                Enroll.student_id == student_id, Enroll.semester_id == semester_id
            )
        ).all()
        return [e.class_name for e in enroll]


@router.get("/", response_model=List[Enroll])
def get_all():
    with Session(engine) as session:
        return session.exec(select(Enroll)).all()


@router.get("/semester/{semester_id}")
def get_students(semester_id: int):
    with Session(engine) as session:
        enroll = session.exec(
            select(Enroll).where(Enroll.semester_id == semester_id)
        ).all()
        return [
            {
                "student": f"{e.student.first_name} {e.student.last_name}",
                "class": e.class_name,
            }
            for e in enroll
        ]


@router.delete("/student/{student_id}")
def remove_student_from_class(student_id: int, class_name: str):
    with Session(engine) as session:
        student = session.exec(select(Student).where(Student.id == student_id)).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        enroll = session.exec(
            select(Enroll).where(
                Enroll.student_id == student_id, class_name == class_name
            )
        ).first()

        if not enroll:
            raise HTTPException(
                status_code=404, detail="Student is not enrolled to the class"
            )

        session.delete(enroll)
        session.commit()
        return Response(status_code=204)


@router.get("/semester/{name}/{year}")
def get_by_semester(
    name: str,
    year: int,
    name_start_char: Optional[str] = Query(
        default=None,
        description="Starting char to find in first_name or last_name",
        max_length=1,
    ),
    international_students: Optional[bool] = False,
    gender: Optional[str] = Query(default=None, enum=["male", "female"]),
):
    with Session(engine) as session:
        semester = session.exec(
            select(Semester).where(Semester.name == name, Semester.year == year)
        ).first()
        if not semester:
            raise HTTPException(status_code=404, detail="Semester not found")
        enroll = session.exec(
            select(func.sum(Enroll.credits), Enroll.student_id)
            .where(Enroll.semester_id == semester.id)
            .group_by(Enroll.student_id)
            .having(func.sum(Enroll.credits) < 10)
        ).all()

        student_ids = [e.student_id for e in enroll]

        stmt = (
            select(Enroll, Student)
            .where(Student.id.in_(student_ids))
            .where(Enroll.student_id == Student.id)
            .where(Enroll.semester_id == semester.id)
        )
        if name_start_char:
            stmt = stmt.where(
                or_(
                    Student.first_name.startswith(name_start_char),
                    Student.last_name.startswith(name_start_char),
                )
            )
        if international_students:
            stmt = stmt.where(Student.nationality != "usa")
        if gender:
            stmt = stmt.where(Student.gender == gender)

        students = session.exec(stmt).all()
        return students
