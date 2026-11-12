<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

개발 모드의 `<React.StrictMode>` 때문일 가능성이 가장 커요. React 18부터 StrictMode는 개발 중에 컴포넌트를 마운트, 언마운트, 다시 마운트해요. 그래서 이펙트가 한 번 더 실행돼요.

**왜 일부러 그러나요?**
이펙트에 정리(cleanup) 코드가 빠졌는지 찾아내려는 거예요. 구독 해제나 요청 취소를 빼먹으면 두 번 실행될 때 버그가 바로 드러나요. 프로덕션 빌드에서는 한 번만 실행돼요.

**해결: 이펙트를 두 번 돌려도 안전하게 만들어요**

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/data', { signal: controller.signal })
    .then(res => res.json())
    .then(setData)
    .catch(e => {
      if (e.name !== 'AbortError') throw e;
    });

  return () => controller.abort(); // cleanup
}, []);
```

이렇게 하면 첫 번째 요청은 취소되고, 두 번째 요청만 결과를 반영해요.

**피할 것**
- `StrictMode`를 지우거나 `useRef` 플래그로 두 번째 실행을 막지 마세요. 증상만 가리고, 실제 버그(경쟁 상태, 중복 구독)는 그대로 남아요.

**StrictMode가 아닌 다른 원인**
프로덕션에서도 두 번 실행된다면 아래를 확인해 보세요.
1. 의존성 배열의 객체나 함수가 렌더마다 새로 만들어져서 매번 바뀌는 경우
2. 부모가 `key` 변경이나 조건부 렌더링으로 컴포넌트를 다시 마운트하는 경우
3. 같은 컴포넌트가 화면에 두 번 렌더되는 경우

다음 단계로, `index.js`(또는 `main.jsx`)에 `<React.StrictMode>`가 있는지 확인해 보세요. 있고 개발 모드에서만 두 번 실행된다면 정상 동작이에요. 이펙트 코드를 붙여 주시면 cleanup이 필요한지 봐 드릴게요.
