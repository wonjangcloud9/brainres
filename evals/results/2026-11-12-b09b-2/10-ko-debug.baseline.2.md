<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

가장 흔한 원인은 **React 18의 Strict Mode**입니다.

## 원인

`index.js`(또는 `main.jsx`)에 이렇게 감싸져 있을 겁니다:

```jsx
<React.StrictMode>
  <App />
</React.StrictMode>
```

**개발 모드에서만** Strict Mode가 컴포넌트를 마운트 → 언마운트 → 다시 마운트하며 effect를 의도적으로 두 번 실행합니다. 이는 cleanup 함수가 제대로 작성됐는지, effect가 멱등(idempotent)한지 검증하기 위한 것입니다. **프로덕션 빌드에서는 한 번만 실행됩니다.**

## 해결 방법

버그가 아니라 검증 동작이므로, 끄기보다 effect를 올바르게 작성하는 게 맞습니다.

**1. cleanup 함수 추가**

```jsx
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id);   // 정리
}, []);
```

**2. fetch는 abort 처리**

```jsx
useEffect(() => {
  const controller = new AbortController();
  fetch(url, { signal: controller.signal })
    .then(res => res.json())
    .then(setData)
    .catch(e => { if (e.name !== 'AbortError') console.error(e); });
  return () => controller.abort();
}, [url]);
```

**3. 또는 `ignore` 플래그 패턴**

```jsx
useEffect(() => {
  let ignore = false;
  fetchData().then(d => { if (!ignore) setData(d); });
  return () => { ignore = true; };
}, []);
```

## 다른 가능한 원인

- **의존성 배열 문제**: 의존성에 매 렌더마다 새로 만들어지는 객체/함수/배열이 있으면 계속 재실행됩니다. `useMemo`/`useCallback`을 쓰거나 원시값만 의존성에 넣으세요.
- **부모의 리렌더/리마운트**: `key`가 바뀌거나 조건부 렌더링으로 컴포넌트가 다시 마운트되는 경우.
- **상태 업데이트 연쇄**: effect 안에서 setState → 의존성 변경 → effect 재실행.

## 임시 확인용 (권장하지 않음)

`<React.StrictMode>`를 제거하면 한 번만 실행되지만, 문제를 숨길 뿐입니다.

코드를 보여주시면 어떤 경우인지 정확히 짚어드릴게요.
