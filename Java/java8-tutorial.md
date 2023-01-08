# Modern Java - A Guide to Java 8

- Java 8 가이드
- https://github.com/winterbe/java8-tutorial

## Default Methods for Interfaces

Java 8은 인터페이스에 non-abstract 메소드의 구현체를 추가할 수 있도록 default 메소드를 제공합니다.
이 기능은 또한 `virtual extension methods`라고도 불립니다.

```java
interface Formula {
    double calculate(int a);

    default double sqrt(int a) {
        return Math.sqrt(a);
    }
}
```

```java

Formula formula = new Formula() {
    @Override
    public double calculate(int a) {
        return sqrt(a * 100); // default method를 사용할 수 있다.
    }
}

formula.calculate(100);
formula.sqrt(16);
```

위에서 formula는 `anonymous object`로 구현되었습니다.
이는 Java 8에서는 인터페이스를 구현하는 익명 클래스를 만들 수 있도록 허용합니다.
하지만 위의 코드는 조금 장황한 느낌이 있어서 다음 섹션에서 더 나이스한 방법으로 구현하는 방법에 대해서 살펴본다.

## Lambda expressions

```java
List<String> names = Arrays.asList("peter", "anna", "mike", "xenia");

Collections.sort(names, new Comparator<String>() {
    @Override
    public int compare(String a, String b) {
        return b.compareTo(a);
    }
});
```

Collections.sort는 static utility method로써 두 개의 인자를 받는다. 위와 같이 anonymous object를 사용하여 구현할 수 있지만,
자바 8에서는 람다식을 사용해서 더 짧은 문법으로 구현 가능하다.

```java
Collections.sort(names, (String a, String b) -> {
    return b.compareTo(a);
})
```

많이 짧아졌지만 더 짧아질 수 있다.

```java
Collections.sort(names, (String a, String b) -> b.compareTo(a))
```

- compareTo는 두 문자열을 사전 순서대로 비교한다.
- 두 문자열이 동일하다면 0을 반환하는데 다르다면 음수 또는 양수를 반환한다.
- https://mine-it-record.tistory.com/133

## Functional Interfaces

람다식이 어떻게 자바의 타입 시스템과 잘 맞을까? 각 람다는 인터페이스에 의해 명시된, 주어진 타입에 대응한다.
이 인터페이스는 추상 메소드를 정확히 하나만 가져야 한다. 이런 인터페이스를 `functional interface`라고 한다.

```java
@FunctionalInterface
interface Converter<F, T> {
    T convert(F from);
}

Converter<String, Integer> converter = (from) -> Integer.valueOf(from);
Integer converted = converter.convert("123");
System.out.println(converted); // 123
```

두 번째 추상 메서드를 인터페이스에 선언하려고하면 컴파일러는 에러를 발생시킨다.

## Method and Constructor References

위의 코드 예제는 `static method references`를 활용하여 더 간단해질 수 있다.

```java
Converter<String, Integer> converter = Integer::valueOf;
Integer converted = converter.convert("123");
System.out.println(converted); // 123
```

자바 8은 `::` 키워드를 통해서 메서드의 참조나 생성자를 전달할 수 있도록 해준다.

```java
class Something {
    String startsWith(String s) {
        return String.valueOf(s.charAt(0));
    }
}
```

```java
Something something = new Something();
Converter<String, String> converter = something::startsWith;
String converted = converter.convert("Java");
System.out.println(converted); // "J"
```

`::` 키워드가 생성자와 함께 사용되는 경우 어떻게 되는지 보자.

````java
class Person {
    String firstName;
    String lastName;

    Person() {}

    Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
}

새로운 person을 만드는데 사용되기위한 person factory interface를 만들어보자.

