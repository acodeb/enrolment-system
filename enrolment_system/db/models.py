from pydantic import BaseModel


class Student(BaseModel):
    first_name: str
    last_name: str
    phone_number: int
    nationality: str
    gender: str

    class Config:
        orm_mode = True
