# 자바 어노테이션

- https://docs.oracle.com/javase/tutorial/java/annotations/index.html

# 어노테이션 (Annotations)

- 어노테이션은 메타데이터의 한 형태
- 어노테이션은 몇 가지의 사용 사례를 가지고 있다.
  - Information for the compiler - 어노테이션은 컴파일러가 에러를 발견하고 경고를 내도록 사용될 수 있다.
  - Compile-time and deployment-time processing - 소프트웨어 툴들은 어노테이션 정보를 코드, XML 파일 등을 생성할 수 있다.
  - Runtime processing - 몇 어노테이션들은 런타임에 접근할 수 있다.

# Annotations Basics

## The Format of an Annotation

- 어노테이션은 @로 시작하고, 그 뒤에 어노테이션의 이름이 온다.

```java
@Entity
```

- @를 at sign character라고 부르나보다.
- @는 컴파일러에게 어노테이션임을 알려준다.

```java
@Override
void mySuperMethod() { ... }
```

- 어노테이션은 이름이 있거나, 없을 수 있는 요소들을 포함할 수 있다.

```java
@Author(
    name = "Benjamin Franklin",
    date = "3/27/2003"
)
class MyClass { ... }
```

혹은

```java
@SuppressWarning(value = "unchecked")
void myMethod() { ... }
```

- 만약 요소가 하나만 있고, 이름이 value 라면 이름을 생략할 수 있다.

```java
@SuppressWarning("unchecked")
void myMethod() { ... }
```

- 요소가 없는 어노테이션은, 괄호를 생략할 수 있다. (예: @Override)
- 동일한 선언에 여러 어노테이션을 사용할 수 있다.

```java
@Author(name = "Jane Doe")
@EBook
class MyClass { ... }
```

- 어노테이션이 동일한 타입을 가진다면, 이 어노테이션은 repeating annotation로 호출된다.

```java
@Author(name = "Jane Doe")
@Author(name = "John Smith")
class MyClass { ... }
```

- Repeating annotations는 Java SE 8 부터 지원된다.
- 아래에서 더 자세히 봐보자.

- 어노테이션의 타입은 `java.lang` 혹은 `java.lang.annotation`에 정의된 타입 중 하나가 될 수 있다.
- `Override`와 `SuppressWarnings`는 predefined Java annotations이다.
- 직접 어노테이션을 정의해서 사용할 수 있다.
- 위의 Author와 EBook은 사용자 정의 어노테이션이다.

## Where Annotations Can be Used

어노테이션이 사용될 수 있는 곳은? 어노테이션은 선언부에 사용될 수 있다.

- declaration of classes, fields, methods
- other program elements

```java

// 1. Class instance creation expression:
new @Interned MyObject();

// 2. Type cast
myString = (@NonNull String) str;

// 3. implements clause:
class UnmodifiableList<T> implements
    @Readonly List<@Readonly T> { ... }

// 4. Thrown exception declaration:
void monitorTemperature() throws
    @Critical TemperatureException { ... }
```

# Declaring an Annotation Type

전통적으로 소프트웨어 그룹은 중요한 정보를 클래스의 몸통에 주석으로 남겼다.

```java
public class Generation3List extends Generation2List {
    // Author: John Doe
    // Date: 3/17/2002
    // Current revision: 6
    // Last modified: 4/12/2004
    // By: Jane Doe
    // Reviewers: Alice, Bill, Cindy

    // class code goes here
}
```

주석에 똑같은 메타데이터를 추가하기위해서, 어노테이션을 사용할 수 있다. 어노테이션 정의는 `@interface` 키워드를 사용한다.

```java
@interface ClassPreamble {
    String author();
    String date();
    int currentRevision() default 1;
    String lastModified() default "N/A";
    String lastModifiedBy() default "N/A";
    // Note use of array
    String[] reviewers();
}
```

위와 같이 어노테이션을 정의하면 다음과 같이 사용할 수 있다.

```java
@ClassPreamble (
    author = "John Doe",
    date = "3/17/2002",
    currentRevision = 6,
    lastModified = "4/12/2004",
    lastModifiedBy = "Jane Doe",
    reviewers = {"Alice", "Bob", "Cindy"}
)
public class Generation3List extends Generation2List {

}
```

> 어노테이션의 정보를 Javadoc-generated 문서에 나타내기 위해서는, `@Documented` 어노테이션을 사용해야 한다는 것 잊지말자.

