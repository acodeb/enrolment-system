from app.db.models import Semester
from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.db.connection import engine
from typing import List


router = APIRouter(prefix="/semester")


@router.post("/", response_model=Semester)
def post(semester: Semester):
    with Session(engine) as session:
        sem = session.exec(
            select(Semester).where(
                Semester.name == semester.name, Semester.year == semester.year
            )
        ).all()
        if sem:
            raise HTTPException(400, detail="Semester already exists")

        db_semester = Semester.from_orm(semester)
        session.add(db_semester)
        session.commit()
        session.refresh(db_semester)
        return db_semester


@router.get("/", response_model=List[Semester])
def list():
    with Session(engine) as session:
        return session.exec(select(Semester)).all()


@router.get("/{id}", response_model=Semester)
def get(id: int):
    with Session(engine) as session:
        semester = session.get(Semester, id)
        if not semester:
            raise HTTPException(status_code=404, detail="Semester not found")
        return semester
