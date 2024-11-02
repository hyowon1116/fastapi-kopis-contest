from typing import List, Optional
from fastapi import APIRouter

from src.data.kopis import *
from src.logger import ServingLogger

router = APIRouter(prefix="/kopis")

#공연목록
@router.post("/play")
def get_play(input:PlayRequest) -> Optional[List[PlayResponse]]:
    ServingLogger().info(input)

    from src.api.kopis import get_play as _get_play
    data = _get_play(input)
    return data if isinstance(data, list) else [data]

# 공연 상세
@router.post("/playDetail")
def get_play_detail(input:PlayDetailRequest) -> Optional[PlayDetailResponse]:
    from src.api.kopis import get_play_detail as _get_play_detail
    data = _get_play_detail(input)
    return data

# 공연 시설 목록
@router.post("/theatre")
def get_theatre(input: TheatreRequest) -> Optional[List[TheatreResponse]]:
    from src.api.kopis import get_theatre as _get_theatre

    data = _get_theatre(input)
    return data if isinstance(data, list) else [data]

# 공연 시설 상세
@router.post("/theatreDetail") 
def get_theatre_detail(input:TheatreDetailRequest)-> Optional[TheatreDetailResponse]:
    from src.api.kopis import get_theatre_detail as _get_theatre_detail

    data = _get_theatre_detail(input)
    return data

# 기획/제작사 목록
@router.post("/company")
def get_company(input: CompanyRequest) -> Optional[List[CompanyResponse]]:
    from src.api.kopis import get_company as _get_company

    data = _get_company(input)
    # return data
    return data if isinstance(data, list) else [data]


# 수상작 목록
@router.post("/award")
def get_award(input: KopisRequest) ->Optional[List[AwardResponse]]:
    from src.api.kopis import get_award as _get_award

    data = _get_award(input)
    return data if isinstance(data, list) else [data]

# 축제 목록
@router.post("/festival")
def get_festival(input: KopisRequest) -> Optional[List[FestivalResponse]]:
    from src.api.kopis import get_festival as _get_festival

    data = _get_festival(input)
    return data if isinstance(data, list) else [data]

# 극작가 목록
@router.post("/playwright")
def get_playwright(input: KopisRequest) ->Optional[List[PlaywrightResponse]]:
    from src.api.kopis import get_playwright as _get_playwright

    data = _get_playwright(input)
    return data if isinstance(data, list) else [data]


@router.post("/companyPlay")
def get_company_play(input:CompanyPlayRequest) -> Optional[List[CompanyPlayResponse]]:
    from src.api.kopis import get_company_play as _get_company_play

    data = _get_company_play(input)
    return data if isinstance(data, list) else [data]

@router.post("/theatreStat")
def get_theatre_stat(input:TheatreStatRequest) -> Optional[List[TheatreStatResponse]]:
    from src.api.kopis import get_theatre_stat as _get_theatre_stat
    data = _get_theatre_stat(input)
    return data if isinstance(data, list) else [data]
