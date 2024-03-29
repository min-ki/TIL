# Traffic Management

istio의 트래픽 라우팅 규칙은 서비스 간의 API 호출과 트래픽의 제어를 쉽게 할 수 있도록 해줍니다. istio는 서킷 브레이커, 타임아웃, 재시도와 같은 설정을 간편하게 설정할 수 있도록 하고, A/B 테스트, 카나리 배포, 퍼센트 기반의 트래픽 분할의 단계별 배포 등을 쉽게할 수 있도록 해준다. 이러한 기능들을 out-of-box로 제공하고 있기때문에 애플리케이션에서는 의존하고 있는 서비스 혹은 네트워크 장애로 인한 일시적인 문제가 발생할때 조용히 다시 복구될 수 있도록 해준다.

istio의 트래픽 관리 모델은 서비스들과 함께 배포되는 Envoy라는 프록시에 강하게 의존한다. 서비스의 모든 송/수신 트래픽은 Envoy를 통해서 이루어지며, 서비스에 대한 변화없이 다양한 서비스에 걸친(서비스 메시) 트래픽 제어 등을 쉽게할 수 있게 해준다.

자세한 아키텍처 구현은 [여기](https://istio.io/latest/docs/ops/deployment/architecture/)를 살펴보자.

## Istio에서 트래픽을 어떻게 관리하는가?

메시(mesh)로 직접 들어오는 트래픽을 위해, Istio는 모든 엔드포인트들과 각 서비스들이 어디에 속하는지 알아야할 필요가 있다. 이러한 정보를 저장하기 위해 서비스 레지스트리(service registry)를 가지고 있고, istio는 이것을 service discovery system에 연결한다. 예를들어, 만약 쿠버네티스 클러스터에 istio를 설치했다면, istio는 자동으로 클러스터 내의 모든 서비스와 엔드포인트를 발견한다.

서비스 레지스트리를 사용하면, Envoy 프록시는 연관된 서비스로 트래픽을 라우팅할 수 있다. 대부분의 마이크로서비스 기반의 애플리케이션은 트래픽 처리를 위해 각 서비스마다 여러 개의 인스턴스를 가지고 있고, 떄로는 로드 밸런싱 풀에서도 참조된다. 기본값으로, Envoy 프록시는 **least request models**를 사용해서 서비스의 로드 밸런싱 풀로 트래픽을 분배한다. 그래서 트래픽이 많은 호스트는 요청을 받지않고 나중에 다른 호스트들보다 적어지면 그때 다시 요청을 받는다.

기본적으로 istio의 서비스 디스커버리와 로드 밸런싱은 서비스 메시로 동작하는데 문제없지만, istio는 더 많은 것을 할 수 있다. 예를들면 다음과 같은 것들이 있다.

- A/B 테스트를 위해 percentage 기반의 트래픽 분배
- 특정한 서비스의 부분집합으로 트래픽의 로드 밸런싱 정책을 다르게 적용
- 메시로 들어오고 나가는 트래픽에 대한 특별한 룰 적용

이러한 것들을 istio가 가진 트래픽 관리 API를 사용해서 적용할 수 있다.

다른 Istio 설정과 같이, 이 트래픽 관리 API 또한 Kubernetes custom resource definitions (CRDs)를 사용해서 명시한다.

이 문서의 나머지 가이드는 트래픽 관리 API의 리소스들에 대해서 각각 살펴보고 무엇을 할 수 있는지 알아본다.

트래픽 관리 리소스들은 다음과 같다.

- 가상 서비스 (Virtual Services)
- Destination rules
- Gateways
- Servie entries
- Sidecars

## 가상 서비스(Virtual Services)

가상 서비스는 destination rule와 함께 istio의 트래픽 라우팅 기능의 핵심이다.
가상 서비스는 요청이 istio 서비스 메시 내의 서비스로 어떻게 라우팅되는지를 정의한다. 각 virtual service는 라우팅 규칙들의 집합으로 구성되는데 규칙들은 istio가 주어진 요청에 대해 일치하는 virtual service를 찾아 실제 목적지를 찾을 때가지 정의된 순서대로 평가한다.

### 왜 가상 서비스(virtual service)를 사용할까?

가상 서비스는 istio의 트래픽 관리를 유연하고 강력하게 만드는 핵심 역할을 한다. 가상 서비스는 클라이언트의 요청과 목적지를 디커플링함으로써 앞의 핵심 역할을 달성한다. 가상 서비스는 또한 트래픽을 워크로드로 전달하기 위한 다양한 트래픽 라우팅 정책을 지정할 수 있는 많은 기능을 제공한다.

왜 이게 유용할까? 가상 서비스 없이는, Envoy는 least requests 로드 밸런싱을 사용하여 모든 서비스 인스턴스에 트래픽을 분산시킨다. 우리는 작업자에 대해 아는 것을 통해 이러한 행동을 개선시킬 수있다.

가상 서비스가 있다면 한개 이상의 호스트명으로 트래픽의 행동을 명시할 수 있다. 가상 서비스의 라우팅 규칙을 사용해서 Envoy 프록시가 가상 서비스의 트래픽을 적절한 목적지로 보낼지 알려줄 수 있다. 경로의 목적지는 같은 서비스의 다른 버전이 될 수 있고, 완전히 다른 서비스가 될 수 있다.

### 가상 서비스 예제

```yml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
  - reviews
  http:
  - match:
    - headers:
        end-user:
          exact: jason
    route:
    - destination:
        host: reviews
        subset: v2
  - route:
    - destination:
        host: reviews
        subset: v3
```

### The hosts field
The hosts field lists the virtual service’s hosts - in other words, the user-addressable destination or destinations that these routing rules apply to. This is the address or addresses the client uses when sending requests to the service.

```yml
hosts:
- reviews
```

The virtual service hostname can be an IP address, a DNS name, or, depending on the platform, a short name (such as a Kubernetes service short name) that resolves, implicitly or explicitly, to a fully qualified domain name (FQDN). You can also use wildcard ("*") prefixes, letting you create a single set of routing rules for all matching services. Virtual service hosts don’t actually have to be part of the Istio service registry, they are simply virtual destinations. This lets you model traffic for virtual hosts that don’t have routable entries inside the mesh.


## Reference

- https://istio.io/latest/docs/concepts/traffic-management/#introducing-istio-traffic-management
