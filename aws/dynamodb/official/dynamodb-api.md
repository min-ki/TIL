# DynamoDB API

Amazon DynamoDB를 사용하려면, 몇가지 API 동작을 알아야한다. 아래는 이러한 동작들을 카테고리별로 나눠놓았다.

- Topics
  - Control plane
  - Data plane
  - DynamoDB Streams
  - Transactions

## Control plane

Control plane operations는 DynamoDB 테이블을 만들고 관리하게 해준다. 그리고, 인덱스, 스트림, 다른 테이블과의 의존관계 등을 설정하는데 사용한다. 아래는 Control plane의 operation들이다.

- CreateTable: 새로운 테이블을 생성. 선택적으로, 하나 이상의 세컨더리 인덱스를 만들 수 있고, 테이블에 DynamoDB 스트림을 활성화 할 수 있다.
- DescribeTable: primary key schema, 처리량 설정, 인덱스 정보와 같은 테이블에 대한 정보를 반환.
- ListTables: 테이블 목록의 이름들을 반환.
- UpdateTable: 테이블의 설정 혹은 인덱스를 수정한다. 테이블에 새로운 인덱스를 생성하거나 삭제하고, 스트림 설정을 변경할 수 있다.
- DeleteTable: 테이블과 연관된 객체들을 삭제한다.

## Data plane

Data plane은 CRUD(create, read, update, delete) 액션을 테이블에 수행하도록 해준다. 몇몇 data plane 작업은 데이터를 세컨더리 인덱스로부터 조회한다.
또한, `PartiQL`을 사용해서 테이블에 대한 쿼리를 수행할 수 있다.

### PartiQL - a SQL-compatible query language

- ExecuteStatement: 테이블로부터 여러개의 아이템을 읽는다. 테이블에 하나의 아이템에 대해 쓰기나 업데이트를 할 수 있다. 단일 아이템을 쓰거나 업데이트할때는, 반드시 primary key 속성을 명시해야한다.
- BatchExecuteStatement: 테이블로부터 쓰기, 수정, 읽기 작업을 수행한다. 이 작업은 ExecuteStatement보다 효율적인데, 왜나하면 애플리케이션이 데이터를 읽고 쓰는데 한번의 네트워크 라운드 트립만 필요하기 때문이다.

### Class APIs

**Creating data**

- PutItem
- BatchWriteItem

**Reading data**

- GetItem
- BatchGetItem
- Query
- Scan

**Updating data**

- UpdateItem

**Deleting data**

- DeleteItem
- BatchWriteItem

## DynamoDB Streams

- ListStreams
- DescribeStream
- GetShardIterator
- GetRecords

## Transactions

트랜잭션은 ACID; atomicity, consistency, isolation, durability를 제공함으로써 애플리케이션이 쉽게 데이터 정합성을 유지할 수 있도록 해준다.
PartiQL 혹은 classic API를 사용해서 트랜잭션을 수행할 수 있다.
