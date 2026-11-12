<!-- Q: 이 쿼리 설명해줘.

```sql
SELECT c.id FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;
``` -->

주문이 한 건도 없는 고객의 id를 찾는 쿼리예요.

**동작 순서**

1. `customers`의 모든 행에 `orders`를 `customer_id = c.id`로 LEFT JOIN해요. 주문이 있는 고객은 주문 수만큼 행이 나와요. 주문이 없는 고객도 한 행으로 남고, `o`의 컬럼은 전부 NULL이에요.
2. `WHERE o.id IS NULL`로 `o.id`가 NULL인 행만 남겨요. 매칭된 주문이 없다는 뜻이에요.
3. `c.id`만 출력해요.

**예시**

| customers.id | orders.id | 결과 |
|---|---|---|
| 1 | 10 | 제외 |
| 1 | 11 | 제외 |
| 2 | NULL | **포함** |

고객 1은 주문이 두 건이라 제외되고, 고객 2는 주문이 없어서 결과에 나와요.

**알아둘 점**

- `o.id`는 orders의 PK라서 정상 데이터에서는 NULL이 될 수 없어요. 그래서 "NULL이면 JOIN 실패"로 해석할 수 있어요.
- 같은 결과를 내는 다른 방법은 `WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id)`예요. 의도가 더 잘 드러나요. 성능은 DB와 인덱스에 따라 달라서 `EXPLAIN`으로 확인해 보세요.
- 이 패턴을 안티 조인(anti-join)이라고 불러요.

다음 단계로, 쓰는 DB가 정해져 있으면 `orders.customer_id`에 인덱스가 있는지 확인해 보세요.
