# [Promesa](https://github.com/funcool/promesa)

클로저를 위한 promise 라이브러리이며 concurrency toolkit이다.

## promise란?

promesa 공식문서에서 promise를 다음과 같이 정의하고 있다.

> promise는 비동기 작업의 결과를 나타내는 **추상화**이며, **에러 개념**을 가지고 있다.

JVM에서는 `CompletebleFuture`를, JS에서는 `Promise`를 사용한다.

promise에는 다음과 같은 가능한 상태들이 존재한다.

- `resolved` : promise가 값을 가지고 있다는 것을 의미한다.
- `rejected` : promise가 에러를 가지고 있다는 것을 의미한다.
- `pending`  : promise가 값을 가지고 있지 않다는 것을 의미한다.


promise의 상태가 resolved 혹은 rejected 되었을 때 이것은 `done` 이라고 간주된다.

> NOTE: 많은 부분들이 런타임에 상관없이 동일하게 동작하지만, 플랫폼에 따라 한계들이 존재한다.

## Creating a Promise

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


## Chaining computations

이 섹션은 promesa가 제공하는 다른 연산들을 연속적으로 실행하는데 도움을 주는 매크로와 헬퍼들에 대해서 설명한다.

### then

promise에 변환을 체이닝하기위한 가장 일반적인 방법은 범용 목적인 `then` 함수를 사용하는 것이다.

```clojure
@(-> (p/resolved 1)
     (p/then inc))

;; => 2

;; flatten result
@(-> (p/resolved 1)
     (p/then (fn [x] (p/resolved (inc x)))))

;; => 2
```

위의 예에서 보듯이, `then`은 plain value를 반환하는 함수 뿐만 아니라 promise 인스턴스를 반환하는 함수도 처리한다. (자동으로 평탄화된다.)
퍼포먼스에 민감한 코드를 위해서는, `map`이나 `mapcat`과 같은 더 구체적인 함수를 사용하는 것이 좋다.

### chain
여러개의 변환을 하나의 스텝에서 적용하고 싶다면, `chain` 과 `chain'` 함수를 사용하면 된다.

```clojure
(def result
  (-> (p/resolved 1)
      (p/chain inc inc inc)))

@result
;; => 4
```

> NOTE: chain은 then, then'과 유사하지만 여러개의 변환 함수를 인자로 받는다.

### `->`, `->>`, `as->` 매크로

`->`와 `->>`는 6.1.431 버전에서 추가되었다. `as->`는 6.1.434 버전에서 추가되었다.

스레딩 매크로는 매번 `then`을 사용하는 것 대신에, 체이닝 연산을 더 간결하게 만들어준다.

아래 예제에서 `then`을 사용하는 것과 `->`를 사용하는 것을 비교해보자.

```clojure
(-> (p/resolved {:a 1 :c 3})
    (p/then #(assoc  % :b 2))
    (p/then #(dissoc % :c )))
```

다음은, `->`를 사용해서 위의 코드를 더 간결하게 만든 것이다. then이 생략되었고, 매번 체이닝 연산마다 then을 사용하지 않아도 된다.

```clojure
(p/-> (p/resolved {:a 1 :c 3})
      (assoc :b 2)
      (dissoc :c))
```

`->>`와 `as->`는 clojure.core 매크로와 동일하지만, promise와 함께 동작한다는 점에서 다르다.

### handle

하나의 단일 콜백에서 `rejected` 혹은 `resolved` 콜백을 처리하고싶다면, `handle` 함수를 사용하면 된다.

```clojure
(def result
  (-> (p/promise 1)
      (p/handle (fn [result error]
                   (if error :rejected :resolved)))))

@result
;; => :resolved
```

위의 handle은 then과 같이 동일하게 동작한다. 만약 함수가 promise를 반환한다면, 자동으로 unwrapped된다.

여기서, unwrapped된다는 것은, promise를 반환했지만 result와 error로 자동으로 분리된다는 것을 의미한다.

### finally

finally 함수는 promise가 resolved되거나 rejected되었을 때, 항상 실행되는 함수를 제공한다. (사이드 이펙트가 있을 수 있다.)

```clojure
(def result
  (-> (p/promise 1)
      (p/finally (fn [_ _]
                   (println "finally")))))

@result
;; => 1
;; => stdout: "finally"
```

위의 예제에서, 마지막에 finally 함수가 실행되지만 함수의 리턴 값은 무시된다. 그리고, 새로운 promise 인스턴스가 finally 이전의 원래의 것을 미러링해서 반환한다.

