<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자**를 주문 수가 많은 순으로 보여줘요.

1. `WHERE created_at >= NOW() - INTERVAL '30 days'`: 지금부터 30일 전 이후에 생성된 주문만 남겨요.
2. `GROUP BY user_id`: 남은 주문을 사용자별로 묶어요.
3. `COUNT(*) AS c`: 사용자마다 주문 건수를 세고, 결과 열 이름을 `c`로 붙여요.
4. `HAVING COUNT(*) >= 3`: 주문이 3건 미만인 사용자는 결과에서 제외해요. `WHERE`는 그룹화 전 행을 거르고, `HAVING`은 그룹화 후 집계 결과를 거른다는 점이 핵심이에요.
5. `ORDER BY c DESC`: 주문 건수가 많은 사용자부터 내림차순으로 정렬해요.

결과에는 `user_id`와 `c`(주문 건수) 두 열만 나와요. `NOW()`와 `INTERVAL '30 days'` 문법은 PostgreSQL 기준이라서, MySQL이나 다른 DB에서는 날짜 함수를 바꿔야 할 수 있어요.

자주 구매하는 사용자를 찾는 용도로 보이는데, 특정 기간 기준으로 쓰려면 `NOW()` 대신 고정 날짜를 넣어 보세요. 실제로 실행해 보고 싶으면 DB 종류와 `orders` 테이블 스키마를 알려 주세요.
