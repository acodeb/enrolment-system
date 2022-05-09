from typing import Optional
from sqlmodel import Field, SQLModel


class Student(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    first_name: str
    last_name: str
    phone_number: int
    nationality: str
    gender: str


class ClassModel(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    semester: int
