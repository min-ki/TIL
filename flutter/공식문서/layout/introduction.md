# [Layout in Flutter](https://docs.flutter.dev/ui/layout)

## 개요
- 위젯(Widgets)은 UI를 만들기 위해 사용되는 클래스이다.
- 위젯은 레이아웃과 UI 요소 둘다 사용된다.
- 복잡한 위젯을 만들기 위해 간단한 위젯을 조합한다.

## Lay out a widget

이번섹션은 플러터에서 하나의 위젯을 배치하기 위해서 어떻게 해야하는지 다룬다.

### 1. Select a layout widget

다양한 레이아웃 위젯중에서 선택을 하자.

- Align, AspectRatio, Baseline, Center, ConstrainedBox... 많다.

### 2. Create a visible widget

텍스트 위젯은 다음과 같이 만든다.
```dart
Text('Hello World'),
```

이미지 위젯은 다음과 같이 만든다.

```dart
Image.asset(
    'images/lake.jpg',
    fit: BoxFit.cover,
)
```

아이콘 위젯은 다음과 같이 만든다.

```dart
Icon(
    Icons.star,
    color: Colors.red[500],
)
```

### 3. Add the visible widget to the layout widget

눈에 보이는 위젯을 레이아웃 위젯에 추가한다.

모든 레이아웃 위젯은 다음과 같은 속성을 가진다.

- child: Center와 Container같은 단일 자식을 가지는 위젯은 child 속성을 사용한다.
- children: Row, Column, ListView와 같은 다중 자식을 가지는 위젯은 children 속성을 사용한다.

텍스트(Text) 위젯을 Center 위젯에 추가하자.
```dart

// Center layout widget은 단일 자식을 가지므로 child 속성을 사용한다.
const Center(
    child: Text('Hello World'),
)
```

### 4. Add the layout widget to the page

플러터 앱은 그 자체로 위젯이고, 모든 위젯들은 `build()` 메서드를 가진다.

build() 메서드에 의해 초기화되고 반환된 위젯은 위젯에 보이게 된다.

#### MaterialApp

Material app에서, `Scaffold` 위젯을 사용할 수 있다. 이 위젯은 기본 배너, 배경색, 그리고 drawers, snack bars, bottom sheets와 같은 것들을 추가할 수 있는 API를 가지고 있다.

```dart
// lib/main.dart

import 'package:flutter/material.dart';

class MyApp extends StatelessWidget {
    const MyApp({super.key});

    @override
    Widget build(BuildContext context) {
        return MaterialApp(
            title: 'Flutter layout demo',
            home: Scaffold(
                appBar: AppBar(
                    title: const Text('Flutter layout demo'),
                ),
                // 레이아웃 위젯을 body에 추가하면 된다.
                body: const Center(
                    child: Text('Hello World'),
                ),
            ),
        );
    }
}
```

> Material library는 Material Design 원칙을 따라 구현된 위젯들이다. 

#### Non-Material apps

Material app이 아닌 경우, `Center` 위젯을 build() 메서드에 직접 추가하면 된다.

```dart
// lib/main.dart

class MyApp extends StatelessWidget {
    const MyApp({super.key});

    @override
    Widget build(BuildContext context) {
        return Container(
            decoration: const BoxDecoration(color: Colors.white),
            child: const Center(
                child: Text(
                    'Hello World',
                    textDirection: TextDirection.ltr,
                    style: TextStyle(
                        fontSize: 32,
                        color: Colors.black87,
                    ),
                ),
            ),
        ),
    };
}
```

material app이 아닌 앱은 기본으로 앱바, 타이틀, 배경색을 가지지 않는다.
만약 이런 요소들을 원하면 직접 만들어라.


## Lay out multiple widgets vertically and horizontally

가장 흔한 레이아웃 패턴 중 하나는 위젯을 수직 또는 수평으로 배치하는 것이다.

- 수평으로 위젯들을 배치하기 위해서는 `Row` 위젯을 사용하면 된다.
- 수직으로 위젯들을 배치하기 위해서는 `Column` 위젯을 사용하면 된다.
- Row, Column들은 저 수준의 위젯. 많은 커스터마이징을 할 수 있다.
- Row 대신 ListTile, Column 대신 ListView와 같은 고수준 위젯을 사용할 수도 있다.

## Aligning widgets

row 또는 column에 위젯을 배치할 때, `mainAxisAlignment`과 `crossAxisAlignment` 속성을 사용하여 위젯을 정렬할 수 있다.

- row에서 main axis는 수평이고, cross axis는 수직
![row_diagram](https://docs.flutter.dev/assets/images/docs/ui/layout/row-diagram.png)

- column에서 main axis는 수직이고, cross axis는 수평
![column_diagram](https://docs.flutter.dev/assets/images/docs/ui/layout/column-diagram.png)

```dart
Row(
    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
    children: [
        Image.asset('images/pic1.jpg'),
        Image.asset('images/pic2.jpg'),
        Image.asset('images/pic3.jpg'),
    ],
);s
```

- 위에서 Image.asset에 사용되는 파일들은 pubspec.yaml에 추가되어야 한다.
- 만약, Image.network를 사용ㅇ하면 pubspec.yaml은 수정할 필요 없다.

```dart
Column(
    mainAxisAlignment: MainAxisAlignment.spaceEvenly, // 컬럼위젯은 주축이 수직
    // 수직방향으로 이미지들이 쌓인다.
    children: [
        Image.asset('images/pic1.jpg'),
        Image.asset('images/pic2.jpg'),
        Image.asset('images/pic3.jpg'),
    ],
)

```

## Sizing widgets

레이아웃이 디바이스에 맞추기에 너무 크다면, 노란색과 검정색 패턴이 영향받은 모서리에 나타난다.
![layout-too-large](https://docs.flutter.dev/assets/images/docs/ui/layout/layout-too-large.png)

위젯은 row 또는 column에서 `Expanded` 위젯을 사용해서 알맞은 사이즈로 조정될 수 있다.

```dart

Row(
    crossAxisAlignment: CrossAxisAlignment.center,
    children: [
        Expanded(
            child: Image.asset('images/pic1.jpg'),
        ),
        Expanded(
            child: Image.asset('images/pic2.jpg'),
        ),
        Expanded(
            child: Image.asset('images/pic3.jpg'),
        ),
    ],
);
```

flex 속성을 사용하여 위젯이 얼만큼 공간을 차지할 지 결정할 수 있다.
flex 단어 뜻을 보니 관절을 굽히다. 근육을 수축시키다라는 뜻이 있다.

그렇다면, flex factor가 1인것은 1만큼 수축시킨다는 뜻

그러면 flex factor를 2로 늘리면 수축시킨것을 조금 늘려서 2배로 공간을 차지하게 되는 것으로 이해하면 쉬울 것 같다.

```dart
Row(
    crossAxisAlignment: CrossAxisAlignment.center,
    children: [
        Expanded(
            child: Image.asset('images/pic1.jpg'),
        ),
        Expanded(
            flex: 2,
            child: Image.asset('images/pic2.jpg'),
        ),
        Expanded(
            child: Image.asset('images/pic3.jpg'),
        ),
    ],
);
```
![flex-factor-2](https://docs.flutter.dev/assets/images/docs/ui/layout/row-expanded-visual.png)