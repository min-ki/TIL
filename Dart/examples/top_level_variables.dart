String description;

void main() {
    // 초기화 전에 사용하면 에러발생
    // Dart/examples/top_level_variables.dart:1:8: Error: Field 'description' should be initialized because its type 'String' doesn't allow null.
    description = "Feijoada!"; // 페이조아다? 브라질 대표 음식 고기 스튜
    print(description);
}

