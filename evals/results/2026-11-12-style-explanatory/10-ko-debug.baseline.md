<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

**원인은 거의 확실히 React 18+ 의 Strict Mode입니다.**

`index.js`나 `main.jsx`(또는 Next.js의 기본 설정)에 이런 코드가 있을 거예요.

```jsx
<React.StrictMode>
  <App />
</React.StrictMode>
```

**개발 모드에서만** Strict Mode가 컴포넌트를 마운트한 뒤 이펙트를 `실행 → 정리(cleanup) → 다시 실행`합니다. 프로덕션 빌드에서는 한 번만 실행됩니다.

`★ Insight ─────────────────────────────────────`
- 이중 실행은 버그가 아니라 **의도된 검증 장치**입니다. 이펙트에 cleanup이 빠졌거나 순수하지 않은 코드가 있으면 바로 드러나게 하려는 거예요.
- React는 앞으로 "화면이 사라졌다가 다시 나타나는" 기능(Offscreen, Activity 등)을 지원하려 합니다. 그래서 이펙트가 언제든 mount/unmount를 반복해도 안전해야 합니다.
`─────────────────────────────────────────────────`

## 어떻게 대응할까?

**1. cleanup을 제대로 작성하기 (정석)**

```jsx
useEffect(() => {
  const conn = createConnection();
  conn.connect();
  return () => conn.disconnect(); // 두 번째 실행 전에 정리됨
}, []);
```

**2. fetch는 취소 처리하기**

```jsx
useEffect(() => {
  const controller = new AbortController();
  fetch('/api/data', { signal: controller.signal })
    .then(r => r.json())
    .then(setData)
    .catch(e => { if (e.name !== 'AbortError') throw e; });
  return () => controller.abort();
}, []);
```

**3. 데이터 패칭은 직접 `useEffect`로 하지 않기**

TanStack Query, SWR 같은 라이브러리나 프레임워크의 데이터 로딩 기능을 쓰면 중복 요청, 경쟁 상태, 캐싱을 대신 처리해 줍니다.

**4. 한 번만 실행돼야 하는 코드(예: 분석 이벤트 전송)**

앱 초기화처럼 정말 한 번만 필요한 것은 컴포넌트 밖 모듈 레벨로 빼는 걸 권장합니다.

```jsx
let didInit = false;
function App() {
  useEffect(() => {
    if (!didInit) {
      didInit = true;
      // 초기화 로직
    }
  }, []);
}
```

## 하지 말아야 할 것

`StrictMode`를 제거하면 증상은 사라지지만, 문제를 숨길 뿐이에요. 실제 사용자 환경에서 빠른 페이지 전환이나 재마운트 때 같은 버그가 다시 나타날 수 있습니다.

`★ Insight ─────────────────────────────────────`
- 판단 기준: "이펙트를 두 번 돌려도 결과가 같은가?" 그렇다면 올바르게 작성된 거예요.
- 이중 실행이 거슬린다면 cleanup이 필요한 부분을 놓쳤다는 신호로 받아들이면 됩니다.
`─────────────────────────────────────────────────`

혹시 `StrictMode`가 아닌 것 같다면 코드를 보여주세요. 부모 컴포넌트의 리렌더링, `key` 변경, 의존성 배열의 객체/함수 참조 같은 다른 원인도 확인해 볼 수 있습니다.
