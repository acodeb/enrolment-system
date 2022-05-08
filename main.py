from fastapi import FastAPI
from enrolment_system.db.db import SessionLocal, Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# docker run --name my-db -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
