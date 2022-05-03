import requests

url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "3b59fbff4131ee8172a082040b00265c",
    "redirect_uri" : "https://localhost.com",
    "code" : "AUEyAu6-itB54BZVwhE9iLKdyt9cFCoBDq2L4z66xXXZxHkaxqTx7cRftv7hYeBaZiiCqgorDNIAAAGAaMACIA"
}

response = requests.post(url, data=data)

if response.status_code != 200:
    print("error becaus ", response.json())
else:
    tokens = response.json()
    print("성공")
    print(tokens)
