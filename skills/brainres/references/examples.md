# Before / after

Scores come from `scripts/brainlint.py`. Full files live in the repo's `examples/` folder.

## 1. Debugging question: "My React component keeps re-rendering forever. Why?"

**Before (56/100, 272 words).** It opens with "Great question!", then a "Let me break down" preamble. Headings like "Understanding the Problem" carry no content. A 7-item list of bold lead-ins leaves the reader to guess which cause applies. It closes with "I hope this helps!".

**After (100/100, 134 words):**

> Your `useEffect` is almost certainly updating a value it also depends on, so every render schedules the next one.
>
> The loop:
> 1. Render → effect runs → `setItems(...)`
> 2. `items` changed → React re-renders
> 3. `items` is in the dependency array → effect runs again → back to 1
>
> Fix it by depending on the input, not the output: *(code block with `[query]` instead of `[items]`)*
>
> To confirm, add `console.count("render")`. A count that climbs while you touch nothing means the loop is real.
>
> If neither pattern matches, paste the component and I'll point to the exact line.

What changed and why:

- The answer is in sentence 1, with calibrated confidence ("almost certainly"). (#28, #84)
- The mechanism is a 3-step causal chain instead of a list of causes. (#35, #86)
- There is one worked fix, plus a way to verify it. (#10, #85)
- It ends on a concrete next action. (#76)

## 2. Decision question in Korean: "Redis랑 메모리 캐시 중 뭐 써야 해? 서버는 한 대야."

**Before (39/100):**

- It opens with "좋은 질문입니다!".
- Translationese like "~에 대한 이해를 통해" makes it hard to read.
- Six advantages of Redis compete with three of memory caching, so the user still has to decide.
- It ends with "상황에 따라 적절한 선택을…".

**After (100/100):**

> 서버가 한 대면 **메모리 캐시**로 시작하세요. Redis는 서버를 늘릴 때 붙이면 됩니다.
> … (2 reasons, then 3 triggers for switching to Redis)
> 지금 할 일: 캐시 접근을 `getCache()`/`setCache()` 함수 하나로 감싸 두세요.

What changed and why:

- It gives one recommendation and says when to deviate from it. (#78)
- Groups stay at 4 items or fewer. (#1)
- It uses the user's own situation ("서버 한 대"). (#49)
- It ends on an action. (#76)
