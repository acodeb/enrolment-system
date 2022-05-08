from fastapi import FastAPI, Depends
from app.db.connection import Base, engine, SessionLocal
from app.db import schema
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/student", response_model=schema.Student)
def post(student: schema.Student, db: Session = Depends(get_db)):
    pass
    # create(student, db)


@app.get("/student", response_model=schema.Student)
def get(db: Session = Depends(get_db)):
    pass
    # create(student, db)
