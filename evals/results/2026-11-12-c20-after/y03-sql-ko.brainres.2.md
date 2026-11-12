<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자**를 주문 수가 많은 순서로 보여줍니다.

1. `WHERE created_at >= NOW() - INTERVAL '30 days'`: 지금부터 30일 전 이후에 생성된 주문만 남깁니다.
2. `GROUP BY user_id`: 남은 주문을 사용자별로 묶습니다.
3. `COUNT(*) AS c`: 각 사용자의 주문 건수를 `c`라는 이름으로 셉니다.
4. `HAVING COUNT(*) >= 3`: 묶은 뒤에 주문이 3건 미만인 사용자를 뺍니다. 집계 결과를 거르므로 `WHERE`가 아니라 `HAVING`을 씁니다.
5. `ORDER BY c DESC`: 주문 수가 많은 사용자가 위에 오도록 정렬합니다.

결과는 `user_id`와 `c`(주문 건수) 두 열입니다. 예를 들어 "최근 한 달 동안 자주 주문한 충성 고객" 목록을 뽑을 때 쓸 수 있습니다.

`INTERVAL '30 days'`와 `NOW()`는 PostgreSQL 문법입니다. MySQL이나 다른 DB에서는 날짜 함수가 달라서 그대로 실행되지 않을 수 있습니다.

`created_at`에 인덱스가 있으면 기간 필터가 빨라집니다. 실제 실행 계획은 `EXPLAIN ANALYZE`로 확인해 보세요.
