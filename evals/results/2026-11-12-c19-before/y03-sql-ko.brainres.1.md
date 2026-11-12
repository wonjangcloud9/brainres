<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자**를 주문 수가 많은 순으로 뽑습니다.

동작 순서는 다음과 같습니다.

1. `WHERE`: `created_at`이 지금부터 30일 전 이후인 주문만 남깁니다.
2. `GROUP BY user_id`: 사용자별로 묶습니다.
3. `COUNT(*) AS c`: 각 사용자의 주문 건수를 `c`라는 이름으로 셉니다.
4. `HAVING COUNT(*) >= 3`: 묶은 뒤 건수가 3 이상인 사용자만 남깁니다.
5. `ORDER BY c DESC`: 주문 수가 많은 사용자부터 내림차순으로 정렬합니다.

결과는 `user_id`와 `c` 두 열로 나옵니다. 자주 구매하는 고객을 찾거나 재구매 고객 목록을 만들 때 쓰는 형태입니다.

`WHERE`와 `HAVING`의 차이는 중요합니다. `WHERE`는 묶기 전 개별 주문을 거르고, `HAVING`은 묶은 뒤 그룹을 거릅니다. 그래서 건수 조건은 `HAVING`에 써야 합니다.

`INTERVAL '30 days'`와 `NOW()` 문법은 PostgreSQL 기준입니다. 다른 DB를 쓰면 날짜 함수를 바꿔야 할 수 있습니다. 예를 들어 MySQL은 `NOW() - INTERVAL 30 DAY`로 씁니다.

다음으로 이 쿼리를 실제 테이블에 돌려 결과 건수를 확인하거나, 특정 기간 조건을 바꿔 보는 것을 권합니다.