```java
interface PersonFactory<P extends Person> {
    P create(String firstName, String lastName);
}
````

factory를 메뉴얼하게 구현하는 대신에, 생성자 레퍼런스를 붙일 수 있다.

```java
PersonFactory<Person> personFactory = Person::new;
Person person = personFactory.create("Peter", "Parker");
```

`Person::new` 를 통해서 Person 생성자의 레퍼런스를 만들었다. 자바 컴파일러는 자동으로 PersonFactory.create의 시그니쳐와 매칭되는 생성자를 선택한다.

## Lambda Scopes

람다식에서 바깥 스코프 변수들에 접근하는 것은 anonymous objects와 유사하다. local outer scope로부터 final variables에 접근할 수 있다. 뿐만 아니라, 인스턴스 필드와 정적 변수에 접근 가능하다.

### Accessing local variables

람다식의 바깥 스코프의 final 로컬 변수에 접근해보자.

```java
final int num = 1;
Converter<Integer, String> stringConverter = (from) -> String.valueOf(from + num); // num은 final이기 때문에 접근이 가능하다.

stringConverter.convert(2); // 3
```

final로 선언하지 않았더라도 암시적으로 다른 곳에서 사용되지 않는다면 컴파일된다.

```java
int num = 1;
Converter<Integer, String> stringConverter = (from) -> String.valueOf(from + num); // final이 아니지만 암시적으로 final이다.

stringConverter.convert(2); // 3
```

하지만, 다른 곳에서 사용되는 경우 컴파일 에러가 발생한다.

```java
int num = 1;
Converter<Integer, String> stringConverter = (from) -> String.valueOf(from + num);

num = 3;
```

위의 예시는 아래에서 `num = 3` 과 같이 변경하려고 하기때문에 암시적으로 final이 아니기 때문에 컴파일 에러가 발생한다.

## Accessing fields and static variables (필드와 정적 변수에 접근)

지역 변수 대조적으로, 람다 식 내에서 인스턴스 필드와 정적 변수에 읽고 쓸 수 있다.
이 동작은 anonymous objects와 같이 알려져있다.

```java
class Lambda4 {
    static int outerStaticNum;
    int outerNum;

    void testScopes() {
        Converter<Integer, String> stringConverter1 = (from) -> {
            outerNum = 23; // instance field
            return String.valueOf(from);
        };

        Converter<Integer, String> stringConverter2 = (from) -> {
            outerStaticNum = 72; // static field
            return String.valueOf(from);
        };
    }
}
```

## Accessing Default Interface Methods

- 첫번 째 섹션의 formula 예시에서 `Formula` 인터페이스에는 default method인 `sqrt`를 익명 객체를 포함하는 정의했다.
  이 것은 람다식에서 동작하지 않는다.
- default methods는 람다식에서 사용할 수 없다. 왜냐하면 람다식은 인터페이스의 구현이 아니기 때문이다.

```java
Formula formula = (a) -> sqrt(a * 100); // compile error
```

## Built-in Functional Interfaces

- JDK 1.8 API는 많은 내장 함수형 인터페이스를 제공한다.
- 몇몇은 `Comparator`, `Runnable`과 같이 자바의 오래된 버전으로 부터 잘알려진 것들이다.
- 이러한 이미 존재하는 인터페이스들은 `@FunctionalInterface` 어노테이션을 통해서 람다식을 지원하도록 확장되었다.
- Java 8 API는 삶을 더 쉽게해주는 새로운 함수형 인터페이스를 완전히 새롭게 제공한다.
- 이러한 새로운 인터페이스의 몇몇은 `Google Guava` 라이브러리로부터 왔다고 알려져있다.

### Predicates

- Predicates는 하나의 인자를 받아서 boolean을 반환하는 함수이다.
- 이 인터페이스는 predicates를 복잡한 논리 용어 (and, or, negate)로 조합하기 위한 다양한 default methods를 포함한다.

```java
Predicate<String> predicate = (s) -> s.length() > 0;

predicate.test("foo");             // true
predicate.negate().test("foo");    // false - negate는 test의 반대를 반환한다.

Predicate<Boolean> nonNull = Objects::nonNull; // static method reference의 사용
Predicate<Boolean> isNull = Objects::isNull;

