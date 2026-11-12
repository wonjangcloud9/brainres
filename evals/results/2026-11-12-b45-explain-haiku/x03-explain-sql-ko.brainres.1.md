<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

최근 30일 동안 주문을 3건 이상 한 사용자를 주문 수가 많은 순서로 보여 주는 쿼리예요.

1. `WHERE created_at >= NOW() - INTERVAL '30 days'`: 지금부터 30일 전 이후에 생성된 주문만 남겨요.
2. `GROUP BY user_id`: 남은 주문을 사용자별로 묶어요.
3. `COUNT(*) AS c`: 각 사용자의 주문 수를 세고 `c`라는 이름을 붙여요.
4. `HAVING COUNT(*) >= 3`: 주문이 3건 이상인 사용자만 남겨요.
5. `ORDER BY c DESC`: 주문 수가 많은 사용자부터 내림차순으로 정렬해요.

결과에는 `user_id`와 주문 수 `c` 두 열이 나와요.

헷갈리기 쉬운 부분은 **WHERE는 묶기 전에, HAVING은 묶은 뒤에** 적용된다는 점이에요. 그래서 기간 조건은 WHERE에, 건수 조건은 HAVING에 들어가요.

`NOW() - INTERVAL '30 days'`는 PostgreSQL 문법이에요. MySQL이나 SQL Server에서는 `DATE_SUB`나 `DATEADD`처럼 다르게 써야 해요. 사용하는 DB가 무엇인지 알려 주시면 그에 맞게 바꿔 드릴게요.
