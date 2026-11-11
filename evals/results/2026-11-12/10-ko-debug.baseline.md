<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

거의 확실하게 **React Strict Mode** 때문입니다.

## 원인

React 18부터 개발 모드에서 `<React.StrictMode>`로 앱을 감싸면, 컴포넌트가 마운트될 때 **effect를 일부러 두 번 실행**합니다 (mount → unmount(cleanup) → mount). 이는 cleanup이 빠졌거나 effect가 순수하지 않은 버그를 조기에 발견하기 위한 의도된 동작입니다.

- **개발 모드에서만** 발생합니다. 프로덕션 빌드에서는 한 번만 실행됩니다.
- Next.js는 `reactStrictMode`가 기본으로 켜져 있고, Vite/CRA 템플릿도 `main.jsx`에 `<StrictMode>`가 들어 있습니다.

## 해결 방법

Strict Mode를 끄는 것보다, **effect를 두 번 실행해도 안전하게 만드는 것**이 올바른 방법입니다.

**1. cleanup 함수 추가**
```jsx
useEffect(() => {
  const ws = new WebSocket(url);
  return () => ws.close(); // 정리
}, [url]);
```

**2. 데이터 fetch는 취소 처리**
```jsx
useEffect(() => {
  const controller = new AbortController();
  fetch('/api/data', { signal: controller.signal })
    .then(res => res.json())
    .then(setData)
    .catch(e => { if (e.name !== 'AbortError') console.error(e); });
  return () => controller.abort();
}, []);
```

**3. 가능하면 직접 fetch 대신 라이브러리 사용**
TanStack Query, SWR 등은 중복 요청과 캐싱을 알아서 처리해줍니다.

## 임시로 확인만 하고 싶다면

`<StrictMode>`를 제거하면 한 번만 실행되는 걸 확인할 수 있습니다. 다만 근본 해결은 아니니 확인용으로만 쓰세요.

## Strict Mode 외의 가능성

만약 **프로덕션에서도** 두 번 실행된다면 다른 원인입니다:
- 의존성 배열의 값이 바뀌어서 재실행되는 경우 (객체/함수가 매 렌더마다 새로 생성되는 경우 등)
- 부모 컴포넌트가 리마운트되는 경우 (`key` 변경, 조건부 렌더링 등)
- 같은 컴포넌트가 두 곳에 렌더링된 경우

코드를 보여주시면 어떤 경우인지 더 정확히 짚어드릴 수 있습니다.
