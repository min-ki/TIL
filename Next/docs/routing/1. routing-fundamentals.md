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

## 폴더와 파일의 역할 (Roles of Folders and Files)

https://nextjs.org/docs/app/building-your-application/routing#roles-of-folders-and-files

- Next.js는 파일 시스템 기반의 라우터를 다음과 같이 사용한다.
- 폴더는 경로를 정의하는데 사용한다. 경로는 page.js 파일을 포함하고있는 루트 폴더에서 마지막 리프 폴더까지의 파일 시스템 계층 구조를 따르는 단일 경로이다.
- 파일은 라우트 세그먼트에 대한 UI를 만드는데 사용된다. 아래나오는 파일 컨벤션을 확인해보면 된다.

## 경로 세그먼트 (Route Segment)

https://nextjs.org/docs/app/building-your-application/routing#route-segments

경로 안에서 각각의 폴더는 경로 세그먼트를 나타낸다. 각 경로 세그먼트는 URL 경로에서 해당 세그먼트에 매핑된다.

<img src="https://nextjs.org/_next/image?url=%2Fdocs%2Flight%2Froute-segments-to-path-segments.png&w=3840&q=75">

위의 예시를 보면 app/dashboard/settings 계층구조로 폴더가 존재하고, 이것이 URL 경로에서 /dashboard/settings로 매핑된다.

## 중첩 경로 (Nested Routes)

https://nextjs.org/docs/app/building-your-application/routing#nested-routes

중첩 경로를 만들기 위해서, 서로 다른 폴더를 중첩시키면 된다. 예를들어, /dashboard/settings 경로를 만들기 위해서 app 디렉토리에 두개의 새로운 폴더를 중첩시키면 된다. 위의 예시와 동일.

`/dashboard/settings` 경로는 3개의 세그먼트로 구성되어있다.

1. / (Root segment)
2. dashboard (Segment)
3. settings (Leaf segment)

## 파일 컨벤션 (File Conventions)

https://nextjs.org/docs/app/building-your-application/routing#file-conventions

| 파일명       | 설명                                                                           |
| ------------ | ------------------------------------------------------------------------------ |
| layout       | 공유 레이아웃 UI를 만들때 사용하는 파일명                                      |
| page         | 경로마다 유니크한 UI, 공개적으로 접근가능한 경로를 만들기 위해 사용하는 파일명 |
| loading      | 로딩 UI를 만들기 위한 파일명                                                   |
| not-found    | 리소스를 찾을 수 없을 때 보여주기 위한 파일명                                  |
| error        | 에러 UI를 나타내는 파일명                                                      |
| global-error | 글로벌 에러의 UI를 만들기위한 파일명                                           |
| route        | 서버사이드 API 진입점을 위한 파일명                                            |
| template     | Specialized re-rendered Layout UI                                              |
| default      | Fallback UI for Parallel Routes                                                |

> Good to know: .js, .jsx, or .tsx file extensions can be used for special files.
> 앞에 언급된 확장자가 사용가능하다는 것

## 컴포넌트 계층 (Component Hierarchy)

https://nextjs.org/docs/app/building-your-application/routing#component-hierarchy

> The React components defined in special files of a route segment are rendered in a specific hierarchy:

경로 세그먼트에서 특별한 파일에 정의된 리액트 컴포넌트는 특정 계층구조로 렌더링된다.

- layout.js
- template.js
- error.js (React error boundary)
- loading.js (React suspense boundary)
- not-found.js (React error boundary)
- page.js or nested layout.js

<img src="https://nextjs.org/_next/image?url=%2Fdocs%2Flight%2Ffile-conventions-component-hierarchy.png&w=3840&q=75">

위의 사진을 보면 layout.js가 가장 상위에 위치하고, 그 다음에 template.js, error.js, loading.js, not-found.js, page.js가 위치한다.
ErrorBoundary의 Fallback으로 error.js와 not-found.js가 사용된다.

> In a nested route, the components of a segment will be nested inside the components of its parent segment.

중첩된 경로에서는, 세그먼트의 컴포넌트들은 부모 세그먼트의 컴포넌트들 안에 중첩된다.

<img src="https://nextjs.org/_next/image?url=%2Fdocs%2Flight%2Fnested-file-conventions-component-hierarchy.png&w=3840&q=75">

이미지를 보면 B (settings)는 A (dashboard)의 하위 컴포넌트로 중첩된다.

## Colocation

https://nextjs.org/docs/app/building-your-application/routing#colocation

### 코로케이션이란?

> 코로케이션(colocation)은 단일 위치 내에 여러 엔티티를 배치하는 행위이다.

- https://ko.wikipedia.org/wiki/%EC%BD%94%EB%A1%9C%EC%BC%80%EC%9D%B4%EC%85%98

> In addition to special files, you have the option to colocate your own files (e.g. components, styles, tests, etc) inside folders in the app directory.

특별한 파일 외에도, 컴포넌트/ 스타일 / 테스트 / 기타 등등을 app 디렉토리 내부의 폴더에 함께 배치할 수 있다. 이를 코로케이션이라고 부른다.

> This is because while folders define routes, only the contents returned by page.js or route.js are publicly addressable.

폴더는 경로를 정의하지만, page.js나 route.js에서 반환된 내용만이 공개적으로 접근가능하기때문에, 다른 엔티티를 배치해서 코로케이션을 할 수 있다.

<img src="https://nextjs.org/_next/image?url=%2Fdocs%2Flight%2Fproject-organization-colocation.png&w=3840&q=75">

- 위 이미지를 보면 앱 라우터 (app 폴더) 내부에 components, lib 등의 폴더를 확인할 수 있다.
- /components/button, /lib/constants, /api/db와 같은 경로는 접근불가능한 엔티티다.

## Advanced Routing Patterns

https://nextjs.org/docs/app/building-your-application/routing#advanced-routing-patterns

> The App Router also provides a set of conventions to help you implement more advanced routing patterns.

앱 라우터는 더 복잡한 경로 패턴을 구현하는데 도움이 되는 일련의 컨벤션을 또한 제공한다.

어떤 컨벤션을 제공하나?

> Parallel Routes: Allow you to simultaneously show two or more pages in the same view that can be navigated independently. You can use them for split views that have their own sub-navigation. E.g. Dashboards.

병렬 경로: 동시에 두개 이상의 페이지를 하나의 뷰에서 보여줄 수 있게 해준다. 이것들은 서로 독립적으로 탐색할 수 있다. 하나의 뷰에서 각각 자신의 서브 네비게이션을 가지는 분할 뷰를 위해 사용할 수도 있다. 예를들어, 대시보드 같은 것이 예시.

> Intercepting Routes: Allow you to intercept a route and show it in the context of another route. You can use these when keeping the context for the current page is important. E.g. Seeing all tasks while editing one task or expanding a photo in a feed.

경로 인터셉트: 경로를 가로채서 다른 경로의 컨텍스트에서 보여줄 수 있게 해준다. 현재 페이지의 컨텍스트를 유지하는 것이 중요할 때 사용할 수 있다. 예를들어, 하나의 작업을 편집하면서 모든 작업을 볼 수 있거나, 피드에서 사진을 확대하는 것이 예시.

> These patterns allow you to build richer and more complex UIs, democratizing features that were historically complex for small teams and individual developers to implement.

이러한 패턴들은 더 풍부하고 복잡한 UI를 구축할 수 있게 해주며, 과거에는 작은 팀과 개발자들이 구현하기 어려웠던 기능들을 더 쉽게 구현할 수 있게 해준다.
