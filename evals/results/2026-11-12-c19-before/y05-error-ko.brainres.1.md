<!-- Q: 이거 왜 나?

```
TypeError: Cannot read properties of undefined (reading 'map')
    at UserList (UserList.jsx:12:18)
``` -->

`UserList`가 렌더링될 때 `.map`을 호출하는 값이 `undefined`이기 때문입니다. 보통 `UserList.jsx` 12줄 근처에서 `users.map(...)`이나 `props.items.map(...)` 같은 코드가 있고, 그 변수가 아직 준비되지 않았습니다.

흔한 원인은 세 가지입니다.

1. **비동기 데이터가 아직 도착하지 않음.** `useEffect`에서 fetch한 값을 초기값 없이 `useState()`로 두면 첫 렌더링에서 `undefined`입니다.
2. **부모가 prop을 전달하지 않음.** `<UserList />`처럼 `users` 없이 쓰면 `props.users`가 `undefined`입니다.
3. **API 응답 구조가 다름.** 예를 들어 응답이 `[...]`인데 코드는 `res.data.users`를 기대하면 `undefined`가 됩니다.

가장 빠른 방어는 기본값을 주는 것입니다.

```jsx
// 1) 기본값 지정
function UserList({ users = [] }) {
  return users.map(u => <li key={u.id}>{u.name}</li>);
}

// 2) 또는 가드
{users?.map(u => <li key={u.id}>{u.name}</li>)}
```

이 방법은 증상만 막습니다. 근본 원인을 찾으려면 `users`를 쓰는 곳에 `console.log(users)`를 넣고, 값이 언제 `undefined`인지 확인하세요.

12번 줄 코드와 `UserList`를 부르는 부모 컴포넌트를 보여주시면 어느 원인인지 바로 짚어 드리겠습니다.
