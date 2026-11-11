# 🧠 brainres

**뇌가 실제로 읽기 쉬운 Claude 답변.**

[English](README.md) · 한국어

`caveman`은 Claude를 짧게 만들고, `humanizer`는 사람처럼 들리게 만듭니다.
**brainres는 이해되게 만듭니다.** 인지과학, 심리언어학, 의사결정 과학, 인간–AI 신뢰 연구에서 **725개 연구 결과**를 검토했습니다. 각 결과는 글쓰기 규칙으로 적용하거나, 이유를 적고 제외했습니다.

[![Claude Code plugin](https://img.shields.io/badge/Claude_Code-plugin-d97757)](#설치) [![coverage](https://img.shields.io/badge/findings_applied-596%2F596-2ea44f)](research/coverage.md) [![reviewed](https://img.shields.io/badge/findings_reviewed-725-blue)](research/) [![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![built by](https://img.shields.io/badge/built_by-a_20--min_Claude_loop-8a63d2)](LOOP_LOG.md) [![Brain Score](https://img.shields.io/badge/Brain_Score-96%2F100_A-2ea44f)](https://github.com/wonjangcloud9/brainres)

---

## 같은 질문, 두 가지 답

> *"Redis랑 그냥 메모리 캐시 중에 뭐 써야 해? 서버는 한 대야."*

<table>
<tr><th>흔한 AI 답변 · Brain Score <b>41</b></th><th>brainres 적용 · Brain Score <b>100</b></th></tr>
<tr valign="top"><td>

좋은 질문입니다! 캐시 선택에 대한 고민은 많은 개발자들이 겪는 문제입니다. 자세히 설명해 드리겠습니다.

**## 개요**
캐싱 전략의 선택에 있어서 고려해야 할 사항은 매우 다양하며, 애플리케이션의 요구사항과 인프라 환경에 대한 이해를 통해 적절한 솔루션을 선택하는 것이 중요한 것입니다…

**## Redis의 장점**
- **영속성**: …
- **확장성**: …
- … *(6개, 전부 굵게)*

**## 인메모리 캐시의 장점**
- … *(3개)*

결론적으로, 상황에 따라 적절한 선택을 하시는 것이 좋을 것 같습니다. 궁금한 점이 있으시면 언제든지 물어보세요!

</td><td>

서버가 한 대면 **메모리 캐시**로 시작하세요. Redis는 서버를 늘릴 때 붙이면 됩니다.

메모리 캐시가 맞는 이유는 두 가지입니다.

- 네트워크를 안 거쳐서 더 빠릅니다. Redis는 같은 머신에서도 0.1~1ms가 걸리지만, 프로세스 안 메모리 조회는 1마이크로초도 안 걸립니다.
- 따로 띄우고 관리할 서버가 없습니다.

Redis가 필요해지는 순간은 이 셋 중 하나가 생길 때입니다.

- 서버가 2대 이상이 되어 캐시를 같이 봐야 할 때
- 재시작해도 캐시가 남아 있어야 할 때
- 세션이나 랭킹처럼 여러 프로세스가 같은 데이터를 고칠 때

지금 할 일: 캐시 접근을 `getCache()`/`setCache()` 같은 함수 하나로 감싸 두세요. 나중에 Redis로 바꿀 때 그 함수 안만 고치면 됩니다.

</td></tr>
</table>

달라진 점은 네 가지입니다.

- 추천 하나와 바꿀 시점을 함께 줍니다(기본값 효과).
- 한 묶음에 3개 이하만 둡니다(작업기억 한계 ≈ 4).
- 질문자의 상황("서버 한 대")을 그대로 씁니다.
- 마지막은 지금 할 일로 끝냅니다.

전체 예시는 [`examples/`](examples/)에 있습니다.

## 설치

```bash
claude plugin install brainres --marketplace wonjangcloud9/brainres
```

Claude Code 안에서 설치하려면 `/plugin marketplace add wonjangcloud9/brainres`를 실행한 뒤 `/plugin install brainres@brainres`를 실행하세요.

설치하면 바로 모든 답변에 적용됩니다. 실측 비용은 아래와 같습니다([`scripts/token_cost.sh`](scripts/token_cost.sh), Claude 토크나이저, Sonnet 3회 중앙값).

| 부분 | 토큰 | 언제 |
|---|---:|---|
| 규칙 카드 | 418 | 세션당 1회 |
| 리마인더 | 79 | 매 메시지 |
| 스킬 본문 | 3,893 | 스킬을 호출할 때만 |

20번 주고받는 세션이면 추가 입력은 약 2,000토큰입니다(캐싱 전 기준). 카드의 11줄은 전체 연구를 RICE로 다시 줄 세워 골랐습니다([순위표](research/core-card-ranking.md)). 리마인더를 두는 이유는 긴 대화에서 지시가 점점 흐려지기 때문입니다.

**끄기와 출력 스타일**

- 끄려면 `export BRAINRES=off` 또는 `touch ~/.claude/brainres.off`를 실행하세요.
- 출력 스타일로 쓰려면 `/output-style`에서 **brainres**를 고르세요. 규칙은 같고, 코딩 지침도 유지됩니다.
- 출력 스타일을 쓸 때는 `BRAINRES=off`로 두면 카드가 두 번 들어가지 않습니다. 다만 리마인더도 함께 꺼집니다.

**다른 곳에서 쓰기** (모두 같은 원본에서 [`scripts/build_dist.py`](scripts/build_dist.py)로 생성):

| 어디서 | 파일 | 방법 |
|---|---|---|
| claude.ai / Claude 데스크톱 | [`dist/brainres-skill.zip`](dist/brainres-skill.zip) | 설정 → 스킬 → 업로드 |
| ChatGPT, Gemini 등 모든 LLM | [`dist/system-prompt.md`](dist/system-prompt.md) | 맞춤 지침에 붙여 넣기(1,011바이트, ChatGPT 1,500자 칸에 들어감) |
| Codex 등 AGENTS.md를 읽는 에이전트 | [`dist/AGENTS.md`](dist/AGENTS.md) | 레포 루트에 복사하거나 기존 AGENTS.md 뒤에 붙이기 |
| Cursor | [`dist/cursor/brainres.mdc`](dist/cursor/brainres.mdc) | `.cursor/rules/brainres.mdc`로 복사 |
| 플러그인 없이 Claude Code | `skills/brainres/` | `cp -R skills/brainres ~/.claude/skills/brainres` 후 `/brainres` |

hook은 플러그인으로 설치했을 때만 붙습니다. 다른 방법으로 설치하면 규칙 카드나 스킬은 들어가지만, 매 메시지 리마인더는 붙지 않습니다.

## 10가지 규칙

| # | 규칙 | 근거 |
|---|---|---|
| 1 | **첫 문장에 답.** 그다음 이유, 그다음 세부. | BLUF, 외재적 인지부하(Sweller) |
| 2 | **다음 할 일로 끝내기.** "도움이 되셨길" 대신. | 계열위치 효과, 피크엔드 법칙 |
| 3 | **내용만큼만 길게.** 사실은 100단어, 설명은 300단어 이하. 500단어가 넘으면 맨 위에 요약. | 읽기 속도(Brysbaert 2019), 긴 LLM 답변이 신뢰를 부풀림(Steyvers 2025) |
| 4 | **4개씩 묶기.** 더 많으면 소제목으로 나누기. | 작업기억 ≈ 4 덩어리(Cowan 2001) |
| 5 | **내용에 맞는 형식.** 추론은 문단, 순서는 번호 목록, 비교는 표. | 인지적 적합성(Vessey), 인과 연결어(Trabasso) |
| 6 | **강조는 아껴서.** 내용을 담은 소제목, 문단당 굵은 글씨 최대 1개. | 신호 원리(메타분석 g≈.5), 폰 레스토프 효과 |
| 7 | **구체적으로, 질문자의 것으로.** 질문자의 파일과 값으로 만든 예제 하나. | 구체성, 자기참조, 풀이 예제 효과(g=.48) |
| 8 | **질문자의 단어 그대로, 개념 하나에 용어 하나.** 새 용어는 쓰기 전에 정의. | 어휘 동조, 지식의 저주 |
| 9 | **얼버무리지 말고 보정.** "70% 정도 확신합니다"라고 말하고, 확인 방법을 함께. | 수치 불확실성은 신뢰를 유지(van der Bles 2020), 1인칭 단서가 과신을 줄임(Kim 2024) |
| 10 | **쉬운 문장.** 한 문장에 생각 하나, 능동태, 중첩절 없이. 한국어는 번역투(~에 대한, ~을 통해, ~하는 것이다)를 뺍니다. | 중심 내포 비용(Gibson 2022), 부정문 처리 비용 |

**동조 대신 정직합니다.** 질문의 전제를 확인하고, 근거가 있을 때만 동의하며, 아첨하지 않습니다. 아첨하는 AI는 신뢰를 높이지만 판단력을 해칩니다(Cheng 2026, *Science*).

**상대 수준에 맞춥니다.** 전문가에게는 짧게, 초보자에게는 용어 정의, 비유 하나, 예제 하나를 먼저 줍니다(전문성 역전 효과). 설명, 결정, 숫자, 코드, 절차, 학습, 오류 교정 같은 상황별 원리는 [참고 파일](skills/brainres/references/)로 나눠 두고, 필요할 때만 꺼내 씁니다.

## 모드

| 모드 | 용도 |
|---|---|
| 기본 | 모든 답변. 항상 켜져 있음. |
| `scan` | 답과 4개 이하 항목만. 훑어보기용, 전문가용. |
| `learn` | 설명 전 질문 하나, 풀이 예제, 마지막에 확인 질문 1~2개(인출 연습). |
| `rewrite` | 붙여 넣은 글을 규칙대로 다시 쓰고, 빠진 주장이 없는지 확인. |
| `score` | brainlint로 채점. |
| `off` | 잠시 끄기. |

## brainlint: 답변 채점기

의존성 없는 채점기입니다. 한국어와 영어를 지원하고, 한국어 번역투도 잡습니다.

```bash
python3 skills/brainres/scripts/brainlint.py answer.md
```
```
Brain Score: 41/100 (D)  ·  lang=ko
  -15  preamble         opens with filler: '좋은 질문입니다! ...'      [Primacy effect + BLUF]
  - 8  outro            ends with generic sign-off                   [Recency effect]
  - 6  translationese   3 translationese patterns (~에 대한, ~을 통해)  [Processing fluency]
  - 5  list_overload    list of 6 items; chunks of <=4               [Chunking (Cowan 4±1)]
  - 4  long_sentences   1 sentence(s) over 20 eojeol                 [Working-memory load]
```

검사 항목마다 연구 결과 하나에 대응합니다. 다만 휴리스틱일 뿐, 이해도 시험은 아닙니다.

**내 README도 채점해서 배지로 달 수 있습니다.**

```bash
python3 skills/brainres/scripts/brainlint.py --badge README.md
```

이 문서는 96점입니다. 맨 위 예시에 일부러 넣은 22어절짜리 나쁜 문장 때문입니다. 영어 README는 100점입니다.

## 감이 아니라 근거

7개 카탈로그에서 연구 결과 **725개**를 검토했습니다. 각 결과에는 출처, 근거 등급, 그리고 규칙 또는 제외 이유가 붙어 있습니다.

| 구분 | 개수 |
|---|---:|
| 적용 대상 (모두 스킬 규칙이 인용) | 596 / 596 |
| 이유를 적고 제외 (텍스트와 무관, 재현 실패, 뉴로미스, 조작적 기법) | 129 |

분야끼리 겹치는 결과는 한 번만 셉니다. 현황은 [`research/coverage.md`](research/coverage.md)에 있고, 적용 개수가 줄어드는 커밋은 검증에서 막힙니다.

**프롬프트는 가볍게 유지합니다.** 상시 카드는 418토큰입니다. 상황별 원리는 13개 참고 파일에 나눠 두고, 그 상황일 때만 읽습니다.

**쓰지 않는 뉴로미스**: 학습 스타일, 좌뇌/우뇌, "8초 집중력", 데일의 원뿔, Bionic Reading, "도파민 자극" 포맷팅, "집중 회복에 23분". 카탈로그에 모두 30개가 있습니다.

**솔직한 한계.** LLM 채팅 답변의 포맷 규칙을 통제 실험으로 검증한 연구는 아직 없습니다. 저희도 아직 안 했습니다. 기준값은 튜닝할 출발점이고, 사람 대상 이해도 벤치마크는 [로드맵](BACKLOG.md)에 있습니다.

## 밤새 루프가 만드는 레포

이 레포는 스스로 개선됩니다.

- 20분마다 Claude Code 루프가 [RICE 점수 백로그](BACKLOG.md)에서 1위 항목을 골라 구현하고, 검증하고, 푸시합니다.
- 백로그가 비면 다시 리서치합니다.
- 모든 회차는 [`LOOP_LOG.md`](LOOP_LOG.md)에 기록되고, 진행 절차는 [`LOOP.md`](LOOP.md)에 있습니다.

## 기여

이슈와 PR 환영합니다. 특히 brainres 때문에 답변이 **더 나빠진** 사례가 반갑습니다. 규칙은 `research/`의 연구를 인용할 때만 추가됩니다.

MIT © wonjangcloud9
