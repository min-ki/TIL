# Generic Type

```java

// <T1, T2, ..., Tn> 이 부분을 type parameters 혹은 type variables라고 부른다.
class name<T1, T2, ..., Tn> { /* ... */ }
```

\<T\> 에는 _Non-Primitive_ 타입이면 어떤 것이든 가능하다.
예를들어, 클래스, 인터페이스, 배열 등

```java

public class Box<T> {
    private T t;
    public void set(T t) { this.t = t; }
    public T get() { return t; }
}
```

## Type Parameter 네이밍 컨벤션

- 단수, Uppercase

- E: Element (자바 컬렉션 프레임워크에서 주로 사용)
- K: Key
- N: Number
- T: Type
- V: Value
- S, U, V etc: 2nd, 3rd, 4th types

## Type parameters를 여러개 사용하는 법

```java
public interface Pair<K, V> {
    public K getKey();
    public V getValue();
}

public class OrderedPair<K, V> implements Pair<K, V> {

    private K key;
    private V value;

    public OrderedPair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public K getKey() { return key; }
    public V getValue() { return value; }
}
```

```java

// Key는 문자형이고 Value는 정수형인 OrderedPair
Pair<String, Integer> p1 = new OrderedPair<String, Integer>("minki", 10);

// Key, Value가 둘다 문자형인 OrderedPair
Pair<String, String> p2 = new OrderedPair<String, String>("hello", "world");
```

## Auto Boxing과 Unboxing

위의 예시에서 타입이 Integer이지만 int 타입의 값을 전달하고 있는데 이러한 타입간의 변환을 자바에서는 Auto Boxing과 Unboxing이라고 한다.

### Auto Boxing

자바 컴파일러가 원시 데이터 타입을 래퍼 클래스로 자동 변환 시켜주는 것

- int -> Integer
- char -> Character

### Unboxing

자바 컴파일러가 래퍼 클래스를 원시 데이터 타입으로 자동으로 변환시켜 주는 것

- Integer -> int
- Character -> char

### 참고자료

- https://docs.oracle.com/javase/tutorial/java/data/autoboxing.html
