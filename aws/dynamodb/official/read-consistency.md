# Read consistency

Amazon DynamoDB는 다수의 AWS 리전에서 이용이 가능하다. 각 리전은 독립적이고 다른 AWS 리전과는 격리되어있다. 예를들어, 만약 us-east-2 지역에서 People이라고 불리는 테이블을 호출했고 그리고 us-west-2 지역의 People 테이블을 호출한다면, 이것들은 완전히 별개의 테이블로 간주된다.

모든 AWS 리전은 가용영역이라 불리는 몇개의 영역으로 구성되어있다. 각 가용영역은 다른 가용영역의 장애로부터 격리되어있으며, 같은 리전 내의 다른 가용영역간의 연결을 저렴하고, 적은 지연시간으로 연결할 수 있도록 제공한다. 이러한 점은 동일 리전 내 여러 가용영역에 걸쳐 신속한 데이터 복제를 가능하게 한다.

애플리케이션이 DynamoDB 테이블에 데이터를 쓰고 HTTP 200 response(OK)를 응답받았을 때, 쓰기는 완료되었고 영속화되었다. 데이터는 최종적으로 여러 지역의 스토리지에 복제되고 이것은 보통 1초 내로 처리된다.

DynamoDB는 `eventually consistent`와 `strongly consistent reads`를 지원한다.

## Eventually Consistent Reads

DynamoDB 테이블로부터 데이터를 읽을 때, 응답은 최근 쓰기 연산의 결과를 반영하지 않을수도 있다. 응답은 갱신되지 않은 데이터를 포함할 수 있다. 만약 잠시 후에, 읽기 요청을 다시 보낸다면 응답은 최신 데이터를 반환할 것이다.

## Strongly Consistent Reads

strongly consistent read 요청을할때, DynamoDB는 이전에 성공한 모든 선행 쓰기 연산으로부터 업데이트를 반영하여, 가장 최근에 업데이트된 데이터를 반환한다. 하지만, 이러한 방식의 일관성은 몇가지 단점을 초래한다.

- Strongly consistent reads는 GSI (Global Secondary Index)에 대해서는 지원되지 않는다.
- Strongly consistent reads는 eventually consistent reads보다 더 많은 처리량을 사용한다. 네트워크 지연 혹은 정전 등이 발생한다면, strongly consistent read는 사용할 수 없고 DynamoDB는 HTTP 500 (Server Error)를 반환할 것이다.
- 만약 읽기요청이 첫 시도에서 리더 노드에 도달할 수 없다면, strongly consistent reads는 높은 지연시간을 초래할 수 있다.

> DynamoDB는 eventually consistent reads를 기본적으로 사용한다. Read operations (GetItem, Query, Scan)에 대해서는 ConsistentRead 파라미터를 사용하여 strongly consistent reads를 사용할 수 있다.
