<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

React 18+ 개발 모드의 **StrictMode**가 컴포넌트를 의도적으로 mount → unmount → mount 시켜서 effect가 두 번 실행되는 겁니다. 정리(cleanup)가 빠졌거나 순수하지 않은 effect를 찾아내기 위한 동작이고, **프로덕션 빌드에서는 한 번만** 실행됩니다.

**해결 방법**
- 올바른 대응: effect에 cleanup 함수를 추가하세요.
  ```jsx
  useEffect(() => {
    const ctrl = new AbortController();
    fetch(url, { signal: ctrl.signal }).then(...);
    return () => ctrl.abort();
  }, [url]);
  ```
  구독/타이머/이벤트 리스너도 동일하게 해제 로직을 넣으면 두 번 실행돼도 문제가 없습니다.
- 데이터 fetching은 직접 useEffect로 하기보다 TanStack Query, SWR 같은 라이브러리를 쓰면 중복 요청이 알아서 처리됩니다.
- 임시로 확인만 하려면 `<React.StrictMode>`를 제거하면 한 번만 실행되지만, 버그를 숨기는 것이라 권장하지 않습니다.

`useRef`로 "이미 실행됨" 플래그를 두는 방식은 편법이라 피하는 게 좋습니다.

StrictMode를 안 쓰는데도 두 번 실행된다면 deps 배열에 매 렌더마다 바뀌는 객체/함수가 들어있거나, 부모가 리마운트되고 있는 건지 코드를 보여주시면 확인해드릴게요.
