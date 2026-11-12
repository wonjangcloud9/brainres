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

절에 따라 나눠서 보면 이렇게 동작해요.

- **`WHERE created_at >= NOW() - INTERVAL '30 days'`**: 지금부터 30일 전 이후에 생성된 주문만 남겨요. `INTERVAL` 문법은 PostgreSQL 기준이에요.
- **`GROUP BY user_id`**: 남은 주문을 사용자별로 묶어요.
- **`COUNT(*) AS c`**: 각 사용자의 주문 수를 `c`라는 이름으로 세요.
- **`HAVING COUNT(*) >= 3`**: 묶은 뒤에 주문이 3건 미만인 사용자를 제외해요. 그룹에 조건을 거는 곳이 `HAVING`이라서 `WHERE`가 아니라 여기에 써요.
- **`ORDER BY c DESC`**: 주문 수가 많은 사용자가 위로 오도록 정렬해요.

결과는 `user_id`와 `c` 두 열이에요. 예를 들어 `(user_id=42, c=7)`이면 사용자 42가 최근 30일 동안 주문을 7번 했다는 뜻이에요.

MySQL이나 SQLite에서 실행하면 `INTERVAL '30 days'` 문법이 맞지 않아 오류가 나요. 그때는 `NOW() - INTERVAL 30 DAY`(MySQL)나 `datetime('now', '-30 days')`(SQLite)로 바꿔야 해요.
