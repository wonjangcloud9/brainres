<!-- Q: 리액트에서 useEffect가 두 번 실행돼. 왜 그래? -->

React 18 이상에서 개발 모드(`npm run dev`)이고 `<React.StrictMode>`로 감싸져 있으면, React가 일부러 effect를 두 번 실행해요. 프로덕션 빌드에서는 한 번만 실행돼요(~95% 확신).

**왜 이렇게 하나요?**
React가 마운트 → 언마운트 → 다시 마운트를 흉내 내서, cleanup이 빠진 effect를 미리 찾아내려는 거예요. 나중에 Offscreen 같은 기능으로 컴포넌트가 실제로 재마운트될 수 있어서, 그때 버그가 나지 않게 하는 검사예요.

**확인 방법**
`main.jsx`(또는 `index.js`)에 `<React.StrictMode>`가 있는지 보세요. 있다면 그게 원인이에요.

**올바른 해결: cleanup을 작성하세요**

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/data', { signal: controller.signal })
    .then(res => res.json())
    .then(setData)
    .catch(err => {
      if (err.name !== 'AbortError') console.error(err);
    });

  return () => controller.abort(); // 첫 번째 실행을 정리
}, []);
```

구독이나 타이머도 같아요. `addEventListener`는 `removeEventListener`로, `setInterval`은 `clearInterval`로 정리하면 두 번 실행해도 문제가 없어요.

**피해야 할 방법**
StrictMode를 지우면 로그는 한 번만 찍히지만, 숨어 있던 버그도 같이 가려져요. `useRef` 플래그로 두 번째 실행을 막는 방식도 같은 이유로 권하지 않아요.

StrictMode가 없는데도 두 번 실행된다면 `useEffect`의 의존성 배열 값이 바뀌는지, 부모가 컴포넌트를 다시 마운트하는지(`key` 변경 등)를 확인해야 해요. 해당 컴포넌트 코드를 보여주시면 같이 볼게요.
