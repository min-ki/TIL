# Transducers

> Transducers are composable algorithmic transformations.

Transducer는 조합할 수 있는 알고리즘 변환기이다.

> They are independent from the context of their input and output sources and specify only the essence of the transformation in terms of an individual element.

Transducer는 입력과 출력 소스의 컨텍스트와 독립적이며, 개별 요소의 관점에서 변환의 본질만을 명시한다.

> Because transducers are decoupled from input or output sources, they can be used in many different processes - collections, streams, channels, observables, etc.

왜나하면 transducers는 입력과 출력 소스로부터 분리되어 있기 때문에, collections, streams, channels, observables 등 다양한 프로세스에서 사용될 수 있다.

> Transducers compose directly, without awareness of input or creation of intermediate aggregates.

Transducers는 입력의 인지 혹은 중간 집계물의 생성 없이 직접 조합된다.

## Terminology

> A reducing function is the kind of function you’d pass to reduce - it is a function that takes an accumulated result and a new input and returns a new accumulated result:

reducing function은 reduce에 전달해야하는 함수의 일종이다. 이 함수는 누적된 결과와 새로운 입력을 받아서 새로운 누적된 결과를 반환한다.

```clojure
;; reducing funciton signature
whatever, input -> whatever
```

A transducer (sometimes referred to as xform or xf) is a transformation from one reducing function to another:

transducer (때때로 xform이나 xf라고도 한다.)는 reducing function에서 다른 reducing function으로의 변환을 의미한다.

```clojure
;; transducer signature
(whatever, input -> whatever) -> (whatever, input -> whatever)
```

## Defining Transformations With Transducers (Transducer와 함께 변환을 정의하기)

> Most sequence functions included in Clojure have an arity that produces a transducer.

클로저에 포함된 대부분의 시퀀스 함수는 transducer를 생성하는 arity를 가지고 있다.

> This arity omits the input collection; the inputs will be supplied by the process applying the transducer.

이 arity는 입력 컬렉션을 생략한다. 입력은 transducer를 적용하는 프로세스에 의해 제공된다.

> Note: this reduced arity is not currying or partial application.

참고: 이 줄어든 arity는 커링이나 부분 적용이 아니다.

For example:

```clojure
(filter odd?) ;; 홀수를 필터링하는 transducers를 반환한다.
(map inc) ;; 1씩 증가시키는 transducers를 반환한다.
(take 5) ;; 처음 5개의 요소만 반환하는 transducers를 반환한다.
```

위의 예시는 시퀀스 함수에 보통 사용하는 함수에서 뒤에 collection을 생략한 것이다.

> Transducers compose with ordinary function composition.
> Transducer는 일반적인 함수의 조합과 같이 조합된다.

> A transducer performs its operation before deciding whether and how many times to call the transducer it wraps.

Transducer는 wrap하는 transducer를 호출할지 여부와 호출 횟수를 결정하기 전에 작업을 수행한다.

> The recommended way to compose transducers is with the existing **comp** function:

Transducer를 조합을 위한 가장 권장하는 방법은 기존의 **comp** 함수를 사용하는 것이다.

```clojure
(def xf
  (comp
    (filter odd?)
    (map inc)
    (take 5)))
```

> The transducer xf is a transformation stack that will be applied by a process to a series of input elements.

Transducer xf는 입력 요소들의 시리즈에 적용되어질 변환 스택이다.

> Each function in the stack is performed before the operation it wraps.

변환 스택의 각 함수는 wrap하는 작업을 하기전에 수행된다.

> Composition of the transformer runs right-to-left but builds a transformation stack that runs left-to-right (filtering happens before mapping in this example).

변환기의 조합은 오른쪽에서 왼쪽으로 실행되지만, 변환 스택은 왼쪽에서 오른쪽으로 실행된다. (이 예시에서는 필터링이 매핑보다 먼저 실행된다.)

> As a mnemonic, remember that the ordering of transducer functions in comp is the same order as sequence transformations in ->>.

As a mnemonic은 우리가 기억하기 쉽게 하기 위한 것이다. 예를들어, 무언가 외울때 앞자리만 따서 초성을 외우는 방식과 같이 기억하기 쉽게 무언가를 비교하거나 하는 것

comp의 transducer 함수의 순서를 기억하자. 이 순서는 스레딩 매크로 (->>) 시퀀스 변환의 순서와 동일하다.

> The transformation above is equivalent to the sequence transformation:

위의 변환은 아래의 시퀀스 변환과 동일하다.

```clojure
(->> coll
    (filter odd?)
    (map inc)
    (take 5))
```

> The following functions produce a transducer when the input collection is omitted:

다음 함수들은 입력 컬렉션이 생략되었을 때 transducer를 반환한다.

```clojure
map cat mapcat filter remove take take-while take-nth drop drop-while replace partition-by partition-all keep keep-indexed map-indexed distinct interpose dedupe random-sample
```

## Transducer를 사용하는 것은 무엇이 좋을까?

- efficiency를 향상시켜준다.
- modular한 방식으로 코드를 더 효율적으로 작성하게 해준다.

## 참고자료

- https://clojure.org/reference/transducers
- https://stackoverflow.com/questions/26317325/can-someone-explain-clojure-transducers-to-me-in-simple-terms
- https://www.youtube.com/watch?v=6mTbuzafcII
