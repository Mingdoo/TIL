# WebSocket

- 웹 소켓 개요
- http 프로토콜과의 차이
- 동작원리
  - 웹소켓 핸드쉐이크
  - 특징
- ws/wss, http/https



참고자료

https://ko.javascript.info/websocket

https://datatracker.ietf.org/doc/html/rfc6455#section-4.1

## 웹 소켓 개요

- 소켓 통신은 Server와 Client가 특정 포트를 통해 연결을 유지하고 있는 양방향 통신입니다.
- 기존 Http 통신과 달리, 서버는 양방향 통신을 유지하기 때문에 Ajax와 같이 사용자가 요청을 보낼 때만 응답을 보내지 않고, 서버가 먼저 데이터를 전송할 수 있습니다.



## http 프로토콜과의 차이

![image](https://user-images.githubusercontent.com/57826388/95358518-1ca49780-0904-11eb-9386-e4ecb76381d6.png)

### **Http 통신의특징**

- Client가 요청을 보내는 경우에만 Server가 응답하는 단방향 통신
- Server로부터 응답을 받은 후에는 연결이 바로 종료
- 실시간 연결이 아니고, 필요한 경우에만 Server로 요청을 보내는 상황에 유리



### **Socket 통신의특징**

- Server와 Client가 계속 연결을 유지하는 양방향 통신
- Server와 Client가 실시간으로 데이터를 주고받는 상황이 필요한 경우에 사용



## 동작원리

- 핸드쉐이크

웹 소켓은 http로 handshake를 한 후 ws로 프로토콜을 변환합니다.

간단한 그림으로 표현하면 다음과 같습니다.

![img](https://media.vlpt.us/images/pbg0205/post/ee268b65-79f0-4405-abcf-b939667b6116/%EC%9B%B9%20%EC%86%8C%EC%BC%93%20%EA%B0%84%EB%8B%A8%20%EC%A0%95%EB%A6%AC.PNG)

이 때, 브라우저가 웹 서버에 http(get) 요청을 보낼 때, 특별한 규칙이 있습니다.

```http
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Origin: http://example.com
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
```

이는 Client가 핸드쉐이크 처음 보내는 request입니다. 여기서, Upgrade : websocket은 프로토콜을 websocket으로 바꾸겠다는 선언과 같습니다. [RFC 6455](https://datatracker.ietf.org/doc/html/rfc6455#section-4.1)에 따르면 필수 규칙은 다음과 같습니다.

>
>
>The request MUST contain a |**Host**| header field whose value
>        contains /host/ plus optionally ":" followed by /port/ (when not
>        using the default port).
>
>The request MUST contain an |**Upgrade**| header field whose value
>        MUST include the "websocket" keyword.
>
>The request MUST contain a |**Connection**| header field whose value
>        MUST include the "Upgrade" token.
>
>The request MUST include a header field with the name
>        |**Sec-WebSocket-Key**|.  The value of this header field MUST be a
>        nonce consisting of a randomly selected 16-byte value that has
>        been base64-encoded (see Section 4 of [RFC4648]).  The nonce
>        MUST be selected randomly for each connection.
>
>NOTE: As an example, if the randomly selected value was the
>sequence of bytes 0x01 0x02 0x03 0x04 0x05 0x06 0x07 0x08 0x09
>0x0a 0x0b 0x0c 0x0d 0x0e 0x0f 0x10, the value of the header
>field would be "AQIDBAUGBwgJCgsMDQ4PEC=="
>
>The request MUST include a header field with the name |**Origin**|
>        [RFC6454] if the request is coming from a browser client.  If
>        the connection is from a non-browser client, the request MAY
>        include this header field if the semantics of that client match
>        the use-case described here for browser clients.  The value of
>        this header field is the ASCII serialization of origin of the
>        context in which the code establishing the connection is
>        running.  See [RFC6454] for the details of how this header field
>        value is constructed.
>
>The request MUST include a header field with the name
>        |**Sec-WebSocket-Version**|.  The value of this header field MUST be
>        13.

여기서, `Sec-WebSocket-Key`는 각 연결마다 랜덤으로 생성된 16바이트 숫자의 base64 변환형태로 전송되어야 합니다. 또한, `Sec-WebSocket-Version`은 명시적으로 13으로 헤더에 포함되어야 합니다.

이를 받은 서버는

```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

와 같이 response를 보내며 핸드쉐이크를 완성하고 나면 `protocol switching` 과정이 진행됩니다. (response 101)

이 때, `Sec-WebSocket-Accept`부분은 사용자가 보낸 key와 magic string을 합쳐 sha1 해싱을 거쳐 base64로 인코딩 되어 전달되어야 합니다.



이를 통해 웹소켓 연결이 완성된 이후, 클라이언트와 서버는 `메시지`의 개념으로 데이터를 주고받는데, 이 메시지는 프레임으로 구성되어 있습니다. (프레임은 utf-8의 텍스트, 바이너리 데이터 등으로 이루어집니다.)



- 특징

최초 접속에서만 http 프로토콜을 통해 핸드쉐이킹을 하기 때문에 http 헤더를 사용합니다.

웹 소켓을 위한 별도의 포트는 없고, 기존 포트를 사용합니다(http-80, https-443).

메시지에 포함되는 내용은 텍스트와 바이너리입니다.

Html5 이전 기술에는 적용이 어렵습니다.



## ws/wss, http/https

핸드쉐이킹을 통해 ws(websocket) 혹은 wss(websocket secure)라는 소켓이 생성되고 이를 통해 통신을 하게 됩니다.

두 소켓은 http와 https의 관계와 유사합니다.

ws는 WebSocket 클라이언트 라이브러리에 http를 사용하여 WebSocket 서버에 연결하도록 지시합니다. 마찬가지로 wss는 WebSocket 클라이언트 라이브러리에 https를 사용하여 WebSocket 서버에 연결하도록 지시합니다.



> 메인 웹페이지 자체가 https라면 모든 api 요청, 이미지 로딩, 웹소켓 등에도 동일하게 SSL이 적용되어야 합니다. 웹소켓은 wss, 다른 모든 요청은 https가 되겠지요.
>
>  
>
> https를 사용하는 이유가 세션 쿠키나 api 토큰 등 민감한 정보가 노출되지 않도록 하기 위해서인데, http를 사용하는 api 요청이나 웹소켓이 단 한 개라도 있다면 거기에 접속할 때 세션 쿠키나 토큰이 노출될 테니 https를 쓰는 의미가 없어집니다. 그래서 최근 브라우저들은 mix content 발생시 이미지 외에는 아예 접속 시도조차 하지 않습니다. (원칙적으로는 이미지도 로딩하면 안되지만, 다 깨져보인다고 사용자들이 너무 싫어해서 타협한 것 같습니다.)
>
> https://xetown.com/questions/780401

