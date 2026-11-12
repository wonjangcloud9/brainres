<!-- Q: SQL이랑 NoSQL 차이 정리해줘. -->

# SQL vs NoSQL 차이

## 핵심 비교

| 구분 | SQL (관계형) | NoSQL (비관계형) |
|---|---|---|
| **데이터 모델** | 테이블(행/열), 고정 스키마 | 문서, 키-값, 컬럼 패밀리, 그래프 등 다양 |
| **스키마** | 사전에 엄격히 정의 (schema-on-write) | 유연, 동적 변경 가능 (schema-on-read) |
| **관계 처리** | JOIN, 외래 키로 정규화된 관계 표현 | 보통 JOIN 약함, 중복 저장(비정규화)으로 해결 |
| **확장 방식** | 주로 수직 확장(Scale-up), 수평 확장은 어려움 | 수평 확장(Scale-out, 샤딩)에 설계됨 |
| **트랜잭션** | ACID 강력 지원 | 제품별 상이, 전통적으로 BASE(최종적 일관성), 최근엔 ACID 지원도 증가 |
| **쿼리 언어** | 표준 SQL | 제품별 고유 API/쿼리 |
| **대표 제품** | MySQL, PostgreSQL, Oracle, SQL Server | MongoDB, Redis, Cassandra, DynamoDB, Neo4j |

## NoSQL 유형

- **Document**: JSON 형태 문서 저장 (MongoDB, Couchbase)
- **Key-Value**: 단순 키로 빠른 조회 (Redis, DynamoDB)
- **Wide-Column**: 대용량 쓰기·분산에 강함 (Cassandra, HBase)
- **Graph**: 노드·엣지 관계 탐색 (Neo4j)

## 장단점

**SQL**
- 장점: 데이터 무결성, 복잡한 쿼리/집계, 성숙한 생태계, 강한 일관성
- 단점: 스키마 변경 비용, 대규모 분산 확장 어려움

**NoSQL**
- 장점: 유연한 스키마, 대용량·고속 처리, 손쉬운 수평 확장
- 단점: 복잡한 JOIN·트랜잭션 제한, 데이터 중복·일관성 관리 부담, 표준 부재

## 언제 무엇을 쓰나

- **SQL 선택**: 금융·주문·결제처럼 정합성이 중요, 관계가 복잡, 다양한 조회/리포팅 필요
- **NoSQL 선택**: 트래픽/데이터 폭증, 스키마가 자주 바뀜, 로그·세션·캐시·실시간 피드·IoT 등 단순 접근 패턴

## 참고

- 둘은 대체 관계가 아니라 **용도에 따라 병행**하는 경우가 많습니다 (예: 주문은 PostgreSQL, 세션/캐시는 Redis).
- 경계가 흐려지는 추세입니다: PostgreSQL의 JSONB, MongoDB의 멀티 도큐먼트 트랜잭션, NewSQL(CockroachDB, Spanner)처럼 확장성과 ACID를 함께 노리는 제품도 있습니다.
- 기본값을 고르라면, 요구사항이 불확실할 때는 **SQL(PostgreSQL)로 시작**하고 필요할 때 NoSQL을 추가하는 편이 안전합니다.
