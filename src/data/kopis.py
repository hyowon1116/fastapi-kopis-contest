from typing import List, Optional, Union
from pydantic import BaseModel, HttpUrl


class PlayRequest(BaseModel):
    stdate: str  # 필수, 공연 시작일자
    eddate: str  # 필수, 공연 종료일자
    cpage: int  # 필수, 현재 페이지
    rows: int  # 필수, 페이지당 목록 수
    
    shprfnm: Union[str, None] = None  # 선택, 공연명
    shprfnmfct: Union[str, None] = None  # 선택, 공연시설명
    shcate: Union[str, None] = None  # 선택, 장르코드
    prfplccd: Union[str, None] = None  # 선택, 공연장코드
    signgucode: Union[str, None] = None  # 선택, 지역(시도)코드
    signgucodesub: Union[str, None] = None  # 선택, 지역(구군)코드
    kidstate: Union[str, None] = None  # 선택, 아동공연 여부
    prfstate: Union[str, None] = None  # 선택, 공연 상태코드
    openrun: Union[str, None] = None  # 선택, 오픈런 여부
    afterdate: Union[str, None] = None  # 선택, 해당일자 이후 등록/수정된 항목만 출력

class PlayResponse(BaseModel):
    mt20id: Optional[str] = None  # 공연ID
    prfnm: Optional[str] = None  # 공연명
    prfpdfrom: Optional[str] = None  # 공연 시작일 (형식: YYYY.MM.DD)
    prfpdto: Optional[str] = None  # 공연 종료일 (형식: YYYY.MM.DD)
    fcltynm: Optional[str] = None  # 공연시설명 (공연장명)
    poster: Optional[str] = None  # 포스터 이미지 경로 (URL)
    area: Optional[str] = None  # 공연 지역
    genrenm: Optional[str] = None  # 공연 장르명
    prfstate: Optional[str] = None  # 공연 상태
    openrun: Optional[str] = None  # 오픈런 여부 (Y/N)


class PlayDetailRequest(BaseModel):
    mt20id:str # 공연아이디

class _TicketClass(BaseModel):
    relatenm: Optional[str] = None
    relateurl : HttpUrl

class _relateClass(BaseModel):
    relate: Union[_TicketClass, List[_TicketClass]]

class _styurlClass(BaseModel):
    styurl : Union[HttpUrl, List[HttpUrl]]

class PlayDetailResponse(BaseModel):
    mt20id: Optional[str] = None
    prfnm: Optional[str] = None
    prfpdfrom: Optional[str] = None
    prfpdto: Optional[str] = None
    fcltynm: Optional[str] = None
    prfcast: Optional[str] = None
    prfcrew: Optional[str] = None
    prfruntime: Optional[str] = None
    prfage: Optional[str] = None
    entrpsnm: Optional[str] = None
    entrpsnmP: Optional[str] = None
    entrpsnmA: Optional[str] = None
    entrpsnmH: Optional[str] = None
    entrpsnmS: Optional[str] = None
    pcseguidance: Optional[str] = None
    poster: Optional[HttpUrl] = None
    sty: Optional[str] = None
    area: Optional[str] = None
    genrenm: Optional[str] = None
    openrun: Optional[str] = None
    visit: Optional[str] = None
    child: Optional[str] = None
    daehakro: Optional[str] = None
    festival: Optional[str] = None
    musicallicense: Optional[str] = None
    musicalcreate: Optional[str] = None
    updatedate: Optional[str] = None
    prfstate: Optional[str] = None
    styurls: Optional[_styurlClass] = None
    mt10id: Optional[str] = None
    dtguidance: Optional[str] = None
    relates: Optional[_relateClass] = None


class TheatreRequest(BaseModel):
    cpage: int  # 필수, 현재 페이지
    rows: int  # 필수, 페이지당 목록 수
    
    shprfnmfct: Union[str, None] = None  # 선택, 공연시설명
    fcltychartr: Union[str, None] = None  # 선택, 공연시설 특성 코드
    signgucode: Union[str, None] = None  # 선택, 지역(시도) 코드
    signgucodesub: Union[str, None] = None  # 선택, 지역(구군) 코드
    afterdate: Union[str, None] = None  # 선택, 해당일자 이후 등록/수정된 항목만 출력

