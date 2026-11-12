<!-- Q: 리액트에서 'Too many re-renders' 에러가 떠요. 왜 그래요? -->

'Too many re-renders' 에러는 렌더링 중에 state를 바꾸는 코드가 있어서, 렌더 → setState → 다시 렌더 → setState … 무한 루프가 생길 때 발생합니다. React가 무한 루프를 막으려고 던지는 에러예요.

## 흔한 원인

**1. 이벤트 핸들러를 호출해버린 경우 (가장 흔함)**

```jsx
// ❌ 렌더링 중에 즉시 실행됨
<button onClick={setCount(count + 1)}>+</button>

// ✅ 함수를 넘겨야 함
<button onClick={() => setCount(count + 1)}>+</button>
```

`onClick={handleClick()}`처럼 괄호를 붙여도 같은 문제가 생깁니다. `onClick={handleClick}` 또는 `onClick={() => handleClick(id)}`로 쓰세요.

**2. 컴포넌트 본문에서 직접 setState 호출**

```jsx
function App() {
  const [count, setCount] = useState(0);
  setCount(1); // ❌ 렌더할 때마다 실행 → 무한 루프
  return <div>{count}</div>;
}
```

필요하면 `useEffect` 안으로 옮기거나, 이벤트 핸들러에서 호출하세요.

**3. useEffect 의존성 문제**

```jsx
// ❌ 의존성 배열이 없으면 매 렌더마다 실행 → setState → 렌더 …
useEffect(() => {
  setData(fetchData());
});

// ✅
useEffect(() => {
  setData(fetchData());
}, []);
```

의존성에 객체/배열 리터럴이나 매번 새로 만들어지는 함수를 넣어도 매 렌더마다 effect가 다시 실행됩니다. `useMemo`/`useCallback`으로 고정하거나 원시값만 의존성으로 쓰세요.

**4. 렌더 중에 부모의 setState를 호출하는 경우**

자식 컴포넌트 렌더링 중에 부모에서 받은 `setX`를 호출하면 같은 현상이 일어납니다.

## 찾는 방법

- 에러 스택에서 어떤 컴포넌트인지 확인
- 해당 컴포넌트에서 `set...(` 호출이 렌더 본문, JSX 속성(`onClick={foo()}`), 의존성 없는 `useEffect` 중 어디에 있는지 확인

코드를 붙여주시면 정확히 어느 부분이 문제인지 짚어드릴게요.
