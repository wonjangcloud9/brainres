<!-- Q: useEffect가 뭐고, 언제 써야 하고, 자주 하는 실수는 뭐예요? -->

useEffect는 렌더링이 끝난 뒤 컴포넌트 밖의 시스템(서버, 타이머, 브라우저 API 등)과 동기화하는 React 훅이에요.

```jsx
useEffect(() => {
  const ws = new WebSocket(`wss://chat.example.com/${roomId}`);
  return () => ws.close(); // 정리(cleanup)
}, [roomId]); // roomId가 바뀔 때만 다시 실행
```

실행 시점은 의존성 배열이 정해요. 배열이 없으면 매 렌더링 후, `[]`이면 처음 한 번, `[a, b]`이면 a나 b가 바뀔 때 실행해요.

## 언제 쓰나요

- 외부 시스템 연결: 웹소켓, 구독, 이벤트 리스너
- 브라우저 API 사용: `document.title`, 타이머, `localStorage`
- 서버 데이터 가져오기: 다만 React Query나 SWR 같은 라이브러리가 더 안전해요

## 자주 하는 실수

1. **파생값을 state와 effect로 만들기.** 렌더링 중에 계산하면 돼요.
   ```jsx
   // 나쁨
   useEffect(() => setFullName(first + ' ' + last), [first, last]);
   // 좋음
   const fullName = first + ' ' + last;
   ```
2. **클릭 같은 이벤트 처리를 effect에 넣기.** 사용자 동작의 결과는 이벤트 핸들러에서 처리해요.
3. **의존성 배열 누락.** 오래된 값(stale closure)을 읽는 버그가 생겨요. `eslint-plugin-react-hooks`의 `exhaustive-deps` 경고를 따르세요.
4. **cleanup 누락.** 리스너나 타이머가 쌓이고, 느린 응답이 나중에 도착해 state를 덮어써요. fetch는 `AbortController`나 `ignore` 플래그로 막아요.
5. **객체나 함수를 의존성에 넣기.** 매 렌더링마다 새로 만들어져 effect가 무한 반복돼요. effect 안으로 옮기거나 `useMemo`, `useCallback`을 써요.

개발 모드의 Strict Mode에서는 effect가 두 번 실행돼요. 이건 cleanup이 빠졌는지 찾아주는 의도된 동작이라 버그가 아니에요.

판단 기준은 하나예요. "React 밖의 무언가와 맞춰야 하나?"에 아니오라면 effect가 필요 없을 가능성이 높아요. 지금 쓰는 effect 코드를 보여주시면 필요한지 같이 확인해 드릴게요.
