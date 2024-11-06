from typing import List, Optional
from fastapi import APIRouter

from src.data.culture import *
from src.logger import ServingLogger

router = APIRouter(prefix="/culture")

#공연목록
@router.post("/job")
def get_job(input:JobRequest) -> Optional[List[JobResponse]]:

    from src.api.culture import get_job as _get_job
    data = _get_job(input)
    return data if isinstance(data, list) else [data]