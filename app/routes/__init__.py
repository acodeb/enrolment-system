from fastapi import APIRouter
from . import student


routes = APIRouter(prefix="/api/v1")
routes.include_router(student.routes)
