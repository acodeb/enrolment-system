from fastapi import FastAPI
from app.db.connection import create_db_and_tables
from app.routes import router

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
