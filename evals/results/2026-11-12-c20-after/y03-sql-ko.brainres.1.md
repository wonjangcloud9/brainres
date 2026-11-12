<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자를 주문 수가 많은 순서로** 보여줘요.

- **WHERE**: `created_at`이 지금으로부터 30일 이내인 주문만 남겨요.
- **GROUP BY user_id**: 남은 주문을 사용자별로 묶어요.
- **HAVING COUNT(*) >= 3**: 묶은 뒤 주문이 3건 이상인 사용자만 남겨요. 행을 거르는 `WHERE`와 달리 `HAVING`은 그룹을 거를 때 써요.
- **ORDER BY c DESC**: 주문 수 `c`가 많은 사용자부터 정렬해요.

`INTERVAL '30 days'`는 PostgreSQL 문법이에요. MySQL에서는 `DATE_SUB(NOW(), INTERVAL 30 DAY)`로 바꿔야 해요. 실행 DB를 알려주시면 그에 맞게 고쳐 드릴게요.
