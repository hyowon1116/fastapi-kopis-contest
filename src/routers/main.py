import time
from typing import Union
from fastapi import APIRouter

from src.logger import ServingLogger


router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}