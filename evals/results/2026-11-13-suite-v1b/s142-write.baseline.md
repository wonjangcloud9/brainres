<!-- Q: 자바스크립트로 배열에서 중복을 제거하는 함수 만들어줘. -->

```javascript
// 원시값(숫자, 문자열 등) 배열의 중복 제거
const unique = (arr) => [...new Set(arr)];

unique([1, 2, 2, 3, 'a', 'a']); // [1, 2, 3, 'a']
```

`Set`은 `SameValueZero` 비교를 하므로 `NaN`도 중복 처리되고, 처음 나온 순서가 유지됩니다.

객체 배열에서 특정 키 기준으로 중복을 제거해야 한다면:

```javascript
const uniqueBy = (arr, keyFn) => {
  const seen = new Set();
  return arr.filter((item) => {
    const key = keyFn(item);
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
};

uniqueBy(
  [{ id: 1, n: 'a' }, { id: 1, n: 'b' }, { id: 2, n: 'c' }],
  (o) => o.id
);
// [{ id: 1, n: 'a' }, { id: 2, n: 'c' }]
```

파일로 저장하거나 테스트가 필요하면 말씀해 주세요.
