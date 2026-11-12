<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

최근 30일 안에 주문을 3건 이상 한 사용자를 찾아서, 주문 횟수가 많은 순으로 보여주는 쿼리예요.

단계별로 보면:

1. **`FROM orders WHERE created_at >= NOW() - INTERVAL '30 days'`**: 현재 시각 기준 30일 이내에 생성된 주문만 추립니다.
2. **`GROUP BY user_id`**: 사용자별로 묶습니다.
3. **`COUNT(*) AS c`**: 각 사용자의 주문 건수를 셉니다.
4. **`HAVING COUNT(*) >= 3`**: 묶은 뒤 주문 건수가 3건 이상인 사용자만 남깁니다. (`WHERE`는 그룹화 전 행 필터, `HAVING`은 그룹화 후 결과 필터입니다.)
5. **`ORDER BY c DESC`**: 주문 건수가 많은 사용자부터 정렬합니다.

결과는 `user_id`와 `c`(최근 30일 주문 수) 두 컬럼이며, 흔히 "최근 한 달 단골/重복 구매 고객"을 뽑을 때 쓰는 패턴입니다.

참고로 `INTERVAL '30 days'` 문법은 PostgreSQL 스타일이에요. MySQL에서는 `INTERVAL 30 DAY`처럼 작성해야 합니다. 또 `NOW() - 30일`은 "정확히 30×24시간 전"이라 날짜 경계(자정)가 아니라 현재 시각 기준이라는 점도 알아두세요.
