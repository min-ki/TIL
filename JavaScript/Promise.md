## Promise란 무엇인가?

Promise에 대해 다시 한번 정리하고, 그 동안은 Promise.all() 정도까지만 많이 사용하였는데 다른 메서드들도 한번 정리해보려고 한다.

MDN에 나와있는 정의는 Promise 객체는 비동기 작업이 맞이할 미래의 완료 혹은 실패와 그에 해당하는 결과 값을 나타낸다고 적혀있다.

Promise는 다음 중 하나의 상태를 가진다.

1. 대기(pending): 이행하거나 거부되지 않은 초기 상태
2. 이행(fulfilled): 연산이 성공적으로 완료됨.
3. 거부(rejected): 연산이 실패함.

### Promise의 속성

- Promise.length : 값이 언제나 1인 길이 속성이라고 한다. (생성자 인수의 수)
- Promise.prototype : Promise 생성자의 프로토타입을 나타낸다.

### Promise의 메서드

- Promise.all(iterable)
- Promise.race(iterable)
- Promise.reject()
- Promise.resolver()

#### Promise.all(iterable)

iterable 객체 내의 프라미스가 모두 처리되면, 그 때 새로운 프라미스가 이행이되고, iterable 객체의 모든 프라미스의 결과 값을 담은 배열이 새로운 프라미스의 결과 값이 된다.
만약 전달된 프라미스 중 하나라도 reject(거부) 된다면, Promise.all는 에러가 발생한 시점에서 해당하는 프라미스의 reject가 실행되어진다.

#### Promise.race(iterable)

Promise.all과 비슷하지만 가장 먼저 처리되는 프라미스의 결과 혹은 에러를 반환한다.

### Promise 명세

- ECMAScript (ECMA-262) 의 표준으로 정의

#### reference

- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
- https://joshua1988.github.io/web-development/javascript/promise-for-beginners/
- https://ko.javascript.info/promise-api