```java
import java.lang.annotation.*;

@Documented // 이 어노테이션을 붙여줘야 Javadoc에 나타난다.
@interface classPreamble {
    // Annotation element definitions
}
```

# Predefined Annotation Types

Java SE API에 미리 정의된 어노테이션 타입들의 목록

일부 어노테이션 타입들을 자바 컴파일러를 위해 사용되고, 일부는 다른 어노테이션 타입을 위해 사용된다.

## Annotation Types Used by the Java Language

- `java.lang`에 정의된 predefined annotation types는 다음과 같다.
  - `@Deprecated`
  - `@Override`
  - `@SuppressWarnings`

### @Deprecated

- 이 어노테이션은 컴파일러에게 해당 요소가 더 이상 사용되지 않는다는 것을 알려준다.
- 이 어노테이션으로 마킹된 메서드나 클래스, 필드 등을 사용한다면 컴파일러에서 경고를 발생시킨다.
- 이 어노테이션에는 `@Documented`가 붙어있어 Javadoc에도 나타난다. (deprecated되었다고 나타난다.)

```java
@Documented
@Retention(value=RUNTIME)
@Target(value={CONSTRUCTOR,FIELD,LOCAL_VARIABLE,METHOD,PACKAGE,PARAMETER,TYPE})
public @interface Deprecated
```

### @Override

- 이 어노테이션은 컴파일러에게 해당 메서드가 오버라이드되는 메서드임을 알려준다.
- 어노테이션 정의를 보면 `@Target`이 `METHOD`로 되어있는데, 이는 오버라이드되는 메서드에만 사용할 수 있다는 것을 의미한다.
- 메서드를 오버라이딩할때 이 어노테이션을 사용하는 것이 필수는 아니지만, 사용하면 컴파일러가 오버라이드가 제대로 되었는지 검사해준다. 그러니까 사용하는 것이 좋다 ⭐️

```java
@Target(value=METHOD)
@Retention(value=SOURCE)
public @interface Override
```

### @SuppressWarnings

- 이 어노테이션은 컴파일러에게 경고를 보여주지 말라고 알려주는 것이다.
- 예를들어, deprecated된 메서드를 사용해서 경고가 발생한다면, 이 어노테이션을 사용해서 경고를 보이지 않게 할 수 있다.

```java
@SuppressWarnings("deprecation")
void useDeprecatedMethod() {
    // deprecation warning
    // deprecate 경고가 나타나지 않는다.
    objectOne.deprecatedMethod();
}
```

- 모든 컴파일러의 경고는 카테고리에 속해있다.
- 자바 언어 스펙에 컴파일러 경고는 크게 두 개의 카테고리로 나눈다.
  1. deprecation
  2. unchecked

unchecked warning은 제네릭 문법이 만들어지기 전에 작성된 레거시 코드를 사용할 때 발생할 수 있다.

여러 개의 경고 카테고리를 종료할 때는 다음과 같이 사용할 수도 있다.

```java
@SuppressWarning({"unchecked", "deprecation"})
```

### @SafeVarargs

- Java 1.5부터 소개된 가변인자 (varargs)에 대한 경고를 억제하는 어노테이션이다.
- varagrs는 다음과 같이 생겼다.

```java
public String concat(String... strings) {
    // ...
}

concat("a", "b", "c"); // 여러 인자를 가변적으로 전달할 수 있다.
```

- 그래서 경고는 언제 발생하나? 이 블로그에 자세히 써있다. https://icarus8050.tistory.com/88
  - 가변인자와 제네릭을 같이 사용하면 문제가 발생할 수 있다.
- 이펙티브 자바 32번 Item을 보자.
- 자바 8에서는 오직 정적 메서드와 final 인스턴스 메서드에만 사용할 수 있다.
- 자바 9에서는 private 인스턴스 메서드에도 사용할 수 있다.

### @FunctionalInterface

- 자바 8에서 소개된 이 어노테이션은, 타입 선언이 funtional interface가 되도록 의도되었는지를 나타낸다.

## Annotations That Apply to Other Anotations

- `meta-annotations`라고도 불린다.
- 다른 어노테이션에 적용할 수 있는 어노테이션을 말한다.
- `java.lang.annotation`에 정의된 몇몇의 meta-annotation 타입들이 있다.

### @Retention

