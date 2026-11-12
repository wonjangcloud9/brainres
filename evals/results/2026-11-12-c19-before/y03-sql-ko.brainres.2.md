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

1. `WHERE created_at >= NOW() - INTERVAL '30 days'`: 지금부터 30일 전 이후에 생성된 주문만 남겨요.
2. `GROUP BY user_id`: 남은 주문을 사용자별로 묶어요.
3. `COUNT(*) AS c`: 각 사용자의 주문 수를 `c`라는 이름으로 세요.
4. `HAVING COUNT(*) >= 3`: 집계 후 주문 수가 3건 이상인 사용자만 남겨요. `WHERE`는 행 단위 필터라서 집계 조건은 `HAVING`에 써야 해요.
5. `ORDER BY c DESC`: 주문 수가 많은 사용자부터 내림차순으로 정렬해요.

결과는 `user_id`와 `c` 두 열이에요. 예를 들어 `(42, 7)`은 사용자 42가 최근 30일 동안 주문을 7건 했다는 뜻이에요.

`INTERVAL '30 days'`와 `NOW()` 문법은 PostgreSQL 방식이에요. MySQL이라면 `NOW() - INTERVAL 30 DAY`처럼 써야 해요.

원하시면 같은 쿼리에 사용자 이름을 붙이거나, 기간을 파라미터로 바꾸는 예제를 만들어 드릴게요.