```clojure
(defn finally
  "Like `handle` but ignores the return value. Returns a promise that
  will mirror the original one."
  ([p f]
   (pt/-finally (pt/-promise p) f))
  ([p f executor]
   (pt/-finally (pt/-promise p) f executor)))
```

finally 함수의 내부를 보면서 자세히 살펴보자.

```clojure
(extend-protocol pt/IPromise
  CompletionStage
  
  ...

  (-finally
    ([it f]
    (.whenComplete ^CompletionStage it
                    ^BiConsumer (pu/->Consumer2 f))) ;; ->Consumer2는 deftype

    ([it f executor]
    (.whenCompleteAsync ^CompletionStage it
                        ^BiConsumer (pu/->Consumer2 f)
                        ^Executor (exec/resolve-executor executor)))))
```

위의 코드는 pt/-finally 프로토콜의 구현부이다. Java의 CompletionStage 인터페이스를 구현한 promise 인스턴스 (CompletableFuture)를 받아서, whenComplete 함수에 BiConsumer를 전달한다.

.whenComplete 함수의 인터페이스는 다음과 같다. `whenComplete(BiConsumer<? super T,? super Throwable> action)`

이 인터페이스는 두개의 인자를 받고 결과는 반환하지 않는 함수형 인터페이스이다. 다른 함수형 인터페이스와 다르게 BiConsumer는 사이드 이펙트를 기대한다.

```clojure
(.whenComplete ^CompletionStage it
               ^BiConsumer (pu/->Consumer2 f))

it.whenComplete(action) ;; 위의 코드는 다음과 같이 이해하면 된다.
```

위의 함수 호출예시는 clojure java interop을 사용해서, whenComplete 함수를 호출하는 것이다.

> java interop은 다음과 같이 사용할 수 있다. `(.instanceMember instance args*)`

위에서는 it이 CompletionStage 인터페이스를 구현한 CompletableFuture의 인스턴스이다. 그리고, whenComplete 함수를 호출하면서, BiConsumer를 전달한다.

그리고 finally는 원래의 promise를 반환한다고 하는데, whenComplete를 조금더 자세히 봐보자.

`CompletableFuture<T>	whenComplete(BiConsumer<? super T,? super Throwable> action)`

현재 스테이지가 완료되면, 인자로 전달된 action을 실행합니다. 현재 스테이지와 같은 결과 혹은 예외와 함께 새로운 CompletionStage를 반환합니다. 이를 통해서 finally가 미러링되는 동작을 확인할 수 있습니다.

### map

최종적으로 resolved된 promise의 값에 함수를 적용한 값을 가지는 새로운 promise 인스턴스를 반환한다.

```clojure
(def result
  (->> (p/resolved 1)
       (p/map inc)))

@result
;; => 2
```

then과는 대조적으로, nested promise를 자동으로 unwrapping을 해주지 않는다.
unwrapping을 하고싶다면 `mapcat` 을 사용하면 된다.

### mapcat

map과 동일하게 함수를 적용한 값과함께 새로운 promise 인스턴스를 반환한다.
map과 다른점은 map은 값을 반환하지만, mapcat은 promise를 반환한다는 점이다.

```clojure
(def result
 (->> (p/resolved 1)
      (p/mapcat (fn [v] (p/resolved (inc v))))))
```

### hmap

map과 동일한 방식으로 함수를 적용한다. 다만, 함수의 인자는 resolved된 값과 error를 받는다.
위의 mapcat 예제에서는 mapcat의 함수로 resolved된 값만 받았지만, hmap은 resolved된 값과 error를 받는다. 함수의 반환 값으로 완료될 promise를 반환받는다.

```clojure
(def result
  (->> (p/resolved 1)
       (p/hmap (fn [v _error] (inc v)))))

@result
;; => 2
```

### hcat

mapcat과 동일한 방식으로 함수를 적용한다. 다만, 함수의 인자는 resolved된 값과 error를 받는다. 함수는 반드시 promise를 반환해야한다.

```clojure
(def result
  (->> (p/resolved 1)
        (p/hcat (fn [v _] (p/resolved (inc v))))))

@result
;; => 2
```


# 참고자료
- https://funcool.github.io/promesa/latest/promises.html
- https://www.youtube.com/playlist?list=PLZ9NgFYEMxp6aIJ8c6sxI8jakvub-vQxb
- https://www.youtube.com/playlist?list=PLZ9NgFYEMxp6aIJ8c6sxI8jakvub-vQxb