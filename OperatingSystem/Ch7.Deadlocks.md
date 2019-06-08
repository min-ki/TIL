# Chapter 7. Deadlocks

- System Model
- Deadlock Characterization
- Methods for Handling Deadlocks
- Deadlock Prevention
- Deadlock Avoidance
- Deadlock Detection
- Recovery from Deadlock





## System Model

- 시스템은 자원들로 이루어져 있다.
- 각 자원의 타입들은 R1, R2, … Rn 으로 부른다. (CPU, Printers, Semaphores/locks 등)
- 각 프로세스는 다음 흐름에 따라서 자원을 사용한다.
  - 요청(request) : 만약 자원이 사용 불가능하다면, 프로세스는 대기한다.
  - 사용(use)
  - 방출(release)
  - 예시
    - file : open, close
    - memory : allocate, free
    - semaphore : wait, signal



## Deadlocks은 언제 발생하는가?

- 프로세스에는 장치 또는 소프트웨어 구성에 대한 독점 액세스 권한이 부여된다.(리소스)
- 각 교착 프로세스가 다른 교착된 프로세스에 의해 할당된 자원을 필요로할 때 데드락이 발생한다.
- 즉, 다른 프로세스가 사용하고 있는 자원을 서로 필요로할 때, 데드락이 발생





## 교착상태 발생조건 4가지

- 만약 4가지 발생조건이 동시에 존재한다면 교착상태가 발생한다.

- 4가지 발생조건

  - 상호배제(Mutual exclusion) : 같은 시간대에 하나의 프로세스가 딱 하나의 자원만 사용
  - 점유 및 대기(Hold and Wait)  : 최소한 하나의 자원을 점유한 프로세스가 다른 프로세스의 자원을 획득하기위해 대기
  - 비선점(No preemption) : 자원은 오직 할당된 프로세스가 스스로 방출을 할때만 방출될 수 있음
  - 순환대기(Circular wait) 

