<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자**를 주문 수가 많은 순서로 보여줘요.

단계별로 보면 다음과 같아요.

1. `WHERE created_at >= NOW() - INTERVAL '30 days'`: 지금부터 30일 전 이후에 생성된 주문만 남겨요. `INTERVAL '30 days'`는 PostgreSQL 문법이에요.
2. `GROUP BY user_id`: 남은 주문을 사용자별로 묶어요.
3. `COUNT(*) AS c`: 각 사용자의 주문 건수를 세고, 그 결과를 `c`라는 이름으로 불러요.
4. `HAVING COUNT(*) >= 3`: 묶은 뒤에 주문이 3건 미만인 사용자를 걸러내요. 개수 조건은 `WHERE`가 아니라 `HAVING`에 써야 해요.
5. `ORDER BY c DESC`: 주문 수가 많은 사용자부터 내림차순으로 정렬해요.

결과에는 `user_id`와 `c` 두 열이 나와요. 예를 들어 "최근 30일간 자주 주문하는 충성 고객 목록"이나 "이상 주문 패턴 의심 계정 점검"에 쓸 수 있어요.

`orders` 테이블에 `created_at`이 `timestamp` 타입이어야 이 쿼리가 의도대로 동작해요. 타임존 기준으로 30일을 자르고 싶다면 `NOW()` 대신 `CURRENT_DATE - INTERVAL '30 days'`처럼 바꿔 볼 수 있어요.
