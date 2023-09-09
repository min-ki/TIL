# Kotlin Basic

- 프로그램 진입점은 main 함수이다.

```kotlin
// 프로그램 진입점
fun main() {}
```

## val, var

- val: 한번만 할당 가능한 변경 불가능한 변수
- var: 여러 번 재할당이 가능한 변수
    - 여러 번 값을 변경할 수 있지만, 타입을 변경할 수는 없다.

```kotlin
var x = 10
x = 25 // 가능
x = 25.5 // 정수타입 -> 부동소수점 변경 불가능

## 함수 (fun)

```kotlin
fun 함수이름(arg1: Type1, arg2: Type2, ...): ReturnType {
    return result
}
```

- 코틀린은 파라미터의 타입을 추론한다. ->  파라미터 각각에 타입 명시 필요

### 함수 축약형

```kotlin
fun 함수이름(arg1: Type1, arg2: Type2, ...): ReturnType = 식(expression)
```
- 파라미터의 타입은 추론하지 못하지만, 식의 타입을 추론할 수 있기 때문에 반환 타입을 생략할 수 있다.



