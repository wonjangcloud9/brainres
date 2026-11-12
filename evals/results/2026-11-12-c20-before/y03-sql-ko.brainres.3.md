<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자**를 주문 수가 많은 순서로 보여줘요.

단계별로 보면 이렇습니다.

1. **`WHERE`**: 현재 시각에서 30일 전 이후에 생성된 주문만 남겨요.
2. **`GROUP BY user_id`**: 남은 주문을 사용자별로 묶어요.
3. **`COUNT(*) AS c`**: 각 사용자의 주문 건수를 세고, 그 값을 `c`라는 이름으로 불러요.
4. **`HAVING COUNT(*) >= 3`**: 집계 후에 주문이 3건 미만인 사용자를 제외해요.
5. **`ORDER BY c DESC`**: 주문 수가 많은 사용자부터 내림차순으로 정렬해요.

`WHERE`와 `HAVING`은 필터링하는 시점이 달라요. `WHERE`는 묶기 전 개별 행을, `HAVING`은 묶은 뒤 그룹을 걸러요. 그래서 건수 조건은 `HAVING`에 써야 해요.

`INTERVAL '30 days'` 문법을 보면 PostgreSQL이나 호환 DB일 가능성이 커요. 다른 DB를 쓰신다면 날짜 계산 문법을 바꿔야 할 수 있어요.

원하시는 게 "최근 30일 기준 헤비 구매자 추출"이라면 이 쿼리가 그대로 맞아요. 사용자 이름이나 주문 금액도 함께 보고 싶으시면 `users` 테이블과 조인하는 쿼리로 바꿔 드릴게요.
