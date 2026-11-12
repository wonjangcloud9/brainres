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
2. `GROUP BY user_id`: 사용자별로 묶어요.
3. `COUNT(*) AS c`: 각 사용자의 주문 건수를 `c`라는 이름으로 세요.
4. `HAVING COUNT(*) >= 3`: 묶은 뒤에 3건 미만인 사용자를 제외해요. `WHERE`는 묶기 전 행을, `HAVING`은 묶은 뒤 그룹을 거른다는 점이 핵심이에요.
5. `ORDER BY c DESC`: 주문 수가 많은 사용자가 위에 오도록 정렬해요.

주의할 점이 두 가지 있어요.

- **롤링 윈도우예요.** `NOW() - 30 days`는 실행하는 순간부터 거꾸로 30일이라서, "이번 달"이나 "지난 30일 달력 기준"과 결과가 다를 수 있어요.
- **취소·환불 주문도 세요.** `status` 같은 조건이 없으므로 취소된 주문까지 포함돼요. 구매 확정 건만 보려면 `WHERE`에 상태 조건을 추가해야 해요.

이 쿼리는 PostgreSQL 문법(`INTERVAL '30 days'`)이라서 MySQL이나 다른 DB에서는 날짜 연산 부분을 바꿔야 해요. 실제 결과가 예상과 맞는지 확인하려면 `SELECT COUNT(*) FROM orders WHERE created_at >= NOW() - INTERVAL '30 days'`로 전체 대상 건수를 먼저 확인해 보세요.
