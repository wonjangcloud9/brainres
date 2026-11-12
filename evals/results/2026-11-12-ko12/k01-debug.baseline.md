<!-- Q: 파이썬에서 TypeError: 'NoneType' object is not subscriptable 에러가 나. 왜 그래? -->

## 원인

`None`인 값에 대해 `[...]`(인덱싱/슬라이싱/키 조회)를 했기 때문에 나는 에러입니다. 즉, 어떤 변수가 기대와 달리 `None`인데 `x[0]`, `x["key"]` 같은 걸 시도한 거예요.

## 흔한 원인들

1. **반환값이 없는 함수 결과를 사용**
   ```python
   def get_data():
       data = [1, 2, 3]
       # return을 빼먹음 → None 반환

   result = get_data()
   print(result[0])  # TypeError
   ```

2. **제자리(in-place) 메서드의 반환값을 대입**
   ```python
   a = [3, 1, 2]
   a = a.sort()      # sort()는 None을 반환
   print(a[0])       # TypeError
   ```
   `append`, `extend`, `reverse`, `sort` 등도 마찬가지입니다.

3. **조건문에서 return이 빠지는 경로**
   ```python
   def find(x):
       if x > 0:
           return [x]
       # x <= 0이면 None 반환
   find(-1)[0]  # TypeError
   ```

4. **값이 없을 수 있는 함수**: `re.match()`, `dict.get()`, `os.environ.get()`, DB/API 조회 결과 등이 `None`을 반환할 수 있습니다.
   ```python
   m = re.match(r"\d+", "abc")
   m[0]  # m이 None → TypeError
   ```

## 디버깅 방법

- 에러 메시지의 **줄 번호**를 확인하고, 그 줄에서 `[...]`를 쓰는 변수를 찾습니다.
- 바로 앞에 `print(repr(변수))`를 넣어 `None`인지 확인합니다.
- 그 변수가 어디서 대입됐는지 거슬러 올라가 `return` 누락이나 `None` 반환 가능성을 찾습니다.

## 해결 방법

- 함수에 `return`을 추가한다.
- `a = a.sort()` 대신 `a.sort()` 또는 `a = sorted(a)`를 쓴다.
- `None` 가능성을 처리한다:
  ```python
  if result is not None:
      print(result[0])
  ```
  또는 `dict.get("key", 기본값)`처럼 기본값을 지정합니다.

---

정확한 원인을 알려면 에러가 난 코드와 전체 traceback을 붙여 주세요. 현재 디렉터리의 파일이라면 파일명을 알려주셔도 제가 직접 살펴볼 수 있어요.
