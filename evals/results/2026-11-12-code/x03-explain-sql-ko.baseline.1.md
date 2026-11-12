<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

최근 30일 동안 주문을 3건 이상 한 사용자를 찾아서, 주문 횟수가 많은 순으로 보여주는 쿼리예요.

단계별로 보면:

1. **`FROM orders WHERE created_at >= NOW() - INTERVAL '30 days'`**: 현재 시각 기준 30일 이내에 생성된 주문만 대상으로 해요.
2. **`GROUP BY user_id`**: 사용자별로 주문을 묶어요.
3. **`COUNT(*) AS c`**: 사용자별 주문 건수를 계산해요.
4. **`HAVING COUNT(*) >= 3`**: 묶은 뒤 주문 건수가 3건 이상인 사용자만 남겨요. (집계 결과에 대한 조건이라 `WHERE`가 아니라 `HAVING`을 써요.)
5. **`ORDER BY c DESC`**: 주문 건수가 많은 사용자부터 정렬해요.

결과는 `user_id`와 `c`(최근 30일 주문 수) 두 컬럼이에요. 보통 단골 고객, 재구매율 분석, 이상 주문 패턴 탐지 같은 용도로 쓰여요.

참고로 `INTERVAL '30 days'` 문법은 PostgreSQL 스타일이에요. MySQL에서는 `INTERVAL 30 DAY`로 써야 해요.