Predicate<String> isEmpty = String::isEmpty;
Predicate<String> isNotEmpty = isEmpty.negate();
```

### Functions

Functions는 인자를 하나 받고 결과를 반환하는 함수이다. Default method들은 여러 개의 함수를 체이닝해서 사용할 수 있다.

```java
Function<String, Integer> toInteger = Integer::valueOf;
Function<String, Integer> backToString = toInteger.andThen(String::valueOf);

backToString.apply("123"); // "123"
```

### Suppliers

suppliers는 주어진 generic type의 결과를 반환한다. Functions와 다르게, Suppliers는 인자를 받지 않는다.

```java
Supplier<Person> personSupplier = Person::new;
personSupplier.get(); // new Person
```

### Consumers

컨슈머 (Consumers)는 하나의 입력 인자로부터 수행될 수 있는 연산을 나타낸다.

```java
Consumer<Person> greeter = (p) -> System.out.println("Hello, " + p.firstName);
greeter.accept(new Person("Luke", "Skywalker"));
```

- 위에서 greeter의 메서드로 실행하는 accept는 Consumer 인터페이스의 메서드이다.
- accept 함수는 주어진 입력을 받아 실행하고 종료한다. 여기서 주의깊게 봐야할 점은 반환값이 `void` 라는 것이다.
- 컨슈머라는 것은 입력을 받고 실행만하고 아무런 결과도 반환하지 않는다.

### Comparators

Comparators는 이전 버전의 자바에서도 잘 알려져 있다. 자바 8은 이 인터페이스에 다양한 디폴트 메서드를 추가했다.

```java
Comparator<Person> comparator = (p1, p2) -> p1.firstName.compareTo(p2.firstName);

Person p1 = new Person("John", "Doe");
Person p2 = new Person("Alice", "Wonderland");

comparator.compare(p1, p2); // > 0 보다 큰 값이 나온다.
comparator.reversed().compare(p1, p2); // < 0 보다 작은 값이 나온다.
```

## Optionals

- Optionals은 functional interface가 아니다.
- 자바의 `NullPointerException` 예외를 방지하기 위한 목적으로 만들어졌다.
- `Optional` 은 값이 null 혹은 non-null일 수 있는 값을 위한 `단순한 컨테이너` 이다.
- https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html

```java
Optional<String> optional = Optional.of("bam");

optional.isPresent(); // true - 값이 존재하는지 여부

optional.get(); // "bam" - 값이 존재하면 값을 반환하고, 존재하지 않으면 NoSuchElementException을 던진다.

optional.orElse("fallback"); // "bam" - 값이 존재하면 값을 반환하고, 존재하지 않으면 fallback을 반환한다.

// public void ifPresent(Consumer<? super T> consumer)
// ifPresent는 컨슈머를 전달받아서 값이 존재하면 컨슈머를 실행한다.
// 컨슈머이기때문에 반환값이 void이다.
optional.ifPresent((s) -> System.out.println(s.charAt(0)));
```

## Streams

- `java.util.Stream` 하나 이상의 연산들이 수행될 수 있는 원소들의 시퀀스를 나타낸다.
- 스트림 연산들은 `intermediate` 이거나 `terminal` 이다.
  - `terminal` 연산들은 특정 타입의 결과를 반환한다.
  - `intermediate` 연산들은 스트림을 반환한다. 이는 연산들을 연결할 수 있게 해준다.
- 스트림은 하나의 소스로부터 생성된다. 이 소스는 컬렉션, 배열, I/O 채널, 랜덤 숫자 생성기 등이 될 수 있다. 맵은 스트림을 생성하는데 사용될 수 없다.
- 스트림은 매우 강력해서 별도로 튜토리얼 작성했다고한다. [Java 8 Streams tutorials](http://winterbe.com/posts/2014/07/31/java8-stream-tutorial-examples/)

예시를 보자.

```java
List<String> stringCollection = new ArrayList<>();

