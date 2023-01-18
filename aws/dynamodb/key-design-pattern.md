# Amazon DynamoDB 키 디자인 패턴 Webinar

- https://www.youtube.com/watch?v=I7zcRxHbo98

## 중요 컨셉

### Table Structure

<img src="images/table-structure.jpg">

- 가장 큰 단위는 테이블
- 하나의 테이블에는 무한대에 가까운 아이템을 넣을 수 있다. (RDBMS의 row)
- 아이템은 키와 속성으로 구성
- RDBMS에서는 column이라고 하는데 DynamoDB는 attribute라는 용어를 사용한다.
- PK 덕분에 낮은 지연시간으로 아이템을 찾을 수 있다.
- Key
  - Partition Key (PK): 내가 찾고자 하는 아이템이 어떤 파티션에 있는지 where로 찾을 수 있게 해주는 키
    - 등호연산자, 범위 연산자, begins with, between과 같은 연산자를 사용할 수 있다.
  - Sort Key (SK)
    - 오름차순, 내림차순 정렬로 데이터를 조회할 수 있다.

### Primary Key

<img src="images/primary-key.jpg">

- PK + SK를 합쳐서 Primary Key라고 한다.
- 오직 Primary Key로만 검색이 가능하다. (Scan은 제외)
- Primary Key가 없으면 조회가 불가능하다. => 그래서, Access Pattern이 RDBMS보다 중요하다.

### 데이터베이스 스케일링

<img src="images/database-scaling.jpg">

- 전통적인 RDBMS는 보통 스케일업
- NoSQL은 많은 샤드로 스케일 아웃 전략을 사용

## 제약 조건

## Tenet

## 디자인 패턴 및 비정규화

## 싱글 테이블 디자인 예제
