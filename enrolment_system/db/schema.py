from enrolment_system.db.db import Base
from sqlalchemy import Column, Integer, String


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone_number = Column(Integer)
    nationality = Column(String)
    gender = Column(String)
