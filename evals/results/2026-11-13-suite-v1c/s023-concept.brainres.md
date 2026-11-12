<!-- Q: 클로저가 뭐예요? -->

클로저(closure)는 함수가 자기가 만들어진 곳의 변수를 기억해서, 그 바깥 범위가 끝난 뒤에도 계속 쓸 수 있는 기능이에요.

예시를 JavaScript로 볼게요.

```javascript
function makeCounter() {
  let count = 0;          // 바깥 함수의 변수
  return function () {    // 안쪽 함수가 count를 기억해요
    count += 1;
    return count;
  };
}

const counter = makeCounter();
counter(); // 1
counter(); // 2
```

`makeCounter()`는 이미 끝났지만, 반환된 함수는 `count`에 계속 접근해요. 이 "함수 + 기억하는 변수 묶음"이 클로저예요.

쓰임새는 크게 두 가지예요.

- **상태 숨기기**: `count`는 밖에서 직접 바꿀 수 없어요. 반환된 함수로만 바꿀 수 있어요.
- **설정값 고정**: 값을 미리 넣어 둔 함수를 만들 수 있어요. 예를 들어 `makeMultiplier(3)`처럼요.

주의할 점이 하나 있어요. 클로저는 변수의 값이 아니라 변수 자체를 기억해요. 그래서 반복문 안에서 `var`로 만든 변수를 클로저가 잡으면, 모두 같은 변수를 보게 돼요. `let`을 쓰면 반복마다 새 변수가 생겨서 이 문제가 없어요.

Python, Swift, Kotlin 등 다른 언어 기준으로 보고 싶으시면 말씀해 주세요.
