<!-- Q: 결제 실패 시 자동 재시도 기능 설계 문서를 써줘. 결제는 Stripe를 쓰고 있어. -->

Stripe 결제 구조(Subscription/Invoice 기반인지, 일회성 PaymentIntent인지)를 아직 모르기 때문에 두 경우를 모두 다루고 가정은 문서에 명시해서 작성하겠습니다.


<invoke name="Write">
<parameter name="file_path">/private/var/folders/5v/r7qdd9b90t91plfwnfk5hdqm0000gn/T/tmpqaim4e_c/docs/payment-retry-design.md</parameter>
<parameter name="content"># 결제 실패 자동 재시도 설계 문서

- 상태: Draft
- 작성일: 2026-11-13
- 결제 수단: Stripe

## 1. 배경 및 문제

카드 결제는 일시적 사유(잔액 부족, 은행 일시 장애, 네트워크 오류 등)로 실패하는 경우가 많고, 상당수는 시간이 지나 재시도하면 성공한다. 현재 실패한 결제를 수동으로 처리하거나 그대로 이탈시키면 비자발적 이탈(involuntary churn)과 매출 손실이 발생한다. 이를 줄이기 위해 자동 재시도(dunning) 체계를 도입한다.

## 2. 목표 / 비목표

### 목표
- 복구 가능한 실패는 자동으로 재시도하여 결제 복구율을 높인다.
- 복구 불가능한 실패는 재시도하지 않고 즉시 고객에게 결제 수단 변경을 안내한다.
- 중복 청구를 절대 발생시키지 않는다 (멱등성 보장).
- 재시도 상태를 추적하고 관측할 수 있다.

### 비목표
- 결제 대행사 교체 또는 다중 PG 지원
- 환불/분쟁(dispute) 처리 자동화
- 카드 정보 직접 저장 (Stripe가 보관, PCI 범위 최소화)

## 3. 전제 (확인 필요)

| 항목 | 가정 |
|---|---|
| 과금 모델 | 구독(Stripe Billing) 중심, 일부 일회성 결제(PaymentIntent) 존재 |
| 백엔드 | Stripe 웹훅을 수신할 수 있는 서버가 있음 |
| 저장소 | 관계형 DB 사용 |
| 알림 | 이메일 발송 수단 존재 |

가정이 다르면 4장의 방식 선택이 달라진다.

## 4. 접근 방식 선택

### 옵션 A. Stripe Billing의 Smart Retries + 자동 이메일 사용 (권장: 구독 결제)
- Stripe가 ML 기반으로 최적 시점에 재시도하고, 재시도 횟수·최종 처리(구독 취소/미납 처리)를 대시보드에서 설정한다.
- 직접 구현할 코드가 적고 카드 네트워크 규칙 변화에도 Stripe가 대응한다.
- 우리는 웹훅으로 상태만 동기화하고 서비스 접근 권한을 제어한다.

### 옵션 B. 자체 재시도 스케줄러 (일회성 PaymentIntent용)
- Invoice가 없는 결제는 Smart Retries 대상이 아니므로 자체 구현이 필요하다.
- 실패 코드별 정책, 스케줄, 멱등 키를 직접 관리한다.

### 결정
- 구독 결제: **옵션 A**를 기본으로 하고, 앱 측에서는 웹훅 처리와 접근 제어만 구현한다.
- 일회성 결제: **옵션 B**를 최소 범위로 구현한다 (6장).
- 두 경로 모두 동일한 내부 상태 모델(5장)과 알림 정책을 공유한다.

## 5. 상태 모델

```
            payment_failed (retryable)
 ACTIVE ───────────────────────────────► PAST_DUE ──┐
   ▲                                        │       │ 재시도 성공
   │ paid                                   │       ▼
   └────────────────────────────────────────┴──── ACTIVE
                                            │
                  재시도 소진 / non-retryable │
                                            ▼
                                       UNPAID / CANCELED
```

- `ACTIVE`: 정상
- `PAST_DUE`: 결제 실패, 재시도 진행 중. 유예 기간 동안 서비스 유지 (정책은 8장)
- `UNPAID` / `CANCELED`: 재시도 소진 또는 복구 불가 사유로 종결

### 데이터 모델 (예시)

