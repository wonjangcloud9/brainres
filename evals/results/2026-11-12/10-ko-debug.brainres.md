<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

개발 모드에서 `<StrictMode>`가 켜져 있기 때문입니다. React 18 이상은 StrictMode 안에서 컴포넌트를 마운트한 뒤 곧바로 언마운트하고 다시 마운트해서, effect가 "마운트 → cleanup → 마운트" 순서로 두 번 실행됩니다. 프로덕션 빌드에서는 한 번만 실행됩니다.

**왜 이러는가:** cleanup이 없거나 잘못된 effect(구독 해제 누락, 요청 취소 누락 등)를 개발 중에 바로 드러내려는 의도적인 검사입니다. 버그가 아니라 기능입니다.

**확인 방법:** `main.jsx`(또는 `index.js`)에서 `<React.StrictMode>`를 잠시 지우면 한 번만 실행됩니다. 단, 이건 확인용이고 영구 해결책으로 쓰지 마세요.

**올바른 대응:** effect가 두 번 돌아도 문제없게 cleanup을 작성합니다.

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/data', { signal: controller.signal })
    .then(res => res.json())
    .then(setData)
    .catch(err => {
      if (err.name !== 'AbortError') console.error(err);
    });

  return () => controller.abort(); // 첫 번째 실행을 취소
}, []);
```

이렇게 하면 첫 요청은 취소되고 두 번째 요청만 살아남습니다. 이벤트 리스너나 타이머도 같은 원리로 `return` 안에서 해제하세요.

**StrictMode가 원인이 아닐 수도 있는 경우(~20%):** StrictMode를 껐는데도 두 번 실행되면 의존성 배열의 객체나 함수가 매 렌더마다 새로 만들어지거나, 부모가 리마운트(`key` 변경, 조건부 렌더링)되고 있을 가능성이 큽니다.

다음 단계: 해당 effect 코드와 의존성 배열을 보여주시면 어느 쪽인지 바로 짚어드리겠습니다.
