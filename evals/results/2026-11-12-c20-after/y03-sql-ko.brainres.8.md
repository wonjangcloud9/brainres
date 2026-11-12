<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자**를 주문 수가 많은 순서로 찾습니다.

1. `WHERE created_at >= NOW() - INTERVAL '30 days'`: 최근 30일 안에 생성된 주문만 남깁니다.
2. `GROUP BY user_id`: 사용자별로 묶습니다.
3. `COUNT(*) AS c`: 각 사용자의 주문 수를 `c`로 셉니다.
4. `HAVING COUNT(*) >= 3`: 묶은 뒤 주문이 3건 미만인 사용자를 제외합니다. `WHERE`는 묶기 전 행을, `HAVING`은 묶은 뒤 그룹을 거른다는 점이 핵심입니다.
5. `ORDER BY c DESC`: 주문 수가 많은 사용자부터 보여줍니다.

`INTERVAL '30 days'`와 `NOW()`는 PostgreSQL 문법입니다. MySQL이라면 `NOW() - INTERVAL 30 DAY`로 바꿔야 합니다.

결과에 사용자 이름이 필요하면 `users` 테이블과 `user_id`로 JOIN하면 됩니다.
