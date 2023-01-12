# [Promesa](https://github.com/funcool/promesa)

클로저를 위한 promise 라이브러리이며 concurrency toolkit이다.

## promise란?

promesa 공식문서에서 promise를 다음과 같이 정의하고 있다.

> promise는 비동기 작업의 결과를 나타내는 **추상화**이며, **에러에 대한 개념**을 가지고 있다.



JVM에서는 `CompletebleFuture`를, JS에서는 `Promise`를 사용한다.

promise에는 다음과 같은 가능한 상태들이 존재한다.

- `resolved` : promise가 값을 가지고 있다는 것을 의미한다.
- `rejected` : promise가 에러를 가지고 있다는 것을 의미한다.
- `pending`  : promise가 값을 가지고 있지 않다는 것을 의미한다.


promise의 상태가 resolved 혹은 rejected 되었을 때 이것은 `done` 이라고 간주된다.

> NOTE: 많은 부분들이 런타임에 상관없이 동일하게 동작하지만, 플랫폼에 따라 한계들이 존재한다.

### Creating a Promise

promise instance를 만드는 다양한 방법이 있다. plain value를 가지는 promise를 만들기 원한다면, polymorphic `promise` 함수를 사용하면 된다.

```clojure
(require '[promesa.core :as p])

;; 값으로부터 promise를 생성한다.
(p/promise 1)

;; rejected promise를 생성한다. (error를 가진다.)
(p/promise (ex-info "error" {}))
```

제공되는 값에 따라서 적절한 promise instance로 자동 변환된다. 제공된 값이 exception이라면 rejected promise가 생성되고, 그렇지 않다면 resolved promise가 생성된다.

만약 이미 값이 `resolved` 혹은 `rejected` 인지 안다면, 변환을 생략하고 바로 `resolved` 혹은 `rejected` 함수를 사용할 수 있다.

```clojure
;; resolved promise를 생성한다.
(p/resolved 1)
;; => #object[java.util.concurrent.CompletableFuture 0x3e133219 "resolved"]

;; rejected promise를 생성한다.
(p/rejected (ex-info "error" {}))
;; => #object[java.util.concurrent.CompletableFuture 0x3e563293 "rejected"]
```

또다른 옵션으로 `deferred` 함수를 사용하면, 값이 없는 promise를 생성하고 비동기적으로 `p/resolve!` 혹은 `p/reject!` 함수를 사용하여 값을 제공할 수 있다.

```clojure
(defn sleep
  [ms]
  (let [p (p/deferred)] ;; deferred 함수를 사용해 promise를 생성한다.
    (future (p/resolve! p)) ;; future를 통해서 비동기적으로 값을 제공한다.
    p))
```

또다른 옵션은 팩토리 함수를 사용하는 방법이 있다. 자바스크립트에 친숙하다면, 접근방식이 유사하다.

```clojure
@(p/create (fn [resolve reject]
              (resolve 1)))
```

아래는 자바스크립트로 promise를 만드는 방법이다. 비슷하게 resolve, reject를 인자로 전달받는 것을 확인할 수 있다.

```javascript
new Promise((resolve, reject) => {
  ...
})
```

> NOTE: reader macro인 `@`는 JVM에서만 동작한다.

팩토리 함수를 사용하는 것은 현재 스레드 내에서 동기적으로 실행된다. 만약 비동기적으로 실행되길 원한다면, executor를 제공해서 비동기적으로 실행되도록 할 수 있다. (JVM에서만 가능)

```clojure
(require '[promesa.exec :as exec])

@(p/create (fn [resolve reject] (resolve 1)) exec/default-executor)
```

공식문서 예제에서는 [default-executor](https://github.com/funcool/promesa/blob/master/src/promesa/exec.cljc)를 제공하고있다. 직접 내부를 들여다보면서 조금 더 자세히 살펴보자.

```clojure
(defonce
  ^{:doc "Default executor instance, ForkJoinPool/commonPool in JVM, MicrotaskExecutor on JS."}
  default-executor
  (delay
    #?(:clj  (ForkJoinPool/commonPool)
       :cljs (microtask-executor))))
```

JVM에서는 `ForkJoinPool/commonPool`을 사용하고, JS에서는 `microtask-executor`를 사용한다. `microtask-executor`는 브라우저에서 제공하는 `Promise`를 사용한다. `Promise`는 microtask queue를 사용하기 때문에, 비동기적으로 실행된다.

또다른 방법으로 `do` 매크로를 사용하는 방법이 있다.

```clojure
(p/do
  (let [a (rand-int 10)
        b (rand-int 10)]
      (+ a b)))
```

`do` 매크로는 클로저의 do 블록과 유사하게 동작한다. 그래서 이 블럭 안에 어떠한 식이든 사용할 수 있다. 하지만, 마지막 식의 결과값이 반환값이 된다. 이 식은 plain value가 될 수도 있고 또다른 promise가 될 수도 있다.

**do 블록 내에서 예외가 발생한다면, 스택의 예외를 다시 raise하는 대신에 rejected promise를 반환할 것이다.**

do가 하나 이상의 식을 포함한다면, 각 식은 promise 식으로 간주되며, 순차적으로 실행되어지고, 이전 식이 resolution될때까지 기다린다.

```clojure
(p/do (expr1)
      (expr2)
      (expr3))
```

위의 코드는 다음 `let` 매크로를 사용한 것과 동일하다.

```clojure
(p/let [_ (expr1)
        _ (expr2)]
    (expr3))
```

마침내, promesa는 `clojure.core/future`와 유사하게 `future` 매크로를 제공한다.

```clojure
@(p/future (some-complex-task))
;; => "result-of-complex-task"
```

--- 

지금까지 promise를 생성하는 방법에 대해서 알아보았다. 다시한번 복습하자면 다음과 같다.

1. `(p/promise)` : plain value or error를 전달해서 promise를 생성

2. `(p/resolved 1)` or `(p/rejected (ex-info {}))` : 전달할 값이 resolved될지 rejected될지 명확하다면 이렇게 사용할 수도 있다.

3. `p/deferred`를 사용해서 값이 없는 promise를 생성한다. 그리고 나중에 `resolve`나 `reject`를 호출해서 값을 전달할 수 있다.

4. `p/create`를 사용해서 promise를 생성한다. 자바스크립트와 유사하게 생겼다는 점이 있으며 동기적으로 실행된다는 점을 유심히 보자. 비동기적으로 실행하고 싶다면 executor를 전달하는 방법이 있다.

5. `p/do`를 사용해서 promise를 생성한다. 클로저의 do 블록과 유사하게 동작한다. 마지막 식의 결과값이 반환값이 된다. 이 식은 plain value가 될 수도 있고 또다른 promise가 될 수도 있다.


# 참고자료
- https://funcool.github.io/promesa/latest/promises.html
- https://www.youtube.com/playlist?list=PLZ9NgFYEMxp6aIJ8c6sxI8jakvub-vQxb
- https://www.youtube.com/playlist?list=PLZ9NgFYEMxp6aIJ8c6sxI8jakvub-vQxb