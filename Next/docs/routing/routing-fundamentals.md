# Routing Fundamentals

https://nextjs.org/docs/app/building-your-application/routing

## Terminology (전문용어)

처음에는 문서에서 사용하는 용어들 소개한다.

<img src="https://nextjs.org/_next/image?url=%2Fdocs%2Flight%2Fterminology-component-tree.png&w=3840&q=75">

- Tree (트리): 계층구조를 시각화하기위한 convention. 예를들어서, 컴포넌트 트리란 부모와 자식 컴포넌트들을 이루는 계층 구조를 말한다.
- SubTree (서브트리): 트리의 일부분을 지칭하는 용어. 위의 이미지에서는 root를 나타내는 dashboard컴포넌트가 있고 그 하위 Leaf까지 포함한 영역을 서브트리라고 한다.
- Root (루트): 트리 또는 서브트리의 첫 번째 노드를 지칭한다. app이 루트가 될 수도 있고, dashboard 와 같이 서브트리에서 첫 번째 노드가 루트가 될 수도 있다.
- Leaf (리프 / 말단): 서브트리에서 children이 없는 노드를 나타낸다. URL의 마지막 세그먼트와 같은 것이 예시

<img src="https://nextjs.org/_next/image?url=%2Fdocs%2Flight%2Fterminology-url-anatomy.png&w=3840&q=75">

- URL Segment(URL 세그먼트): 슬래시(slash)로 구분된 URL 경로의 부분
    - ex): acme.com/dashboard/settings에서 dashboard와 settings는 URL 세그먼트이다.

- URL Path (URL 경로): 도메인 뒤에 위치하는 것들.
    - ex): acme.com/dashboard/settings에서 /dashboard/settings는 URL 경로이다.