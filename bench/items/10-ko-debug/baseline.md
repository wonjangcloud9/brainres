<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

가장 흔한 원인은 **React 18의 Strict Mode**입니다.

## 원인

개발 모드에서 `<React.StrictMode>`로 앱을 감싸면, React가 컴포넌트를 마운트한 뒤 **의도적으로 한 번 언마운트 → 재마운트**합니다. 그래서 `useEffect`가 다음 순서로 실행됩니다.

1. effect 실행
2. cleanup 실행
3. effect 다시 실행

이는 effect가 cleanup을 제대로 구현했는지, 재실행되어도 안전한지 검증하기 위한 동작입니다. **프로덕션 빌드에서는 한 번만 실행됩니다.**

```jsx
// main.jsx / index.jsx
<React.StrictMode>
  <App />
</React.StrictMode>
```

Next.js(App Router)는 기본적으로 Strict Mode가 켜져 있고, Vite/CRA 템플릿도 보통 포함되어 있습니다.

## 해결 방법

Strict Mode를 끄는 것은 권장하지 않고, **effect를 올바르게 작성**하는 게 정석입니다.

**1. cleanup 함수 작성**

```jsx
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id);
}, []);
```

**2. 데이터 fetch는 abort 처리**

```jsx
useEffect(() => {
  const controller = new AbortController();
  fetch('/api/data', { signal: controller.signal })
    .then(res => res.json())
    .then(setData)
    .catch(e => {
      if (e.name !== 'AbortError') console.error(e);
    });
  return () => controller.abort();
}, []);
```

**3. 이벤트 구독은 해제**

```jsx
useEffect(() => {
  window.addEventListener('resize', onResize);
  return () => window.removeEventListener('resize', onResize);
}, []);
```

**4. fetch는 라이브러리 사용 고려**: React Query, SWR 등은 중복 요청 처리를 알아서 해줍니다.

## 다른 가능한 원인

- **의존성 배열 값이 바뀌어서** 재실행되는 경우 (객체/배열/함수를 의존성에 넣으면 매 렌더마다 새로 만들어져 재실행됨)
- **부모가 리마운트**되는 경우 (`key`가 바뀌거나 조건부 렌더링 위치가 바뀜)
- **상태 변경으로 인한 리렌더**에서 의존성 배열이 없는 경우 (`useEffect(() => {...})`)

## 임시로 확인만 하고 싶다면

Strict Mode를 잠깐 꺼서 원인이 맞는지 확인할 수 있습니다.

```jsx
// StrictMode 제거
<App />
```

한 번만 실행된다면 Strict Mode가 원인입니다. 확인 후엔 다시 켜두고 effect를 고치세요.

코드를 보여주시면 어떤 경우인지 더 정확히 짚어드릴 수 있어요.
