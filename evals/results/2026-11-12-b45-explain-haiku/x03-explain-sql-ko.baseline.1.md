<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자**를 찾아서, 주문 수가 많은 순서대로 보여주는 쿼리입니다.

단계별로 보면:

1. `WHERE created_at >= NOW() - INTERVAL '30 days'`
   - 현재 시각 기준 30일 전 이후에 생성된 주문만 남깁니다.
2. `GROUP BY user_id`
   - 남은 주문을 사용자(`user_id`)별로 묶습니다.
3. `SELECT user_id, COUNT(*) AS c`
   - 사용자마다 주문 건수를 세고, 그 값을 `c`라는 별칭으로 보여줍니다.
4. `HAVING COUNT(*) >= 3`
   - 그룹으로 묶은 뒤, 주문이 3건 이상인 사용자만 남깁니다. (`WHERE`는 행 단위 필터, `HAVING`은 그룹 단위 필터라서 여기서는 `HAVING`을 씁니다.)
5. `ORDER BY c DESC`
   - 주문 건수가 많은 사용자부터 내림차순으로 정렬합니다.

**결과:** 한 달 동안 자주 주문한 충성 고객이나 대량 구매자를 찾는 용도로 쓸 수 있습니다. 참고로 `INTERVAL '30 days'`와 `NOW()`는 PostgreSQL 문법이라, 다른 DB에서는 문법을 조금 바꿔야 할 수 있습니다.
