from sqlmodel import create_engine, SQLModel

DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def drop_db():
    SQLModel.metadata.drop_all(engine)
