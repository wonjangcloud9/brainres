<!-- Q: 자바스크립트에서 const로 선언한 배열에 push 할 수 있어? -->

네, 가능합니다.

`const`는 **변수 재할당**을 막을 뿐, 참조하는 객체나 배열의 **내용 변경**은 막지 않습니다.

```js
const arr = [1, 2, 3];

arr.push(4);      // ✅ 가능 → [1, 2, 3, 4]
arr[0] = 100;     // ✅ 가능 → [100, 2, 3, 4]

arr = [5, 6, 7];  // ❌ TypeError: Assignment to constant variable.
```

`arr`가 저장하고 있는 것은 배열 자체가 아니라 배열을 가리키는 참조(주소)입니다. `const`는 그 참조가 다른 값으로 바뀌는 것만 막습니다.

내용 변경까지 막고 싶다면 `Object.freeze()`를 쓰면 됩니다.

```js
const arr = Object.freeze([1, 2, 3]);

arr.push(4);  // ❌ TypeError: Cannot add property 3, object is not extensible
```

참고로 `Object.freeze()`는 얕은(shallow) 동결이라, 중첩된 객체나 배열 내부까지는 막지 못합니다.
