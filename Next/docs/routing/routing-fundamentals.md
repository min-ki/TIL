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

## `App` 라우터 (Router)

Next.js Version 13에서 도입된 앱 라우터 (App Router)는 React Server Components를 기반으로 한다.

앱 라우터는 공유 레이아웃 (shared layouts), 중첩 라우팅 (nested routing), 로딩 상태 (loading states), 에러 핸들링 (error handling) 등을 지원한다.

앱 라우터는 `app` 이름의 폴더 안에서 동작한다.

앱 라우터는 `pages` 폴더방식과 함께 사용할 수 있어서 점진적으로 앱라우터 적용이 가능하다. (pages 방식이 아예 없어지는 것이 아닌 app 라우터도 같이 쓸 수있다.)

그래서, 기존의 pages 폴더 방식을 사용하면서 새로운 기능을 추가하고 싶다면, `app` 폴더를 만들어서 사용할 수 있다.

페이지 디렉토리 사용하면 (https://nextjs.org/docs/pages/building-your-application/routing) 여기서 페이지 라우터 문서를 확인해보자.

> Good to know: The App Router takes priority over the Pages Router. Routes across directories should not resolve to the same URL path and will cause a build-time error to prevent a conflict.

> 알아두면 좋은 것: 앱 라우터는 페이지 라우터보다 높은 우선순위를 가진다. 디렉토리 간의 라우트는 동일한 URL 경로로 해석되어 빌드 시간 오류가 발생하며 충돌을 방지한다.

<img src="https://nextjs.org/_next/image?url=%2Fdocs%2Flight%2Fnext-router-directories.png&w=3840&q=75">

By default, components inside app are React Server Components.
기본 설정으로, 앱 라우터 내부의 컴포넌트들은 리액트 서버 컴포넌트이다.

This is a performance optimization and allows you to easily adopt them, and you can also use Client Components.
이 설정은 성능을 최적화하고 서버 컴포넌트를 쉽게 적용할 수 있게 해주고, 클라이언트 컴포넌트도 사용할 수 있다.

> Recommendation: Check out the Server page if you're new to Server Components.

> 추천: 서버 컴포넌트에 대해 처음 접하신다면 서버 컴포넌트 페이지를 확인해보세요.

