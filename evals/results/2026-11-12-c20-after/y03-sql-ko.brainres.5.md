<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자**를 찾아, 주문 수가 많은 순으로 보여줍니다.

단계별로 보면 다음과 같아요.

1. `WHERE`: `created_at`이 지금부터 30일 이내인 주문 행만 남깁니다.
2. `GROUP BY user_id`: 남은 주문을 사용자별로 묶습니다.
3. `COUNT(*) AS c`: 각 사용자의 주문 건수를 세고, 그 값에 `c`라는 별칭을 붙입니다.
4. `HAVING COUNT(*) >= 3`: 집계가 끝난 뒤 주문이 3건 이상인 사용자만 남깁니다.
5. `ORDER BY c DESC`: 주문 건수가 많은 사용자부터 내림차순으로 정렬합니다.

`WHERE`와 `HAVING`은 필터링 시점이 다릅니다.

| 절 | 필터링 대상 | 시점 |
|---|---|---|
| `WHERE` | 개별 주문 행 | 집계 전 |
| `HAVING` | 사용자별 집계 결과 | 집계 후 |

참고로 `NOW() - INTERVAL '30 days'`는 PostgreSQL 문법입니다. MySQL이나 다른 DB를 쓰신다면 날짜 함수를 바꿔야 합니다. 실행할 DB가 어떤 종류인지 알려주시면 맞게 고쳐 드릴게요.
