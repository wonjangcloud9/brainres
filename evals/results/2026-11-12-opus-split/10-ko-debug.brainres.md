<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

개발 모드의 **StrictMode** 때문이에요. 버그가 아니고, 프로덕션 빌드에서는 한 번만 실행돼요.

## 왜 두 번 실행되나요

React 18부터 StrictMode는 개발 모드에서 컴포넌트를 일부러 다시 마운트해요. 실행 순서는 이래요.

1. 마운트 → effect 실행
2. 언마운트 → cleanup 실행
3. 다시 마운트 → effect 재실행

목적은 cleanup이 빠진 effect를 일찍 찾아내는 거예요. `main.jsx`나 `index.js`에서 `<React.StrictMode>`로 감쌌는지 확인해 보세요.

## 해결: StrictMode를 끄지 말고 cleanup을 쓰세요

두 번 실행돼도 결과가 같으면 올바른 effect예요. 데이터 요청은 이렇게 써요.

```jsx
useEffect(() => {
  let ignore = false;

  fetch(`/api/users/${id}`)
    .then(res => res.json())
    .then(data => {
      if (!ignore) setUser(data);
    });

  return () => {
    ignore = true; // 첫 번째 요청 결과는 버려요
  };
}, [id]);
```

다른 경우도 같은 원칙이에요.

- 이벤트 리스너: cleanup에서 `removeEventListener`를 호출해요.
- 타이머: cleanup에서 `clearInterval`을 호출해요.
- 웹소켓: cleanup에서 연결을 닫아요.

## 프로덕션에서도 두 번 실행된다면

StrictMode와는 다른 원인이에요. 주로 이 세 가지를 확인하세요.

- 의존성 배열의 객체나 함수가 렌더마다 새로 만들어져요.
- 부모의 `key`가 바뀌어서 컴포넌트가 다시 마운트돼요.
- 같은 컴포넌트가 화면에 두 번 렌더링돼요.

프로덕션에서도 두 번 실행되면 해당 컴포넌트 코드를 보여 주세요.
