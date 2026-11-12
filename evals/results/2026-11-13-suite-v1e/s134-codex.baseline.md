<!-- Q: 이 쿼리 설명해줘.

```sql
SELECT c.id FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;
``` -->

이 쿼리는 **주문이 한 건도 없는 고객의 id**를 찾는 쿼리입니다. 이를 "안티 조인(anti-join)" 패턴이라고 부릅니다.

## 동작 순서

1. **`FROM customers c`**: 모든 고객을 기준(왼쪽 테이블)으로 시작합니다.

2. **`LEFT JOIN orders o ON o.customer_id = c.id`**: 각 고객에 해당하는 주문을 붙입니다.
   - 주문이 있는 고객은 주문 수만큼 행이 생깁니다.
   - 주문이 없는 고객도 LEFT JOIN이므로 행이 유지되며, `o`의 모든 컬럼이 `NULL`로 채워집니다.

3. **`WHERE o.id IS NULL`**: `o.id`가 NULL인 행만 남깁니다. 즉, 매칭되는 주문이 없었던 고객만 남습니다.

4. **`SELECT c.id`**: 그 고객들의 id를 반환합니다.

## 예시

customers:

| id |
|----|
| 1  |
| 2  |
| 3  |

orders:

| id  | customer_id |
|-----|-------------|
| 10  | 1           |
| 11  | 1           |
| 12  | 3           |

LEFT JOIN 결과:

| c.id | o.id |
|------|------|
| 1    | 10   |
| 1    | 11   |
| 2    | NULL |
| 3    | 12   |

여기서 `o.id IS NULL`인 행은 고객 2뿐이므로 결과는 `2`입니다.

## 참고

- `o.id`는 orders의 PK(항상 NOT NULL)라서, NULL이면 "매칭 실패"를 의미합니다. 그래서 `o.id`로 검사하는 것이 안전합니다.
- 같은 결과를 내는 다른 방식:
  ```sql
  SELECT c.id FROM customers c
  WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
  ```
  `NOT EXISTS`는 의도가 더 명확하고, 대부분의 DB에서 성능도 LEFT JOIN 방식과 비슷하거나 더 좋습니다.
- `NOT IN`은 `orders.customer_id`에 NULL이 있으면 결과가 비어버리는 함정이 있어, 이 용도로는 LEFT JOIN이나 `NOT EXISTS`를 권장합니다.
