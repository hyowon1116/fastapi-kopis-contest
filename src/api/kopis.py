from functools import lru_cache
import json
import requests
from requests_toolbelt import MultipartEncoder
import xmltodict

from src.config import get_settings
from src.data.kopis import *
from src.logger import ServingLogger

KOPISSERVICEKEY = get_settings().KOPISSERVICEKEY

def _request(final_url):
    request = requests.get(final_url)
    # 요청이 성공했는지 확인
    if request.status_code == 200:
        # ServingLogger().info(request.content)
        data = xmltodict.parse(request.content)
        try:
            result = data['dbs']
            return result['db'] if result else result
        except: 
            result = data['prfsts']
            return result['prfst'] if result else result

    else:
        raise Exception(f"Error: {request.status_code}, {request.text}")
    

def get_play(input:PlayRequest):
    URL = 'http://kopis.or.kr/openApi/restful/pblprfr'
    
    params = {
        "service": KOPISSERVICEKEY,  # API 인증키
        "stdate": input.stdate,            # 공연 시작일자
        "eddate": input.eddate,            # 공연 종료일자
        "cpage": input.cpage,              # 현재 페이지
        "rows": input.rows                 # 페이지당 목록 수
    }
    # 선택적으로 필터링 파라미터 추가
    if input.shprfnm:
        params['shprfnm'] = input.shprfnm
    if input.shprfnmfct:
        params['shprfnmfct'] = input.shprfnmfct
    if input.shcate:
        params['shcate'] = input.shcate
    if input.prfplccd:
        params['prfplccd'] = input.prfplccd
    if input.signgucode:
        params['signgucode'] = input.signgucode
    if input.signgucodesub:
        params['signgucodesub'] = input.signgucodesub
    if input.kidstate:
        params['kidstate'] = input.kidstate
    if input.prfstate:
        params['prfstate'] = input.prfstate
    if input.openrun:
        params['openrun'] = input.openrun
    if input.afterdate:
        params['afterdate'] = input.afterdate
    
    # URL에 쿼리 스트링을 추가
    query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
    final_url = f'{URL}?{query_string}'
    # ServingLogger().info(final_url)


    return _request(final_url)
    
def get_play_detail(input:PlayDetailRequest):
    URL = f'http://kopis.or.kr/openApi/restful/pblprfr/{input.mt20id}'

    params = {
    "service": KOPISSERVICEKEY,
    }
    
    query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
    final_url = f'{URL}?{query_string}'

    return _request(final_url)

def get_theatre(input:TheatreRequest):
    
    URL = 'http://kopis.or.kr/openApi/restful/prfplc'

    params = {
        "service": KOPISSERVICEKEY,
        "cpage": input.cpage,
        "rows": input.rows,
    }

    # 선택 항목을 조건부로 추가
    if input.shprfnmfct:
        params['shprfnmfct'] = input.shprfnmfct
    if input.fcltychartr:
        params['fcltychartr'] = input.fcltychartr
    if input.signgucode:
        params['signgucode'] = input.signgucode
    if input.signgucodesub:
        params['signgucodesub'] = input.signgucodesub
    if input.afterdate:
        params['afterdate'] = input.afterdate

    # URL에 쿼리 파라미터 추가
    query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
    final_url = f'{URL}?{query_string}'

    return _request(final_url)

def get_theatre_detail(input:TheatreDetailRequest):
    URL = f'http://kopis.or.kr/openApi/restful/prfplc/{input.mt10id}'

    params = {
        "service": KOPISSERVICEKEY,
    }

    # URL에 쿼리 파라미터 추가
    query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
    final_url = f'{URL}?{query_string}'
    print(final_url)

    return _request(final_url)


def get_company(input:CompanyRequest):
    URL = 'http://kopis.or.kr/openApi/restful/mnfct'

    params = {
        "service": KOPISSERVICEKEY,
        "cpage": input.cpage,
        "rows": input.rows,
    }

    # 선택 항목을 조건부로 추가
    if input.entrpsnm:
        params['entrpsnm'] = input.entrpsnm
    if input.shcate:
        params['shcate'] = input.shcate
    if input.afterdate:
        params['afterdate'] = input.afterdate

    # URL에 쿼리 파라미터 추가
    query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
    final_url = f'{URL}?{query_string}'

    return _request(final_url)