stringCollection.add("ddd2");
stringCollection.add("aaa2");
stringCollection.add("bbb1");
stringCollection.add("aaa1");
stringCollection.add("bbb3");
stringCollection.add("ccc");
stringCollection.add("bbb2");
stringCollection.add("ddd1");
```

- 자바 8의 컬렉션은 `Collection.stream()` 혹은 `Collection.parallelStream()` 을 호출함으로써 스트림을 생성할 수 있도록 확장되었다.

아래부터는 가장 흔한 스트림 연산에 대해서 알아본다.

## Filter

- Filter는 스트림의 모든 원소를 필터하기 위한 predicate를 인자로 받는다.
- 이 연산은 intermediate 연산이다. 이는 스트림을 반환한다.
- filter 후에 값을 보기 위해 `ForEach`를 사용할 수 있다.
- ForEach는 Consumer를 받아서 각 filtered된 스트림의 각 원소에 대해서 실행된다.
- ForEach는 terminal 연산이다. 함수의 반환값은 void이다. 그래서 다른 스트림 연산을 호출할 수 없다.

```java
stringCollection
    .stream()
    .filter((s) -> s.startsWith("a")) // predicate
    .forEach(System.out::println); // Consumer, static method reference 사용한 것을 자세히 보자.

// "aaa2", "aaa1"
```

## Sorted

- Sorted는 `intermediate` 연산이다. 이는 스트림을 반환한다.
- 스트림의 정렬된 view를 반환한다.
- 각 원소들은 커스텀 `Comparator`를 전달하지 않았다면 자연스러운 순서로 정렬된다.

```java
stringCollection
    .stream()
    .sorted()
    .filter((s) -> s.startsWith("a"))
    .forEach(System.out::println);

// "aaa1", "aaa2"
```

- 주의해서 봐야할 것은 실제 컬렉션은 정렬되지 않았다는 것이다. `sorted`는 정렬된 view를 반환한다.
- stringCollection의 순서는 변경되지 않는다.

```java
System.out.println(stringCollection);
// "ddd2", "aaa2", "bbb1", "aaa1", "bbb3", "ccc", "bbb2", "ddd1"
```

## Map

- map은 `intermediate` 연산이다. 이는 스트림을 반환한다.
- 각 원소에 대해서 주어진 함수를 적용한 결과를 포함하는 스트림을 반환한다.
- 다음 예시는 각 문자열을 upper-cased 문자열로 변환한다.
- generic type의 결과 스트림은 map에 전달하는 함수의 generic type에 따라 달라진다.

```java
stringCollection
    .stream()
    .map(String::toUpperCase)
    .sorted((a, b) -> b.compareTo(a))
    .forEach(System.out::println);

// "DDD2", "DDD1", "CCC", "BBB3", "BBB2", "AAA2", "AAA1"
```

## Match

- 다양한 Matching 연산은 특정 predicate가 스트림에 매칭되는지 아닌지를 검사하기 위해서 사용된다.
- Match의 모든 연산은 terminal 연산이다. 이는 boolean을 반환한다.

```java
boolean anyStartsWithA =
    stringCollection
        .stream()
        .anyMatch((s) -> s.startsWith("a"));

System.out.println(anyStartsWithA); // true

boolean allStartsWithA =
    stringCollection
        .stream()
        .allMatch((s) -> s.startsWith("a"));

System.out.println(allStartsWithA); // false

boolean noneStartsWithZ =
    stringCollection
        .stream()
        .noneMatch((s) -> s.startsWith("z"));

System.out.println(noneStartsWithZ); // true
```

## Count

- Count는 terminal 연산이다. 이는 long을 반환한다.
- 스트림의 원소의 개수를 반환한다.

```java
long startsWithB =
    stringCollection
        .stream()
        .filter((s) -> s.startsWith("b"))
        .count();

