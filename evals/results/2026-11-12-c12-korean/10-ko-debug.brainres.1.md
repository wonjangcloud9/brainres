<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

React 18 이상의 개발 모드에서 `<StrictMode>`가 컴포넌트를 일부러 두 번 마운트하기 때문이에요. 프로덕션 빌드에서는 한 번만 실행돼요. (~95% 확신. `index.js`나 `main.jsx`에 `<React.StrictMode>`가 있는지 보면 바로 확인돼요.)

**왜 이렇게 하나요?**
React는 마운트 → 언마운트 → 다시 마운트를 흉내 내요. 그래서 cleanup 함수가 없거나 잘못 짠 effect를 개발 중에 찾아낼 수 있어요. 버그를 숨기지 않고 드러내려는 의도예요.

**예시: 구독 effect**

```jsx
useEffect(() => {
  const ws = new WebSocket(url);
  return () => ws.close(); // cleanup이 있으면 두 번 실행돼도 안전해요
}, [url]);
```

개발 모드에서 실행 순서는 이래요.

1. 연결 생성
2. cleanup으로 연결 종료
3. 연결 다시 생성

cleanup이 있으면 최종 상태는 한 번만 실행한 것과 같아요.

**해결 방법**

- **cleanup을 추가해요.** 이게 정석이에요. 타이머, 이벤트 리스너, 구독을 모두 해제하세요.
- **fetch는 `AbortController`로 취소해요.**
  ```jsx
  useEffect(() => {
    const ctrl = new AbortController();
    fetch(url, { signal: ctrl.signal }).then(/* ... */);
    return () => ctrl.abort();
  }, [url]);
  ```
- **데이터 요청이 중복되는 게 싫다면** React Query나 SWR 같은 라이브러리를 쓰세요. 캐싱과 중복 제거를 해줘요.

**피해야 할 방법**
`useRef`로 "이미 실행했는지" 플래그를 두거나 StrictMode를 끄는 방법은 권하지 않아요. 문제를 숨길 뿐이고, 실제 버그가 프로덕션에서 나타날 수 있어요.

StrictMode가 없는데도 두 번 실행된다면, 부모가 리렌더링되며 의존성 배열의 값이 바뀌고 있을 수 있어요. 다음 단계로 effect 코드와 의존성 배열을 보여 주세요.
