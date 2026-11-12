<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자**를 주문 수가 많은 순으로 보여줍니다.

각 절의 역할은 다음과 같아요.

| 절 | 역할 |
|---|---|
| `WHERE created_at >= NOW() - INTERVAL '30 days'` | 지난 30일 이내에 생성된 주문만 남깁니다. (PostgreSQL 문법입니다.) |
| `GROUP BY user_id` | 사용자별로 주문을 묶습니다. |
| `COUNT(*) AS c` | 각 사용자의 주문 건수를 `c`라는 이름으로 셉니다. |
| `HAVING COUNT(*) >= 3` | 묶은 결과 중 주문이 3건 이상인 사용자만 남깁니다. |
| `ORDER BY c DESC` | 주문 수가 많은 사용자가 위에 오도록 정렬합니다. |

`WHERE`는 묶기 전의 행을, `HAVING`은 묶은 뒤의 그룹을 거른다는 점이 핵심이에요.

`user_id`가 `NULL`인 주문이 있다면 `NULL` 그룹이 하나 생겨 결과에 함께 나올 수 있습니다. 이를 빼려면 `WHERE`에 `AND user_id IS NOT NULL`을 추가하세요.

실제 데이터에서 실행해 보려면 `orders` 테이블에 `created_at` 컬럼의 타입(`timestamp` 또는 `timestamptz`)을 확인해 보시는 것을 권해요. 타입에 따라 30일 경계의 시간대 해석이 달라질 수 있습니다.
