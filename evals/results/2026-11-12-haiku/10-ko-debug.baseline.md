<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

React에서 `useEffect`가 두 번 실행되는 건 대부분 **Strict Mode** 때문이고, 버그가 아니라 의도된 동작입니다.

## 원인

`React.StrictMode`(개발 모드에서만 동작)는 컴포넌트를 마운트 → 언마운트 → 다시 마운트하는 과정을 한 번 더 시뮬레이션합니다. 그래서 effect가 다음 순서로 실행됩니다.

1. effect 실행
2. cleanup 실행
3. effect 다시 실행

보통 `index.js`나 `main.jsx`에 이런 코드가 있을 때 발생합니다.

```jsx
<React.StrictMode>
  <App />
</React.StrictMode>
```

## 왜 이렇게 하냐면

effect의 cleanup이 제대로 작성되었는지 검증하기 위해서입니다. 나중에 React가 컴포넌트를 재사용하거나 대기 상태(Offscreen 등)로 보내는 경우에도 같은 상황이 생기기 때문에, 미리 잡아내도록 만든 것입니다.

## 해결 방법

**1. effect가 올바르게 정리되도록 cleanup을 작성하세요 (권장)**

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/data', { signal: controller.signal })
    .then(res => res.json())
    .then(setData)
    .catch(err => {
      if (err.name !== 'AbortError') console.error(err);
    });

  return () => controller.abort(); // 두 번째 실행 전에 이전 요청 취소
}, []);
```

구독, 타이머, 이벤트 리스너도 마찬가지로 cleanup에서 해제하면 됩니다.

**2. 개발 중에만 두 번 실행되는 게 불편하다면**

Strict Mode를 제거하는 방법이 있지만, 근본 해결은 아닙니다. 가능하면 1번처럼 cleanup을 맞추는 쪽을 추천합니다.

**3. 데이터 fetching은 라이브러리 사용**

TanStack Query, SWR 같은 라이브러리는 중복 요청과 경쟁 상태를 알아서 처리해 줍니다.

## 참고

- 이 현상은 **개발 모드에서만** 나타나고, 프로덕션 빌드에서는 한 번만 실행됩니다.
- 두 번 실행되는 것 자체가 문제인지 확인하려면, 코드에 cleanup이 있는지, 같은 작업(요청, 리스너 등록 등)이 중복되어도 결과가 깨지지 않는지 보세요.

혹시 어떤 effect에서 문제가 생기는지 코드를 보여주시면 더 구체적으로 봐드릴게요.
