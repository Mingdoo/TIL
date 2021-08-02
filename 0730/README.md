# 관통 프로젝트 \#2 (pjt02)



## 작성법

- 폴더와 파일명은 영문으로 작성한다.
- [Github-Flavoured Markdown](https://guides.github.com/features/mastering-markdown/) 으로 작성하며 파일 확장자명은 `.md`
- 짧고 간결하며 핵심적인 문장을 사용한다.
- 필요한 설명이 있으면 관련된 정보가 포함된 외부 링크를 사용 하자.

---



##### problem A. 영화 개수 카운트 기능 구현

- 조건 :
  - 제공되는 tmdb.py를 이용하여 영화 리스트 조회 URL을 생성합니다
  - requests 패키지를 이용하여 URL에 요청을 보냅니다.
- 결과 :
  - popular를 기준으로 받아온 데이터에서 영화 리스트의 개수를 계산합니다.
  - 계산한 정보를 반환하는 함수 popular_count를 완성합니다.



<u>**구현한 것**</u> : response로 받은 json형태의 데이터의 구조를 분석하여 원하는 값을 얻어냈다.

**<u>필요했던 점</u>** : json file의 데이터 타입을 확인하고, python에서 제공하는 key, value 값을 파악하여 key 값으로 value에 접근하는 것.

**<u>알고 있던 점</u>** : json 파일을 로드하면 dictionary 타입으로 사용할 수 있다는 것!

**<u>모르고 있던 점</u>** : 



##### problem B. 특정 조건에 맞는 영화 출력

- 조건 :
  - 제공되는 tmdb.py를 이용하여 영화 리스트 조회 URL을 생성합니다.
  - requests 패키지를 이용하여 URL에 요청을 보냅니다.
- 결과 :
  - 받아온 데이터에서 vote_average를 기준으로 점수가 8 이상인 영화들의 목록을 리스트로 반환하는 함수 vote_average_movies를 완성합니다.



<u>**구현한 것**</u> : response로 받은 json형태의 데이터의 구조를 분석하여 원하는 값을 얻어냈다.

**<u>필요했던 점</u>** : movie_id의 상태를 확인하여 None을 반환하는 트리거를 구현하는 것.

**<u>알고 있던 점</u>** : json 파일을 로드하면 dictionary 타입으로 사용할 수 있다는 것!

**<u>모르고 있던 점</u>** : 



##### problem C. 평점 순 정렬

- 조건 : 
  - 제공되는 tmdb.py를 이용하여 영화 제목을 기준으로 TMDB에서 사용하는 id를 검색합니다.
  - id를 기준으로 추천영화 목록 조회 URL을 생성합니다.
  - requests 패키지를 이용하여 URL에 요청을 보냅니다.
- 결과 : 
  - TMDB에서 추천받은 영화 리스트에서 제목을 리스트에 저장합니다.
  - 저장된 리스트를 반환하는 함수 recommendation을 완성합니다.
  - 올바르지 않은 영화 제목으로 id가 없는 경우 None을 반환합니다.
  - id값은 있지만 추천영화가 없는 경우 빈 리스트를 반환합니다.



<u>**구현한 것**</u> : response로 받은 json형태의 데이터의 구조를 분석하여 원하는 값을 얻어냈다.

**<u>필요했던 점</u>** : dictionary 타입을 key값을 기준으로 정렬하는 것

**<u>알고 있던 점</u>** : json 파일을 로드하면 dictionary 타입으로 사용할 수 있다는 것!

**<u>모르고 있던 점</u>** : 

```python
dict_sorted = sorted(response['results'], 
                     reverse=True, key=(lambda item: item['vote_average']))
#이와 같이 key = <function> 으로 대소비교를 하는것. reverse = True로 역순으로 뽑을 수 있다.
```



##### problem D. 제목 검색, 영화 추천

- 조건 :
  - 제공되는 tmdb.py를 이용하여 영화 제목을 기준으로 TMDB에서 사용하는 id를 검색합니다.
  - id를 기준으로 추천영화 목록 조회 URL을 생성합니다.
  - requests 패키지를 이용하여 URL에 요청을 보냅니다.
- 결과 : 
  - TMDB에서 추천받은 영화 리스트에서 제목을 리스트에 저장합니다.
  - 저장된 리스트를 반환하는 함수 recommendation을 완성합니다.
  - 올바르지 않은 영화 제목으로 id가 없는 경우 None을 반환합니다.
  - id값은 있지만 추천영화가 없는 경우 빈 리스트를 반환합니다.



<u>**구현한 것**</u> : movie_id에 따라 옳은 정보인지, 그렇지 않은지를 판별하는 것.

**<u>필요했던 점</u>** : movie_id 혹은 response를 확인하여 정보의 유효서을 판단하는 것.

**<u>알고 있던 점</u>** : json 파일을 로드하면 dictionary 타입으로 사용할 수 있다는 것!

**<u>모르고 있던 점</u>** : 



##### problem E. 배우, 제작진 리스트 출력

- 조건 : 
  - 제공되는 tmdb.py를 이용하여 영화 제목을 기준으로 TMDB에서 사용하는 id를 검색합니다.
  - id를 기준으로 배우와 제작진 목록 조회 URL을 생성합니다.
  - requests 패키지를 이용하여 URL에 요청을 보냅니다.
- 결과 :
  - cast_id 값이 10보다 작은 배우의 이름을 리스트에 저장합니다.
  - department 값이 Directing인 감독의 이름을 리스트에 저장합니다.
  - 반환되는 딕셔너리는 cast, crew 두개의 key를 가지고 각각 배우 리스트와 제작진 리스트를 value로 갖습니다.
  - 완성된 딕셔너리를 반환하는 함수 credits을 완성합니다. 



<u>**구현한 것**</u> : movie_id에 따라 옳은 정보인지, 그렇지 않은지를 판별하는 것.

**<u>필요했던 점</u>** : movie_id 혹은 response를 확인하여 정보의 유효서을 판단하는 것.

**<u>알고 있던 점</u>** : json 파일을 로드하면 dictionary 타입으로 사용할 수 있다는 것!

**<u>모르고 있던 점</u>** : 



##### problem F. 추가정보 수집

- 조건 :
  - 영화 데이터를 제공하는 다른 API를 사용하여 요청을 보내고 추가적인 정보를
    수집하는 함수를 완성합니다.

- 데이터 :
  - [KMDB](https://www.kmdb.or.kr/info/api/apiDetail/6)
  - [영진위](https://www.kobis.or.kr/kobisopenapi/homepg/main/main.do)
  - [네이버 영화검색 API](https://developers.naver.com/docs/search/movie/)

- 결과 :
  - 자유



```python
from pprint import pprint
import requests

def boxoffice(yyyymmdd):

    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    
    key = '471d01a31185dc4de8bb2a698a0003b1'
    date = str(yyyymmdd)
    
    url += '&key='+key
    url += '&targetDt='+date
    response = requests.get(url).json()

    my_list1 = []
    my_list2 = []
    for movie in response['boxOfficeResult']['dailyBoxOfficeList']:
        my_list1.append(movie['movieNm'])
        my_list2.append(movie['audiAcc'])
    
    print(my_list1)
    print(my_list2)
    my_dict = dict(zip(my_list1, my_list2))
    return my_dict

if __name__ == '__main__':
    pprint(boxoffice(20210729))
```

