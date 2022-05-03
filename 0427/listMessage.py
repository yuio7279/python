import saveToken as st
import json
import requests

#저장된 토큰 정보를 읽어옴
tokens = st.load_tokens(st.KAKAO_TOKEN_FILENAME)

#텍스트 메시지 url
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

#request parameter 설정
headers = {
    "Authorization" : "Bearer " + tokens['access_token']
}

template = {
    "object_type" : "list",
    "header_title" : "초반 사진",
    "header_link" : 
    {
        "web_url" : "www.naver.com",
        "mobile_web_url" : "www.naver.com"
    },
    "contents" : 
    [
        {
            "title" : "1. 광어초밥",
            "description" : "광어는 맛있다",
            "image_url" : "https://search1.kakaocdn.net/argon/0x200_85_hr/8x5qcdbcQwi",
            "image_width" : 50, "image_height" : 50,
            "link" : 
            {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        },
        {
            "title" : "2. 참치초밥",
            "description" : "참치는 맛있다",
            "image_url" : "https://search2.kakaocdn.net/argon/0x200_85_hr/IjIToH1S7J1",
            "image_width" : 50, "image_height" : 50,
            "link" : 
            {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }
    ],
    "buttons" : 
    [
        {
            "title" : "웹으로 이동",
            "link" : 
            {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }
    ]
}
data = {
    "template_object" : json.dumps(template)
}

res = requests.post(url, data=data, headers=headers)
print(res.status_code)

#실패한다면
if res.status_code != 200:
    print("error because ",res.json())
else: #성공한다면
    print("메시지를 성공적으로 보냈습니다.")