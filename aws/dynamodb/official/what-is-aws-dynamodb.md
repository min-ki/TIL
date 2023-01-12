# What is Amazon DynamoDB?

## How it works

### Core components of Amazon DynamoDB

이 문서를 읽어보자. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html

> In DynamoDB, tables, items, and attributes are the core components that you work with. 
DynamoDB에서, 테이블, 아이템, 속성이 핵심 컴포넌트이다.

> A table is a collection of items, and each item is a collection of attributes. 

테이블은 아이템의 컬렉션이다. 각 아이템은 속성들의 컬렉션이다.

> DynamoDB uses primary keys to uniquely identify each item in a table and secondary indexes to provide more querying flexibility.

DynamoDB는 테이블의 아이템을 고유하게 식별하기 위해 기본 키를 사용한다. 그리고 세컨더리 인덱스를 사용하여 더 많은 쿼리 유연성을 제공한다.

> You can use DynamoDB Streams to capture data modification events in DynamoDB tables.

DynamoDB 테이블의 데이터 수정 이벤트를 캡쳐하기 위해 DynamoDB 스트림을 사용할 수 있다.

> There are limits in DynamoDB. For more information, see Service, account, and table quotas in Amazon DynamoDB.

DynamoDB에는 제한이 있다. 자세한 내용은 아마존 DynamoDB의 [서비스, 계정, 테이블 제한을 참조하라.](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html)

> The following video will give you an introductory look at tables, items, and attributes.