- 마킹된 어노테이션이 어떻게 저장될지 명시하는 어노테이션이다.
- 어노테이션을 어떻게 저장할지는 다음과 같이 세 가지 방법으로 나눌 수 있다.

  - `RetentionPolicy.SOURCE` : 소스코드에서만 확인이 가능하고 컴파일 후에는 사라진다.
  - `RetentionPolicy.CLASS` : 컴파일 시점에 컴파일러는 확인이 가능하지만, JVM (Runtime) 에서는 확인이 불가능하다.
  - `RetentionPolicy.RUNTIME` : JVM(Runtime) 에서도 확인이 가능하다.

- 이 어노테이션은 왜 필요했었을까? https://stackoverflow.com/questions/37064357/whats-the-reason-for-java-lang-annotation-retention
  - 결국, 예전에는 이 어노테이션을 처리하는 리플랙션 등이 매우 느렸기 때문에, 성능을 위해 이런 RetentionPolicy를 만들었다.

### @Documented

- 이 어노테이션을 사용하면, 어노테이션 정보가 javadoc에 포함된다.
- 기본설정은, 어노테이션은 javadoc에 포함되지 않는다.

### @Target

이 어노테이션은 어노테이션이 적용될 수 있는 대상을 제한할 수 있다. target annotation은 다음 타입들을 가질 수 있다.

- `ElementType.ANNOTATION_TYPE` : 어노테이션 타입
- `ElementType.CONSTRUCTOR` : 생성자
- `ElementType.FIELD` : 필드
- `ElementType.LOCAL_VARIABLE` : 지역변수
- `ElementType.METHOD` : 메서드
- `ElementType.PACKAGE` : 패키지
- `ElementType.PARAMETER` : 매개변수
- `ElementType.TYPE` : 타입

여러 개를 지정하고 싶다면 다음과 같이 할 수 있다.

```java
@Target(value={CONSTRUCTOR,FIELD,LOCAL_VARIABLE,METHOD,PACKAGE,PARAMETER,TYPE})
```

`@Target`에 동일한 ElementType이 여러 번 지정되면, 컴파일 에러가 발생한다.

```java
// FIELD가 2번 나타나서 컴파일 에러가 발생한다.
@Target({ElementType.FIELD, ElementType.METHOD, ElementType.FIELD})
public @interface Bogus {
    ...
}
```

### @Inherited

- 이 어노테이션을 사용하면, 자식 클래스에서 부모 클래스의 어노테이션을 상속받을 수 있다.
- 이 어노테이션은 클래스에만 사용할 수 있다.

### @Repeatable

- 자바 8에서 소개된 어노테이션으로, 반복적으로 어노테이션을 사용할 수 있게 해준다.

# Type Annotations and Pluggable Type Systems

자바 8 이전에는, 어노테이션은 선언부에만 사용할 수 있었다. 하지만, 자바 8부터는 어노테이션이 어떠한 타입에도 적용할 수 있게 되었다.

이 말은, 타입을 사용하는 곳은 어디는 어노테이션을 사용할 수 있다는 뜻이다.

Type annotations은 더 강력한 타입 체킹을 할 수 있게 해준다. 예를 들어, `@NonNull` 어노테이션을 사용하면, null이 아닌 타입을 사용할 수 있게 해준다.

```java
@NonNull String str;
```

위와 같은 코드를 컴파일할때, 명령어에 `-Xlint:all`을 추가하면, null이 아닌 타입을 사용하지 않았을 때 경고를 준다.

```java
javac -Xlint:all Test.java
```

우리는 각기 다른 종류의 에러를 검사하는 여러 타입 검사 모듈을 사용할 수 있다. 이러한 방식을 통해, 자바의 타입 시스템 위에 특정한 검사를 언제, 어디서 원하는 곳에서 할 수 있도록 추가할 수 있다.

타입 어노테이션의 현명한 사용과 pluggable type checkers와 함께라면, 더 강력하고 에러가 덜 발생하는 코드를 작성할 수 있다.

많은 경우에, 우리는 우리의 타입 검사 모듈을 작성하지 않을 것이다. 이미 많은 서드파티 타입 검사 모듈이 존재한다. 예를들어, University of Washington 대학에서 만든 Checker Framework와 같은 것들을 사용하고 싶을 수도 있다. 이 프레임워크는 NonNull 모듈을 포함하고, 뿐만아니라 정규 표현식 모듈, 뮤텍스 락 모듈을 포함한다. 궁금하다면 https://checkerframework.org/ 이걸 읽어보자.

