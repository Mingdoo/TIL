# cs(네트워크)

##### 0. 3-way handshaking

양쪽 모두 데이터를 전송할 준비가 되었다는 것을 보장하고, 실제로 데이터 전달이 시작하기 전에 한쪽이 다른쪽이 준비되었다는 것을 알 수 있도록 하는 과정.

##### 1. tcp(transmission control protocol)

인터넷 상에서 데이터를 메세지의 형태로 보내기 위해 ip와 함께 사용하는 프로토콜(연결 지향 프로토콜)

특징

- 연결형 서비스(논리적으로 연결을 확립하고, 패킷의 순서가 뒤바뀔 위험이 적으나, 문제가 생기면 재전송을 하는 방법)로 가상 회선 방식을 제공한다.

- IP가 실제로 데이터의 배달처리를 관장하는 동안, TCP는 데이터 패킷을 추적 관리.

- http가 tcp기반 서비스이다.

##### 2. udp(user datagram protocol)

데이터를 데이터그램 단위로 처리하는 프로토콜

- 비연결형
- 신뢰성 낮음
- dns가 udp기반 서비스이다.



### http의 문제점

- http는 평문 통신이기 때문에 도청이 가능하다.
- 통신 상대를 확인하지 않기 때문에 위장 가능
- 변조 가능

### tcp/ip는 도청 가능한 네트워크이다.

- 그래서 SSL로 http를 감싸서 데이터를 암호화하여 전송한다.



### 로드 밸런싱(Load Balancing)

> 둘 이상의 CPU or 저장장치와 같은 컴퓨터 자원들에게 작업을 나누는 것

웹 사이트에 접속하는 인원이 급격하게 늘어나게 되어 서버를 여러대로 나눠서 일하도록 하는 것(scale-out). 이때, 여러 서버에 균등하게 트래픽을 분산하는 것이 로드밸런싱. 로드 밸런싱은 분산식 웹 서비스로, 여러 서버에 부하를 나눠주는 역할을 한다. 로드밸런서를 클라이언트와 서버 사이에 두고, 부하가 일어나지 않도록 여러 서버에 분산시켜주는 방식이다. 서비스를 운영하는 사이트의 규모에 따라 웹 서버를 추가로 증설하면서 로드밸런서로 관리해주면 웹 서버의 부하를 해결할 수 있다.

##### 로드 밸런서가 서버를 선택하는 방식

- 라운드 로빈(Round Robin) : CPU 스케줄링의 라운드 로빈 방식 활용
- Least Connection : 연결 개수가 가장 적은 서버 선택(트래픽으로 인해 세션이 길어지는 경우 권장)
- Source : 사용자 IP를 해싱하여 분배(특정 사용자가 항상 같은 서버로 연결되는 것을 보장)

##### DNS round robin방식

문제점

- 서버의 수만큼 아이피가 필요함
- 균등하게 분산되지 않음
- 서버가 다운되도 확인 불가

##### OSI 7계층

왜 나눌까 ? : 통신이 일어나는 과정을 단계별로 알 수 있고, 특정한 곳에 이상이 생기면 그 단계만 수정할 수 있기 때문이다.



### blocking/non-blocking & synchronous/Asynchronous

#### Blocking / Non-blocking

블럭 논블럭은 호출된 함수가 호출한 함수에게 제어권을 건네주는 유무의 차이이다.

함수 A,B가 있고, A가 B를 호출했다고 하면, A는 호출한 함수, B는 호출된 함수이다. 이 때, blocking은 A가 B를 호출하고 난 후 제어권을 B에게 넘겨준 경우이다. A는 B가 다 마칠 때 까지 기다려야 한다.

non-blocking은 함수B가 할 일을 다 마치지 않아도, 주도권을 A가 가지고있는 상황이다. A는 B를 기다리면서 다른 일을 진행 할 수 있다.

#### Synchronous / Asynchronous

동기 / 비동기는 일을 수행중인 동시성에 주목해야 한다. 즉, B의 수행 결과를 A가 신경 쓰고 있는 지의 유무라고 생각하면 된다.

같은 상황에서 동기(synchronous)인 경우, 함수 A는 함수 B가 일을 하는 중에 기다리면서, 현재 상태가 어떤지 계속 체크한다.

비동기(Asynchronous)인 경우, 함수 B의 수행상태를 함수 B만 체크한다(callback).

![img](https://camo.githubusercontent.com/b7b28ae739c50d5ed8a4594f52f24e671aeeae234befd0991e5230561ba303bf/68747470733a2f2f696d67312e6461756d63646e2e6e65742f7468756d622f523132383078302f3f73636f64653d6d746973746f72793226666e616d653d6874747073253341253246253246626c6f672e6b616b616f63646e2e6e6574253246646e25324664613530597a2532466274713044736a65345a562532466c47653848386e5a676442646746766f3749637a5330253246696d672e706e67)

이는 이를 잘 나타내는 그림이다.
