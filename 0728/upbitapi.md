# upbitapi

> access key : 비밀
>
> secret key : 비밀



Api를 이용하여 나의 지갑에 접근하여 정보를 얻어보자.

- [업비트 개발자 센터](https://docs.upbit.com/) 에 가서 access key, secret key를 받아보자!

```python
import os
import jwt
import uuid
import hashlib
import requests
from urllib.parse import urlencode
from pprint import pprint

#payload에 대한 구조
payload = {
    'access_key' : '<access key>',
    #nonce(난스) 는 임의로 생성되는 암호화 토큰으로 재생 공격을 방지하는 데 사용된다. 
    'nonce' : str(uuid.uuid4())
}

#jwt(json web token)
jwt_token = jwt.encode(payload, '<secret key>')
authorization_token = f'Bearer {jwt_token}'

headers = {'Authorization' : authorization_token}

res = requests.get('https://api.upbit.com/v1/accounts', headers = headers)
pprint(res.json())
```

결과 : 

```json
[{'avg_buy_price': '0',
  'avg_buy_price_modified': True,
  'balance': '0.03592412',
  'currency': 'KRW',
  'locked': '0.0',
  'unit_currency': 'KRW'},
 {'avg_buy_price': '799',
  'avg_buy_price_modified': False,
  'balance': '0.0',
  'currency': 'MANA',
  'locked': '1690.36633122',
  'unit_currency': 'KRW'},
 {'avg_buy_price': '40.6',
  'avg_buy_price_modified': False,
  'balance': '0.00000066',
  'currency': 'TRX',
  'locked': '0.0',
  'unit_currency': 'KRW'},
 {'avg_buy_price': '0',
  'avg_buy_price_modified': False,
  'balance': '0.00003025',
  'currency': 'APENFT',
  'locked': '0.0',
  'unit_currency': 'KRW'}]
```



