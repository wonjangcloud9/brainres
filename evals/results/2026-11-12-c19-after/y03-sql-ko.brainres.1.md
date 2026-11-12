<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

지난 30일 동안 주문을 3건 이상 한 사용자를 주문 수가 많은 순으로 보여주는 쿼리예요.

동작은 네 단계로 나뉩니다.

1. **기간 필터**: `created_at`이 지금부터 30일 전 이후인 주문만 남겨요.
2. **집계**: `user_id`별로 묶어서 주문 건수를 `c`라는 이름으로 셉니다.
3. **조건 필터**: `HAVING COUNT(*) >= 3`으로 주문이 3건 미만인 사용자를 뺍니다. `WHERE`는 행을 거르고 `HAVING`은 집계 결과를 거른다는 점이 핵심이에요.
4. **정렬**: 주문이 많은 사용자가 위로 오도록 `c` 내림차순으로 정렬해요.

결과에는 `user_id`와 `c`(30일간 주문 수) 두 열이 나옵니다. 재구매가 �잦은 고객을 찾거나 활발한 사용자 목록을 뽑을 때 쓰는 패턴이에요.

참고로 `NOW() - INTERVAL '30 days'`는 PostgreSQL 문법입니다. MySQL이라면 `NOW() - INTERVAL 30 DAY`로 바꿔야 해요.
