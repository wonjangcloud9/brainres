<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

최근 30일 동안 주문을 3건 이상 한 사용자를 찾아서, 주문 수가 많은 순서로 보여주는 쿼리예요.

단계별로 보면 이래요.

1. `WHERE created_at >= NOW() - INTERVAL '30 days'`: 지금부터 30일 전까지의 주문만 남겨요.
2. `GROUP BY user_id`: 사용자별로 묶어요.
3. `HAVING COUNT(*) >= 3`: 묶은 뒤 주문 수가 3건 이상인 사용자만 남겨요. `WHERE`는 묶기 전에, `HAVING`은 묶은 후에 걸리는 조건이에요.
4. `ORDER BY c DESC`: 주문 수(`c`)가 많은 사용자부터 정렬해요.

결과는 `user_id`와 `c`(최근 30일 주문 건수) 두 컬럼이에요. 재구매가 잦은 단골 고객을 뽑을 때 쓰는 전형적인 형태예요.

한 가지 주의할 점이 있어요. `INTERVAL '30 days'` 문법은 PostgreSQL 스타일이라, MySQL에서는 `INTERVAL 30 DAY`로 써야 해요. 또 `NOW()` 기준이라 실행 시각에 따라 30일 경계가 달라져요. 날짜 단위로 자르고 싶으면 `CURRENT_DATE - INTERVAL '30 days'`로 바꾸면 돼요.

취소·환불 주문을 제외하고 싶다면 `WHERE`에 상태 조건을 추가하면 돼요. 컬럼명을 알려주시면 반영해 드릴게요.
