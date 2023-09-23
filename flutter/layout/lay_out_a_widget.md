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

