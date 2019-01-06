## 데이터베이스 개념

####  1. 데이터 베이스란?

한 조직의 여러 응용 시스템들이 공용(Shared)하기 위해 통합(Integrated), 저장(Stored)한 운영(Operational) 데이터의 집합

- 통합된 데이터(Integrated data)
  - 최소의 중복
  - 통제된 중복
- 저장 데이터
  - 컴퓨터가 접근 가능한 저장 매체에 저장
  - 테이프, 디스크
- 운영 데이터
  - 한 조직의 고유 기능을 수행하기 위해 필요한 데이터
- 공용 데이터
  - 한 조직의 여러 응용 프로그램이 공동으로 소유, 유지, 이용하는 데이터



#### 2. 데이터베이스의 특성

- 실시간 접근성(real-time accessibilities)
  - 질의에 대한 실시간 처리 및 응답
- 계속적인 변화 (continuous evolution)
  - 갱신, 삽입, 삭제 : 동적 특성
- 동시 공용 (concurrent sharing)
  - 여러 사용자가 동시에 사용
- 내용에 의한 참조 (content reference)
  - 위치나 주소가 아닌 값에 따라 참조



#### 3. 데이터베이스의 구성요소

- 논리적 구성요소
  - 사용자의 입장
  - 데이터 베이스 = { 개체, 관계 }
    - 데이터 베이스는 개체와 관계의 집합이라는 뜻
- 관계
  - 표현하려는 유무형 정보의 객체
  - 정보의 단위
  - 하나 이상의 속성(attribute)으로 구성
    - 데이터의 가장 작은 논리적 단위
  - 개체 집합(entitiy set)
    - entity type vs entity instance
  - 레코드와 대응
    - record type vs record instance
  - 속성 관계(attribute relationship)
    - 개체 내(intra-entity) 관계
  - 개체 관계(entity relationship)
    - 개체 간(inter-entity) 관계



#### 4. 데이터베이스의 구조

- 논리적 구조(logical organization)

  - 사용자의 관점에서 본 데이터의 개념적 구조
  - 데이터의 논리적 배치
  - 논리적 레코드

- 물리적 구조(physical organization)

  - 저장 관점에서 본 데이터의 물리적 배치
  - 저장장치에 저장된 데이터의 실제 구조
  - 추가 정보 포함 : 인덱스, 포인터 체인, 오버플로우 등
  - 물리적 레코드
