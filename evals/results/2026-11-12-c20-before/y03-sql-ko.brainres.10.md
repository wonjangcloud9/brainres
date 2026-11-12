<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

최근 30일 동안 주문을 3건 이상 한 사용자를 주문 수가 많은 순서로 보여주는 쿼리예요.

1. `WHERE created_at >= NOW() - INTERVAL '30 days'`: 지금부터 30일 전 이후에 생성된 주문만 남겨요. `INTERVAL '30 days'` 문법은 PostgreSQL 방식이에요.
2. `GROUP BY user_id`: 사용자별로 주문을 묶어요.
3. `COUNT(*) AS c`: 각 사용자의 주문 건수를 `c`라는 이름으로 세요.
4. `HAVING COUNT(*) >= 3`: 묶은 뒤에 주문이 3건 미만인 사용자를 걸러내요. `WHERE`는 행을 거를 때, `HAVING`은 그룹을 거를 때 써요.
5. `ORDER BY c DESC`: 주문 수가 많은 사용자가 위에 오도록 정렬해요.

결과는 `user_id`와 `c` 두 컬럼이에요. 주문 건수는 `orders` 테이블의 모든 행을 세기 때문에, 취소된 주문도 포함돼요. 취소 주문을 빼려면 `status` 같은 컬럼 조건을 `WHERE`에 추가해야 해요. 이 부분은 테이블 스키마를 확인해야 정확히 알 수 있어요.
