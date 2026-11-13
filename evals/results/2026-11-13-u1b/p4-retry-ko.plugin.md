<!-- Q: 결제 실패 시 자동 재시도 기능 설계 문서를 써줘. 결제는 Stripe를 쓰고 있어. -->

구독(Invoice) 결제라면 직접 만들지 말고 Stripe Smart Retries와 Dunning 이메일을 쓰세요. 일회성 PaymentIntent 결제만 자체 재시도 로직이 필요합니다. 코드베이스와 결제 유형을 아직 몰라서 아래는 가정 기반 초안이에요.

---

# 결제 실패 자동 재시도 설계 문서

## 1. 배경과 목표
- 문제: 일시적 실패(잔액 부족, 네트워크 오류)로 결제가 영구 실패해 매출이 이탈합니다.
- 목표: 복구 가능한 실패만 자동 재시도하고, 복구 불가능한 실패는 즉시 사용자에게 알립니다.
- 비목표: 결제 수단 교체 UI 개편, 환불 로직.

## 2. 결제 유형별 접근

| 유형 | 재시도 주체 | 근거 |
|---|---|---|
| 구독 (Invoice) | Stripe Smart Retries | 내장 기능이고, 카드 승인 확률이 높은 시점을 ML로 골라요 |
| 일회성 (PaymentIntent) | 자체 구현 | Stripe가 자동 재시도하지 않아요 |

Smart Retries는 Dashboard의 Billing → Revenue recovery에서 켭니다. 기본 정책은 2주 안에 8회입니다. 정책 값은 Dashboard에서 확인하세요.

## 3. 실패 분류

`last_payment_error.decline_code`와 `code` 기준으로 나눕니다.

| 분류 | 예시 코드 | 처리 |
|---|---|---|
| 재시도 가능 (soft) | `insufficient_funds`, `processing_error`, `try_again_later` | 백오프 재시도 |
| 재시도 불가 (hard) | `stolen_card`, `lost_card`, `pickup_card`, `fraudulent`, `expired_card` | 재시도 금지, 즉시 결제 수단 변경 요청 |
| 인증 필요 | `authentication_required` | 사용자에게 인증 링크 발송 (`next_action`) |
| 불명확 | `generic_decline`, `do_not_honor` | 최대 1~2회만 재시도 |

hard decline을 반복 재시도하면 카드사 규정 위반이 되거나 Stripe 계정 평판에 불리할 수 있어요. 카드 브랜드별 재시도 횟수 제한은 Stripe 문서에서 확인해야 합니다.

## 4. 자체 재시도 설계 (일회성 결제)

**스케줄**: 1차 실패 후 +1시간, +1일, +3일, +5일. 총 4회 재시도 후 종료합니다. 간격에 지터(±10%)를 넣어요.

**상태 머신**
```
pending → failed_retryable → retry_scheduled → succeeded
                          ↘ failed_final (횟수 소진 / hard decline)
```

**데이터 모델** (`payment_retries`)
- `payment_intent_id` (unique), `attempt_count`, `next_retry_at`, `last_decline_code`, `status`

**실행 흐름**
1. Webhook `payment_intent.payment_failed` 수신
2. 서명 검증 (`Stripe-Signature`) 후 분류
3. 재시도 가능하면 `next_retry_at`을 계산해 저장
4. 워커가 1분 주기로 `next_retry_at <= now` 건을 조회
5. 저장된 PaymentMethod로 `paymentIntents.confirm` 호출 (`off_session: true`)
6. 결과는 webhook으로 확정

## 5. 정합성 규칙
- **멱등성**: 재시도 호출마다 `Idempotency-Key = {payment_intent_id}:{attempt_count}`를 씁니다. 워커가 중복 실행돼도 이중 청구되지 않아요.
- **Webhook 중복**: `event.id`를 저장해 이미 처리한 이벤트는 무시합니다.
- **순서 역전**: webhook 순서는 보장되지 않아요. 상태 전이 전에 Stripe API로 PaymentIntent 현재 상태를 재조회합니다.
- **동시성**: 워커는 행 잠금(`SELECT ... FOR UPDATE SKIP LOCKED`)으로 건을 가져갑니다.

## 6. 사용자 알림
- 1차 실패 즉시: 이메일 + 결제 수단 변경 링크
- 마지막 재시도 24시간 전: 최종 경고
- 최종 실패: 서비스 제한 안내
- 성공 시: 복구 알림

## 7. 모니터링
- 지표: 재시도 성공률(시도 차수별), decline code 분포, 복구 매출, 최종 실패율
- 알림: 재시도 성공률이 급락하면 Stripe 장애나 카드사 이슈를 의심합니다.
- 로그: `payment_intent_id`로 전 과정을 추적합니다.

## 8. 테스트
- Stripe 테스트 카드: `4000000000009995`(insufficient_funds), `4000000000000341`(첨부 후 결제 실패)
- Stripe CLI: `stripe trigger payment_intent.payment_failed`
- 시나리오: 중복 webhook, 워커 중복 실행, 재시도 중 사용자가 카드 교체

## 9. 미결 사항
1. 구독과 일회성 중 어느 쪽이 주력인가요? (구독이면 §4는 불필요)
2. 재시도 중 서비스 접근을 유지할 기간(grace period)
3. 한국 카드 결제의 경우 해외 카드사 규정과 다른 제한이 있는지

---

다음 단계로 §9의 1번을 알려주세요. 그러면 불필요한 섹션을 빼고, 쓰시는 언어와 프레임워크에 맞춰 워커·webhook 코드 스케치를 추가할게요. 파일(`.md`)로 저장해 드릴 수도 있어요.
