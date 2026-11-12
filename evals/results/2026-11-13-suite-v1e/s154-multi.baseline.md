<!-- Q: useEffect가 뭐고, 언제 써야 하고, 자주 하는 실수는 뭐예요? -->

# useEffect란?

`useEffect`는 **렌더링 이후에 "부수 효과(side effect)"를 실행**하기 위한 React 훅입니다. 부수 효과란 렌더링 결과 계산과 직접 관련 없는, 컴포넌트 바깥 세계와의 상호작용을 말합니다. 예를 들면 서버 데이터 fetch, 구독/이벤트 리스너 등록, 타이머, DOM 직접 조작, 외부 라이브러리 연동 등이 있습니다.

```jsx
useEffect(() => {
  // 렌더링 후 실행될 코드
  return () => {
    // (선택) 정리(cleanup): 다음 effect 실행 전 / 언마운트 시 실행
  };
}, [의존성1, 의존성2]);
```

## 의존성 배열의 동작

| 형태 | 실행 시점 |
|---|---|
| `[]` | 마운트 시 1회 (개발 모드 StrictMode에서는 2회) |
| `[a, b]` | 마운트 시 + `a` 또는 `b`가 바뀔 때 |
| 생략 | 매 렌더링 후 |

## 언제 써야 하나?

**"React 바깥 시스템과 동기화"해야 할 때**가 핵심입니다.

```jsx
// 1. 이벤트 리스너 등록/해제
useEffect(() => {
  const onResize = () => setWidth(window.innerWidth);
  window.addEventListener('resize', onResize);
  return () => window.removeEventListener('resize', onResize);
}, []);

// 2. props/state 변경에 따른 데이터 fetch
useEffect(() => {
  const controller = new AbortController();
  fetch(`/api/users/${userId}`, { signal: controller.signal })
    .then(r => r.json())
    .then(setUser)
    .catch(e => { if (e.name !== 'AbortError') throw e; });
  return () => controller.abort();
}, [userId]);

// 3. 문서 제목 등 외부 상태 동기화
useEffect(() => {
  document.title = `${count}개 알림`;
}, [count]);
```

## 자주 하는 실수

### 1. 의존성 배열 누락 / 거짓말
effect 안에서 쓰는 반응형 값(props, state, 함수)은 모두 의존성에 넣어야 합니다. 빼면 **오래된 값(stale closure)**을 참조하게 됩니다. `eslint-plugin-react-hooks`의 `exhaustive-deps` 규칙을 켜 두고 경고를 무시하지 마세요.

### 2. 무한 루프
```jsx
// ❌ 렌더 → effect → setState → 렌더 → ...
useEffect(() => {
  setCount(count + 1);
});

// ❌ 매 렌더마다 새로 만들어지는 객체/배열을 의존성으로
const options = { page };          // 매번 새 참조
useEffect(() => { load(options); }, [options]);
// ✅ 원시값을 의존성으로: [page]
```

### 3. cleanup 누락
리스너, 타이머(`setInterval`), 구독을 정리하지 않으면 메모리 누수와 중복 실행이 생깁니다. fetch는 `AbortController`나 `ignore` 플래그로 **경쟁 상태(race condition)**를 막아야 합니다.

### 4. 불필요한 effect 사용 (가장 흔함)
렌더링 중에 계산할 수 있는 건 effect가 필요 없습니다.

```jsx
// ❌ 파생 상태를 effect로 동기화
const [fullName, setFullName] = useState('');
useEffect(() => {
  setFullName(first + ' ' + last);
}, [first, last]);

// ✅ 그냥 계산
const fullName = first + ' ' + last;
```

- 비싼 계산 → `useMemo`
- 사용자 이벤트(클릭, 제출)에 대한 반응 → **이벤트 핸들러**에서 처리 (effect X)
- props 변경 시 state 초기화 → `key` prop 사용

### 5. async 함수를 바로 전달
```jsx
// ❌ effect 콜백은 cleanup 함수 또는 undefined만 반환해야 함
useEffect(async () => { ... }, []);

// ✅ 내부에서 정의 후 호출
useEffect(() => {
  async function load() { ... }
  load();
}, []);
```

### 6. StrictMode의 이중 실행에 당황
개발 모드에서 effect가 마운트→언마운트→마운트로 두 번 실행되는 건 **cleanup이 제대로 작성됐는지 검증**하는 의도된 동작입니다. 이를 피하려고 `useRef` 플래그로 막기보다 cleanup을 올바르게 작성하세요.

## 한 줄 기준

> "이 코드는 **어떤 상호작용 때문에** 실행되는가?"
> - 사용자 행동 때문 → 이벤트 핸들러
> - 화면에 **표시되었기 때문**에 외부와 동기화해야 함 → `useEffect`

데이터 fetch는 실무에서는 직접 effect로 짜기보다 TanStack Query, SWR 같은 라이브러리나 프레임워크의 데이터 로딩 기능을 쓰는 것이 경쟁 상태·캐싱 문제를 훨씬 덜 겪습니다.
