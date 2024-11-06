from typing import List, Optional, Union
from pydantic import BaseModel, HttpUrl


class JobRequest(BaseModel):
    numOfRows: Optional[str]  # 필수, 공연 시작일자
    pageNo: Optional[str]  # 필수, 공연 종료일자
    keyword: Optional[str]  # 필수, 현재 페이지

class JobResponse(BaseModel):
    title: Optional[str]
    description:Optional[str]
    subDescription:Optional[str]
    url:Optional[str]
    localId:Optional[str]
    issuedDate:Optional[str]
    createdDate:Optional[str]
    agent:Optional[str]
    temporalCoverage:Optional[str]
    period:Optional[str]