from fastapi import APIRouter
from app.routes import enroll, student, semester

router = APIRouter(prefix="/api/v1")
router.include_router(student.router)
router.include_router(enroll.router)
router.include_router(semester.router)
