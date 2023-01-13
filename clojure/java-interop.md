
# Java Interop

## 자바 클래스의 새로운 인스턴스를 생성하는 방법

새로운 인스턴스를 생성하기위해서는 자바 클래스의 생성자를 호출하면 된다. 클로저에서 자바 클래스 생성자를 호출하는 방법에는 2가지가 있다.

1. `new` 함수를 사용하는 방법 ; 여기서 new는 special form 이다.
2. dot(.) notation을 사용하는 방법

아래 코드 예시를 통해서 살펴보도록 하겠다.

```clojure

(ns example
  (:import java.util.ArrayList))

;; 1. new 함수를 사용하는 방법
(new ArrayList (range 10)) ; => [0 1 2 3 4 5 6 7 8 9]

;; 2. dot(.) notation을 사용하는 방법
(ArrayList. (range 10)) ; => [0 1 2 3 4 5 6 7 8 9]
```

