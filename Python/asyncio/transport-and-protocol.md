# asyncio

## Transport와 Protocol

- Transport: 네트워크 연결을 추상화한 객체 (바이트들 어떻게 전송할지) -> how
- Protocol: 데이터를 추상화한 객체 (어떤 바이트들을 전송할지) -> which

> A different way of saying the same thing: a transport is an abstraction for a socket (or similar I/O endpoint) while a protocol is an abstraction for an application, from the transport’s point of view.

위의 두 용어를 다르게 표현하면, transport는 socket(또는 비슷한 I/O endpoint)의 추상화이고, protocol은 application의 추상화이다.

Transport와 Protocol 객체는 항상 1:1 관계이다.

- 프로토콜은 데이터를 전송하기 위해 transport 객체의 메서드를 사용한다.
- 트랜스포트는 수신받은 데이터를 전달하기 위해 프로토콜 객체의 메서드를 사용한다.


### Transport

트랜스포트는 asyncio 라이브러리에서 다양한 통신 채널을 추상화하기위해 제공되는 클래스들이다. 트랜스포트 객체는 항상 asyncio의 이벤트 루프에의해 초기화된다.

asyncio는 다음과 같은 트랜스포트를 구현했다.

- TCP
- UDP
- SSL
- subprocess pipes

트랜스포트의 종류에 따라서 사용가능한 메서드들이 다르다.
트랜스포트 클래스는 스레드 안전하지 않다. 따라서 트랜스포트 객체의 메서드는 항상 asyncio의 이벤트 루프에 의해 호출되어야 한다.


#### Transport 계층

트랜스포트 클래스의 계층구조
[transport-hierachy.md](transport-hierachy.md)


## Reference
- https://docs.python.org/3/library/asyncio-protocol.html