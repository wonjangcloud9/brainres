<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

개발 모드의 `<StrictMode>`가 일부러 effect를 두 번 실행해서 그래요. React 18부터 생긴 동작이에요.

**왜 그렇게 하나요?**
React는 컴포넌트를 마운트하고, 바로 언마운트하고, 다시 마운트해요. 정리(cleanup) 함수가 빠졌거나 잘못된 effect를 개발 중에 미리 찾으려는 거예요. 순서는 이래요.

1. effect 실행
2. cleanup 실행
3. effect 다시 실행

**확인 방법**
`index.js`나 `main.jsx`에 `<React.StrictMode>`가 있는지 보세요. 프로덕션 빌드에서는 한 번만 실행돼요. Next.js는 `reactStrictMode`가 기본으로 켜져 있어요.

**올바른 해결**
StrictMode를 끄지 말고 cleanup을 추가하세요.

```jsx
useEffect(() => {
  const ws = new WebSocket(url);
  return () => ws.close(); // 정리
}, [url]);
```

fetch는 `AbortController`로 취소하거나 `ignore` 플래그를 쓰면 돼요.

```jsx
useEffect(() => {
  let ignore = false;
  fetch(url).then(r => r.json()).then(d => { if (!ignore) setData(d); });
  return () => { ignore = true; };
}, [url]);
```

**StrictMode가 아닌데도 두 번 실행된다면**
- 의존성 배열의 객체나 함수가 매 렌더마다 새로 만들어져요.
- 부모의 `key`가 바뀌거나 부모가 컴포넌트를 다시 마운트해요.

코드를 붙여 주시면 어느 경우인지 바로 짚어 드릴게요.
