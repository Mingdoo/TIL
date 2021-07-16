## telegram api를 사용한 chatbot만들기

```
1845780691:AAEAg8gHFDOCPHO3UHwmEyGpdcoLb1AFz5c : My key value
```

> getUpdates
>
> sendMessage

https://api.telegram.org/bot1845780691:AAEAg8gHFDOCPHO3UHwmEyGpdcoLb1AFz5c/getMe

https://web.telegram.org/z/

###### my chat ID : `1826989968`

> Key, Value값의 구분은 `=` , 다음 문장과의 구분은 `&` 으로 한다.

```python
# example)

url ='https://api.telegram.org/bot1845780691:AAEAg8gHFDOCPHO3UHwmEyGpdcoLb1AFz5c/sendMessage?' # 여기까지 url 
text=%ED%95%98%EC%9D%B4%EB%9D%BC%EA%B3%A0%20%E3%85%8B%E3%85%8B
&
chat_id=1826989968
```

> 헤더는 데이터를 위한 데이터, 메타 데이터를 안에 갖고있다.

### [ungAeeeeeeee.pythonanywhere.com](http://ungaeeeeeeee.pythonanywhere.com/)

#### 파이썬 언어는 스크립트 코드라고 한다!

> 파이썬은 c언어로 번역되어 실행된다 (line by line)



### Flask

```python
#이건 그냥 박아놓고 시작하기
from flask import Flask
app = Flask(__name__)

```

##### 이것저것 바꾸기가 힘드니까 (유동아이피 , 포트 열기 , 등등)

- 해결 : `ngrok` 을 사용하자.

```bash
./ngrok http <port> 
```



```python
import random
numbers = range(1,46)
lucky = random.sample(numbers, 6) #sample은 numbers에서 6개를 뽑아낸다.
```



