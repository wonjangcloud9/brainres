<!-- Q: 이거 왜 나?

```
TypeError: Cannot read properties of undefined (reading 'map')
    at UserList (UserList.jsx:12:18)
``` -->

`UserList.jsx`의 12번째 줄에서 `.map()`을 호출한 값이 `undefined`여서 발생한 오류입니다. 배열이어야 할 변수가 아직 값이 없는 상태입니다.

보통 다음 세 가지 중 하나입니다.

1. **초기값이 없음**: `useState()`를 빈 값으로 두면 첫 렌더링 때 `undefined`입니다. `useState([])`로 바꾸세요.
2. **props를 안 넘김**: 부모 컴포넌트가 `<UserList users={...} />`를 빠뜨리거나 다른 이름으로 넘깁니다.
3. **응답 구조가 다름**: API가 `res.data.users`를 주는데 코드는 `res.users`를 읽습니다. 콘솔에 응답을 찍어 확인하세요.

임시 방어는 다음처럼 쓸 수 있습니다.

```jsx
const list = users ?? [];
return list.map(...)
```

원인을 확실히 찾으려면 `UserList.jsx` 1~15줄과 `UserList`를 쓰는 부모 코드를 보여주세요. 그러면 `users`가 어디서 undefined가 되는지 바로 짚어 드릴게요.
