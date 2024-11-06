from typing import List, Optional, Union
from pydantic import BaseModel, HttpUrl


class JobRequest(BaseModel):
    numOfRows: Optional[int]=10  # 필수, 공연 시작일자
    pageNo: Optional[int]=1  # 필수, 공연 종료일자
    keyword: Optional[str]=None  # 필수, 현재 페이지

class JobResponse(BaseModel):
    title: Optional[str]=None
    description:Optional[str]=None
    subDescription:Optional[str]=None
    url:Optional[str]=None
    localId:Optional[str]=None
    issuedDate:Optional[str]=None
    createdDate:Optional[str]=None
    agent:Optional[str]=None
    temporalCoverage:Optional[str]=None
    period:Optional[str]=None