<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

React 18 이상의 개발 모드에서 `<StrictMode>`가 컴포넌트를 일부러 두 번 마운트하기 때문일 가능성이 높아요 (~90% 확신).

**원리**

StrictMode는 마운트 → 언마운트 → 다시 마운트를 한 번씩 돌려요. 그래서 effect가 실행되고, cleanup이 실행되고, 다시 effect가 실행돼요. 클린업이 빠졌거나 effect가 멱등하지 않은 버그를 미리 찾아내려는 의도예요. 프로덕션 빌드에서는 한 번만 실행돼요.

**확인 방법**

`main.jsx`(또는 `index.js`)에 아래 코드가 있는지 보세요.

```jsx
<React.StrictMode>
  <App />
</React.StrictMode>
```

빌드한 결과물(`npm run build` 후 실행)에서 한 번만 찍히면 이 원인이 맞아요.

**해결 방법**

StrictMode를 끄는 것은 권장하지 않아요. 대신 effect가 두 번 돌아도 안전하도록 cleanup을 작성하세요.

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/data', { signal: controller.signal })
    .then(res => res.json())
    .then(setData)
    .catch(err => {
      if (err.name !== 'AbortError') throw err;
    });

  return () => controller.abort(); // 첫 번째 실행을 취소해요
}, []);
```

구독이나 타이머도 같아요. `addEventListener`는 `removeEventListener`로, `setInterval`은 `clearInterval`로 정리하면 돼요.

**StrictMode가 아닌 다른 원인**

프로덕션에서도 두 번 실행된다면 아래를 확인하세요.

1. 의존성 배열의 객체나 함수가 렌더마다 새로 만들어지는지
2. 부모가 `key` 변경이나 조건부 렌더링으로 컴포넌트를 다시 마운트하는지
3. 같은 컴포넌트가 화면에 두 번 렌더되는지

코드를 붙여주시면 어느 경우인지 바로 짚어드릴게요.
