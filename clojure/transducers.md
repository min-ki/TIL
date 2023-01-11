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

## Using Transducers

Transducers는 많은 상황에서 사용될 수 있다.

### transduce

> One of the most common ways to apply transducers is with the transduce function, which is analogous to the standard reduce function:

transducers를 적용하는 가장 일반적인 방법 중 하나는 `transduce`함수를 사용하는 것이다. 
`transduce` 함수는 표준 reduce 함수와 유사하다.

```clojure
(transduce xform f coll)
(transduce xform f init coll)
```

> transduce will immediately (not lazily) reduce over coll with the transducer xform applied to the reducing function f, using init as the initial value if supplied or (f) otherwise. 

- transduce는 초기값이 있다면 초기값을 사용하고 아니라면 (f)를 한다.
- transduce는 lazily하게 처리되지않고, 즉시 f가 적용된 transducer xform과 함께 전체 컬렉션을 reduce 한다.

> f supplies the knowledge of how to accumulate the result, which occurs in the (potentially stateful) context of the reduce.

- f는 reduce 함수가 실행되면서 reduce 함수의 컨텍스트 내에서 결과가 어떻게 누적되어야 하는지에 대한 방법을 알려준다.

```clojure
(def xf (comp (filter odd?) (map inc)))
(transduce xf + (range 5))
;; => 6

(transduce xf + 100 (range 5))
;; => 106
```

> The composed xf transducer will be invoked left-to-right with a final call to the reducing function f. In the last example, input values will be filtered, then incremented, and finally summed.

xf transducer는 왼쪽에서 오른쪽으로 호출되고 마지막으로 reducing 함수 f가 호출된다. 마지막 예제에서는 입력값이 필터링되고, 증가되고, 마지막으로 합산된다.

자세히 살펴보자.

```clojure
1. (range 5) => (0 1 2 3 4)

2. (filter odd?) => (1 3)

3. (map inc) => (2 4)

4. (+) => 6
```

<img src="https://clojure.org/images/content/reference/transducers/xf.png">


## eduction

- education 아니다. `eduction`이다.
- 라틴어 eductio로부터 파생되었다고 한다.
- educe + -ion
- 의미
  - The act of educing, of deducing: deduction.
  - 

> To capture the process of applying a transducer to a coll, use the eduction function. 

transducer를 컬렉션에 적용하는 과정을 캡쳐하고 싶다면 `eduction` 함수를 사용하면된다.

> It takes any number of xforms and a final coll and returns a reducible/iterable application of the transducer to the items in coll. 

`eduction` 함수는 xform과 컬렉션을 인자로 받고, transducer를 컬렉션의 아이템에 적용한 reducible/iterable을 반환한다.

> These applications will be performed each time reduce/iterator is called.

`reduce/iterator`가 호출될 때마다 이러한 애플리케이션이 수행된다.
(왜 애플리케이션이라고 표현했지? 어떤 과정을 관찰해주기때문에 애플리케이션이라고 표현한건가?)

```clojure
user=> (def iter (eduction xf (range 5)))
;; => #'user/iter

user=> iter
;; => (2 4)

user=> (reduce + 0 iter)
;; => 6
```

위 예시에서 보듯이, 중간에 xform이 적용된 컬레션의 형태를 볼 수 있다.

## into

> To apply a transducer to an input collection and construct a new output collection, use into (which efficiently uses reduce and transients if possible):

transducer에 입력 컬렉션을 적용하고, 새로운 컬렉션을 생성하려면 `into`를 사용하면 된다.

```clojure
(into [] xf (range 1000))
```

## sequence

> To create a sequence from the application of a transducer to an input collection, use sequence:

입력 컬렉션에 대한 transducer의 적용 결과를 시퀀스로 생성하려면 `sequence`를 사용하면 된다.

```clojure
(sequence xf (range 1000))
```

> The resulting sequence elements are incrementally computed. 
시퀀스 요소들의 결과는 증분적으로 계산된다.

> These sequences will consume input incrementally as needed and fully realize intermediate operations. 

이 시퀀스들은 필요할 때마다 입력을 증분적으로 소비하고 중간 연산을 완전히 실현한다.

> This behavior differs from the equivalent operations on lazy sequences.

이러한 동작방식은 lazy 시퀀스에서 동일한 연산과는 다르다.

## Creating Transducers

## Creating Transducible Processes

> Transducers are designed to be used in many kinds of processes. 

Transducers는 다양한 프로세스에서 사용될 수 있도록 디자인 되었다.

A transducible process is defined as a succession of steps where each step ingests an input. 

`transducible` 프로세스는 각 단계에서 입력을 소비하는 순차적인 단계로 정의된다.

The source of the inputs is specific to each process (from a collection, an iterator, a stream, etc). 

입력 소스는 각 프로세스에 따라 다르다. (컬렉션, 이터레이터, 스트림 등)

Similarly, the process must choose what to do with the outputs produced by each step.

비슷하게, 프로세스는 반드시 각 단계에서 생성된 출력물을 어떻게 처리할지 선택해야 한다.


## Transducer를 사용하는 것은 무엇이 좋을까?

- efficiency를 향상시켜준다.
- modular한 방식으로 코드를 더 효율적으로 작성하게 해준다.



## 참고자료

- https://clojure.org/reference/transducers
- https://stackoverflow.com/questions/26317325/can-someone-explain-clojure-transducers-to-me-in-simple-terms
- https://www.youtube.com/watch?v=6mTbuzafcII
