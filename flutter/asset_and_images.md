# 플러터에서 Assets과 이미지 추가하는 법

## 1. pubspec.yaml 파일에 assets 추가

프로젝트 루트를 기준으로 파일을 명시해준다.

```yaml
flutter:
  assets:
    - assets/my_icon.png
    - assets/background.png
```

폴더 내 전체 파일을 추가하고 싶다면 아래와 같이 명시해준다.

```yaml
flutter:
  assets:
    - assets/
```


## Asset bundling

플러터는 앱을 빌드할 때, 앱에 필요한 모든 asset을 `asset bundle` 이라고 부르는 특별한 저장공간에 저장한다. 이 assets들은 앱에서 런타임에 읽을 수 있다.


# Reference
- https://docs.flutter.dev/ui/assets/assets-and-images