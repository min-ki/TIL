## Node.js의 핵심개념

- I/O
- 비동기 vs 동기
- Non-blocking vs blocking

### I/O

- 동시성 문제를 해결하기 위해 Node.js가 나옴
- 네트워크 요청에 대한 I/O가 기존에 다른 것들은 동기 방식으로 동작을 하기 때문에
- I/O는 서버 성능에 중요한 역할
- 그래서 Node.js는 비동기 모델을 채택
- 해당하는 대상이 완료되는 시점을 기다리지 않는다. ⇒ 비동기
- 이벤트 루프 개념
- Node.js는 크롬에서 사용하는 V8에 의해서 이벤트 루프 개념이 동작하게 된다.
- 자바스크립트는 웹 브라우저에서 사용이 되기위해 개발되어서 비동기를 채택
- 이벤트 루프
- javascript는 이벤트 주도 방식의 개발
  - 사용자가 클릭
  - 사용자가 요청을 했을 때 반응
  - 이벤트가 있을 때 콜백 방식을 통해 처리하는 것이 기본 모델

### Node와 웹 브라우저의 차이점

1. window 객체 : Node에서는 window 객체가 없다.
2. require 내장함수 : Node에서는 별다른 설정을 하지 않으면 모듈을 사용하기위해 require()를 사용한다.
3. const : 상수 (변하지 않는 값), let: 변수, var: 변수
   - let은 블록단위 스코프
   - var는 전역 스코프

### Node.js REPL

채팅을 하듯이 Node.js를 다룰 수 있는 것

### NPM

Node.js 의 기본 패키지로 설치 시 같이 설치된다.

### 버전확인

```shell
    npm -v
    node -v
```

### 모듈 설치

```shell
    npm install express # 설치
    npm install 모듈명

    npm install express --save-dev  # package.json 안에 추가를 한다
    npm install nodemon -g # 시스템 전역에 설치

    npm uninstall express # 삭제
    npm uninstall nodemon -g # 시스템 전역에서 삭제
```

### npx

```shell
    npx create-react-app myproject # 최신의 모듈을 바로 실행을 하는 것
```

### Semantic versioning

의미가 있는 버전 관리 체계

- 1.0.0 (3자리의 버전 체계)
- 1.0.0 → 1.0.1
  - 하위 호환이 가능하며 버그를 수정 (Patch release)
- 1.0.0 → 1.1.0
  - 하위 호환이 되며 새로운 기능이 추가되었을 경우 (Minor release)
- 1.0.0 → 2.0.0

  - 하위 호환이 되지 않으며 새로 개발된 경우

> - Patch release: 1.0 or 1.0.x or ~1.0.4
> - Minor release: 1 or 1.x or ^1.0.4
> - Major release: \* or X