- 자원-할당 그래프(Resource-Allocation Graph)

  

  ![자원할당 그래프](https://t1.daumcdn.net/cfile/tistory/132074364FA1FC611C)

  - 요청 간선(request edge) - P_i -> R_j
  - 할당 간선(assignment edge) - R_j -> P_i

  - *자원의 인스턴스가 여러개일 경우, 사이클이 존재하더라도 교착상태가 아닐 수 있음*



## Basic Facts

- 만약 자원할당그래프에 사이클이 없다면 => 데드락이 없다
- 만약 자원할당그래프에 사이클이 있다면
  - 만약 하나의 인스턴스 당 하나의 자원을 가진다면 => 데드락 발생
  - 만약 여러개의 자원 인스턴스를 가진다면 => 데드락 발생가능성이 존재



## Methods for Handling Deadlocks (데드락 관리 방법)

- 시스템이 데드락 상태로 진입하지않도록 보장하는 방법
  - Prevention (예방) : 프로세스의 자원 요청을 제한하는 것
  - Avoidance (회피) : 추가정보를 사용하는 것
- 시스템이 데드락 상태로 진입하는 것을 허용하고 회복하는 방법
  - Detection & Recovry (탐지와 복구)
- 문제를 무시하고 시스템에 데드락이 발생하지 않은 척하는 방법 (무시)
  - 대부분의 운영체제가 사용하고 있는 방법
  - 응용프로그래머에게 데드락을 관리하도록 넘김



## Deadlock Prevention(데드락 예방)

- 요청을 제한하는 방법

  - 데드락의 4가지 발생조건 중 최소한 하나를 예방하는 것

    

  - 상호 배제 (Mutual Exclusion)

    - 공유 가능한 자원들은 교착상태를 발생시키지 않음
    - 상호배제 조건은 공유가 불가능한 자원에 대해서는 반드시 성립해야 함

    

  - 점유 및 대기(Hold and Wait) 

    - 프로세스가 자원을 요청할 때, 다른 자원들을 점유하지 않도록 보장
      - 프로세스가 자원을 요청한 경우 필요한 모든 자원을 할당
      - 프로세스가 자원을 전혀 갖고 있지 않을 때만 자원을 요청할 수 있도록 허용
    - 점유와 대기 조건 방지 방법의 단점
      - 자원효율성이 너무 낮음
      - 기아상태가 발생 가능

    

  - 비 선점(No Preemption)

    - 이미 할당된 자원을 선점할 수 있도록 허용
    - 어떤 자원을 가진 프로세스가 다른 자원을 요청할 때 요청한 자원을 즉시 할당 받을 수 없어 대기해야 한다면, 프로세스는 현재 가진 자원을 모두 해제(선점). 프로세스가 작업을 시작할 때는 요청한 새로운 자원과 해제한 자원을 모두 확보해야 함. 이미 실행한 작업의 상태를 잃을 수 있음.

    - 전용 입출력장치 등을 빼앗아 다른 프로세스에 할당 후 복구하는 과정이 간단하지 않음.
    - 프로세스가 어떤 자원을 요청할 때, 요청한 자원이 사용 가능한지 검사, 사용할 수 있다면 자원 할당. 사용할 수 없다면 대기 프로세스가 요청한 자원을 점유하고 있는지 검사. 요청한 자원을 대기 프로세스가 점유하고 있다면, 자원을 해제(선점)하고 요청 프로세스에 할당. 요청한 자원을 사용할 수 없거나 실행 중인 프로세스가 점유하고 있다면 요청 프로세스는 대기. 프로세스가 대기하는 동안 다른 프로세스가 점유한 자원을 요청하면 자원을 해제할 수 있음.

  
  - 순환 대기(Circular Wait) 
    - 모든 자원에 일련의 순서를 부여, 각 프로세스가 오름차순으로만 자원을 요청
    - 계층적 요청 방법으로 순환 대기의 가능성을 제거하여 교착상태 예방
    - 상당한 자원 낭비를 초래



## Deadlock Avoidance(데드락 회피)

- 목적 : 덜 엄격한 조건을 요구하여 자원을 더 효율적으로 사용
- 시스템은 몇 가지의 추가적인 정보를 더 가지도록 필요로한다.
- 가장 단순하고 가장 유용한 모델은 각 프로세스가 필요할 수 있는 각 유형의 최대 리소스 수를 선언할 것을 요구한다.
- 교착상태 회피 알고리즘이 리소스의 상태를 동적으로 검사하여 순환 대기상태가 발생하지 않도록 한다.
- 자원-할당 상태는 다음과 같이 정의된다.
  - 이용가능 한 수
  - 할당된 자원의 수
  - 프로세스의 최대 요구량



## Safe State

- 두가지 상태 : 안정 상태(safe state), 불 안정 상태(unsafe state)
- 프로세스가 사용가능한 자원을 요청할 때, 시스템은 할당이 시스템을 안정 상태로 유지하는지에 대해 결정해야함
- 만약 모든 프로세스가 안정 상태를 위한 순서가 존재한다면 시스템은 safe state이다.
- 순열<P1, P2, … Pn> 에 대해 각 프로세스 P_i가 현재 이용가능한 것에 만족되늘 수있는 요청을 할때 + 모든 P_j가 점유하고 있는 자원을 충족한다면 safe 하다.
- That is
  - 만약 P_i 자원이 즉시 이용가능하지 않다면, P_i는 모든 P_j 가 끝날때까지 기다려야한다.
  - P_j가 끝나면, P_i는 필요한 자원을 얻고, 실행하고, 할당된 자원을 반환하고 종료한다.
  - P_i가 종료했을 때, P_i+1은 필요한 자원을 얻고 위 과정을 반복한다.



## Basic Facts

- 만약 시스템이 safe state 라면 데드락이 발생하지 않는다.
- 만약 시스템이 unsafe state 라면 데드락이 발생할 가능성이 있다.
- 회피(Avoidance) => 시스템이 unsafe state로 진입하지 않도록 보장한다.



## 회피 알고리즘(Avoidance Algorithms)

- 자원의 타입이 단일 인스턴스일 경우(single instance of a resource type)
  - 자원-할당 그래프 사용(Use a resource-allocation graph)
- 자원의 타입이 다중 인스턴스일 경우(Multiple instance of a resource type)
  - 은행원 알고리즘을 사용(Use the banker's algorithm)



## Resource-Allocation Graph Scheme

- 예악간선(Claim edge) P_i => R_j 는 점선을 통해서 프로세스 i가 자원 J를 요청할 수 있음을 나타낸다.
- 예약 간선은 프로세스가 자원을 요청했을 때 요청간선으로 변환된다.
- 요청 간선은 자원이 프로세스에게 할당되면은 할당 간선으로 변환된다.
- 자원이 프로세스에 의해서 방출되었을 때, 할당간선은 요청 간선으로 재 변환된다.
- 자원들은 시스템에서 선행되어 요청되어야한다.
- 요청 간선에서 할당 간선으로 변환할 때, 자원 할당 그래프에서 사이클이 생성되지 않는 경우에만 요청을 승인할 수 있다.



## Banker's Algorithm (은행원 알고리즘)

- 은행원 알고리즘은 운영체제가 안정 상태를 유지할 수 있는 요구만 수락하고 불안정 상태를 초래할 사용자의 요구는 나중에 만족될 때까지 계속 거절.

  

- 자원에 다수의 인스턴스가 있을 때 사용

- 은행원 알고리즘을 위해서 3가지의 정보가 필요함

  - 각 프로세스가 최대로 자원을 얼마나 요구할지에 대한 정보
  - 각 프로세스가 자원을 얼마나 사용하는 지
  - 시스템이 얼마나 자원을 보유하고 있는지

- 각 프로세스가 자원을 요청할 때 대기해야 할 수 있다.
- 프로세스가 모든 자원을 획득할 때, 유한한 시간 내에 반환해야 한다.



### Data Structure for the Banker's Algorithm

프로세스의 수를 n이라 하고, 자원 타입의 수를 m이라고 정의한다.

- Available : m 길이의 벡터, available[j] = k 는 R_j 자원타입의 인스턴스는 K가 이용가능하다는 뜻

- Max : n * m 의 배열, Max[i,j] = K는 프로세스 P_i가 R_j자원의 인스턴스를 k개 최대로 요청할 수 있다는 뜻

- Allocation : n * m 의 배열, Allocation[i,j] = k 는 P_i가 현재 R_j 인스턴스의 k개를 할당받고 있다는 뜻

- Need : n * m의 배열, Need[i, j] = k는 P_i가 태스크를 끝낼때 까지 앞으로 K개의 R_j인스턴스를 더 필요로 한다는 뜻

  => `Need[i,j] = Max[i,j] - Allocation[i,j]`





## Safety Alogorithm

1. 초기화
   - Work =  길이 m인 배열 => Work = Available
   - Finish = 길이 n인 배열  => Finish[i] = false for i = 0, 1, …., n-1

2. 두개의 조건을 만족하는 i를 찾는다.
   - Finish[i] = false
   - Need_i <= Work
   - 만약 못찾으면 4번으로 간다.
3. 연산 실행
   - Work = Work + Allocation_i
   - Finish[i] = true
   - 2번으로 간다.
4. 모든 i에 대해 Finish[i] == true이면
   - 시스템은 safe state이다.



## Resource-Request Algorithm for Process P_i

- Request_i = 프로세스 P_i를 위한 요청 배열
- 만약 Request_i[j] = k 라면 프로세스 P_i는 자원 R_j의 인스턴스를 k개 원하는 것

1. 만약 Request_i <= Need_i 라면 2번으로 간다. 그렇지 않으면 condition error를 발생시킨다. 왜냐하면 프로세스가 최대 요청개수를 초과했기 때문에.
2. 만약 Request_i <= Avaiable 라면 3번으로 간다. 그렇지 않으면, P_i는 자원이 이용가능하지 않기 때문에 기다려야한다.

3. 상태를 수정함으로써 P_i에 자원을 할당하는 척..?

   - Available = Available - Request_i;

   - Allocation_i = Allocation_i + Request_i;
   - Need_i = Need_i - Request_i;
     - 만약 safe => 자원들은 프로세스 P_i에 할당된다.
     - 만약 unsafe => P_i는 대기해야하며, 이전의 자원 할당 상태가 복구된다.



## Deadlock Detection (데드락 탐지)

- 데드락 상태로의 진입을 시스템이 허용한다.
- 탐지 알고리즘
- Recovery scheme  => 복구 계획



##  Single Instance of Each Resource Type

- Maintain wait-for graph
  - 노드들은 프로세스들
  - P_i -> P_j 는 p_i가 프로세스 p_j를 기다리는 것
- 주기적으로 그래프의 사이클을 찾기위한 알고리즘을 실행시킨다. 사이클이 만약 존재한다면, 데드락이 있다는 것이다.



## Several Instance of a Resource Type

- Available 
- Allocation
- Request
- 현재상태만 보면 되므로 Need가 필요없다.



## Detection Algorithm(탐지 알고리즘)

1. 초기화
   - Work = Available
   - if Allocation_i != 0 -> Finish[i] = false; 아니라면 Finish[i] = true
2. 다음 조건을 만족하는 인덱스 i를 찾는다.
   - Finish[i] == false
   - Request <= work (work는 Available 임)
   - i가 존재하지 않는다면 4번으로 간다.
3. 조건에 만족하는 인덱스를 찾았다면
   - Work = Work + Allocation_i
   - Finish[i] = true
   - 2번으로 간다.
4. 조건을 만족하지 못한다면
   - 모든 i의 Finish[i] == false라면 시스템은 데드락 상태이다
   - 더욱이, Finish[i] == false이면 프로세스 P_i는 데드락 상태



## Detection-Algorithm Usage

- 언제, 얼마나 자주, 알고리즘을 부르는 것은 다음에 달려있다.
  - 데드락이 종종 어떻게 발생하는지?
  - 몇 개의 프로세스를 롤백해야하는지?
    - 각 불연속적인 사이클마다 하나씩
- 만약 탐색 알고리즘이 임의로 불러진다면, 자원 그래프에 많은 그래프가 있을지도 모르고, 그래서 우리는 교착상태에 빠진 많은 것들이 어떤 것에 의해 교착상태에 빠지는 지 알지 못할 것이다.



## Recovery from Deadlock: Process Termination

데드락 회복 : 프로세스 종료

- 모든 데드락된 프로세스를 종료시킨다.
- 데드락 사이클이 제거될때까지 한번에 하나의 프로세스를 종료시킨다.

- 종료시키기위해 선택하는 순서는 어떻게 되어야나는지?
  - 프로세스의 우선순위를 고려
  - 수행시간에 따라서(짧게 수행한 것 먼저 종료)
  - 리소스가 많은 프로세스(무조건 많은 것이 우선은 아니다.)
  - 얼마나 많은 프로세스가 종료를 위해서 필요한지
  - 프로세스가 interactive하거나 batch인지



## Recovery from Deadlock : Resource Preemption

- Selecting a victim : minimize cost (비용을 최소화)
- Rollback : return to some safe state, restart process for that state
- Starvation(기아) : same process may always be picked as victim, include number of rollback in cost factor

