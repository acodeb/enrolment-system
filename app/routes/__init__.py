from fastapi import APIRouter
from app.routes import student, semester

router = APIRouter(prefix="/api/v1")
router.include_router(student.router)
router.include_router(semester.router)
