from typing import List, Optional
from src.data.job import *
from fastapi import APIRouter

from src.data.kopis import *
from src.logger import ServingLogger

router = APIRouter(prefix="/job")

#공연목록
@router.post("/")
def get_job(input:JobRequest) -> Optional[List[JobResponse]]:

    from src.api.job import get_job as _get_job
    data = _get_job(input)
    return data if isinstance(data, list) else [data]