class TheatreResponse(BaseModel):
    fcltynm: Optional[str] = None  # 공연시설명
    mt10id: Optional[str] = None   # 공연시설ID
    mt13cnt: Optional[int] = None  # 공연장 수
    fcltychartr: Optional[str] = None  # 시설특성
    sidonm: Optional[str] = None   # 지역(시도)
    gugunnm: Optional[str] = None  # 지역(구군)
    opende: Optional[int] = None   # 개관연도


class TheatreDetailRequest(BaseModel):
    mt10id: str # 공연시설id

class _SubFacility(BaseModel):
    prfplcnm: Optional[str]           # 공연장명
    mt13id: Optional[str]             # 공연장 ID
    seatscale: Optional[int]          # 좌석 수
    stageorchat: Optional[str]        # 무대/좌석 여부
    stagepracat: Optional[str]        # 무대/연습실 여부
    stagedresat: Optional[str]        # 무대/좌석 여부
    stageoutdrat: Optional[str]       # 무대/외부 여부
    disabledseatscale: Optional[int]  # 장애인 좌석 수 (선택적)
    stagearea: Optional[str]  # 무대 면적 (선택적)

class _mt13(BaseModel):
    mt13: Union[_SubFacility, List[_SubFacility]]

class TheatreDetailResponse(BaseModel):
    fcltynm: Optional[str] = None          # 공연시설명
    mt10id: Optional[str] = None           # 공연시설 ID
    mt13cnt: Optional[int] = None          # 공연장 수
    fcltychartr: Optional[str] = None      # 시설 특성
    opende: Optional[int] = None           # 개관 연도
    seatscale: Optional[int] = None        # 총 좌석 수
    telno: Optional[str] = None            # 전화번호
    relateurl: Optional[str] = None        # 관련 URL
    adres: Optional[str] = None            # 주소
    la: Optional[float] = None             # 위도
    lo: Optional[float] = None             # 경도
    restaurant: Optional[str] = None       # 음식점 여부
    cafe: Optional[str] = None             # 카페 여부
    store: Optional[str] = None            # 상점 여부
    nolibang: Optional[str] = None         # 노래방 여부
    suyu: Optional[str] = None             # 수유실 여부
    parkbarrier: Optional[str] = None      # 주차장 장애인 여부
    restbarrier: Optional[str] = None      # 화장실 장애인 여부
    runwbarrier: Optional[str] = None      # 경사로 장애인 여부
    elevbarrier: Optional[str] = None      # 엘리베이터 장애인 여부
    parkinglot: Optional[str] = None       # 주차장 여부
    mt13s: Optional[_mt13] = None    # 서브 시설 목록


class CompanyRequest(BaseModel):
    cpage: int  # 필수, 현재 페이지
    rows: int  # 필수, 페이지당 목록 수
    
    entrpsnm: Union[str, None] = None  # 선택, 기획/제작사 명
    shcate: Union[str, None] = None  # 선택, 장르 코드
    afterdate: Union[str, None] = None  # 선택, 해당일자 이후 등록/수정된 항목만 출력

class CompanyResponse(BaseModel):
    prfnm: Optional[str] = None            # 최신 작품
    entrpsnm: Optional[str] = None         # 기획/제작사명
    genrenm: Optional[str] = None          # 장르
    telno: Optional[str] = None            # 전화번호
    relateurl: Optional[str] = None        # 홈페이지
    mt30id: Optional[str] = None           # 기획/제작사 ID

class KopisRequest(BaseModel):
    stdate: str  # 필수, 공연 시작일자
    eddate: str  # 필수, 공연 종료일자
    cpage: int  # 필수, 현재 페이지
    rows: int  # 필수, 페이지당 목록 수
    
    shprfnm: Union[str, None] = None  # 선택, 공연명
    shprfnmfct: Union[str, None] = None  # 선택, 공연시설명
    shcate: Union[str, None] = None  # 선택, 장르 코드
    prfplccd: Union[str, None] = None  # 선택, 공연장 코드
    signgucode: Union[str, None] = None  # 선택, 지역(시도) 코드
    signgucodesub: Union[str, None] = None  # 선택, 지역(구군) 코드
    kidstate: Union[str, None] = None  # 선택, 아동공연 여부
    prfstate: Union[str, None] = None  # 선택, 공연 상태 코드
    afterdate: Union[str, None] = None  # 선택, 해당일자 이후 등록/수정된 항목만 출력

