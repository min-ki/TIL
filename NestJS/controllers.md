# Controllers

## Controller

---

- 클라이언트에서 보내는 요청을 처리하고 클라이언트에게 요청을 반환하는 책임을 가진 역할을 담당하는 것
- 컨트롤러의 목적은 **어플리케이션을 위한 특정한 요청을 받기 위한 것**
- 라우팅 메커니즘은 컨트롤러가 어떠한 요청을 처리할 지 제어하는 것
- 각 컨트롤러는 하나 이상의 경로를 가지는 경우가 많고, 각기 다른 경로(라우터)들은 다른 액션(비지니스 로직)을 수행함
- NestJS에서 컨트롤러를 생성하기 위해서는, **클래스**와 **데코레이터**를 사용한다.
- 데코레이터는 클래스에 필요한 메타 데이터들을 연결하기 위해서 사용하고, Nest가 routing map을 생성하도록 한다. (request에 부합하는 컨트롤러와 묶기 위해서)

## Routing

- 컨트롤러를 정의하기 위해서 `@Controller()` 데코레이터 사용
- `@Controller('cats')` 와 같이 라우트 경로의 prefix를 optional하게 지정할 수 있음
- path prefix를 사용하면 연관이 있는 라우터들을 쉽게 그룹으로 묶을 수 있고, 중복되는 코드를 줄일 수 있음

```ts
import { Controller, Get } from "@nestjs/common";

@Controller("cats")
export class CatsController {
  @Get()
  findAll(): string {
    return "This action returns all cats";
  }
}
```

`$ nest g controller cats` 와 같이 CLI를 통해서 쉽게 controller를 생성할 수 있음

- `@Get()` HTTP Request 메서드 데코레이터는 Nest 프레임워크에게 HTTP 요청을 위한 특정한 엔드포인트를 처리하는 핸들러를 생성 해준다.
- 엔드포인트는 HTTP 요청 메서드와 라우트 경로와 일치하게 된다.
- 여기서 라우트 경로란 컨트롤러에서 선언된 prefix와 결합되어 결정된 경로이다.
- 위의 코드에서는 findAll의 메서드는 GET /cats 의 라우팅 경로를 가지게 된다.
- Nest 프레임워크는 `@Controller()` 와 `@Get()` 을 통해서 요청을 해당 핸들러와 자동으로 맵핑시켜준다.
- `@Controller()` 와 `@Get()` 의 path 설정은 둘 다 optional 하다.
- Nest에서는 위의 코드를 실행하면 200 status code를 반환한다. 그 이유는 Nest 에서는 두개의 다른 Response를 조작하는 옵션을 제공하는 개념이 존재

  1. **Standard (recommended)**

     위와 같은 데코레이터 내장 메서드를 사용해 요청을 처리하는 핸들러가 자바스크립트 오브젝트 혹은 배열을 반환할 때, 이것은 자동적으로 JSON으로 직렬화 된다.

     그러나, 자바스크립트의 원시 타입을 반환할 때는 Nest 프레임워크는 자동적으로 직렬화를 하지 않고 보낸다.

     이러한 점은 응답의 처리를 간결하게 만들어준다. 단지 우리는 값을 반환하고, Nest 프레임워크가 나머지 부분을 담당해준다.

     더욱이, 응답 코드는 POST 요청에서 201 응답 코드를 사용하는 것을 제외하고, 항상 200을 기본 값으로 가진다.

     우리는 이러한 프레임워크의 행동을 `@HttpCode(...)` 데코레이터를 핸들러 레벨에서 추가함으로써 쉽게 변경할 수 있다.

  2. **Library-specific**

     우리는 express와 같은 라이브러리에서 사용하는 응답 객체 (response object)를 `@Res()` 라는 데코레이터에 의해 핸들러 메서드에 주입된 응답 객체를 대신하여 사용할 수 있다.

     이러한 접근 방식은, 각 라이브러리의 Native한 방식을 사용하여 처리할 수 있다.

     예를 들어 express에서는 `response.status(200).send()` 와 같이 사용할 수 있다.

  **Warning**
  Nest는 핸들러가 library-specific 한 방식을 사용하는 것을 나타내는 `@Res()` 혹은 `@Next()` 사용하는 것을 감지할 수 있다.
  만약 동시에 standard와 library specific한 방식을 사용할 경우 standard 접근 방식은 자동으로 disabled 되고 생각하는 대로 더이상 동작하지 않는다.
  두개의 방식을 동시에 사용하고 싶다면, `@Res({ passthrough: true })` 같이 반드시 옵션을 설정해야 한다.

## Request object

