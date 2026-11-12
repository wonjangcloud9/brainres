<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

# useEffect가 두 번 실행되는 이유

거의 대부분 **React 18 이상의 `StrictMode`** 때문입니다. 버그가 아니라 **의도된 동작**입니다.

## 원인: StrictMode의 개발 모드 동작

개발 모드에서 `<StrictMode>`로 감싼 컴포넌트는 React가 일부러 다음 순서로 실행합니다.

```
마운트 → effect 실행 → 언마운트(cleanup 실행) → 다시 마운트 → effect 실행
```

```jsx
// main.jsx / index.js
<React.StrictMode>
  <App />
</React.StrictMode>
```

**목적:** cleanup 함수를 빠뜨린 effect를 찾아내기 위해서입니다. 구독, 타이머, 이벤트 리스너 등을 정리하지 않으면 두 번 실행될 때 문제가 바로 드러납니다.

**중요:** 이 동작은 **개발 모드에서만** 일어납니다. 프로덕션 빌드에서는 한 번만 실행됩니다.

## 올바른 해결 방법: cleanup 작성

StrictMode를 끄기보다는 effect가 두 번 실행돼도 문제가 없도록 만드는 것이 권장됩니다.

### 1. 이벤트 리스너 / 타이머

```jsx
useEffect(() => {
  const id = setInterval(() => console.log('tick'), 1000);
  return () => clearInterval(id); // cleanup
}, []);
```

### 2. 데이터 fetch (AbortController 사용)

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/data', { signal: controller.signal })
    .then(res => res.json())
    .then(setData)
    .catch(err => {
      if (err.name !== 'AbortError') console.error(err);
    });

  return () => controller.abort(); // 첫 번째 요청 취소
}, []);
```

또는 플래그 방식도 쓸 수 있습니다.

```jsx
useEffect(() => {
  let ignore = false;
  fetchData().then(result => {
    if (!ignore) setData(result);
  });
  return () => { ignore = true; };
}, []);
```

> 실무에서는 TanStack Query, SWR 같은 라이브러리를 쓰면 중복 요청과 캐싱 문제를 알아서 처리해 줍니다.

### 3. 정말 한 번만 실행돼야 하는 경우 (예: 앱 초기화)

컴포넌트 밖에서 실행하거나 모듈 레벨 플래그를 씁니다.

```jsx
let didInit = false;

function App() {
  useEffect(() => {
    if (didInit) return;
    didInit = true;
    initAnalytics(); // 앱 전체에서 한 번만
  }, []);
}
```

## StrictMode가 아닌데도 두 번 실행된다면

다음을 확인해 보세요.

| 원인 | 확인 방법 |
|---|---|
| **의존성 배열 값이 바뀜** | 객체나 함수를 의존성에 넣으면 렌더마다 새 참조가 생깁니다. `useMemo`/`useCallback`을 쓰거나 원시값을 의존성으로 쓰세요. |
| **의존성 배열 누락** | `useEffect(fn)`처럼 배열이 없으면 매 렌더마다 실행됩니다. |
| **컴포넌트가 리마운트됨** | 부모에서 `key`가 바뀌거나 조건부 렌더링으로 컴포넌트가 사라졌다가 다시 생기는 경우입니다. |
| **컴포넌트가 두 군데 렌더링됨** | 같은 컴포넌트를 실수로 두 번 사용하고 있지 않은지 확인하세요. |

## StrictMode를 꺼도 되나요?

`<React.StrictMode>`를 제거하면 두 번 실행은 사라집니다. 하지만 **권장하지 않습니다.** 프로덕션에서도 Fast Refresh, 라우트 전환, 향후 React 기능 등으로 리마운트는 언제든 일어날 수 있어서, cleanup이 없는 코드는 결국 다른 곳에서 버그를 일으킵니다.

---

코드를 보여주시면 어떤 원인인지, 어떻게 고치면 될지 구체적으로 봐 드릴게요.