System.out.println(startsWithB); // 3
```

## Reduce

- Reduce는 terminal 연산이다. 스트림의 각 원소들에 주어진 함수를 적용해 결과를 반환한다.
- 결과는 reduced value를 가지고 있는 `Optional`이다.

```java
Optional<String> reduced =
    stringCollection
        .stream()
        .sorted()
        .reduce((s1, s2) -> s1 + "#" + s2);

reduced.ifPresent(System.out::println);
// "aaa1#aaa2#bbb1#bbb2#bbb3#ccc#ddd1#ddd2"
```

## Parallel Streams

- 위에서 언급한 streams는 sequential(순차적) 혹은 parallel(병렬적)로 실행될 수 있다.
- sequential streams는 단일 스레드에서 실행되고, parallel streams는 멀티 스레드에서 동시에 수행된다. (병렬로)
- parallel streams는 내부적으로 fork-join framework를 사용한다.
- https://m.blog.naver.com/tmondev/220945933678

예시를 통해 sequential vs parallel 비교해본다.

먼저 큰 사이즈의 유니크한 원소의 리스트를 만든다.

```java
int max = 1000000;
List<String> values = new ArrayList<>(max);
for (int i = 0; i < max; i++) {
    UUID uuid = UUID.randomUUID();
    values.add(uuid.toString());
}
```

### Sequential Sort

```java
long t0 = System.nanoTime();

long count = values.stream().sorted().count();
System.out.println(count);

long t1 = System.nanoTime();

long millis = TimeUnit.NANOSECONDS.toMillis(t1 - t0);
System.out.println(String.format("sequential sort took: %d ms", millis));

// sequential sort took: 899 ms
```

### Parallel Sort

```java
long t0 = System.nanoTime();

long count = values.parallelStream().sorted().count();
System.out.println(count);

long t1 = System.nanoTime();

long millis = TimeUnit.NANOSECONDS.toMillis(t1 - t0);
System.out.println(String.format("parallel sort took: %d ms", millis));

// parallel sort took: 472 ms
```

위 두 코드조각에서 보듯이 parallel sort가 대략 50% 정도 빠르다.

## Maps

- 위에서 이미 언급했듯이 map은 직접적으로 스트림을 지원하지는 않는다.
- Map에는 `stream()` 메서드가 없지만, `map.keySet().stream()` 혹은 `map.values().stream()` 혹은 `map.entrySet().stream()`을 사용할 수 있다.

```java
Map<String, String> map = new HashMap<>();

for (int i = 0; i < 10; i++) {
    map.putIfAbsent(i, "val" + i); // 키가 없다면 추가
}

// forEach는 consumer를 전달받는다.
map.forEach((id, val) -> System.out.println(val));
```

```java
map.computeIfPresent(3, (num, val) -> val + num);

// map에는 기존에 3이라는 키가 있었고, 그 값은 val3이었다.
// 그래서 val3 + 3 = val33이 되었다.
map.get(3); // val33

// map에는 기존에 9라는 키가 있었고, 그 값은 val9이었다.
// 아래에서는 null을 반환했기 때문에 9라는 키는 null로 바뀌었다.
map.computeIfPresent(9, (num, val) -> null);
map.get(9); // null


// map에 23이라는 키가 없었기 때문에, 23이라는 키와 val23이라는 값을 추가했다.
map.computeIfAbsent(23, num -> "val" + num);
map.containsKey(23); // true

// 3이라는 키가 없다면 3이라는 키와 bam이라는 값을 추가한다.
map.computeIfAbsent(3, num -> "bam");

// 3이라는 키가 이미 있었기 때문에, 3이라는 키와 "bam"이라는 값을 추가하지 않았다.
map.get(3); // val33
```

- map에서 entries를 삭제하는 방법에 대해서 알아본다.

```java
map.remove(3, "val3");
map.get(3); // val33

map.remove(3, "val33");
map.get(3); // null
```

- helpful method

```java
map.getOrDefault(42, "not found"); // not found
```

- map의 entries를 병합하는 것은 쉽다.

```java
map.merge(9, "val9", (value, newValue) -> value.concat(newValue));
map.get(9); // val9

