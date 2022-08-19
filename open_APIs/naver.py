import requests
def search_api(code,client_id,client_secret,params):
    headers = {
        "X-Naver-Client-Id" : client_id,
        "X-Naver-Client-Secret" : client_secret
    }
    url = f"https://openapi.naver.com/v1/search/{code}.json"
    res = requests.get(url,params=params,headers=headers)
    result = res.json()
    if res.status_code != 200:
        print(result)
        result = None
    return result

def translate_api(text,client_id,client_secret,source="ko",target="en",url = "https://openapi.naver.com/v1/papago/n2mt" ):
    headers =  {
    "X-Naver-Client-Id" : client_id,
    "X-Naver-Client-Secret" : client_secret
    }
    data = {
        "source": source, # 원본언어 코드
        "target": target, # 목적언어 코드
        "text" : text # 번역할 텍스트
    }
    res = requests.post(url,headers=headers,data=data)
    result = res.json()
    if res.status_code == 200:
        result = result["message"]["result"]["translatedText"]
    return result