핸들러들은 종종 클라이언트 요청에 대한 상세한 정보에 접근할 필요가 있다. Nest 프레임워크는 플랫폼 아래서 **request object**에 접근하는 방법을 제공한다. Nest 프레임워크에서는 `@Req()` 데코레이터를 핸들러 메서드의 시그니쳐에 추가함으로써 요청 객체를 Nest 프레임워크가 주입 할 수 있도록 지시할 수 있다.

```ts
import { Controller, Get, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("cats")
export class CatsController {
  @Get()
  findAll(@Req() request: Request): string {
    return "This action returns all cats";
  }
}
```

express 요청 객체에 대한 타입 지원이 필요하다면 `@types/express` 패키지를 설치하면 된다.

request object는 HTTP 요청을 나타내고, query string, parameters, headers, body 등과 같은 프로퍼티들을 가진다.

NestJS에서는 이러한 프로퍼티들을 직접 수동으로 사용하지 않고, 데코레이터를 통해서 사용할 수 있다.

Nest 프레임워크는 HTTP 플랫폼들 (Express와 Fastify 등)간의 타입 호환성을 위해서 `@Res()` 와 `@Response()` 데코레이터들을 제공한다.

`@Res()` 는 단순히 `@Response()` 의 별칭이다. 이 두개의 데코레이터들은 네이티브 플랫폼의 response 객체의 인터페이스에 직접적으로 관련이 있다.

위의 데코레이터들 사용할 때에는 각 플랫폼에 해당하는 타입 정의를 import 하여 사용하면 된다.

`@Res()` or `@Response()` 를 메서드 핸들러에서 주입을 할 땐, Nest 프레임워크에서 해당 핸들러를 Library-specific mode로 인식하는 것을 기억하고 사용할 때에는 response를 잘 관리하도록 주의를 기울여야한다.

## Resources

Nest 프레임워크는 모든 표준 HTTP 메서드를 데코레이터들을 통해서 제공한다.

- `@Get()`
- `@Post()`
- `@Put()`
- `@Delete()`
- `@Patch()`
- `@Options()`
- `@Head()`
- `@All()` : 모든 요청을 처리하는 엔드포인트를 정의

## Route Wildcards

Nest 프레임워크는 패턴 기반의 라우팅 또한 지원한다. 예를들어, 와일드 카드(asterisk) 를 사용하여 어떠한 문자열의 조합을 매칭할 수도 있다.

- ?, +, \*, () 를 라우트 경로로 사용하고, 정규 표현식으로 사용 가능
- 하이픈(-) 과 점 (.) 은 문자열 기반 경로로 문자 그대로 해석된다.

```ts
@Get('ab*cd')
findAll() {
	return 'THis route uses a wildcard';
}
```

## Status Code (상태 코드)

Status Code는 POST 요청 (201 status code) 를 제외하고 항상 기본적으로 200 이다.

핸들러 레벨에서 `@HttpCode(...)` 데코레이터를 추가하여 동작을 쉽게 변경할 수 있다.

`@HttpCode()` 데코레이터는 `@nestjs/common` 로부터 가져온다.

```ts
@Post()
@HttpCode(204)
create() {
	return 'This action adds a new cat';
}
```

## Header (헤더)

사용자 지정 응답 헤더를 사용하려면 `@Header()` 데코레이터를 사용하거나 라이브러리 별 응답 객체를 사용하고 `res.header()` 를 직접 호출 할 수도 있다.

`@Header()` 데코레이터는 `@nestjs/common` 으로 부터 가져온다.

```ts
@Post()
@Header('Cache-Control', 'none')
create() {
	return 'This action adds a new cat';
}
```

## Redirection

응답을 특정 URL로 redirection 하려면 `@Redirect()` 데코레이터 혹은 `res.redirect()` 를 사용하면 된다.

`@Redirect()` 데코레이터는 필수적으로 url을 입력받고 선택적으로 status Code를 입력받는다. 입력을 생략한다면 디폴트로 302 를 사용한다.

```ts
@Get()
@Redirect('https://nestjs.com', 301)
```

가끔은 동적으로 redirect URL 혹은 HTTP Status code를 반환하기를 원할 때는 핸들러 메서드로 부터 다음과 같은 모양의 오브젝트를 반환하면 된다.

```ts
{
	"url": string,
	"statusCode": number
}
```

위의 반환되는 값들은 `@Redirect()` 데코레이터로 입력되는 값들을 오버라이드한다.

```ts
@Get('docs')
@Redirect('https://docs.nestjs.com', 302)
getDocs(@Query('version') version) {
	if (version && verion === '5') {
		return { url: 'https://docs.nestjs.com/v5/ };
	}
}
```

