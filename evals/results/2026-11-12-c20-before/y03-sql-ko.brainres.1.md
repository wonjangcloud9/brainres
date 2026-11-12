<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

최근 30일 동안 주문을 **3건 이상** 한 사용자를 주문 수가 많은 순서대로 보여주는 쿼리예요.

단계별로 보면:

1. `WHERE created_at >= NOW() - INTERVAL '30 days'`: 지금부터 30일 전 이후에 생성된 주문만 골라요.
2. `GROUP BY user_id`: 남은 주문을 사용자별로 묶어요.
3. `COUNT(*) AS c`: 각 사용자의 주문 건수를 세고, 결과 열 이름을 `c`로 붙여요.
4. `HAVING COUNT(*) >= 3`: 묶은 뒤에 주문이 3건 미만인 사용자를 제외해요. `WHERE`는 행을 거르고 `HAVING`은 그룹을 거른다는 점이 핵심이에요.
5. `ORDER BY c DESC`: 주문 수가 많은 사용자가 위로 오도록 정렬해요.

`INTERVAL '30 days'`와 `NOW()`는 PostgreSQL 문법이에요. MySQL이라면 `NOW() - INTERVAL 30 DAY`로 써야 해요.

실제 데이터에서 이 쿼리를 돌리려면 `created_at`에 인덱스가 있는지 확인해 보세요. 주문 테이블이 크면 날짜 조건 때문에 전체 스캔이 생길 수 있어요. `EXPLAIN ANALYZE`로 실행 계획을 보면 바로 알 수 있어요.
