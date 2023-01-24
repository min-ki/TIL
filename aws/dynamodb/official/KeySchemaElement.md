# [KeySchemaElement](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_KeySchemaElement.html)

키 스키마의 단일 요소를 나타낸다. 키 스키마는 속성이 테이블의 primary key를 구성하거나, 인덱스의 키 속성인지를 지정한다.

KeySchemaElement는 정확히 하나의 primary key의 속성을 나타낸다. 예를들어, 간단한 primary key는 하나의 KeySchemaElement로 표현된다. 복합 primary key는 파티션 키를 위해 하나의 KeySchemaElement와 정렬 키를 위해 다른 KeySchemaElement가 필요하다.

KeySchemaElement는 반드시 스칼라, 최상위 속성이어야 한다. 데이터 타입은 String, Number, Binary 중 하나여야 한다. 속성은 List 혹은 Map안에 중첩될 수 없다.

## Contents

### AttributeName

- Key attribute의 이름
- String 타입이다.
- 최소 1자, 최대 255자의 길이 제약이 있다.
- 필수

### KeyType

- HASH: 파티션 키
- RANGE: 정렬 키
- 필수

```clojure
:KeySchema           [{:AttributeName "속성명"
                       :KeyType       "HASH"}]
```

```clojure
:KeySchema           [{:AttributeName "속성명"
                       :KeyType       "RANGE"}]
```

### Note

아이템의 파티션 키는 hash attribute라고 알려져있다. "hash attribute"라는 용어는 여러 파티션들 간에 데이터를 분산시키기위해 내부적으로 해시 함수를 사용하는 것으로부터 유래했다고 한다.

아이템의 정렬 키는 range attribute라고 알려져있다. "range attribute"라고 불리는 용어는 다이나모DB가 아이템을 정렬 키 값의 정렬된 순서를 기준으로 동일한 파티션에 물리적으로 가깝게 저장하기 때문이다.
