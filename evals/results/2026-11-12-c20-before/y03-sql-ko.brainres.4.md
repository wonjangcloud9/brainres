<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

지난 30일 동안 주문을 3건 이상 한 고객(`user_id`)을 주문 수가 많은 순서로 보여주는 쿼리예요.

단계별로 보면 이렇습니다.

1. **`WHERE`**: `created_at`이 지금부터 30일 전 이후인 주문만 남겨요. 기간 조건이 집계 전에 적용돼요.
2. **`GROUP BY user_id`**: 남은 주문을 고객별로 묶어요.
3. **`COUNT(*) AS c`**: 각 고객의 주문 건수를 `c`라는 이름으로 세요.
4. **`HAVING COUNT(*) >= 3`**: 집계된 결과에서 3건 미만인 고객을 빼요. `WHERE`는 행을, `HAVING`은 그룹을 거른다는 점이 다릅니다.
5. **`ORDER BY c DESC`**: 주문이 많은 고객이 위에 오도록 정렬해요.

결과는 `user_id`와 `c` 두 컬럼이에요. 예를 들어 `(user_id=42, c=7)`은 42번 고객이 최근 30일 동안 7건을 주문했다는 뜻입니다.

참고할 점이 두 가지 있어요.
- `NOW() - INTERVAL '30 days'`는 PostgreSQL 문법이에요. MySQL이나 다른 DB에서는 다르게 써야 해요.
- 상한 조건이 없어서 미래 날짜의 `created_at`도 포함돼요. 정확히 "최근 30일"만 원하면 `AND created_at < NOW()`를 추가하세요.

이 결과로 헤비 구매 고객을 찾거나 재구매 캠페인 대상을 뽑을 때 쓸 수 있어요. 특정 고객의 주문 내역도 함께 보고 싶다면 `user_id`로 `orders`를 조인하는 쿼리를 만들어 드릴게요.
