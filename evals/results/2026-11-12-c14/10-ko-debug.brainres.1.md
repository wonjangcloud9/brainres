<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

개발 모드의 `<StrictMode>` 때문일 가능성이 가장 커요. React 18 이상은 개발 중에 컴포넌트를 마운트, 언마운트, 다시 마운트해서 cleanup이 빠진 effect를 찾아내요. 그래서 effect가 두 번 돌아요. 프로덕션 빌드에서는 한 번만 실행돼요.

**확인 방법**

`index.js`나 `main.jsx`에 `<React.StrictMode>`가 있는지 보세요. Next.js는 `reactStrictMode`가 기본으로 켜져 있어요.

**해결: effect를 두 번 돌아도 안전하게 만들기**

StrictMode를 끄는 건 권하지 않아요. 문제를 숨길 뿐이에요. 대신 cleanup을 작성하세요.

```jsx
useEffect(() => {
  const ws = new WebSocket(url);
  ws.onmessage = handle;

  return () => ws.close(); // 언마운트 때 정리
}, [url]);
```

데이터 요청이라면 중복 응답을 무시하게 만들어요.

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch(`/api/user/${id}`, { signal: controller.signal })
    .then(r => r.json())
    .then(setUser)
    .catch(e => {
      if (e.name !== "AbortError") throw e;
    });

  return () => controller.abort();
}, [id]);
```

**StrictMode가 아닌 다른 원인**

| 원인 | 확인 방법 |
|---|---|
| 의존성 배열의 객체나 함수가 매 렌더마다 새로 만들어짐 | 배열 안의 값을 `console.log`로 비교해요 |
| 부모가 `key`를 바꾸거나 컴포넌트를 조건부로 다시 마운트함 | effect 안에서 `console.log("mount")`를 찍어요 |

두 번 실행이 개발 모드에서만 보이고 프로덕션에서는 한 번이라면 StrictMode예요. 코드를 붙여주시면 어느 쪽인지 같이 확인할게요.