map.merge(9, "concat", (value, newValue) -> value.concat(newValue));
map.get(9); // val9concat
```

## Date API

- 자바 8은 `java.time` 패키지를 통해 새로운 Date API를 제공한다.
- 새로운 Date API는 `Joda-Time` 과 비슷하지만, 동일하지는 않다.

### Clock

- Clock은 current date와 time에 대한 접근을 제공한다.
- Clocks은 timezone을 알고있고, Unixh EPOCH로부텉 밀리세컨즈의 현재 시간을 얻기위해 `System.currentTimeMillis()`를 사용하는 대신에 사용될 수 있다.
- 타임라인에서 동시간대에 일어나는 이벤트는 또한 `Instant` 클래스에 의해 표현될 수 있다.
- Instants는 Legacy인 `java.util.Date`를 생성하기 위해 사용될 수 있다.

```java
Clock clock = Clock.systemDefaultZone();
long millis = clock.millis();

Instant instant = clock.instant();
Date legacyDate = Date.from(instant);   // legacy java.util.Date
```

### Timezones

- Timezones은 `ZoneId`에 의해 표현된다.
- static factory methods에 의해 쉽게 접근할 수 있다.
- Timezones는 지역 시간과 비교하기 위해서 offsets를 제공한다.

```java

// https://docs.oracle.com/javase/8/docs/api/java/time/ZoneId.html#getAvailableZoneIds--
System.out.println(ZoneId.getAvailableZoneIds());
// prints all available timezone ids

ZoneId zone1 = ZoneId.of("Europe/Berlin");
ZoneId zone2 = ZoneId.of("Brazil/East");
System.out.println(zone1.getRules());
System.out.println(zone2.getRules());

// ZoneRules[currentStandardOffset=+01:00]
// ZoneRules[currentStandardOffset=-03:00]
```

### LocalTime

- LocalTime은 timezone 없이 시간을 표현한다.
- 예를들어 10pm or 17:30:15

```java
LocalTime now1 = LocalTime.now(zone1);
LocalTime now2 = LocalTime.now(zone2);

System.out.println(now1.isBefore(now2));  // false

long hoursBetween = ChronoUnit.HOURS.between(now1, now2);
long minutesBetween = ChronoUnit.MINUTES.between(now1, now2);

System.out.println(hoursBetween);      // -3
System.out.println(minutesBetween);    // -239
```

- https://docs.oracle.com/javase/8/docs/api/java/time/temporal/ChronoUnit.html
- ChronoUnit은 period 특정 시점의 간격에 대한 단위를 나타내기 위해 사용하는 것 같다.
- LocalTime은 시간 문자열 파싱을 포함해서, 새로운 인스턴스를 만들기 위해 심플화한 다양한 factory methods를 제공한다.

```java
LocalTime late = LocalTime.of(23, 59, 59);
System.out.println(late); // 23:59:59

DateTimeFormatter germanFormatter =
        DateTimeFormatter
                .ofLocalizedTime(FormatStyle.SHORT)
                .withLocale(Locale.GERMAN);

LocalTime leetTime = LocalTime.parse("13:37", germanFormatter);
System.out.println(leetTime); // 13:37
```

## LocalDate

- LocalDate는 distinct date를 나타낸다.
- 불변하고 LocalTime과 완전 유사하게 동작한다.
- 아래 예시에서는 date에 일자를 더하고 빼고, 달과 년도를 구하는 것을 보여준다.
- **주의해서 볼점은 불변하기 때문에 모든 연산은 새로운 instant를 반환한다는 것이다.**

```java
LocalDate today = LocalDate.now();
LocalDate tomorrow = today.plus(1, ChronoUnit.DAYS);
LocalDate yesterday = today.minusDays(2);

