<!-- Q: 파이썬에서 TypeError: 'NoneType' object is not subscriptable 에러가 나. 왜 그래? -->

`None`인 값에 `[...]`(인덱싱)를 써서 나는 에러예요. 어떤 변수나 함수 반환값이 `None`인데, 리스트나 딕셔너리처럼 `x[0]`, `x["key"]`로 접근한 거예요.

**흔한 원인 4가지**

1. 반환값 없는 함수: `return`이 없거나 조건에 따라 빠져서 `None`이 나와요.
2. 제자리 변경 메서드: `list.sort()`, `list.append()`, `list.reverse()`는 `None`을 반환해요.
3. 못 찾은 결과: `re.match()`, `dict.get()`, `soup.find()`는 없으면 `None`을 줘요.
4. 외부 입력: JSON, DB, API 응답에서 값이 비어 있어요.

**예시**

```python
nums = [3, 1, 2]
sorted_nums = nums.sort()   # sort()는 None을 반환해요
print(sorted_nums[0])       # TypeError: 'NoneType' object is not subscriptable
```

고치려면 `sorted(nums)`를 쓰거나 `nums.sort()` 후 `nums[0]`을 쓰면 돼요.

```python
m = re.match(r"(\d+)", "abc")
print(m[1])                 # m이 None이라 에러
```

이럴 땐 `if m:`으로 먼저 확인해요.

**원인 찾는 법**

트레이스백의 마지막 줄 번호를 보고, 그 줄에서 `[...]` 바로 앞의 변수를 `print(변수)`나 `print(type(변수))`로 찍어 보세요. `None`이 나오면 그 변수를 만든 곳으로 거슬러 올라가면 돼요.

에러가 난 줄의 코드와 트레이스백을 붙여 주면 정확한 원인을 짚어 드릴게요.
