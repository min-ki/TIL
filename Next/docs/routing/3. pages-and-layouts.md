# Pages and Layouts

https://nextjs.org/docs/app/building-your-application/routing/pages-and-layouts

layout.js, page.js, template.js와 같은 특별한 파일들은 경로(route)를 위한 UI를 만들수 있게 해준다.
이 페이지(문서)는 이러한 파일들을 어떻게 & 언제 사용하는지 설명한다.

## Pages (페이지)

> A page is UI that is unique to a route. You can define a page by default exporting a component from a page.js file.

페이지는 경로마다 유니크한 UI이다. page.js 파일로부터 컴포넌트를 `default exporting` 함으로써 페이지를 정의할 수 있다.

- default export와 같이 볼만한 개념은 named export

> For example, to create your index page, add the page.js file inside the app directory:

예를들어, index 페이지를 만들기 위해서는 app 폴더 내에 page.js 파일을 추가하면 된다.

<img src="https://nextjs.org/_next/image?url=%2Fdocs%2Flight%2Fpage-special-file.png&w=3840&q=75">

위 이미지 예시는 app 폴더 바로 하위의 page.js는 / 경로에 매핑되고, dashboard 폴더 내의 page.js는 /dashboard 경로에 매핑된다.

```typescript
// `app/page.tsx` is the UI for the `/` URL
// / URL을 위한 UI를 정의하기 위한 컴포넌트
export default function Page() {
  // export default로 컴포넌트를 정의
  return <h1>Hello, Home page!</h1>;
}
```

> Then, to create further pages, create a new folder and add the page.js file inside it. For example, to create a page for the /dashboard route, create a new folder called dashboard, and add the page.js file inside it:

그리고, 추가적인 페이지를 만들기 위해서는 새로운 폴더를 만들고 그 안에 page.js 파일을 추가하면 된다. 예를들어, /dashboard 경로를 위한 페이지를 만들기 위해서 dashboard라는 새로운 폴더를 만들고 그 안에 page.js 파일을 추가하면 된다.

```typescript
// app/dashboard/page.tsx
// `app/dashboard/page.tsx` is the UI for the `/dashboard` URL
export default function Page() {
  return <h1>Hello, Dashboard Page!</h1>;
}
```

### Good to know:

- The .js, .jsx, or .tsx file extensions can be used for Pages.
- A page is always the leaf of the route subtree.
- A page.js file is required to make a route segment publicly accessible.
- Pages are Server Components by default, but can be set to a Client Component.
- Pages can fetch data. View the Data Fetching section for more information.