LocalDate independenceDay = LocalDate.of(2014, Month.JULY, 4);
DayOfWeek dayOfWeek = independenceDay.getDayOfWeek();
System.out.println(dayOfWeek); // FRIDAY
```

- 문자열을 LocalDate로 파싱

```java
DateTimeFormatter germanFormatter =
        DateTimeFormatter
                .ofLocalizedDate(FormatStyle.MEDIUM)
                .withLocale(Locale.GERMAN);

LocalDate xmas = LocalDate.parse("24.12.2014", germanFormatter);
System.out.println(xmas); // 2014-12-24
```

## LocalDateTime

- LocalDateTime은 날짜와 시간을 나타낸다.
- LocalDateTime은 불변(immutable)하고 LocalTime과 LocalDate와 유사하게 동작한다.

```java
LocalDateTime sylvester = LocalDateTime.of(2014, Month.DECEMBER, 31, 23, 59, 59);

DayOfWeek dayOfWeek = sylvester.getDayOfWeek();
System.out.println(dayOfWeek); // WEDNESDAY

Month month = sylvester.getMonth();
System.out.println(month); // DECEMBER

long minuteOfDay = sylvester.getLong(ChronoField.MINUTE_OF_DAY);
System.out.println(minuteOfDay); // 1439
```

- 타임존 정보를 추가해서 `instant`로 변환될 수 있다.
- instant는 쉽게 legacy date API와 호환될 수 있다.

```java
Instant instant = sylvester
        .atZone(ZoneId.systemDefault())
        .toInstant();

Date legacyDate = Date.from(instant);
System.out.println(legacyDate); // Wed Dec 31 23:59:59 CET 2014
```

- datetime의 Formatting도 잘 동작한다.
- 미리 정의된 pattern 대신에 커스텀 패턴을 사용할 수 있다.

```java
DateTimeFormatter formatter =
        DateTimeFormatter
                .ofPattern("MMM dd, yyyy - HH:mm");

LocalDateTime parsed = LocalDateTime.parse("Nov 03, 2014 - 07:13", formatter);

String string = formatter.format(parsed);
System.out.println(string); // Nov 03, 2014 - 07:13
```

**`java.text.NumberFormat`과 다르게 새로운 `DateTimeFormatter`는 immutable하고 thread-safe 하다.**

## Annotations

- 자바 8에서 어노테이션은 repeatable 할 수 있게 되었다.
- 자바 8은 `@Repeatable` 어노테이션을 사용해서 어노테이션을 반복할 수 있게 했다.

```java
@interface Hints {
    Hint[] value();
}

@Repeatable(Hints.class)
@interface Hint {
    String value();
}
```

### Variant 1: Using the container annotation (old school)

```java
@Hints({@Hint("hint1"), @Hint("hint2")})
class Person {}
```

### Variant 2: Using the repeatable annotation (new school)

```java
@Hint("hint1")
@Hint("hint2")
class Person {}
```

- variant 2를 사용하면 자바 컴파일러는 암시적으로 `@Hints` 어노테이션을 추가한다.
- 중요한 점은 어노테이션 정보를 리플렉션을 통해서 읽는다는 것이다.

```java

Hint hint = Person.class.getAnnotation(Hint.class);
System.out.println(hint); // null

Hints hints1 = Person.class.getAnnotation(Hints.class);
System.out.println(hints1.value().length); // 2

Hint[] hints2 = Person.class.getAnnotationsByType(Hint.class);
System.out.println(hints2.length); // 2
```

- variant 2에서 `@Hints` 어노테이션을 Person 클래스에 사용하지 않았지만 `getAnnotation(Hints.class)` 를 통해서 읽을 수 있다.
- 더 간편한 방법으로 `getAnnotationsByType(Hint.class)`를 사용할 수 있다. 이렇게 하면 모든 `@Hint` 어노테이션에 직접 접근이 가능하다.
- 게다가, 자바 8에서 어노테이션의 사용이 새로운 두 타겟으로 확장되었다.

```java
@Target({ElementType.TYPE_PARAMETER, ElementType.TYPE_USE})
@interface MyAnnotation {}
```
