<!-- Q: 자바스크립트로 배열에서 중복을 제거하는 함수 만들어줘. -->

`Set`을 쓰면 한 줄로 끝나요.

```js
const unique = (arr) => [...new Set(arr)];

unique([1, 2, 2, 3, 1]); // [1, 2, 3]
unique(["a", "b", "a"]); // ["a", "b"]
```

첫 등장 순서는 유지돼요. `Set`은 `===`와 비슷하게 비교하므로 원시값(숫자, 문자열)은 잘 되지만, 객체는 참조가 같아야 같은 값으로 봐요. 또 `NaN`은 서로 같다고 처리해요.

객체 배열은 기준 키를 정해서 걸러야 해요.

```js
const uniqueBy = (arr, keyFn) => {
  const seen = new Set();
  return arr.filter((item) => {
    const key = keyFn(item);
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
};

uniqueBy([{ id: 1 }, { id: 2 }, { id: 1 }], (o) => o.id);
// [{ id: 1 }, { id: 2 }]
```

파일로 저장하길 원하면 경로를 알려주세요.
