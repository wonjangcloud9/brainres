<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

이 쿼리는 **최근 30일 동안 주문을 3건 이상 한 사용자**를 찾아, 주문 횟수가 많은 순서대로 보여주는 쿼리입니다.

단계별로 보면:

1. **`FROM orders`**: 주문 데이터가 담긴 `orders` 테이블에서 조회합니다.
2. **`WHERE created_at >= NOW() - INTERVAL '30 days'`**: 현재 시각 기준 30일 이내에 생성된 주문만 남깁니다. (PostgreSQL 문법입니다.)
3. **`GROUP BY user_id`**: 사용자별로 묶습니다.
4. **`COUNT(*) AS c`**: 각 사용자의 주문 건수를 `c`라는 별칭으로 셉니다.
5. **`HAVING COUNT(*) >= 3`**: 그룹 단위 필터로, 주문이 3건 이상인 사용자만 남깁니다. `WHERE`는 행을 거르고 `HAVING`은 집계된 그룹을 거른다는 점이 차이입니다.
6. **`ORDER BY c DESC`**: 주문 건수가 많은 사용자부터 내림차순으로 정렬합니다.

**결과**: `user_id`와 최근 30일간의 주문 건수가 나오며, 자주 주문하는 충성 고객이나 대량 구매자를 파악하는 데 쓸 수 있습니다.

참고로 `created_at`에 타임존 정보가 있거나 `orders`에 취소된 주문이 섞여 있다면, 필요에 따라 `status` 조건을 추가해 결과를 더 정확하게 만들 수도 있습니다.
