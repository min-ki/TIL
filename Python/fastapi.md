# FastAPI

## Swagger 문서에 request duration 표시하기

아래와 같이 FastAPI 앱을 생성할 때 `swagger_ui_parameters` 파라미터를 추가한다. 참고 (https://github.com/tiangolo/fastapi/issues/564)

```python
app = FastAPI(swagger_ui_parameters={"displayRequestDuration": True})
```