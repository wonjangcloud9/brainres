<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 고객**을 주문 수가 많은 순서로 찾아요.

처리 순서는 다음과 같아요.

1. `WHERE`: `created_at`이 지금부터 30일 이내인 주문만 남겨요.
2. `GROUP BY user_id`: 남은 주문을 고객별로 묶어요.
3. `COUNT(*) AS c`: 고객마다 주문 건수를 세고, 결과 열 이름을 `c`로 붙여요.
4. `HAVING COUNT(*) >= 3`: 주문이 3건 미만인 고객을 결과에서 빼요. `WHERE`는 행을 거르고 `HAVING`은 묶은 그룹을 거른다는 점이 핵심이에요.
5. `ORDER BY c DESC`: 주문 수가 많은 고객부터 보여줘요.

결과는 `user_id`와 `c` 두 열이에요. 예를 들어 `user_id = 42, c = 7`이면 42번 고객이 최근 30일 동안 7건을 주문했다는 뜻이에요.

참고로 `NOW() - INTERVAL '30 days'`는 PostgreSQL 문법이에요. MySQL이라면 `DATE_SUB(NOW(), INTERVAL 30 DAY)`로 바꿔야 해요. 또 `COUNT(*)`는 취소된 주문도 세므로, 취소 건을 빼려면 `WHERE`에 `status <> 'cancelled'` 같은 조건을 더하세요. `status` 열 이름은 실제 스키마에 맞춰 바꿔야 해요.
