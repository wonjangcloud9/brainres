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

절별로 나누면 다음과 같습니다.

- `FROM orders`: 주문 테이블을 읽습니다.
- `WHERE created_at >= NOW() - INTERVAL '30 days'`: 지금부터 30일 전 이후에 생성된 주문만 남깁니다.
- `GROUP BY user_id`: 같은 `user_id`끼리 묶습니다.
- `COUNT(*) AS c`: 묶음마다 주문 건수를 세고, 그 값을 `c`라는 이름으로 부릅니다.
- `HAVING COUNT(*) >= 3`: 묶은 뒤에 주문이 3건 이상인 사용자만 남깁니다. `WHERE`는 행을 묶기 전에, `HAVING`은 묶은 후에 거른다는 점이 다릅니다.
- `ORDER BY c DESC`: 주문 건수가 많은 사용자가 위에 오도록 정렬합니다.

결과는 `user_id`와 `c` 두 열입니다. 예를 들어 `(user_id=42, c=7)`이면 사용자 42가 최근 30일 동안 7건을 주문했다는 뜻입니다.

`INTERVAL '30 days'`와 `NOW()` 문법은 PostgreSQL 기준입니다. MySQL이라면 `NOW() - INTERVAL 30 DAY`로 바꿔야 합니다.

다음으로 상위 사용자의 이름이나 이메일도 함께 보고 싶다면, `users` 테이블과 `user_id`로 `JOIN`하는 쿼리를 만들어 드릴 수 있습니다.
