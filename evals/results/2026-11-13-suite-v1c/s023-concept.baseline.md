<!-- Q: 클로저가 뭐예요? -->

**클로저(closure)**는 함수가 자신이 정의된 위치의 변수(렉시컬 환경)를 기억하고, 그 함수가 원래 스코프 밖에서 호출되더라도 해당 변수에 계속 접근할 수 있는 개념입니다.

## 간단한 예시 (JavaScript)

```javascript
function makeCounter() {
  let count = 0;          // 외부 함수의 지역 변수

  return function () {    // 내부 함수 = 클로저
    count += 1;
    return count;
  };
}

const counter = makeCounter();
console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
```

`makeCounter()`의 실행은 이미 끝났지만, 반환된 내부 함수는 `count`를 계속 기억하고 있습니다. 이렇게 "함수 + 그 함수가 기억하는 환경"의 묶음이 클로저입니다.

## Python 예시

```python
def make_multiplier(n):
    def multiply(x):
        return x * n    # 바깥 함수의 n을 기억
    return multiply

double = make_multiplier(2)
print(double(5))  # 10
```

## 어디에 쓰나요?

- **데이터 은닉**: `count`를 외부에서 직접 수정할 수 없음 (private 변수처럼 동작)
- **함수 팩토리**: 설정값을 기억하는 함수를 만들어냄 (`make_multiplier`처럼)
- **콜백/이벤트 핸들러**: 정의 시점의 상태를 유지한 채 나중에 실행
- **함수형 프로그래밍**: 커링, 메모이제이션 등

## 주의할 점

- 클로저가 변수를 계속 참조하므로, 불필요하게 오래 유지하면 **메모리가 해제되지 않을 수** 있습니다.
- 반복문 안에서 클로저를 만들 때, JavaScript의 `var`는 함수 스코프라 모든 클로저가 같은 변수를 공유하는 함정이 있습니다. `let`을 쓰면 반복마다 새 변수가 생겨 해결됩니다.

특정 언어에서의 클로저가 궁금하시면 말씀해 주세요.
