<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

최근 30일 동안 주문을 3건 이상 한 사용자를 주문 수가 많은 순서로 뽑는 쿼리예요.

단계별로 보면 이래요.

1. `WHERE created_at >= NOW() - INTERVAL '30 days'`: 지금부터 30일 전 이후에 생성된 주문만 남겨요.
2. `GROUP BY user_id`: 남은 주문을 사용자별로 묶어요.
3. `COUNT(*) AS c`: 각 사용자의 주문 건수를 `c`라는 이름으로 세요.
4. `HAVING COUNT(*) >= 3`: 집계된 결과에서 주문이 3건 미만인 사용자를 제외해요. 집계 뒤에 거르는 조건이라 `WHERE`가 아니라 `HAVING`을 써요.
5. `ORDER BY c DESC`: 주문 건수가 많은 사용자가 위에 오도록 정렬해요.

결과는 `user_id`와 `c` 두 열이에요. 예를 들어 `(user_id=42, c=7)`은 42번 사용자가 최근 30일간 주문을 7건 했다는 뜻이에요.

`NOW() - INTERVAL '30 days'` 문법은 PostgreSQL 기준이에요. MySQL이라면 `NOW() - INTERVAL 30 DAY`로 써야 해요. 실행 중인 DB 종류를 알려주시면 문법이 맞는지 확인해 드릴게요.
