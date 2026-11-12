<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

# useEffect가 두 번 실행되는 이유

대부분은 **React 18 이상의 `StrictMode`** 때문입니다. **개발 모드에서만** 일어나고, 프로덕션 빌드에서는 한 번만 실행됩니다.

## StrictMode가 일부러 두 번 실행하는 이유

```jsx
// main.jsx / index.js
<React.StrictMode>
  <App />
</React.StrictMode>
```

StrictMode는 개발 중에 컴포넌트를 **마운트 → 언마운트 → 다시 마운트**합니다. 그래서 effect가 **실행 → cleanup → 다시 실행**됩니다.

목적은 **cleanup을 빠뜨린 버그를 찾는 것**입니다. 화면 전환, Fast Refresh, 앞으로 나올 기능(예: `<Activity>`)처럼 컴포넌트가 실제로 다시 마운트되는 상황은 많습니다. 두 번 실행했을 때 문제가 생긴다면, 그 코드는 그런 상황에서도 문제가 생깁니다.

## 해결 방법: StrictMode를 끄기보다 cleanup 작성

### 1. 구독 / 이벤트 리스너
```jsx
useEffect(() => {
  const handler = () => console.log('resize');
  window.addEventListener('resize', handler);
  return () => window.removeEventListener('resize', handler); // ✅ cleanup
}, []);
```

### 2. 타이머
```jsx
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id);
}, []);
```

### 3. 데이터 fetch
```jsx
useEffect(() => {
  let ignore = false;
  // 또는 AbortController 사용
  fetch(`/api/user/${id}`)
    .then(res => res.json())
    .then(data => {
      if (!ignore) setUser(data);
    });
  return () => { ignore = true; };
}, [id]);
```
요청은 두 번 가지만, 첫 번째 결과는 무시되므로 동작에는 문제가 없습니다. 실무에서는 **TanStack Query, SWR** 같은 라이브러리를 쓰면 캐싱과 중복 제거를 알아서 처리해 줍니다.

### 4. 정말 한 번만 실행해야 하는 경우
결제, 분석 이벤트 전송, 앱 초기화처럼 한 번만 실행돼야 하는 코드는 effect 밖으로 빼는 것이 좋습니다.
```jsx
// 모듈 최상단에서 한 번만 실행
if (typeof window !== 'undefined') {
  initAnalytics();
}

// 또는 사용자 이벤트 핸들러에서 실행
<button onClick={handlePurchase}>구매</button>
```

## StrictMode가 아닌 다른 원인

프로덕션에서도 두 번 실행된다면 아래를 확인해 보세요.

| 원인 | 확인할 점 |
|---|---|
| **의존성 배열 값이 바뀜** | 객체나 배열, 함수를 렌더링마다 새로 만들면 매번 다른 값으로 취급됩니다. `useMemo`/`useCallback`을 쓰거나 원시값을 의존성으로 넣으세요. |
| **의존성 배열 누락** | `useEffect(fn)`처럼 배열이 없으면 렌더링될 때마다 실행됩니다. |
| **컴포넌트가 실제로 재마운트됨** | 부모의 조건부 렌더링(`{show && <Comp />}`), `key` 변경, 라우터 설정을 확인하세요. |
| **컴포넌트가 두 곳에서 렌더링됨** | 같은 컴포넌트가 트리에 두 번 들어가 있는지 확인하세요. |

## 요약

- 개발 모드에서만 두 번 실행된다면 **StrictMode의 정상 동작**입니다.
- 끄지 말고 **cleanup 함수를 제대로 작성**하는 것이 올바른 대응입니다.
- 프로덕션에서도 두 번 실행된다면 **의존성 배열이나 재마운트**를 의심해 보세요.

어떤 코드에서 문제가 생기는지 보여주시면 구체적으로 봐드릴게요.
