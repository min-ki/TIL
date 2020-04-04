# Day2

## Object.assign

각기 다른 속성의 객체들을 합치려면 `Object.assign` 을 사용하면 된다.

```js
const obj = {
  text: "object text"
};

const newObj = {
  name: "node.js"
};

const mergedObjet = Object.assign({}, obj, newObj);
```

또 다른 방법으로는, spread 연산자를 사용하면 된다.

```js
const obj = {
  text: "object text"
};

const newObj = {
  name: "node.js"
};

const mergedObject = {
  ...obj,
  ...newObj
};
```

## Set

중복을 제거하기 위한 자료구조로 사용되는 Set을 js에서 사용하는 방법은 다음과 같다.

```js
const test = new Set()
test.add(1)
test.add(1)
test.add(2)
test.add(3)

for(const item of test) {
    console.log(item) // 1 2 3 출력
}

// 특정 요소 존재 체크
has() 메서드

const isHas = test.has(2) // true
```

## Some

최소 한개이상의 조건에 대해서 만족하면 참 값을 반환하는 메소드

```js
"use strict";

const arr = [1, 0, -1, -2];
const result = arr.some(key => key < 0); // 0보다 작은 것이 하나라도 있으면 참
console.log(result); // true
```

## every

모든 조건이 만족하면 참 값을 반환하는 메소드

```js
"use strict";

const arr = [1, 2, 3, 4];
const result = arr.every(key => key > 0); // 모두 0이상이여야 참
console.log(result); // true
```