class AwardResponse(BaseModel):
    mt20id: Optional[str] = None             # 공연 ID
    prfnm: Optional[str] = None              # 공연명
    prfpdfrom: Optional[str] = None          # 공연 시작일
    prfpdto: Optional[str] = None            # 공연 종료일
    fcltynm: Optional[str] = None            # 공연 시설명 (공연장명)
    poster: Optional[HttpUrl] = None         # 포스터 이미지 경로
    genrenm: Optional[str] = None            # 공연 장르명
    prfstate: Optional[str] = None           # 공연 상태
    awards: Optional[str] = None             # 수상 실적

class FestivalResponse(BaseModel):
    mt20id: Optional[str] = None             # 공연 ID
    prfnm: Optional[str] = None              # 공연명
    prfpdfrom: Optional[str] = None          # 공연 시작일
    prfpdto: Optional[str] = None            # 공연 종료일
    fcltynm: Optional[str] = None            # 공연 시설명 (공연장명)
    poster: Optional[HttpUrl] = None         # 포스터 이미지 경로
    genrenm: Optional[str] = None            # 공연 장르명
    prfstate: Optional[str] = None           # 공연 상태
    festival: Optional[str] = None           # 축제 여부

class PlaywrightResponse(BaseModel):
    mt20id: Optional[str] = None             # 공연 ID
    prfnm: Optional[str] = None              # 공연명
    prfpdfrom: Optional[str] = None          # 공연 시작일
    prfpdto: Optional[str] = None            # 공연 종료일
    fcltynm: Optional[str] = None            # 공연 시설명 (공연장명)
    poster: Optional[HttpUrl] = None         # 포스터 이미지 경로
    genrenm: Optional[str] = None            # 공연 장르명
    prfstate: Optional[str] = None           # 공연 상태
    author: Optional[str] = None             # 원작자
    creator: Optional[str] = None            # 창작자

class CompanyPlayRequest(BaseModel):
    mt30Id: str

class CompanyPlayResponse(BaseModel):
    rnum: Optional[int] = None  # 순번
    mt20Id: Optional[str] = None  # 공연 ID
    prfNm: Optional[str] = None  # 공연명
    prfPdFrom: Optional[str] = None  # 공연 시작일
    prfPdTo: Optional[str] = None  # 공연 종료일
    prfPdTo2: Optional[str] = None  # 공연 종료일2 (기타 용도)
    genreCode: Optional[str] = None  # 장르 코드
    openRun: Optional[str] = None  # 오픈런 여부 (Y/N)
    genreNm: Optional[str] = None  # 장르명
    fcltyNm: Optional[str] = None  # 공연시설명
    prfplcNm: Optional[str] = None  # 공연장명
    seatScale: Optional[str] = None  # 좌석 규모
    entrpsNm: Optional[str] = None  # 기업명

class TheatreStatRequest(BaseModel):
    cpage: int  # 필수, 현재 페이지
    rows: int  # 필수, 페이지당 목록 수
    stdate: str  # 필수, 공연 시작일자 (YYYYMMDD 형식)
    eddate: str  # 필수, 공연 종료일자 (YYYYMMDD 형식)

    # 선택 변수들
    sharea: Union[str, None] = None  # 선택, 지역(시도) 코드
    shprfnmfct: Union[str, None] = None  # 선택, 공연시설명 (예: 예술의전당)

class TheatreStatResponse(BaseModel):
    prfnmfct: Optional[str] = None  # 공연시설명
    prfnmplc: Optional[str] = None  # 공연장명
    seatcnt: Optional[int] = None  # 좌석수
    prfcnt: Optional[int] = None  # 공연건수
    prfprocnt: Optional[int] = None  # 개막편수
    prfdtcnt: Optional[int] = None  # 상연횟수
    totnmrs: Optional[int] = None  # 총 티켓판매수