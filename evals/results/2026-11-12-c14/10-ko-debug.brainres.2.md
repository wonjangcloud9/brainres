<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

개발 모드에서 `<StrictMode>`를 쓰고 있다면, React가 일부러 effect를 두 번 실행해요. 프로덕션 빌드에서는 한 번만 실행돼요.

**왜 그렇게 하나요?** React 18부터 StrictMode는 컴포넌트를 마운트 → 언마운트 → 다시 마운트해요. cleanup 함수가 빠졌거나 잘못된 effect를 개발 중에 바로 드러내기 위해서예요.

**확인 방법:** `main.jsx` (또는 `index.js`)에 `<React.StrictMode>`가 있는지 보세요.

```jsx
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

**해결 방법:** StrictMode를 끄는 것은 권하지 않아요. 문제를 숨길 뿐이에요. 대신 effect가 두 번 돌아도 안전하게 cleanup을 작성하세요.

```jsx
useEffect(() => {
  const ws = new WebSocket(url);
  return () => ws.close(); // 언마운트 때 정리
}, [url]);
```

fetch라면 `AbortController`로 첫 번째 요청을 취소해요.

```jsx
useEffect(() => {
  const ctrl = new AbortController();
  fetch(url, { signal: ctrl.signal })
    .then(r => r.json())
    .then(setData)
    .catch(e => { if (e.name !== 'AbortError') throw e; });
  return () => ctrl.abort();
}, [url]);
```

StrictMode가 없는데도 두 번 실행된다면, 의존성 배열의 객체나 함수가 렌더마다 새로 만들어지는 경우일 수 있어요. 코드를 보여 주시면 원인을 찾아 드릴게요.
