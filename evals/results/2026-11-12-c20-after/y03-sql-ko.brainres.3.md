<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자**를 주문 수가 많은 순서로 뽑습니다.

| 절 | 역할 |
|---|---|
| `WHERE created_at >= NOW() - INTERVAL '30 days'` | 지금부터 30일 전 이후에 생성된 주문만 남깁니다. 그룹화 전에 행을 거릅니다. |
| `GROUP BY user_id` | 같은 사용자의 주문을 한 묶음으로 합칩니다. |
| `COUNT(*) AS c` | 사용자마다 주문 건수를 세고, 결과 열 이름을 `c`로 붙입니다. |
| `HAVING COUNT(*) >= 3` | 묶은 뒤에 주문이 3건 미만인 사용자를 뺍니다. 집계 값으로 거르므로 `WHERE`가 아니라 `HAVING`을 씁니다. |
| `ORDER BY c DESC` | 주문 수가 많은 사용자부터 내림차순으로 정렬합니다. |

`INTERVAL '30 days'`와 `NOW()`는 PostgreSQL 문법입니다. MySQL이나 다른 DB에서는 `DATE_SUB` 같은 다른 함수를 써야 합니다.

주의할 점은 주문 상태입니다. 쿼리는 취소되거나 환불된 주문도 모두 셉니다. 실제 구매 횟수만 보고 싶다면 `AND status = 'completed'` 같은 조건을 `WHERE`에 추가하면 됩니다. 테이블에 상태 컬럼이 있는지 알려주시면 정확한 조건을 적어 드릴게요.
