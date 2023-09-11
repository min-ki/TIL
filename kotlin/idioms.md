# Kotlin Idioms(관용구)

코틀린에서 자주 사용되는 관용구

## Create DTOs (POJOs/POCOs)

- POJO: Plain Old Java Object
- POCO: Plain Old CLR Object

```kotlin
data class Customer(val name: String, val email: String)
```

data class로 정의한 위의 Customer 클래스는 다음과 같은 기능을 제공한다.

- 프로퍼티에 대한 getters, setters를 제공한다. (var 변수에 대해서)
- equals()
- hashCode()
- toString()
- copy() -> copy on write?
- component1(), component2(), ...


