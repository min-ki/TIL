# Comments

https://dart.dev/language/comments

> Dart supports single-line comments, multi-line comments, and documentation comments.

다트는 한줄 주석 (single-line), 여러줄 주석 (multi-line), 문서 주석 (documentation comments)을 지원한다.

## 한줄 주석 (single-line comments)

> A single-line comment begins with //. Everything between // and the end of line is ignored by the Dart compiler.

한줄 주석은 `//`로 시작한다. `//`와 라인의 끝 사이의 모든 것은 다트 컴파일러에 의해 무시된다.

```dart
void main() {
    // TODO: refactor into an AbstractLlamaGreetingFactory?
    print('Welcome to my Llama farm!');
}
```

## 여러줄 주석 (multi-line comments)

> A multi-line comment begins with /_ and ends with _/. Everything between /_ and _/ is ignored by the Dart compiler (unless the comment is a documentation comment; see the next section). Multi-line comments can nest.

여러줄 주석은 `/*`로 시작하고 `*/`로 끝난다. `/*`와 `*/` 사이의 모든 것은 다트 컴파일러에 의해 무시된다. 여러줄 주석은 중첩될 수 있다.

```dart
void main() {
  /*
   * This is a lot of work. Consider raising chickens.

  Llama larry = Llama();
  larry.feed();
  larry.exercise();
  larry.clean();
   */
}
```
