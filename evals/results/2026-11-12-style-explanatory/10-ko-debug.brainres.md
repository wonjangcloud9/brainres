<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

개발 모드에서 `<StrictMode>`가 컴포넌트를 마운트, 언마운트, 재마운트하기 때문이에요. React 18부터 생긴 동작이고, 프로덕션 빌드에서는 한 번만 실행돼요.

React는 effect에 정리(cleanup) 코드가 빠졌는지 미리 드러내려고 일부러 이렇게 해요. 정리 함수가 올바르면 두 번 실행해도 결과가 같아야 해요. 그래서 중복 실행이 눈에 띈다면 정리 코드가 없다는 신호예요.

`main.jsx`에서 `<StrictMode>`로 감싼 부분을 확인해 보세요.

```jsx
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>
)
```

**해결은 `<StrictMode>`를 지우는 게 아니라 cleanup을 추가하는 거예요.** 예를 들어 구독이나 타이머는 이렇게 고쳐요.

```jsx
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id); // 언마운트 때 정리
}, []);
```

데이터 fetch라면 요청이 두 번 나가는 게 보일 수 있어요. 이때는 `AbortController`로 첫 요청을 취소해요.

```jsx
useEffect(() => {
  const controller = new AbortController();
  fetch('/api/data', { signal: controller.signal })
    .then(r => r.json())
    .then(setData)
    .catch(e => { if (e.name !== 'AbortError') throw e; });
  return () => controller.abort();
}, []);
```

`useRef` 플래그로 두 번째 실행을 막는 방법은 피하세요. 문제를 숨길 뿐이고, 실제 환경의 재마운트(예: Offscreen, 빠른 새로고침)에서 다시 깨져요.

`★ Insight ─────────────────────────────────────`
- StrictMode의 이중 실행은 개발 모드 전용이에요. 버그가 아니라 cleanup 누락을 찾는 검사예요.
- 두 번 실행해도 안전한 effect가 올바른 effect예요. 이 성질을 "멱등성"이라고 불러요.
- 의존성 배열이 `[]`가 아니어도 마운트 직후 한 번은 똑같이 두 번 실행돼요.
`─────────────────────────────────────────────────`

두 번 실행되는 effect 코드를 붙여 주시면 어떤 cleanup이 필요한지 같이 봐 드릴게요.
