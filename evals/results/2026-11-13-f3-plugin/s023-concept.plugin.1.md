<!-- Q: 클로저가 뭐예요? -->

클로저(closure)는 함수가 자기가 만들어진 곳의 변수를 기억하고, 그 바깥 범위가 끝난 뒤에도 쓸 수 있게 하는 기능이에요.

보통 변수는 함수가 끝나면 사라져요. 하지만 안쪽 함수가 그 변수를 참조하면, 언어가 그 변수를 계속 살려 둬요. 이렇게 "함수 + 기억된 변수" 묶음이 클로저예요.

**예시 (JavaScript)**

```js
function makeCounter() {
  let count = 0;          // makeCounter가 끝나도 사라지지 않아요
  return function () {
    count += 1;
    return count;
  };
}

const counter = makeCounter();
counter(); // 1
counter(); // 2
```

`makeCounter()`는 이미 끝났지만, 반환된 함수가 `count`를 기억해요. 그래서 호출할 때마다 값이 올라가요. 바깥에서는 `count`를 직접 건드릴 수 없어서, 값을 숨기는 용도로도 써요.

**어디에 쓰나요?** 이벤트 핸들러, 콜백, 데이터 은닉, 함수 팩토리에 자주 써요. JavaScript, Python, Swift, Kotlin 등 대부분의 현대 언어가 지원해요.

혹시 프로그래밍 언어 **Clojure**를 물어보신 거라면 말씀해 주세요. 그건 Lisp 계열의 함수형 언어라서 따로 설명드릴게요. 쓰시는 언어를 알려 주시면 그 언어로 예제를 바꿔 드릴 수 있어요.
