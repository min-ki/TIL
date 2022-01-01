# unittest.mock - 모의 객체 라이브러리

- mock은 파이썬에서 테스트 대상 시스템의 일부분을 모의 객체로 교체할 수 있는 라이브러리
- 많은 mocking 프레임워크에서 사용하는 기록(record) -> 재생(replay) or 액션 (action) -> 어서션(assertion) 패턴을 기반으로 한다.

## Side_effect

- side_effect를 사용하면 모의 객체(mock)가 호출될 때 예외를 발생시키는 것을 포함해 부작용을 수행할 수 있다.

```python
mock = Mock(side_effect=KeyError('foo'))
mock()

Traceback (most recent call last):
    ...
KeyError: 'foo'

```

## patch() 데코레이터

- 클래스나 객체를 쉽게 모킹할 수 있도록 하는 것

```python

from unittest.mock import patch

@patch('module.ClassName2') # 아래 ClassName1이 실행된 후 실행
@patch('module.ClassName1') # 먼저 실행된다.
def test(MockClass1, MockClass2):

    module.ClassName1()
    module.ClassName2()

    assert MockClass1 is module.ClassName1
    assert MockClass2 is module.ClassName2

    assert MockClass1.called
    assert MockClass2.called

```

## 파이썬 매직 메서드의 Mocking

- MagicMock 클래스를 사용

```python

mock = MagicMock()

# __str__ 매직메서드를 모킹한다.
mock.__str__.return_value = 'foobarbaz'

str(mock) # 'foobarbaz'
```
