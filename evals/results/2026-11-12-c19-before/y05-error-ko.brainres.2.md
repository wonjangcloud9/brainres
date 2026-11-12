<!-- Q: 이거 왜 나?

```
TypeError: Cannot read properties of undefined (reading 'map')
    at UserList (UserList.jsx:12:18)
``` -->

`UserList` 안에서 `.map()`을 호출한 값이 `undefined`여서 납니다. 배열이어야 하는데 값이 없는 상태예요.

보통 원인은 세 가지입니다.

1. **데이터가 아직 안 왔어요.** API 응답 전에 첫 렌더링이 일어나면 `users`가 `undefined`입니다.
2. **props 이름이 틀렸어요.** 부모가 `items`로 넘기는데 `UserList`는 `users`를 기다리는 식입니다.
3. **응답 구조가 달라요.** `data.users`를 기대했는데 실제로는 `data`가 배열이거나 그 반대입니다.

12번째 줄에서 `.map`이 붙은 변수를 확인해 보세요. 임시로 막으려면 기본값을 주면 됩니다.

```jsx
const list = users ?? [];
return list.map(...)
```

다만 기본값은 증상만 가리니, 값이 왜 없는지 먼저 확인하는 편이 좋아요.

`UserList.jsx`와 이 컴포넌트를 쓰는 부모 코드를 보여주시면 어느 경우인지 바로 짚어 드릴게요.
