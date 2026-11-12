<!-- Q: useEffect가 뭐고, 언제 써야 하고, 자주 하는 실수는 뭐예요? -->

`useEffect`는 렌더링이 끝난 뒤에 "부수 효과"(React 바깥 세계와의 동기화)를 실행하는 React Hook이에요.

## 기본 형태

```jsx
useEffect(() => {
  // 렌더 후 실행할 코드
  return () => {
    // 정리(cleanup): 다음 effect 실행 전, 언마운트 시 호출
  };
}, [dep1, dep2]); // 의존성 배열
```

의존성 배열의 동작은 이래요.

| 배열 | 실행 시점 |
|---|---|
| 생략 | 매 렌더 후 |
| `[]` | 마운트 후 한 번 |
| `[a, b]` | 마운트 후, 그리고 `a`나 `b`가 바뀔 때 |

## 언제 쓰나요

React 바깥 시스템과 동기화할 때만 써요.

- 서버 데이터 가져오기 (fetch)
- 이벤트 리스너 등록 (`window.addEventListener`)
- 타이머, WebSocket, 구독
- 브라우저 API 조작 (`document.title`, 포커스)

```jsx
useEffect(() => {
  const onResize = () => setWidth(window.innerWidth);
  window.addEventListener("resize", onResize);
  return () => window.removeEventListener("resize", onResize);
}, []);
```

## 자주 하는 실수

**1. 계산으로 끝날 일에 쓰기**
state에서 파생되는 값은 렌더 중에 계산하면 돼요. effect에서 `setState`하면 렌더가 한 번 더 일어나요.

```jsx
// 나쁨
useEffect(() => setFullName(first + " " + last), [first, last]);
// 좋음
const fullName = first + " " + last;
```

**2. 클릭 같은 사용자 동작을 effect로 처리하기**
"버튼을 눌러서 생긴 일"은 이벤트 핸들러에 넣으세요.

**3. 의존성 배열 거짓말**
effect 안에서 쓰는 값을 배열에서 빼면 오래된 값(stale closure)을 읽어요. 린트 규칙 `react-hooks/exhaustive-deps`를 켜 두고 경고를 따르세요.

**4. cleanup 누락**
리스너, 타이머, 구독을 정리하지 않으면 메모리 누수와 중복 실행이 생겨요.

**5. fetch의 경쟁 상태(race condition)**
요청이 순서 없이 도착하면 옛 응답이 최신 상태를 덮어써요.

```jsx
useEffect(() => {
  const ctrl = new AbortController();
  fetch(`/api/user/${id}`, { signal: ctrl.signal })
    .then(r => r.json())
    .then(setUser)
    .catch(e => { if (e.name !== "AbortError") throw e; });
  return () => ctrl.abort();
}, [id]);
```

**6. 무한 루프**
effect 안에서 바꾸는 state나, 매 렌더 새로 만들어지는 객체·함수를 의존성에 넣으면 계속 재실행돼요. 객체는 effect 안으로 옮기거나 `useMemo`/`useCallback`을 쓰세요.

**7. 개발 모드에서 두 번 실행된다고 당황하기**
`<StrictMode>`는 개발 중 effect를 일부러 마운트→언마운트→마운트로 실행해요. cleanup이 제대로 짝을 이루는지 확인하려는 것이고, 프로덕션에서는 한 번만 실행돼요.

## 팁

데이터 fetch는 직접 쓰기보다 TanStack Query나 SWR 같은 라이브러리가 캐싱과 경쟁 상태를 대신 처리해 줘요.

다음 단계로, 지금 쓰는 `useEffect` 코드가 있으면 붙여 주세요. 위 실수에 해당하는지 같이 봐 드릴게요.
