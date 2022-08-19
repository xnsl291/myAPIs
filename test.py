from open_APIs import naver
import pprint
import yaml
if __name__ == "__main__": 
    with open("keys.yaml","r",encoding = "utf-8") as f:
        naver_keys = yaml.load(f, Loader = yaml.Loader)
    c_id = naver_keys["c_id"]
    c_pw = naver_keys["c_pw"] 
    params={
        "query":"날씨"
    }  
    result = naver.search_api("cafearticle",c_id,c_pw,params)
    pprint.pprint(result)
    