다음 [비디오](https://www.youtube.com/embed/Mw8wCj0gkRc)는 테이블, 아이템, 속성에 대한 소개를 제공한다.

## Tables, items, and attributes

다음은 DynamoDB 기본 컴포넌트들이다.

- Tables: 다른 데이터베이스 시스템과 유사하게, DynamoDB도 테이블에 데이터를 저장한다.
- Items: 각 테이블은 0개 혹은 그 이상의 아이템들을 포함한다. 아이템은 속성들의 컬렉션이다. **DynamoDB는 테이블에 저장할 수 있는 아이템의 수에 제한이 없다.**
- Attributes: 각 아이템은 하나 혹은 그 이상의 속성들로 구성되어있다. 
  - DynamoDB는 32 레벨 깊이까지 nested attribute를 지원한다.

## Primary Key

> When you create a table, in addition to the table name, you must specify the primary key of the table. 

테이블을 생성할 때, 테이블 이름뿐만 아니라 테이블의 기본 키를 반드시 지정해야 한다.

> The primary key uniquely identifies each item in the table, so that no two items can have the same key.

기본 키는 테이블의 각 아이템을 고유하게 식별하기 때문에, 두 개의 아이템은 같은 키를 가질 수 없다.

> DynamoDB supports two types of primary keys.

DynamoDB는 두 가지 유형의 기본 키를 지원한다.

1. Partition key: partition key라고 알려진 하나의 속성으로 구성된 primary key.
   - **DynamoDB는 파티션 키의 값을 내부 해시 함수의 입력으로 사용한다.**
   - **해시 함수의 출력은 DynamoDB가 내부적으로 데이터를 저장하기 위한 물리 적 저장 위치를 결정하는데 사용된다.**
   - 오직 하나의 파티션 키를 가지는 테이블은, 동일한 파티션 키 값을 가지는 아이템이 두 개 이상 존재할 수 없다.

2. Partion Key and sort Key: composite primary key라고 알려진, 이러한 키의 타입은 두개의 속성으로 구성된다.
   - 첫번째 속성은 partition key이고, 두번째 속성은 sort key이다.
   - DynamoDB는 파티션 키의 값을 내부 해시 함수의 입력으로 사용한다.
   - 출력은 위와 마찬가지로 물리적 저장 위치를 결정하는데 사용한다.
   - **동일한 파티션 키 값을 가지는 모든 아이템은 함께 저장된다. 그리고 sort key에 의해 정렬되어있다.**
   - **여러개의 아이템이 동일한 파티션 키 값을 가지고 있을 수 있지만, sort key 값은 서로 다르다.**
   - composite primary key는 데이터를 쿼리할때 유연함을 준다.


### Note

> The partition key of an item is also known as its hash attribute. The term hash attribute derives from the use of an internal hash function in DynamoDB that evenly distributes data items across partitions, based on their partition key values.

아이템의 파티션 키는 해시 속성으로도 알려져 있다. 해시 속성이라는 용어는 DynamoDB의 내부 해시 함수가 사용되는데, 이 함수는 파티션 키 값에 기반하여 데이터 아이템을 파티션에 균등하게 분배한다.

파티션에 관해 궁금하니 다음 문서들을 읽어보자. 

- https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html
- https://www.alexdebrie.com/posts/dynamodb-partitions/

> The sort key of an item is also known as its range attribute. The term range attribute derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

아이템의 정렬 키는 range attribute라고도 알려져 있다. range attribute라는 용어는 DynamoDB가 동일한 파티션 키 값을 가지는 아이템을 정렬 키 값에 따라 정렬된 순서로 물리적으로 가까이 저장하는 방법에서 유래한다.

> Each primary key attribute must be a scalar (meaning that it can hold only a single value). The only data types allowed for primary key attributes are string, number, or binary. There are no such restrictions for other, non-key attributes.

각 primary key 속성은 반드시 스칼라(단일 값)이어야한다. primary key 속성에 허용되는 데이터 타입은 string, number, binary이다. 다른, key가 아닌 속성에는 이러한 제한이 없다.

## Secondary Indexes

> You can create one or more secondary indexes on a table. A secondary index lets you query the data in the table using an alternate key, in addition to queries against the primary key.

하나의 테이블에 한개 이상의 세컨더리 인덱스를 생성할 수 있다. 세컨더리 인덱스는 primary key에 대한 쿼리 외에, 대체 키를 사용하여 테이블의 데이터를 쿼리할 수 있게 해준다.

> DynamoDB doesn't require that you use indexes, but they give your applications more flexibility when querying your data. After you create a secondary index on a table, you can read data from the index in much the same way as you do from the table.

세컨더리 인덱스를 의무적으로 사용할 필요는 없지만, 이를 통해 데이터를 쿼리할때 애플리케이션에 더 많은 유연성을 줄 수 있다. 테이블에 세컨더리 인덱스를 생성한 후, 테이블에서 데이터를 읽는 것처럼 거의 동일하게 데이터를 읽을 수 있다.

DynamoDB는 두가지 종류의 인덱스를 지원한다.

- Global secondary index : 테이블에서 파티션키와 정렬키가 다른 인덱스이다.
- Local secondary index : 테이블에서 같은 파티션 키를 가지는 인덱스이다. 정렬키는 다르다.


> 🚨 DynamoDB의 각 테이블에는 20개의 global secondary index와 5개의 local secondary index를 가질 수 있다. 🚨


- DynamoDB는 인덱스를 자동으로 유지관리한다. 아이템을 추가, 업데이트, 삭제할 때 DynamoDB는 대응하는 아이템에 대한 인덱스를 자동으로 업데이트한다.
- 인덱스를 생성할 때, 어떤 attributes가 복사되고, 투영되어야할지 지정할 수 있다. 최소한, DynamoDB 기본 테이블의 key 속성들을 인덱스로 투영한다.

## DynamoDB Streams

> DynamoDB Streams is an optional feature that captures data modification events in DynamoDB tables. The data about these events appear in the stream in near-real time, and in the order that the events occurred.
****
DynamoDB 스트림은 DynamoDB 테이블에서 데이터 변경 이벤트를 캡쳐하는 옵션 기능이다. 이러한 이벤트에 대한 데이터는 스트림에 거의 실시간으로 나타나며, **이벤트가 발생한 순서대로 나타난다.**

> Each stream record also contains the name of the table, the event timestamp, and other metadata. Stream records have a lifetime of 24 hours; after that, they are automatically removed from the stream.

각 스트림 레코드는 테이블 이름, 이벤트 타임스탬프, 메타데이터 등을 포함한다. **스트림 레코드의 수명은 24시간이며, 이후에는 스트림에서 자동으로 제거된다.**

> You can use DynamoDB Streams together with AWS Lambda to create a trigger—code that runs automatically whenever an event of interest appears in a stream. 

DynamoDB 스트림와 AWS 람다와 함께 사용해 관심있는 이벤트에 대한 구독을 만들어 자동으로 실행되게 할 수 있다.

<img src="https://docs.aws.amazon.com/images/amazondynamodb/latest/developerguide/images/HowItWorksStreams.png">

> In addition to triggers, DynamoDB Streams enables powerful solutions such as data replication within and across AWS Regions, materialized views of data in DynamoDB tables, data analysis using Kinesis materialized views, and much more.

trigger를 사용하면, DynamoDB 스트림은 AWS 리전 내에서의 데이터 복제, DynamoDB 테이블의 데이터에 대한 materialized views, Kinesis materialized views를 사용한 데이터 분석 등과 같은 강력한 솔루션을 가능하게 한다.

