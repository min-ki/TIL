// Null Safety

void nullableType() {
    int? count; // non-nullable 초기값은 null
    print(count); // null

    count = 10;
    print(count); // 10
}

void nonNullableType() {
    int count;
    count = 10;
    print(count); // 10
}

// void nonNullableTypeError() {
//     int count; // non-nullable 초기값은 null
    
//     // Dart/examples/variables.dart:19:11: Error: Non-nullable variable 'count' must be assigned before it can be used.
//     print(count); // 초기화전에 사용하면 에러발생
// }


void main() {
    nullableType();
    nonNullableType();
    // nonNullableTypeError();
}