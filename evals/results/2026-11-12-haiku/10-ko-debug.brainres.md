<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

**가장 흔한 원인은 개발 모드의 `<React.StrictMode>`예요.** React 18 이후 StrictMode는 개발 환경에서 컴포넌트를 마운트, 언마운트, 다시 마운트해서 effect를 두 번 실행해요. 정리(cleanup) 로직이 올바른지 찾으려는 의도라서 버그가 아니에요.

원인은 크게 세 가지예요.

1. **StrictMode (개발 모드 전용)**: `main.jsx`나 `index.js`에 있는 경우가 많아요. 프로덕션 빌드에서는 한 번만 실행돼요.
2. **의존성 배열 문제**: 객체, 배열, 함수를 렌더마다 새로 만들어 넘기면 effect가 계속 다시 실행돼요. 이 경우는 두 번이 아니라 여러 번 실행돼요.
3. **실제 재마운트**: 부모가 조건에 따라 자식을 떼었다 다시 붙이면 effect가 다시 실행돼요.

**확인 방법:** `npm run build` 후 프로덕션 빌드를 실행해 보세요. 한 번만 실행되면 StrictMode가 원인이에요. 다만 제가 아직 코드를 보지 않아서 단정하기는 어려워요.

**StrictMode 때문이라면 cleanup을 추가해 두세요.** 요청이 중복돼도 안전하도록 만드는 방법이에요.

```jsx
useEffect(() => {
  const controller = new AbortController();
  fetch('/api/data', { signal: controller.signal })
    .then(r => r.json())
    .then(setData);
  return () => controller.abort();
}, []);
```

StrictMode를 끄는 방법도 있지만, 버그를 가리는 것이라 권장하지 않아요. 프로젝트에서 `StrictMode`를 검색해서 결과를 보여 주시면, 어디서 두 번 실행되는지 같이 확인해 드릴게요.