```sql
CREATE TABLE payment_attempts (
  id                 BIGSERIAL PRIMARY KEY,
  customer_id        TEXT NOT NULL,
  stripe_invoice_id  TEXT,
  stripe_pi_id       TEXT,
  attempt_no         INT  NOT NULL,
  status             TEXT NOT NULL,        -- succeeded | failed | scheduled
  decline_code       TEXT,
  failure_category   TEXT,                 -- retryable | non_retryable | needs_action
  next_retry_at      TIMESTAMPTZ,
  idempotency_key    TEXT NOT NULL UNIQUE,
  created_at         TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE processed_webhook_events (
  stripe_event_id TEXT PRIMARY KEY,
  processed_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

## 6. 재시도 정책

### 6.1 실패 유형 분류

`last_payment_error.decline_code` / `code`를 기준으로 분류한다.

| 분류 | 예시 코드 | 처리 |
|---|---|---|
| retryable | `insufficient_funds`, `processing_error`, `issuer_not_available`, `try_again_later`, 네트워크/5xx | 스케줄에 따라 재시도 |
| needs_action | `authentication_required` (3DS), `requires_action` | 재시도하지 않고 고객에게 인증 링크 안내 |
| non_retryable | `stolen_card`, `lost_card`, `pickup_card`, `fraudulent`, `invalid_account`, `card_not_supported` | 재시도 금지, 결제 수단 변경 요청 |
| 미분류 | 그 외 | 보수적으로 1회만 재시도 후 non_retryable 처리 |

> 주의: `do_not_honor`, `generic_decline`은 사유가 불명확하다. 제한된 횟수만 재시도한다. 발급사 사유가 불명확한 코드를 과도하게 재시도하면 카드 네트워크의 재시도 제한 규칙에 걸리거나 승인율이 떨어질 수 있다.

### 6.2 스케줄 (옵션 B 기준, 초안)

| 시도 | 시점 (최초 실패 기준) |
|---|---|
| 1차 | +1일 |
| 2차 | +3일 |
| 3차 | +5일 |
| 4차 | +7일 (최종) |

- 최대 4회, 총 유예 기간 7일 (옵션 A는 Stripe 대시보드에서 동일하게 설정)
- 지수 백오프 + 지터(±2시간)로 동시 처리 부하 분산
- 급여일 등 승인율이 높은 시점은 추후 데이터 기반으로 튜닝

### 6.3 멱등성

- 모든 Stripe 쓰기 요청에 `Idempotency-Key` 헤더를 사용한다.
- 키 형식: `retry:{payment_id}:{attempt_no}`. 동일 시도는 같은 키를 재사용해 네트워크 재전송 시 중복 청구를 막는다.
- `payment_attempts.idempotency_key`의 UNIQUE 제약으로 이중 방어한다.

## 7. 웹훅 처리

### 구독할 이벤트

| 이벤트 | 동작 |
|---|---|
| `invoice.payment_failed` | 실패 분류, 상태를 PAST_DUE로 전환, 알림 발송 |
| `invoice.paid` / `payment_intent.succeeded` | ACTIVE 복구, 예약된 재시도 취소 |
| `payment_intent.payment_failed` | (옵션 B) 다음 재시도 예약 또는 종결 |
| `customer.subscription.updated` / `deleted` | 구독 상태 동기화 |
| `payment_method.attached` / `customer.updated` | 결제 수단 변경 시 즉시 재시도 트리거 |

### 처리 원칙
1. `Stripe-Signature` 검증을 필수로 한다 (raw body 사용).
2. `processed_webhook_events`에 이벤트 ID를 저장해 중복 수신을 무시한다.
3. 이벤트는 순서가 보장되지 않는다. 처리 시 이벤트 payload만 믿지 말고 필요하면 Stripe API로 최신 객체를 재조회한다.
4. 핸들러는 빠르게 2xx를 반환하고, 무거운 작업은 큐에 넘긴다. 실패 시 Stripe가 재전송한다.

## 8. 서비스 접근 정책

- PAST_DUE 유예 기간(기본 7일) 동안은 서비스를 유지하고 상단 배너로 결제 수단 변경을 안내한다.
- 유예 종료 후에도 미납이면 기능을 제한(읽기 전용)하고, 추가 기간 후 구독을 취소한다.
- 구체적 제한 범위는 제품 팀과 확정이 필요하다 (오픈 이슈 1).

## 9. 고객 알림

| 시점 | 채널 | 내용 |
|---|---|---|
| 최초 실패 | 이메일 + 인앱 | 실패 사실, 결제 수단 변경 링크 (Stripe Customer Portal 또는 자체 페이지) |
| 재시도 전 (D-1) | 이메일 | 재시도 예정 안내 |
| 최종 실패 직전 | 이메일 + 인앱 | 서비스 중단 예고 |
| 복구 성공 | 이메일 | 결제 완료 확인 |

- 3DS 필요 건은 별도 템플릿으로 인증 링크(`hosted_invoice_url`)를 제공한다.
- 알림 중복 방지를 위해 `(customer, event_type, attempt_no)` 단위로 발송 이력을 기록한다.

## 10. 장애 및 예외 처리

| 상황 | 대응 |
|---|---|
| Stripe API 타임아웃/5xx | 동일 Idempotency-Key로 재시도 (최대 3회, 지수 백오프) |
| 429 Rate limit | `Retry-After` 존중, 큐 처리량 조절 |
| 웹훅 누락 | 일 1회 reconcile 잡: 최근 N일의 `past_due` Invoice를 Stripe에서 조회해 내부 상태와 대조 |
| 재시도 도중 고객이 결제 수단 변경 | 예약된 재시도를 취소하고 즉시 새 수단으로 시도 |
| 동시 실행 (워커 중복) | 행 단위 락 또는 `SELECT ... FOR UPDATE SKIP LOCKED`로 단일 처리 보장 |

## 11. 보안 / 컴플라이언스

- 카드 번호 등 민감 정보는 저장·로그하지 않는다. Stripe의 ID(`pm_`, `cus_`, `in_`)만 저장한다.
- 웹훅 시크릿과 API 키는 시크릿 매니저에서 관리하고 제한된 권한의 Restricted Key를 사용한다.
- 로그에 고객 이메일 등 개인정보를 남기지 않는다.

## 12. 관측성

### 지표
- 복구율: 최초 실패 건 중 최종 성공 비율 (시도 차수별 분해)
- decline_code 분포
- PAST_DUE 평균 체류 시간
- 중복 청구 건수 (목표 0)
- 웹훅 처리 지연 / 실패율

### 알림(Alert)
- 웹훅 처리 실패율 급증
- 복구율이 기준선 대비 급락
- reconcile 잡에서 불일치 발견

## 13. 테스트 계획

- **Stripe Test Clocks**: 구독 갱신·재시도 스케줄을 시간 가속으로 검증
- **테스트 카드**
  - `4000 0000 0000 0341`: 결제 수단 연결은 성공, 청구 시 실패
  - `4000 0000 0000 9995`: 잔액 부족
  - `4000 0027 6000 3184`: 3DS 인증 필요
- 단위 테스트: 실패 코드 분류, 스케줄 계산, 멱등 키 생성
- 통합 테스트: 웹훅 중복/순서 역전 수신, 재시도 중 결제 수단 변경
- Stripe CLI(`stripe trigger`, `stripe listen`)로 로컬 웹훅 검증

## 14. 롤아웃 계획

1. 테스트 모드에서 전체 흐름 검증
2. 웹훅 핸들러·상태 동기화만 먼저 배포 (재시도는 Stripe 기본 설정)
3. Smart Retries 및 알림 활성화, 신규 구독자 일부(예: 10%)에 적용
4. 지표 확인 후 전체 확대
5. 필요 시 옵션 B(일회성 결제 재시도) 배포

롤백: Stripe 대시보드의 재시도 설정을 이전 값으로 되돌리고 앱 측 feature flag를 끈다.

## 15. 오픈 이슈

1. PAST_DUE 상태에서 서비스 제한 범위와 유예 기간 (제품/CS 합의 필요)
2. 일회성 결제에도 자동 재시도가 필요한지 (고객 동의 및 약관 문구 포함)
3. 지역별 규제 (예: 반복 결제 사전 고지 의무, 카드 네트워크 재시도 횟수 제한) 확인
4. 알림 채널 확장 여부 (SMS, 푸시)
5. 현재 Stripe 계정에 Billing/Smart Retries가 활성화되어 있는지 확인

## 16. 참고

- Stripe Docs: Automatic collection / Smart Retries (Billing)
- Stripe Docs: Idempotent requests
- Stripe Docs: Webhooks, Test clocks, Decline codes
</parameter>
</invoke>
<system-reminder>
Tool result: File created successfully at /private/var/folders/5v/r7qdd9b90t91plfwnfk5hdqm0000gn/T/tmpqaim4e_c/docs/payment-retry-design.md
</system-reminder>
