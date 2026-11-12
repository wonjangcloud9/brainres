<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

개발 모드의 `<React.StrictMode>` 때문이에요. React 18부터 StrictMode는 컴포넌트를 마운트하고, 곧바로 언마운트한 뒤, 다시 마운트해요. 정리(cleanup) 누락 버그를 미리 드러내려는 의도예요. 프로덕션 빌드에서는 한 번만 실행돼요.

`main.jsx`나 `index.js`에 `<React.StrictMode>`가 있는지 확인해 보세요. Next.js는 `reactStrictMode` 설정이 기본으로 켜져 있어요.

**해결: 이펙트를 대칭으로 만드세요.** 시작한 것은 cleanup에서 반드시 끝내야 해요.

```jsx
useEffect(() => {
  const ctrl = new AbortController();

  fetch('/api/user', { signal: ctrl.signal })
    .then(r => r.json())
    .then(setUser)
    .catch(e => {
      if (e.name !== 'AbortError') throw e;
    });

  return () => ctrl.abort(); // 첫 번째 실행을 취소해요
}, []);
```

구독, 타이머, 이벤트 리스너도 같아요. `subscribe`에는 `unsubscribe`를, `setInterval`에는 `clearInterval`을 짝지어 주세요.

**피할 것:**
- StrictMode를 지우는 건 증상만 가리는 방법이에요. 실제 cleanup 버그가 남아요.
- `useRef` 플래그로 두 번째 실행을 막는 방법도 권하지 않아요. 언마운트 후 재마운트 시나리오에서 깨져요.

데이터 fetching이 목적이라면 TanStack Query나 SWR이 중복 요청과 취소를 대신 처리해 줘요.

문제가 되는 `useEffect` 코드를 붙여 주시면 cleanup을 어떻게 짝지을지 짚어 드릴게요.
