# Defining-Routes

https://nextjs.org/docs/app/building-your-application/routing/defining-routes

> This page will guide you through how to define and organize routes in your Next.js application.

이 페이지는 Next.js 앱에서 경로를 정의하고 구성하는 방법을 안내한다.

## Creating Routes (경로 생성하기)

> Next.js uses a file-system based router where folders are used to define routes.

Next.js는 경로를 정의하는데 사용된 폴더들의 위치를 기반으로하는 파일 시스템 기반의 라우터를 사용한다.

> Each folder represents a route segment that maps to a URL segment. To create a nested route, you can nest folders inside each other.

각 폴더는 URL 세그먼트와 매핑되는 경로 세그먼트를 나타낸다. 중첩 경로를 만들려면, 각 폴더를 중첩시키면 된다.

<img src="https://nextjs.org/_next/image?url=%2Fdocs%2Flight%2Froute-segments-to-path-segments.png&w=3840&q=75">

- 위 이미지에서 dashboard, settings가 각각 경로 세그먼트고 각 세그먼트가 URL 경로에서 매핑된다.
- /dashboard 폴더를만들고 그 하위에 settings 폴더를 만들면 /dashboard/settings 경로가 생성된다.

> A special page.js file is used to make route segments publicly accessible.

page.js라는 특별한 파일은 경로 세그먼트를 공개적으로 접근가능하게 만들기 위해 사용된다.

<img src="https://nextjs.org/_next/image?url=%2Fdocs%2Flight%2Fdefining-routes.png&w=3840&q=75">

- 위의 이미지에서 보듯이 app 하위에 있는 page.js는 / 경로로 매핑된다.
- dashboard 폴더에 있는 page.js는 /dashboard 경로로 매핑된다.
- /dashboard/settings 폴더에 있는 page.js는 /dashboard/settings 경로로 매핑된다.

> In this example, the /dashboard/analytics URL path is not publicly accessible because it does not have a corresponding page.js file. This folder could be used to store components, stylesheets, images, or other colocated files.

위의 예시에서 /dashboard/anlytics URL 경로는 page.js 파일이 없기 때문에 공개적으로 접근할 수 없다. 이 폴더는 컴포넌트, 스타일시트, 이미지, 또는 다른 파일들을 저장하는데 사용될 수 있다.

> Good to know: .js, .jsx, or .tsx file extensions can be used for special files.

## Creating UI

https://nextjs.org/docs/app/building-your-application/routing/defining-routes#creating-ui

> Special file conventions are used to create UI for each route segment. The most common are pages to show UI unique to a route, and layouts to show UI that is shared across multiple routes.

특별한 파일 컨벤션은 각 경로 세그먼트에 대한 UI를 만들기 위해 사용된다. 가장 일반적인 것은 경로마다 유니크한 UI를 보여주기 위해 사용되는 page (page.js)와 여러 경로에 걸쳐 공유되는 UI를 보여주기 위해 사용되는 layout (layout.js)이다.

> For example, to create your first page, add a page.js file inside the app directory and export a React component:

예를들어, 첫번째 페이지를 만들기 위해 app 디렉토리에 page.js 파일을 추가하고 export를 하면된다.

```tsx
// app/page.tsx

export default function Page() {
  return <h1>Hello, Next.js!</h1>;
}
```
