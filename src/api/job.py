from functools import lru_cache
import json
import requests
from requests_toolbelt import MultipartEncoder
import xmltodict

from src.config import get_settings
from src.data.job import *
from src.logger import ServingLogger

JOBSERVICEKEY = get_settings().JOBSERVICEKEY


def _request(final_url):
    request = requests.get(final_url)
    # 요청이 성공했는지 확인
    if request.status_code == 200:
        # ServingLogger().info(request.content)
        data = xmltodict.parse(request.content)
        try:
            result = data['response']['body']['items']
            return result['item'] if result else result
        except: 
            return []

    else:
        raise Exception(f"Error: {request.status_code}, {request.text}")
    
def get_job(input:JobRequest):
    URL = 'http://api.kcisa.kr/API_CIA_077/request'
    
    params = {
        "serviceKey": JOBSERVICEKEY  # API 인증키
        }
    if input.numOfRows:
        params['numOfRows'] = input.numOfRows
    if input.pageNo:
        params['pageNo'] = input.pageNo
    if input.keyword:
        params['keyword'] = input.keyword

    query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
    final_url = f'{URL}?{query_string}'
    print(final_url)

    return _request(final_url)