def get_award(input:KopisRequest):
    URL = 'http://kopis.or.kr/openApi/restful/prfawad'

    params = {
        "service": KOPISSERVICEKEY,
        "stdate": input.stdate,
        "eddate": input.eddate,
        "cpage": input.cpage,
        "rows": input.rows,
    }

    # 선택 항목을 조건부로 추가
    if input.shprfnm:
        params['shprfnm'] = input.shprfnm
    if input.shprfnmfct:
        params['shprfnmfct'] = input.shprfnmfct
    if input.shcate:
        params['shcate'] = input.shcate
    if input.prfplccd:
        params['prfplccd'] = input.prfplccd
    if input.signgucode:
        params['signgucode'] = input.signgucode
    if input.signgucodesub:
        params['signgucodesub'] = input.signgucodesub
    if input.kidstate:
        params['kidstate'] = input.kidstate
    if input.prfstate:
        params['prfstate'] = input.prfstate
    if input.afterdate:
        params['afterdate'] = input.afterdate

    # URL에 쿼리 파라미터 추가
    query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
    final_url = f'{URL}?{query_string}'

    return _request(final_url)

def get_festivals(input:KopisRequest):
    URL = 'http://kopis.or.kr/openApi/restful/prffest'

    params = {
        "service": KOPISSERVICEKEY,
        "stdate": input.stdate,
        "eddate": input.eddate,
        "cpage": input.cpage,
        "rows": input.rows,
    }

    # 선택 항목을 조건부로 추가
    if input.shprfnm:
        params['shprfnm'] = input.shprfnm
    if input.shprfnmfct:
        params['shprfnmfct'] = input.shprfnmfct
    if input.shcate:
        params['shcate'] = input.shcate
    if input.prfplccd:
        params['prfplccd'] = input.prfplccd
    if input.signgucode:
        params['signgucode'] = input.signgucode
    if input.signgucodesub:
        params['signgucodesub'] = input.signgucodesub
    if input.kidstate:
        params['kidstate'] = input.kidstate
    if input.prfstate:
        params['prfstate'] = input.prfstate
    if input.afterdate:
        params['afterdate'] = input.afterdate

    # URL에 쿼리 파라미터 추가
    query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
    final_url = f'{URL}?{query_string}'

    return _request(final_url)

def get_playwright(input:KopisRequest):
    URL = 'http://kopis.or.kr/openApi/restful/prfper'
    
    params = {
        "service": KOPISSERVICEKEY,
        "stdate": input.stdate,
        "eddate": input.eddate,
        "cpage": input.cpage,
        "rows": input.rows,
    }

    # 선택 항목을 조건부로 추가
    if input.shprfnm:
        params['shprfnm'] = input.shprfnm
    if input.shprfnmfct:
        params['shprfnmfct'] = input.shprfnmfct
    if input.shcate:
        params['shcate'] = input.shcate
    if input.prfplccd:
        params['prfplccd'] = input.prfplccd
    if input.signgucode:
        params['signgucode'] = input.signgucode
    if input.signgucodesub:
        params['signgucodesub'] = input.signgucodesub
    if input.kidstate:
        params['kidstate'] = input.kidstate
    if input.prfstate:
        params['prfstate'] = input.prfstate
    if input.afterdate:
        params['afterdate'] = input.afterdate
    # URL에 쿼리 스트링을 추가
    query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
    final_url = f'{URL}?{query_string}'
    
    return _request(final_url)

def get_company_play(input:CompanyPlayRequest):
    url = 'https://www.kopis.or.kr/por/db/mnfct/mnfctViewPrfList.json'
    m = MultipartEncoder(
            fields={
                "mt30Id": input.mt30Id,
                "pageRcdPer": "10"
            }    
        )
    
    # API get
    res = requests.post(url=url, headers={'Content-Type': m.content_type}, data=m)
    decoded = res.json()
    return decoded['resultList']

def get_theatre_stat(input: KopisRequest):
    # 기본 URL
    URL = 'http://kopis.or.kr/openApi/restful/prfstsPrfByFct'
    
    # 필수 매개변수 설정
    params = {
        "service": KOPISSERVICEKEY,
        "cpage": input.cpage,
        "rows": input.rows,
        "stdate": input.stdate,
        "eddate": input.eddate
    }
    
    # 선택 매개변수 추가 (필드가 None이 아닌 경우에만)
    if input.sharea:
        params['sharea'] = input.sharea
    if input.shprfnmfct:
        params['shprfnmfct'] = input.shprfnmfct
    
    # URL에 쿼리 파라미터 추가
    query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
    final_url = f'{URL}?{query_string}'

    # API 요청
    return _request(final_url) 