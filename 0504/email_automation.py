import smtplib
from urllib import response
smtp_info = dict(
    {   
        'smtp_server' : 'smtp.naver.com',
        'smtp_user_id' : 'yuio7279@naver.com',
        'smtp_user_pw' : '!!t459283575',
        'smtp_port' : 587
    }
)

def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        # TLS 보안 연결
        server.starttls()
        #로그인
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])
        #로그인 된 서버에 이메일 전송
        response = server.sendmail(msg['from'], msg['to'], msg.as_string())
        #메시지를 보낼때는 결과는 {}
        if not response:
            print("이메일이 성공적으로 보내졌습니다.")
        else:
            print(response)

import os 
#이메일 메시지에 다양한 형식을 중첩하여 담기 위한 객체
from email.mime.multipart import MIMEMultipart

#이메일 메시지를 이진 데이터로 바꿔주는 인코더
from email import encoders

#텍스트형식
from email.mime.text import MIMEText

#이미지형식
from email.mime.image import MIMEImage

#오디오형식
from email.mime.audio import MIMEAudio

#위의 모든 객체를 생성할 수 있는 기본 객체
# MIMEBase(_maintype, _subtype)
# MIMEBase(<메인타입>,<서브타입>)
from email.mime.base import MIMEBase

msg_dict = {
    'text'  : {'maintype' : 'text', 'subtype':'plain','filename':'0504/res/email_sending/test.txt'}, #텍스트 첨부파일
    'image' : {'maintype' : 'image', 'subtype':'jpg','filename':'0504/res/email_sending/test.jpg'},
    'audio' : {'maintype' : 'audio', 'subtype':'mp3','filename':'0504/res/email_sending/test.mp3'},
    'video' : {'maintype' : 'video', 'subtype':'mp4','filename':'0504/res/email_sending/test.mp4'},
    'application':{'maintype' : 'application', 'subtype':'octect-stream','filename':'0504/res/email_sending/test.pdf'}
}

def make_multimsg(msg_dict):
    multi = MIMEMultipart(_subtype='mixed')

    for key, value in msg_dict.items():
        #각 타입에 적절한 MIMExxx() 함수를 호출하여 msg객체를 생성한다
        if key == 'text':
            with open(value['filename'], encoding='utf-8') as fp:
                msg = MIMEText(fp.read(), _subtype=value['subtype'])
        elif key == 'image':
            with open(value['filename'], encoding='utf-8') as fp:
                msg = MIMEImage(fp.read(), _subtype=value['subtype'])
        elif key == 'audio':
            with open(value['filename'], encoding='utf-8') as fp:
                msg = MIMEAudio(fp.read(), _subtype=value['subtype'])
        else:
            with open(value['filename'], 'rb') as fp:
                msg = MIMEBase(value['maintype'], _subtype=value['subtype'])
                msg.set_payload(fp.read())
                encoders.encode_base64(msg)
            #파일이름을 첨부파일 제목으로 추가
        msg.add_header('Content-Disposition','attachment',filename=os.path.basename(value['filename']))

            #첨부파일 추가
        multi.attach(msg)
    return multi


##구현하기

#메일내용 작성
title = '제목은 테스트로 하겠습니다.'
content = '메일 내용은 반갑습니다. 입니다.'
sender = smtp_info['smtp_user_id']
receiver = smtp_info['smtp_user_id']

#메일 객체 생성 : 한글 지원하는 utf-8로 합니다.
msg = MIMEText(_text = content, _charset = 'utf-8') #이메일 내용 content

msg['Subject'] = title #메일 제목
msg['From'] = sender 
msg['To'] = receiver

send_email(smtp_info,msg)

#첨부 파일이 있는 이메일 보내기


#첨부 파일 추가
multi = make_multimsg(msg_dict)
multi['Subject'] = title
multi['From'] = sender
multi['To'] = receiver
multi.attach(msg)

#첨부파일이 추가된 이메일 전송
send_email(smtp_info, multi)
