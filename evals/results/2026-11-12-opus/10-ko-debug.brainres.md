<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

개발 모드에서 `<StrictMode>`가 effect를 **일부러** 두 번 실행해서 그래요.

React 18부터 StrictMode는 컴포넌트를 마운트하고, 바로 언마운트한 뒤, 다시 마운트해요. cleanup이 빠진 effect를 찾아내려는 동작이에요. 프로덕션 빌드에서는 한 번만 실행돼요.

**확인 방법**
1. `main.jsx`나 `index.js`에서 `<React.StrictMode>`로 감쌌는지 봐요.
2. `npm run build`로 빌드해서 로그가 한 번만 찍히는지 봐요.

**해결책**
StrictMode를 끄지 말고 cleanup 함수를 넣어요. 끄면 버그가 숨을 뿐이에요.

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/user', { signal: controller.signal })
    .then(res => res.json())
    .then(setUser)
    .catch(err => {
      if (err.name !== 'AbortError') throw err;
    });

  return () => controller.abort(); // 첫 실행은 여기서 취소돼요
}, []);
```

첫 요청은 cleanup에서 취소돼요. 그래서 두 번째 요청만 상태에 반영돼요. 이벤트 리스너나 타이머도 같은 방식으로 cleanup에서 해제해요.

**StrictMode가 원인이 아니라면**
- 의존성 배열이 없으면 렌더마다 실행돼요.
- 배열 안에 렌더마다 새로 만드는 객체나 함수가 있어요.
- 부모가 `key`를 바꿔서 컴포넌트가 다시 마운트돼요.

먼저 진입 파일에서 StrictMode 여부를 확인해 보세요. 코드를 붙여 주시면 원인을 짚어 드릴게요.
