# Variables

```dart
var name = 'Bob';
```

- 변수 선언은 `var` 키워드를 사용한다.
- 변수는 참조(Reference)를 저장한다.
- 위의 예시에서, `name`은 String 객체를 참조하고 그 참조객체는 값으로 `Bob`을 가진다.
- name 변수는 String 타입을 가진다고 추론한다.

만약 하나의 타입만 가지지않는다면 `Object` 타입 (또는 `dynamic` 타입)을 사용한다.

```dart
Object name = 'Bob';
```

다른 옵션은 명시적으로 타입을 적어주는 것이다.
```dart
String name = 'Bob';
```

> Dart의 style guide는 지역 변수는 타입 어노테이션을 사용하기보다는 var를 사용하는 것을 추천한다.

## Null safety

- 다트 언어는 null safety를 지원한다.
- 컴파일 시점에 null safety를 검사한다.
- 그래서 다트 언어는 런타임 시점에 null 관련 오류를 발생시키지 않는다.

```dart
String? name // Nullable type. null 또는 string을 가질 수 있다.

String name // Non-nullable type. null을 가질 수 없다.
```

- Nullable 타입은 `?`를 붙여서 표시한다.
- Non-nullable 타입은 `?`를 붙이지 않는다.
- Nullable 타입의 기본값은 null이다.

## Default value
초기화되지않은 nullable 변수는 기본값으로 null을 가진다.

```dart
int? lineCount; // null이 기본값
assert(lineCount == null);
```

null safe한 변수는, 반드시 사용하기전에 초기화되어야한다.

```dart
int lineCount = 0;
```

선언과 초기화는 따로 할 수 있다.

```dart
int lineCount;

if (weLikeToCount) {
  lineCount = countLines();
} else {
  lineCount = 0;
}

print(lineCount);
```

## Late variables

```dart

// late키워드를 사용해 변수를 선언하면 실제로 temperature 변수가 사용될때까지 초기화를 미룰 수 있다.
// 만약 temperature 변수를 사용안하면 readThermometer() 함수는 호출되지 않는다.
late String temperature = readThermometer(); 
```

## Final and const

- final 변수는 한번만 할당할 수 있는 변수
- const는 컴파일 시점에 알려진 상수를 선언할 때 사용한다.

```dart
final name = 'Bob'; // 타입 없이 사용할 수 있다. 
final String nickname = 'Bobby'; // 타입과 함께 사용 가능

name = 'Alice'; // 에러 발생 _ 할당은 한번만 할 수 있다.
```

```dart
const bar = 1000000;
const double atm = 1.01325 * bar;
```

```dart

const Object i = 3;
const list = [i as int]; // typecast
const map = {if (i is int) i: 'int'}
const set = {if (list is List<int>) ...list}; // spread operator도 있다.
```


# Reference
- https://dart.dev/language/variables