```python
from flask import Flask, request
from bs4 import BeautifulSoup
import requests
import random

TOKEN = '1845780691:AAEAg8gHFDOCPHO3UHwmEyGpdcoLb1AFz5c'
APP_URL = f'https://api.telegram.org/bot{TOKEN}/'
sendMessage_url = f'{APP_URL}sendMessage'

app = Flask(__name__)

def pm():
    DATA_URL = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=zfbiuGS26UEPZjeXhIgzs7dwdZ5YO%2BeV6BUE4cF3aaOL83zuyxxzUH%2BGzL36VDB4DyfB8T0kjiL5hP2lWJvJGw%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=서울&ver=1.0'
    response_air = requests.get(DATA_URL)
    data_air = response_air.json()
    items = data_air['response']['body']['items']
    for item in items:
        if item['stationName']=='강남구':
            pm10_data = item['pm10Value']
            message = f'{item["stationName"]}의 미세먼지는 {pm10_data}입니다.'
    return message
def lotto():
    numbers = range(1,46)
    lucky = random.sample(numbers, 6)
    sorted_lucky = sorted(lucky)
    return sorted_lucky
def kospi():
    url = "https://finance.naver.com/sise/"

    #request(요청) 해서 get(얻어)
    res = requests.get(url)

    #사람이 보기에 예쁘진 않지만 python이 보기엔 예쁘다
    data = BeautifulSoup(res.text, 'html.parser') 
    kospi = data.select_one('#KOSPI_now')
    message = f"현재 코스피 지수는 {kospi.text} 입니다."

    return message
def AI():

    url = "https://www.bloter.net/newsSearch?keyword=AI"
    bloter_url = 'https://bloter.net'

    res = requests.get(url)

    
    data = BeautifulSoup(res.text, 'html.parser')
    selector1 = '#container > div > div:nth-child(1) > div.box.newslist_left > ul > li:nth-child(1)'
    selector2 = '#container > div > div:nth-child(1) > div.box.newslist_left > ul > li:nth-child(2)'
    selector3 = '#container > div > div:nth-child(1) > div.box.newslist_left > ul > li:nth-child(3)'

    news = []
    new1 = data.select_one(selector1)
    new2 = data.select_one(selector2)
    new3 = data.select_one(selector3)
    news.append(new1)
    news.append(new2)
    news.append(new3)
    return news
def drama():
    Drama_url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blUw&qvt=0&query=%EC%A3%BC%EA%B0%84%EB%93%9C%EB%9D%BC%EB%A7%88%20%EC%BC%80%EC%9D%B4%EB%B8%94%EC%8B%9C%EC%B2%AD%EB%A5%A0"

    res = requests.get(Drama_url)
    data = BeautifulSoup(res.text, 'html.parser')
    selector1 = '#main_pack > div.content_search.section > div > div.contents03_sub > div > div.rating_cnt > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > p > a'
    selector2 = '#main_pack > div.content_search.section > div > div.contents03_sub > div > div.rating_cnt > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > p > a'
    selector3 = '#main_pack > div.content_search.section > div > div.contents03_sub > div > div.rating_cnt > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > p > a'
    popular_selector1 = '#main_pack > div.content_search.section > div > div.contents03_sub > div > div.rating_cnt > div > table > tbody > tr:nth-child(1) > td.ct.scroll_p > p'
    popular_selector2 = '#main_pack > div.content_search.section > div > div.contents03_sub > div > div.rating_cnt > div > table > tbody > tr:nth-child(2) > td.ct.scroll_p > p'
    popular_selector3 = '#main_pack > div.content_search.section > div > div.contents03_sub > div > div.rating_cnt > div > table > tbody > tr:nth-child(3) > td.ct.scroll_p > p'
    
    
    
    drama1 = data.select_one(selector1)
    popular1 = data.select_one(popular_selector1)
    drama2 = data.select_one(selector2)
    popular2 = data.select_one(popular_selector2)
    drama3 = data.select_one(selector3)
    popular3 = data.select_one(popular_selector3)
    drama = []
    popular = []
    drama.append(drama1)
    drama.append(drama2)
    drama.append(drama3)

    popular.append(popular1)
    popular.append(popular2)
    popular.append(popular3)

    return (drama, popular)

@app.route("/", methods = ['POST']) #조건
def telegram(): #실행
    
    response = request.get_json()
    
    #누가 챗을 보냈는지?
    chat_id = response['message']['from']['id']

    #명령어?
    text = response['message']['text']

    
    print(chat_id, text)
    if text == '/start' or 'help' in text or '/?' in text:
        message = '"미세먼지", "로또", "코스피", "AI", "드라마"의 명령어를 입력해보세요!'
        send_url = f'{sendMessage_url}?chat_id={chat_id}&text={message}'
        requests.get(send_url)
        return 'test', 200
    # 메세지를 사용자에게 보내기
    ## 미세먼지
    elif '미세' in text:
        message = pm()

    ## 로또
    elif '로또' in text:
        for i in range(1,7):
            sorted = lotto()
            message = f'♥{i}번째 숫자 : {sorted[i-1]}♥'
            send_url = f'{sendMessage_url}?chat_id={chat_id}&text={message}'
            requests.get(send_url)
        message = "♥행운을 빕니다♥"
        send_url = f'{sendMessage_url}?chat_id={chat_id}&text={message}'
        requests.get(send_url)
        return 'test', 200
    
    ## 코스피
    elif '코스피' in text:
        message = kospi()
    
    ## 뉴스
    elif ('AI' in text ) or ( '뉴스' in text):
        news = AI()
        for new in news:
            message = f'{new.text}'
            send_url = f'{sendMessage_url}?chat_id={chat_id}&text={message}'
            requests.get(send_url)
        return 'test', 200
    
    ## 드라마
    elif '드라마' in text:
        Drama, Popular = drama()
        for i in range(3):
            message = f'{i+1}위 드라마 : {Drama[i].text}, {Popular[i].text}'
            send_url = f'{sendMessage_url}?chat_id={chat_id}&text={message}'
            requests.get(send_url)
        return 'test', 200
    else:
        message = '그건 무슨말이에요?'

    

    send_url = f'{sendMessage_url}?chat_id={chat_id}&text={message}'
    requests.get(send_url)
    return 'test', 200
    


```

###### web Hooking

```python
TOKEN = '1845780691:AAEAg8gHFDOCPHO3UHwmEyGpdcoLb1AFz5c'
SERVER_URL = 'https://3c30844808de.ngrok.io/'
WEBHOOK_URL = f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={SERVER_URL}'

print(WEBHOOK_URL)
```