# Repeating Annotations

선언부나, 타입에 동일한 어노테이션을 반복해서 적용하기 원하는 상황이 있을 수 있다. 자바 8부터, repeating annotations은 이것을 가능하게 한다.

첫번 째 예시로, 특정한 시간 혹은 주어진 시간에 메서드를 실행하게 하는 타이머 서비스를 작성하고 있을 때 여러 개의 시간을 적용하고 싶을 수 있을 것이다. 이때 아래와 같이 할 수 있도록 해준다.

```java
@Schedule(dayOfMonth="last")
@Schedule(dayOfWeek="Fri", hour="23")
public void doPeriodicCleanup() { ... }
```

두번 째 예시로, 권한을 처리하는 경우가 있다.

```java
@Alert(role="Manager")
@Alert(role="Administrator")
public class UnauthorizedAccessException extends Exception { ... }
```

호환성 문제로 인해, repeating annotations은 자바 컴파일러에 의해 자동으로 생성되는 `container annotation`에 저장되어진다.

컴파일러가 이 작업을 하기 위해서, 두개의 선언부가 코드에서 필요하다.

## Step 1: Declare a Repeatable Annotation Type

```java
import java.lang.annotation.Repeatable;

@Repeatable(Schedules.class)
public @interface Schedule {
    String dayOfMonth() default "first";
    String dayOfWeek() default "Mon";
    int hour() default 12;
}
```

- `@Repeatable` meta-annotation의 값은 부모, 즉 자바 컴파일러가 repeating annotations을 저장하기 위해 생성해야하는 컨테이너 어노테이션의 타입이다.
- 이 예제에서는, containing annotation type는 Schedules가 되고, @Schedule 어노테이션이 @Schedules 어노테이션에 저장된다.

## Step 2: Declare the Containing Annotation Type

- containing annotation type은 반드시 array type인 value element를 가져야 한다.
- array type의 component type은 반드시 repeatable annotation type이 되어야 한다.
  - 배열 앞에 오는 타입을 컴포넌트 타입이라고 하나보다.
- `Schedules` containing annotation type을 위한 선언은 다음과 같다.

```java
public @interface Schedules {
    Schedule[] value(); // 앞의 Schedule[]이 component type이다.
}
```

## Retrieving Annotations (어노테이션 목록을 가져오기)

어노테이션 목록을 획득하기 위해 사용될 수 있는 몇가지 메서드들이 Reflection API에 있다.
`AnnotatedElement.getAnnotation(Class<T>)` 와 같이, 하나의 어노테이션을 반환하는 메서드들의 동작은 변경되지 않는다. 즉, 요청된 타입의 어노테이션이 있다고, 하나의 어노테이션만 있다면 해당 어노테이션을 반환한다. **만약, 요청된 타입에 어노테이션이 여러 개 있다면, 처음으로 발견된 어노테이션을 반환한다.** 이러한 방식으로, 레거시 코드가 계속해서 동작한다.

한번에 다수의 어노테이션을 반환하기 위한 컨테이너 어노테이션을 통해 스캔을 할 수 있는 다른 메서드들은 자바 8에서 소개되었다.

- `AnnotatedElement.getAnnotationsByType(Class<T>)`
  - 연결된 어노테이션이 없는 경우 길이가 0인 배열을 반환한다.
  - https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/AnnotatedElement.html#getAnnotationsByType-java.lang.Class-

## Design Considerations

어노테이션 타입을 디자인할 때, 반드시 타입의 어노테이션들의 카디널리티(cardinality)를 고려해야한다. 즉, 어노테이션 타입이 반복될 수 있는지, 아니면 하나만 존재할 수 있는지를 결정해야한다. 또한, `@Target` meta annotations을 사용해서 어노테이션 타입이 어디에 사용될 수 있는지를 제한할 수 있다.

이러한 디자인 고려사항들을 지키는 것은 프로그래머가 어노테이션을 잘 사용하도록 해줄 수 있다.

# 참고자료

- https://reflectoring.io/java-annotation-processing/#annotation-basics
- https://docs.oracle.com/javase/1.5.0/docs/guide/language/annotations.html
- https://docs.oracle.com/javase/8/docs/api/java/lang/annotation/Documented.html

```

```
