<!-- Q: 이거 왜 나?

```
TypeError: Cannot read properties of undefined (reading 'map')
    at UserList (UserList.jsx:12:18)
``` -->

`users`처럼 배열이어야 할 값이 `undefined` 상태에서 `.map()`을 호출해서 생긴 에러입니다. `UserList.jsx` 12번째 줄에서 이 값을 쓰고 있어요.

보통 원인은 다음 중 하나입니다.

- **초기값 누락**: `useState()`처럼 초기값 없이 선언했고, 데이터가 오기 전에 렌더링됩니다.
- **비동기 로딩 전 렌더링**: `fetch`나 API 응답이 도착하기 전에 `.map()`이 실행됩니다.
- **props 이름 불일치**: 부모가 `users` 대신 `userList` 같은 다른 이름으로 넘깁니다.
- **응답 구조 차이**: API가 배열을 `data.users`처럼 한 단계 안에 감싸서 보내는데, 그대로 배열로 취급합니다.

가장 빠른 방어는 기본값을 주는 것입니다.

```jsx
// props로 받는 경우
function UserList({ users = [] }) {
  return users.map(u => <li key={u.id}>{u.name}</li>);
}

// optional chaining으로 막는 경우
{users?.map(u => <li key={u.id}>{u.name}</li>)}
```

다만 기본값으로 막으면 데이터가 실제로 안 오는 문제가 가려질 수 있습니다. 근본 원인은 값이 어디서 undefined가 되는지 확인해야 찾습니다.

`UserList.jsx` 1~15줄과 이 컴포넌트를 쓰는 부모 코드를 붙여 주세요. 그러면 어떤 원인인지 정확히 짚어 드릴 수 있어요.
