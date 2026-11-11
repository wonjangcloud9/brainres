<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

개발 모드에서 `<React.StrictMode>`가 켜져 있기 때문이에요. React 18 이상은 StrictMode에서 컴포넌트를 마운트 → 언마운트 → 다시 마운트해서 effect를 일부러 두 번 실행해요.

**프로덕션 빌드에서는 한 번만 실행돼요.**

## 왜 이렇게 하나요?

cleanup 함수가 빠졌거나 잘못된 effect를 개발 중에 바로 찾으려는 거예요. effect를 두 번 돌려 보면 구독 해제나 요청 취소를 빠뜨린 코드가 드러나요.

## 확인 방법

`index.js` 또는 `main.jsx`에 이런 코드가 있는지 보세요.

```jsx
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

Next.js라면 `next.config.js`의 `reactStrictMode: true`를 보세요. 이 줄을 지우면 한 번만 실행되지만, 권장하지 않아요.

## 올바른 해결: cleanup 추가

예를 들어 fetch가 두 번 나가는 경우예요.

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/users', { signal: controller.signal })
    .then(res => res.json())
    .then(setUsers)
    .catch(err => {
      if (err.name !== 'AbortError') console.error(err);
    });

  return () => controller.abort();
}, []);
```

첫 번째 요청은 cleanup에서 취소되고, 두 번째만 결과를 반영해요. 구독이나 타이머도 같은 방식이에요.

```jsx
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id);
}, []);
```

## StrictMode가 원인이 아닐 때

StrictMode를 꺼도 두 번 실행된다면 다음을 확인하세요.

1. 부모가 리렌더되면서 컴포넌트가 `key` 변경으로 다시 마운트되는지
2. 의존성 배열의 객체나 함수가 매 렌더마다 새로 만들어지는지
3. 같은 컴포넌트가 두 곳에서 렌더되는지

코드를 보여 주시면 어느 경우인지 바로 짚어 드릴게요. effect 코드와 `index.js`를 붙여 주세요.
