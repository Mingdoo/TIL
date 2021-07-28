# Today I learned



##### 1. nonce(난스), 랜덤 생성 토큰

- 난스(nonce)는 임의로 생성되는 암호화 토큰으로 재생 공격을 방지하는 데 사용됩니다.
- 난스(nonce)는 SOAP 메시지의 임의의 위치에 삽입할 수 있지만, 일반적으로 <UsernameToken> 요소에 삽입됩니다.

참고자료 : [https://ibm.com](https://www.ibm.com/docs/ko/was/9.0.5?topic=services-nonce-randomly-generated-token)



##### 2.  JWT(Json Web Token)

- JWT는 일반적으로 클라이언트와 서버, 서비스와 서비스 사이 통신 시 권한 인가(Authorization)를 위해 사용되는 토큰이다. URL

구조는 다음과 같다.

>
>
>HEADER.PAYLOAD.SIGNATURE
>
>

​	**Header**

- JWT를 검증하는데 필요한 정보를 가진 JSON 객체는 `Base64 URL-Safe` 인코딩된 문자열이다. 헤더(Header)는 JWT를 어떻게 검증(Verify)하는가에 대한 내용을 담고 있다. 참고로 alg는 서명 시 사용하는 알고리즘이고, kid는 서명 시 사용하는 키(Public/Private Key)를 식별하는 값이다.

```json
{
    "alg": "ES256",
    "kid": "Key ID",
}
```

- 즉, 위와 같은 JSON 객체를 문자열로 직렬화하고 UTF-8과 Base64 URL-Safe로 인코딩하면 다음과 같이 헤더를 생성할 수 있다.

```
Base64URLSafe(UTF-8('{"alg": "ES256","kid": "Key ID"}')) -> eyJhbGciOiJFUzI1NiIsImtpZCI6IktleSBJRCJ9
```

```python
#base64를 사용하는 이유는 bianry데이터를 텍스트 기반 규격으로 다룰 수 있기 때문.
#Base64 는 Binary 데이터를 아스키 코드 일부와 일대일로 매칭되는 문자열로 단순 치환되는 인코딩 방식이다.
import base64

#encode
str_input = '{"alg": "ES256","kid": "Key ID"}'
str_encoded = base64.urlsafe_b64encode(bytes(str_input, 'UTF-8')).decode("UTF-8")

print(str_encoded)
#=> eyJhbGciOiJFUzI1NiIsImtpZCI6IktleSBJRCJ9
```

```python
#decode
str_decoded = base64.urlsafe_b64decode(bytes(str_encoded, 'UTF-8')).decode("UTF-8")
print(str_decoded)
#=> {"alg": "ES256","kid": "Key ID"}
```

URL Safe Base64 encoding, decoding 출처 : [[Python] URL Safe Base64 Encoding](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wideeyed&logNo=222022018834)

​	**Payload**

- JWT의 내용이다. 페이로드(Payload)에 있는 속성들을 클레임 셋(Claim Set)이라 부른다. 클레임 셋은 JWT에 대한 내용(토큰 생성자(클라이언트)의 정보, 생성 일시 등)이나 클라이언트와 서버 간 주고 받기로 한 값들로 구성된다.

```json
{
    "iss": "minsoo.kang",
    "iat": "1586364342"
}
```

```python
str_input = '{"iss": "minsoo.kang","iat": "1586364342"}'
str_encoded = base64.urlsafe_b64encode(bytes(str_input, 'UTF-8')).decode('UTF-8')
print(str_encoded)

#=> eyJpc3MiOiAibWluc29vLmthbmciLCJpYXQiOiAiMTU4NjM2NDM0MiJ9
```

​	**Signature**

- 점(.)을 구분자로 해서 헤더와 페이로드를 합친 문자열을 서명한 값이다. 서명은 헤더의 alg에 정의된 알고리즘과 비밀 키를 이용해 성성하고 Base64 URL-Safe로 인코딩한다.

###### 완성된 형태의 JWT : 

```
eyJhbGciOiJFUzI1NiIsImtpZCI6IktleSBJRCJ9.eyJpYXQiOjE1ODYzNjQzMjcsImlzcyI6ImppbmhvLn
NoaW4ifQ.eyJhbGciOiJFUzI1NiIsImtpZCI6IktleSBJRC9.eyJpYXQiOjE1ODYzNjQzMjcsImlzcyI6Imp
pbmhvLnNoaW4ifQ.MEQCIBSOVBBsCeZ_8vHulOvspJVFU3GADhyCHyzMiBFVyS3qAiB7Tm_ME
Xi2kLusOBpanIrcs2NVq24uuVDgH71M_fIQGg
```

