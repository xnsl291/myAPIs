# open API packaging

아래 사이트의 각 open API들을 함수로 구현해서 패키징하기 
- [Naver Developers](https://developers.naver.com/)

    1. search_api (검색API)
        - params(요청변수): 
            - query (string - 필수) : 검색 문자열
        - code(코드 리스트) 
            - 블로그 : blog
            - 뉴스 : news
            - 책: book
            - 백과사전 : encyc
            - 영화: movie
            - 카페글 :cafearticle
            - 오타변환 : errata
            - [API_Reference](https://developers.naver.com/docs/serviceapi/search/blog/blog.md#%EB%B8%94%EB%A1%9C%EA%B7%B8)


    2. translate_api (번역API)
        - text - 번역하고자 하는 문자열(필수)
        - client_id, client_secret - 인증키 (필수)
        - source - 원본언어 (default : ko) 
        - target - 목적언어 (default : en)
        - 언어코드
        
            [ ko:한국어/ en:영어/ ja:일본어/ zh-CN:중국어/ vi:베트남어/ id:인도네시아어/ de:독일어/ es:스페인어/ it:이탈리아어 / fr:프랑스어 ]
        - [API_Reference](https://developers.naver.com/docs/papago/papago-nmt-api-reference.md)

            
        