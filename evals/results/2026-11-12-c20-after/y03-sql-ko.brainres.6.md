<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자를 주문 수가 많은 순으로** 보여줍니다.

각 절의 역할은 다음과 같습니다.

- **`WHERE created_at >= NOW() - INTERVAL '30 days'`**: 지금부터 30일 이내에 생성된 주문만 남깁니다. 행을 거르는 단계입니다.
- **`GROUP BY user_id`**: 남은 주문을 사용자별로 묶습니다.
- **`COUNT(*) AS c`**: 묶음마다 주문 건수를 세고, 그 값을 `c`라는 이름으로 씁니다.
- **`HAVING COUNT(*) >= 3`**: 그룹 단위로 거릅니다. 주문이 3건 미만인 사용자는 결과에서 빠집니다.
- **`ORDER BY c DESC`**: 주문 수가 많은 사용자부터 내림차순으로 정렬합니다.

`WHERE`와 `HAVING`의 차이가 헷갈리기 쉽습니다. `WHERE`는 개별 주문 행을 거르고, `HAVING`은 `GROUP BY`로 만든 집계 결과를 거릅니다.

**참고:** `NOW()`와 `INTERVAL '30 days'`는 PostgreSQL 문법입니다. MySQL에서는 `NOW() - INTERVAL 30 DAY` 형태로 써야 하고, SQL Server에서는 `DATEADD`를 씁니다.

실행 중인 DB가 어떤 것인지 알려주시면, 그 DB에 맞게 쿼리를 고쳐 드릴 수 있습니다.
