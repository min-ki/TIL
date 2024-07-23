# Linking And Navigating

https://nextjs.org/docs/app/building-your-application/routing/linking-and-navigating

Next.js에서 경로들을 탐색하기 위한 방법은 4가지가 있다.

1. `<Link>` 컴포넌트 사용
2. `useRouter` 훅 사용 (client components)
3. `redirect` 함수 사용 (server components)
4. native History API 사용

## `<Link>` 컴포넌트

> <Link> is a built-in component that extends the HTML <a> tag to provide prefetching and client-side navigation between routes. It is the primary and recommended way to navigate between routes in Next.js.

`<Link>` 컴포넌트는 Next.js에서 제공하는 내장 컴포넌트로, <a> 태그를 확장해서 prefetching과 클라이언트 사이드 경로들 간의 탐색을 제공한다. Next.js에서 라우트들 간의 탐색을 하는 주로 권장되는 방법이다.

```tsx
import Link from "next/link";

export default function Page() {
  return <Link href="/dashboard">Dashboard</Link>;
}
```

### Example

#### Linking to Dynamic Segments

> When linking to dynamic segments, you can use template literals and interpolation to generate a list of links. For example, to generate a list of blog posts:

동적 세그먼트에 링크를 걸 때, 템플릿 리터럴과 보간(interpolation)을 사용해서 링크 목록을 생성할 수 있다.

다음 예시를 보자. (블로그 포스트 목록을 생성하는 예시)

```tsx
import Link from "next/link";

export default function PostList({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>
          // 템플릿 리터럴안에 문자열 보간을 통해 동적 세그먼트로 연결을 한다.
          <Link herf={`/blog/${post.slug}`}>{post.title}</Link>
        </li>
      ))}
    </ul>
  );
}
```

#### Checking Active Links

> You can use usePathname() to determine if a link is active. For example, to add a class to the active link, you can check if the current pathname matches the href of the link:

`usePathname()`을 사용해서 링크가 활성화되어 있는지 확인할 수 있다. 예를 들어, 활성화된 링크에 클래스를 추가하기 위해 현재 경로명이 링크의 href와 일치하는지 확인할 수 있다.

```tsx
"use client";

import { usePathname } from "next/navigation";
import Link from "next/link";

export function Links() {
  const pathname = usePathname(); // 현재 경로명을 가져온다.

  return (
    <nav>
      <ul>
        <li>
          <Link className={`link ${pathname === "/" ? "active" : ""}`} href="/">
            Home
          </Link>
        </li>
        <li>
          <Link
            className={`link ${pathname === "/about" ? "active" : ""}`}
            href="/about"
          >
            About
          </Link>
        </li>
      </ul>
    </nav>
  );
}
```

#### Scrolling to an `id`

> The default behavior of the Next.js App Router is to scroll to the top of a new route or to maintain the scroll position for backwards and forwards navigation.

Next.js 앱 라우터의 기본 동작은 새로운 경로로 스크롤을 맨 위로 이동하거나 뒤로/앞으로 탐색할 때 스크롤 위치를 유지하는 것이다.

> If you'd like to scroll to a specific id on navigation, you can append your URL with a # hash link or just pass a hash link to the href prop. This is possible since <Link> renders to an <a> element.

만약 특정 id로 스크롤을 하고 싶다면, URL에 # 해시 링크를 추가하거나 href 속성에 해시 링크를 전달할 수 있다. 이것은 `<Link>`가 `<a>` 요소로 렌더링되기 때문에 가능하다.

```tsx
<Link href="/dashboard#settings">Settings</Link>

// Output
<a href="/dashboard#settings">Settings</a>
```

#### Disabling scroll restoration

> The default behavior of the Next.js App Router is to scroll to the top of a new route or to maintain the scroll position for backwards and forwards navigation.

Next.js 앱 라우터의 기본 동작은 새로운 경로로 스크롤을 맨 위로 이동하거나 **뒤로/앞으로 탐색할 때 스크롤 위치를 유지하는 것**이다.

> If you'd like to disable this behavior, you can pass scroll={false} to the <Link> component, or scroll: false to router.push() or router.replace().

만약 이 동작을 비활성화하고 싶다면, `<Link>` 컴포넌트에 `scroll={false}`를 전달하거나 `router.push()`나 `router.replace()`에 `scroll: false`를 전달할 수 있다.

```tsx
<Link href="/dashboard" scroll={false}>
  Dashboard
</Link>
```

```tsx
// useRouter
import { useRouter } from "next/navigation";

const router = useRouter();

router.push("/dashboard", { scroll: false });
```
