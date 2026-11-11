<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

React 18 이상의 개발 모드에서 `<StrictMode>`가 컴포넌트를 일부러 마운트 → 언마운트 → 재마운트해서 그래요. 프로덕션 빌드에서는 한 번만 실행돼요. (확신 ~90%. `main.tsx`나 `index.js`에서 `<React.StrictMode>`가 있는지 보면 바로 확인돼요.)

**왜 이렇게 하나요?**
cleanup 함수가 빠졌거나 잘못된 effect를 찾아내려는 의도예요. effect가 "실행 → 정리 → 다시 실행"을 견디면, 나중에 컴포넌트가 여러 번 마운트돼도 안전해요.

**어떻게 고치나요?**
StrictMode를 끄지 말고, effect에 cleanup을 추가해요. 예를 들어 fetch는 이렇게 해요.

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/user', { signal: controller.signal })
    .then(res => res.json())
    .then(setUser)
    .catch(err => {
      if (err.name !== 'AbortError') console.error(err);
    });

  return () => controller.abort(); // 첫 번째 실행을 정리해요
}, []);
```

구독이나 타이머도 같은 방식이에요.

```jsx
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id);
}, []);
```

**StrictMode가 원인이 아닐 수도 있어요.**
아래 경우에도 두 번 실행될 수 있어요.

| 원인 | 확인 방법 |
|---|---|
| 의존성 배열의 객체/함수가 매 렌더마다 새로 만들어져요 | 배열 값을 `console.log`로 찍어 비교해요 |
| 부모가 `key`를 바꿔 재마운트해요 | 프로덕션 빌드에서도 두 번 나오는지 봐요 |
| 컴포넌트가 두 곳에서 렌더돼요 | React DevTools에서 인스턴스 수를 세요 |

프로덕션 빌드(`npm run build` 후 실행)에서도 두 번 나오면 StrictMode가 아니라 위 표의 원인이에요.

다음 단계로, 실제 effect 코드를 붙여주시면 어떤 cleanup이 필요한지 짚어드릴게요.
