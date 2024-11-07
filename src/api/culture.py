from functools import lru_cache
import json
import requests
from requests_toolbelt import MultipartEncoder
import xmltodict

from src.config import get_settings
from src.data.culture import *
from src.logger import ServingLogger

def _request(final_url):
    request = requests.get(final_url)
    # 요청이 성공했는지 확인
    if request.status_code == 200:
        # ServingLogger().info(request.content)
        data = xmltodict.parse(request.content)
        try:
            result = data['response']['body']
            return result
        except: 
            return []

    else:
        raise Exception(f"Error: {request.status_code}, {request.text}")
    
def get_job(input:JobRequest):
    URL = 'http://api.kcisa.kr/API_CIA_077/request'
    
    params = {
        "serviceKey": get_settings().CULTURESERVICEKEY  # API 인증키
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

def get_event(input:EventRequest):
    URL = 'http://api.kcisa.kr/openapi/service/rest/meta2020/getGKMAcontest'
    
    params = {
        "serviceKey": get_settings().CULTUREEVENTSERVICEKEY  # API 인증키
        }
    if input.numOfRows:
        params['numOfRows'] = input.numOfRows
    if input.pageNo:
        params['pageNo'] = input.pageNo

    query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
    final_url = f'{URL}?{query_string}'

    return _request(final_url)