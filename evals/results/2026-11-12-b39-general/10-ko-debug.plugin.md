<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

개발 모드의 **StrictMode**가 effect를 일부러 두 번 실행해서 그래요. React 18부터 `<React.StrictMode>` 안에서는 컴포넌트가 마운트 → 언마운트 → 다시 마운트 순서로 한 번 더 돌아요.

**왜 그럴까요?**
cleanup이 빠졌거나 effect가 멱등하지 않은 버그를 미리 드러내려는 의도예요. 실제 앱에서도 컴포넌트가 언마운트됐다가 다시 마운트될 수 있어서, 그때 안전한지 확인하는 거예요.

**확인 방법**
- `index.js`나 `main.jsx`에서 `<React.StrictMode>`로 감싸졌는지 봐요.
- 프로덕션 빌드(`npm run build`)에서는 한 번만 실행돼요.

**해결 방법**
StrictMode를 끄는 건 권장하지 않아요. 대신 effect를 두 번 돌아도 안전하게 만드세요. 예를 들면 이렇게요.

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/data', { signal: controller.signal })
    .then(res => res.json())
    .then(setData)
    .catch(err => {
      if (err.name !== 'AbortError') console.error(err);
    });

  return () => controller.abort(); // cleanup
}, []);
```

구독, 타이머, 이벤트 리스너도 cleanup에서 해제하면 돼요.

**StrictMode와 무관한 경우**
의존성 배열의 객체나 함수가 렌더마다 새로 만들어지면 effect가 반복 실행돼요. 프로덕션에서도 두 번 이상 실행된다면 이쪽을 의심하세요.

다음으로, effect 코드와 의존성 배열을 붙여 주세요. 원인을 바로 짚어 드릴게요.
