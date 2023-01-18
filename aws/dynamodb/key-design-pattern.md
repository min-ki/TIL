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

### 작업 방식

<img src="images/table-automatically-managed.jpg">

- 테이블 단위로 작업을 하면 DynamoDB가 내부적으로 나머지를 알아서 잘 처리한다.

  - 여러 파티션에 나누어서 저장하고, 이러한 파티션의 관리는 DynamoDB가 알아서 해준다.

- 각 파티션이란 단위는 다음과 같은 제약사항을 가진다.
  - 초당 1000개의 쓰기 (1K WCU)
  - 초당 3000개의 읽기 (3K RCU)
  - 10GB의 데이터 저장만 가능
  - **Key Design 할때 기억해야할 중요한 조건 중 하나이다.**

### 수평적 스케일링

<img src="images/horizontal-scale-out.jpg">

- 트래픽이 증가하면서 파티션의 개수가 늘어난다.
  - 각 파티션은 제약사항이 있으므로 처리량은 늘어날 수 없다.
- **여러 개의 파티션이 골고루 사용될 수 있도록 키를 디자인하는 점이 중요하다.**

### 아이템 분포 (이상적 경우)

<img src="images/item-distribution-1.jpg">
<img src="images/item-distribution-2.jpg">

- PK는 OrderId
- 단순히 1,2,3 을 통해서 파티션을 분할한다면 1번 파티션에 모든 데이터가 저장된다. 나머지 파티션은 놀게 되므로 비효울적이 된다. 그래서 DynamoDB는 PK에 해시함수를 적용해서 파티션을 선택하여 저장한다.

### 데이터 복제

<img src="images/data-replication.jpg">

- 파티션은 3개의 가용영역(AZ)에 복제된다.

## 제약 조건

## Tenet

## 디자인 패턴 및 비정규화

## 싱글 테이블 디자인 예제
