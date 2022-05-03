import json
from secrets import token_urlsafe
import requests
import datetime
import os


#카카오 토큰을 저장할 파일명
KAKAO_TOKEN_FILENAME = "0427/res/kakao_message/kakao_token.json"

#저장하는 함수
def save_tokens(filename, tokens):
    with open(filename, "w") as fp:
        json.dump(tokens,fp)

#읽어오는 함수
def load_tokens(filename):
    with open(filename) as fp:
        tokens = json.load(fp)
    return tokens

# refresh_token으로 access_token 갱신하는 함수
def update_tokens(app_key, filename):
    tokens = load_tokens(filename)
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type" : "refresh_token",
        "client_id" : app_key,
        "refresh_token" : tokens['refresh_token']

    }
    response = requests.post(url, data=data)

# 요청 실패시,
    if response.status_code != 200:
        print("error! because", response.json())
        tokens = None
    else: #성공
        print(response.json())
        #기존 파일 백업
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = filename+"."+now
        os.rename(filename, backup_filename)
        #갱신된 토큰 저장
        tokens['access_token'] = response.json()['access_token']
        save_tokens(filename, tokens)
    return tokens

#토큰 저장

#토큰 업데이트 => 토큰 저장 필수
KAKAO_APP_KEY = "3b59fbff4131ee8172a082040b00265c"
# tokens = update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
load_tokens(KAKAO_TOKEN_FILENAME)
# save_tokens(KAKAO_TOKEN_FILENAME, tokens)