## Route parameters

정적 경로는 요청의 일부로 동적 데이터를 수락해야 하는 경우 동작하지 않는다. 매개 변수로 경로를 정의하기 위해서는 경로에 매개 변수 토큰을 추가하여 동적 값을 캡쳐 할 수 있다.

`@Param()` 는 메서드의 파라미터 데코레이터로 사용되고, 메소드 내부에서 파라미터를 사용할 수 있게 해준다.

`@Param()` 데코레이터는 `@nestjs/common` 에서 import 하여 사용

```ts
@Get(':id')
findOne(@Param() params): string {
	console.log(params.id)
	return 'This action return a $#{params.id} cat';
}
```

## Sub-Domain Routing

`@Controller` 데코레이터는 요청들의 HTTP host와 특정한 값이 매칭되는데 필요한 `host` 옵션을 가져올 수 있다.

Fastify 는 nested routers에 대한 지원이 부족하므로 서브 도메인 라우팅을 사용할 때는 Express adapter가 대신 사용될 수 있다.

```ts
@Controller({ host: "admin.example.com" })
export class AdminController {
  @Get()
  index(): string {
    return "Admin page";
  }
}
```

또한, 라우트 경로는 비슷하기 때문에 `host` 옵션은 호스트 옵션에서 동적인 값 또한 취할 수 있다. 동적 값을 사용할 경우에, 호스트 파라미터는 `@HostParam()` 데코레이터를 통해 접근이 가능하다.

```ts
@Controller({ host: ":account.example.com" })
export class AccountController {
  @Get()
  getInfo(@HostParam("account") account: string) {
    // 위처럼 @HostParam() 안의 값과 위의 @Controller 내의 :account와 같이 일치시키면 된다.
    return account;
  }
}
```

## Scope

Nest 프레임워크에서는 거의 모든 것이 들어오는 요청에서 공유된다. 데이터베이스에 대한 연결 풀, 전역 상태의 싱글 톤 서비스 등

Node.js는 모든 요청이 별도의 스레드에 의해 처리되는 요청 / 응답 다중 스레드 상태 비 저장 모델을 따르지 않는다. 따라서 싱글 톤 인스턴스를 사용하는 것이 안전하다.

하지만 가끔은 컨트롤러의 요청 기반으로 동작하는 것이 바람직할 때가 있다. 예를 들어, GraphQL 애플리케이션의 요청 별 캐싱, 요청 추적 또는 다중 테넌시와 같은 것

## Asynchronicity

Nest 프레임워크는 `async` functions 들을 잘 지원한다. 모든 async function 은 Promise를 반환한다. 즉, 우리는 비동기 함수에서 값의 반환을 연기할 수 있고 Nest 프레임워크는 스스로 이것을 resolve 할 수 있다.

```ts
@Get()
async findAll(): Promise<any[]> {
	return [];
}
```

위의 코드는 유효한 코드이다. 게다가, Nest의 라우터 핸들러는 RxJS의 **observable streams**을 반환 할 수 있게 함으로써 더욱 강력해질 수 있다. Nest는 자동적으로 소스를 구독하고 스트림이 완료되면 마지막으로 내 보낸 값을 가져온다.

```ts
@Get()
findAll(): Observable<any[]> {
	return of([]);
}
```

## Request payloads

POST 라우트 핸들러에서 클라이언트 params를 받고 싶을 때는 `@Body()` 데코레이터를 추가하면 된다.

먼저, 우리는 DTO(Data Transfer Object) 스키마를 결정해야한다. DTO는 데이터가 네트워크를 통해서 어떻게 정의되는지 나타내는 객체이다. DTO 스키마를 정의하기 위해서는 Typescript의 interfaces를 사용하거나 혹은 클래스를 사용하면 된다.

Nest 프레임워크의 공식 문서에서는 클래스 방식을 사용하는데 그 이유는 클래스는 자바스크립트의 ES6 표준이고 컴파일된 자바스크립트에서 실제 엔티티로 보존되기 때문에 사용한다고 적혀있다.

반면에, 인터페이스를 사용하면 변환하는 시점에서 삭제되기 때문에 Nest는 런타임 시점에 DTO를 참조할 수 없게 된다.

이러한 차이점은 중요한데, `Pipes` 와 같은 기능들이 런타임 시점에 값 들의 메타 타입에 접근할 추가적인 가능성이 있기 때문이다.

```ts
// DTO 정의

export class CreateCatDto {
  name: string;
  age: string;
  breed: string;
}
```

```ts
@Post()
async create(@Body() createCatDto: CreateCatDto) {
	return 'This action adds a new cat';
}
```
