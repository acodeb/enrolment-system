import enum
from optparse import Option
from typing import List, Optional
from sqlmodel import Column, Enum, Field, SQLModel, Relationship


class SemesterNameEnum(str, enum.Enum):
    fall = "fall"
    spring = "spring"


class GenderEnum(str, enum.Enum):
    male = "male"
    female = "female"


class Enroll(SQLModel, table=True):
    student_id: Optional[int] = Field(
        default=None, foreign_key="student.id", primary_key=True
    )
    semester_id: Optional[int] = Field(
        default=None, foreign_key="semester.id", primary_key=True
    )
    class_name: Optional[str] = Field(default=None, primary_key=True)
    credits: int

    student: "Student" = Relationship(
        back_populates="enroll",
    )
    semester: "Semester" = Relationship(
        back_populates="enroll",
    )


class Semester(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: SemesterNameEnum = Field(sa_column=Column(Enum(SemesterNameEnum)))
    year: int

    enroll: List[Enroll] = Relationship(
        back_populates="semester",
    )


class Student(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    first_name: str
    last_name: str
    phone_number: int
    nationality: str
    gender: GenderEnum = Field(sa_column=Column(Enum(GenderEnum)))

    enroll: List[Enroll] = Relationship(
        back_populates="student",
    )
