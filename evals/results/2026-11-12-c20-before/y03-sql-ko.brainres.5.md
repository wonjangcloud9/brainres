<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자**를 주문 수가 많은 순서대로 찾아줍니다.

1. `FROM orders`: `orders` 테이블을 읽습니다.
2. `WHERE created_at >= NOW() - INTERVAL '30 days'`: 현재 시각에서 30일 전 이후에 생성된 주문만 남깁니다.
3. `GROUP BY user_id`: 같은 `user_id`끼리 묶습니다.
4. `COUNT(*) AS c`: 사용자마다 주문 건수를 세어 `c`라는 이름으로 둡니다.
5. `HAVING COUNT(*) >= 3`: 묶음 결과 중 주문이 3건 이상인 사용자만 남깁니다.
6. `ORDER BY c DESC`: 주문 수가 많은 사용자부터 내림차순으로 정렬합니다.

`WHERE`와 `HAVING`의 차이가 핵심입니다. `WHERE`는 그룹으로 묶기 **전**에 개별 행을 거르고, `HAVING`은 `GROUP BY` 이후의 집계 결과를 거릅니다. 그래서 날짜 조건은 `WHERE`에, 건수 조건은 `HAVING`에 들어갑니다.

`NOW()`와 `INTERVAL '30 days'`는 PostgreSQL 문법입니다. MySQL이라면 `NOW() - INTERVAL 30 DAY`로 바꿔야 합니다.

이 결과를 실제 분석에 쓰려면 `EXPLAIN`으로 `created_at` 컬럼에 인덱스가 타는지 확인해 보세요. 테이블이 크면 날짜 범위 조회가 느릴 수 있습니다.
