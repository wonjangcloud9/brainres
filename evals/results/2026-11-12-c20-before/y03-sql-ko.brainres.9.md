<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 최근 30일 동안 주문을 3건 이상 한 사용자를 주문 수가 많은 순서로 보여줘요.

1. `WHERE`: 지금부터 30일 전 이후에 만들어진 주문만 남겨요.
2. `GROUP BY user_id`: 남은 주문을 사용자별로 묶어요.
3. `COUNT(*) AS c`: 각 사용자의 주문 수를 `c`로 세요.
4. `HAVING COUNT(*) >= 3`: 주문 수가 3건 이상인 사용자만 남겨요.
5. `ORDER BY c DESC`: 주문 수가 많은 순서로 정렬해요.

`WHERE`는 묶기 전의 개별 주문을 걸러내고, `HAVING`은 묶은 뒤의 그룹을 걸러내요. 그래서 `COUNT(*)` 조건은 `WHERE`가 아니라 `HAVING`에 써야 해요.

`NOW() - INTERVAL '30 days'`는 PostgreSQL 문법이에요. MySQL이라면 `NOW() - INTERVAL 30 DAY`로 바꿔야 해요.

같은 사용자의 주문 금액 합계도 함께 보고 싶다면 `SUM(amount)` 같은 컬럼을 `SELECT`에 추가하면 돼요. 금액 컬럼 이름을 알려주시면 쿼리를 바로 만들어 드릴게요.
