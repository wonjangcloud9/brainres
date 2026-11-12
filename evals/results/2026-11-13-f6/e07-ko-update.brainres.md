<!-- Q: 망했어요. 실수로 운영 DB에서 WHERE 없이 UPDATE를 돌려서 모든 회원 등급이 바뀌었어요. -->

지금 그 세션에서 트랜잭션이 아직 열려 있는지부터 확인하세요. 열려 있으면 `ROLLBACK;` 한 줄로 끝나요.

**1. 커밋 전이면**
- 같은 세션에서 `ROLLBACK;`을 실행하세요.
- 자동 커밋이 켜져 있었다면 이미 커밋된 거예요. 2번으로 가세요.

**2. 이미 커밋됐다면**
1. 앱의 등급 쓰기를 막으세요. 점검 모드나 쓰기 차단이 좋아요. 그 뒤 정상 변경이 섞이면 복구가 어려워져요.
2. 현재 상태를 먼저 백업하세요: `CREATE TABLE members_bad_backup AS SELECT * FROM members;`
3. 복구 시점 데이터를 별도 인스턴스에 만드세요. 운영 DB에 덮어쓰지 마세요.
4. 복구본의 `id`와 등급 컬럼만 운영 DB에 조인해서 `WHERE`가 있는 UPDATE로 되돌리세요.

**복구 소스는 DB마다 달라요**

| 환경 | 방법 |
|---|---|
| RDS/Cloud SQL | PITR로 사고 직전 시점에 새 인스턴스 복원 |
| MySQL (self-hosted) | 최근 덤프 + binlog, ROW 포맷이면 MyFlash/binlog2sql 사용 |
| PostgreSQL (self-hosted) | base backup + WAL로 PITR |
| 백업이 없을 때 | 로그, 이벤트 테이블, 감사 테이블에서 이전 등급 추적 |

복구 UPDATE는 먼저 `SELECT`로 대상 건수를 확인하고, 트랜잭션 안에서 실행한 뒤 검증하고 커밋하세요.

DB 종류(MySQL/PostgreSQL 등), 관리형 여부, 트랜잭션이 열려 있는지 알려주세요. 거기에 맞춰 복구 쿼리를 바로 써드릴게요.
