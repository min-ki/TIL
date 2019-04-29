### 2.0 What is Server

- 서버는 컴퓨터
- 요청을 하면 해당하는 응답을 해주는 것
- 특정 URL 요청을 처리해주는 것

### 2.1 What is Express

- 프레임워크
- Node.js에서 작동하는 프레임워크
- `npm install express —save`

```javascript
var express = require('express')
var app = express()

app.get('/', function(req, res) {
	res.send('Hello World')
})

app.listen(3000)
```



- 어플리케이션에 필요한 모듈을 호출할 땐 **require** 명령 사용





### 2.2 Installing Express With NPM

- NPM : Node Package Manager
- npm은 node.js를 설치하면 같이 설치되어짐

- NPM 사용법

  - 버전확인 : `npm —version`
  - npm 업데이트 : `sudo npm install -g npm`
  - npm 모듈 설치 : `npm install <module name>` ex) `npm install express`
  - Default로 로컬모드로 모듈을 설치 -> 모듈을 해당 폴더의 node_modules에 설치
  - npm 모듈 제거 : `npm uninstall <module name>` ex) `npm uninstall express`
  - npm 모듈 업데이트 : `npm update <module name> ` ex) `npm update express`
  - npm 모듈 검색 : `npm search <module name>` ex) `npm search express`

  - npm을 통해 프로젝트 시작



- package-lock.json : 프로젝트의 보안과 관련이 있음



### 2.3 Your First Express Server

- package.json에 scripts를 통해 프로젝트 설정을 하면 좋음

- ```javascript
  const express = require("express");
  const app = express();
  
  const PORT = 4000;
  
  function handleListening() {
      console.log(`Listening on: http://localhost:${PORT}`)
  }
  
  app.listen(PORT, handleListening); 
  ```

  



### app.get(path, callback [, callback ...])

---

HTTP GET 요청의 경로를 콜백함수를 지정해주므로 명시해준다. 

##### Arguments

- path : 미들웨어 함수를 호출하기위한 경로, '/' 가 루트 path이다.
  - 문자열로 나타냄
  - 경로 패턴
  - 정규표현식 
  - 위의 배열의 조합으로 표현
- callback : 콜핵 함수 
  - 미들웨어 함수
  - 일련의 미들웨어 함수
  - 미들웨어 함수의 배열
  - 위의 것들의 조합



### app.listen(port, host, backlog, callback);

---

```javascript
var express = require('express');
var app = express();
app.listen(3000);

// port number가 없거나 0이면 운영체제는 사용되지않는 임의의 숫자를 할당
// app은 express()에 의해 Javascreipt Function이 된다. Node's HTTP server를 처리하는 함수
// 이러한 방식은 HTTP와 HTTPS 두 타입의 버전을 같은 코드를 통해서 쉽게 제공할 수있도록 도와준다.


var express = require('express');
var https = require('https');
var http = require('http');
var app = express();

http.createServer(app).listen(80);
http.createServer(options, app).listen(443);

// app.listen() 함수는 http.Server object를 반환
app.listen = function() {
  var server = http.createServer(this);
  return server.listen.apply(server, arguments);
}
```

