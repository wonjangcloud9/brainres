<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

최근 30일 동안 주문을 3건 이상 한 사용자를 찾아서, 주문 수가 많은 순서대로 보여줘요.

단계별로 보면 이래요.

1. `WHERE created_at >= NOW() - INTERVAL '30 days'`: 지금부터 30일 전 이후에 생성된 주문만 남겨요.
2. `GROUP BY user_id`: 사용자별로 주문을 묶어요.
3. `HAVING COUNT(*) >= 3`: 묶은 뒤 주문 수가 3건 이상인 사용자만 남겨요. `WHERE`는 묶기 전 행을 거르고, `HAVING`은 묶은 뒤 그룹을 걸러요.
4. `ORDER BY c DESC`: 주문 수 `c`가 큰 사용자부터 정렬해요.

결과는 `user_id`와 `c`(최근 30일 주문 수) 두 컬럼이에요. 재구매가 잦은 단골 고객을 뽑는 용도로 자주 써요.

`INTERVAL '30 days'` 문법은 PostgreSQL 스타일이에요. MySQL에서는 `INTERVAL 30 DAY`로 써야 해요. 취소·환불 주문도 세고 싶지 않다면 `WHERE`에 상태 조건(예: `status <> 'cancelled'`)을 추가하면 돼요.
