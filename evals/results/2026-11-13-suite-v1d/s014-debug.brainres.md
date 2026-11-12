<!-- Q: 리액트에서 'Too many re-renders' 에러가 떠요. 왜 그래요? -->

렌더링 중에 state를 바꾸는 코드가 실행돼서 무한 루프가 생기기 때문이에요. state가 바뀌면 리렌더링되고, 그 렌더링에서 또 state를 바꾸면 React가 한도(약 25회)에서 멈추고 이 에러를 던져요.

가장 흔한 원인은 이벤트 핸들러에 함수를 넘기지 않고 **호출 결과**를 넘기는 경우예요.

```jsx
// ❌ 렌더링할 때마다 즉시 실행됨 → setCount → 리렌더 → 반복
<button onClick={setCount(count + 1)}>+</button>

// ✅ 클릭할 때 실행되도록 함수로 감싸기
<button onClick={() => setCount(count + 1)}>+</button>
```

다른 원인은 두 가지예요.

1. **컴포넌트 본문에서 직접 setState 호출**: 조건 없이 `setX(...)`를 본문에 쓰면 매 렌더마다 실행돼요. 이벤트 핸들러나 `useEffect` 안으로 옮기세요.
2. **useEffect 의존성 문제**: effect 안에서 setState를 하는데 의존성 배열이 없거나, 매 렌더 새로 만들어지는 객체·배열을 의존성에 넣으면 루프가 돼요.

```jsx
// ❌ 의존성 배열 없음 → 매 렌더마다 실행
useEffect(() => { setData(fetchData()); });

// ✅ 필요한 값만 의존성에 넣기
useEffect(() => { setData(fetchData()); }, []);
```

어느 경우인지는 에러 메시지의 컴포넌트 이름과 스택에서 확인할 수 있어요. 해당 컴포넌트 코드를 붙여 주시면 원인 줄을 짚어 드릴게요.
