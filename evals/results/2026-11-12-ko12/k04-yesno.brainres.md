<!-- Q: 자바스크립트에서 const로 선언한 배열에 push 할 수 있어? -->

네, 할 수 있어요. `const`는 변수 재할당만 막고, 배열 내용 변경은 막지 않아요.

```js
const arr = [1, 2];
arr.push(3);      // OK → [1, 2, 3]
arr[0] = 10;      // OK → [10, 2, 3]

arr = [4, 5];     // TypeError: Assignment to constant variable.
```

변수 `arr`이 가리키는 배열 참조는 고정되지만, 그 배열 객체는 여전히 변경 가능해서 그래요. 객체도 같은 규칙이에요.

내용 변경까지 막으려면 `Object.freeze(arr)`를 쓰세요. 이후 `push`는 `TypeError`를 던져요. 단, `freeze`는 얕게(shallow) 적용돼서 중첩된 배열이나 객체는 막지 못해요.
