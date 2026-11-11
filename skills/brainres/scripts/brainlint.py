#!/usr/bin/env python3
"""brainlint — score how easy a chat answer is for a human brain to read.

Deterministic, stdlib-only heuristics. Each check maps to a cognitive-science
principle (see research/cognitive-principles.md). Works on English and Korean.

Usage:
  python3 scripts/brainlint.py answer.md            # human report
  python3 scripts/brainlint.py --json answer.md     # machine-readable
  cat answer.md | python3 scripts/brainlint.py -
  python3 scripts/brainlint.py --badge README.md   # markdown badge for your README
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict

# ---------- patterns ----------

PREAMBLE = re.compile(
    r"^\s*(great question|good question|sure[!,. ]|certainly[!,. ]|absolutely[!,. ]|of course[!,. ]|"
    r"i'?d be (happy|glad) to|happy to help|let me (explain|help|break)|thanks for asking|"
    r"좋은 질문|물론입니다|물론이죠|네[,!] ?(알겠습니다|좋습니다)|도와드리겠습니다|설명해 ?드리겠습니다)",
    re.I,
)
OUTRO = re.compile(
    r"(let me know if|hope (this|that) helps|feel free to (ask|reach)|happy to (help|elaborate)|"
    r"if you have any (other |more )?questions|궁금한 (점|것)이 있(으시면|다면)|도움이 되(셨|었)기를|"
    r"추가로 (궁금|필요)하신|언제든(지)? (물어|질문))",
    re.I,
)
HEDGES_EN = re.compile(
    r"\b(might|may|perhaps|possibly|potentially|arguably|it'?s worth noting|it is important to note|"
    r"generally speaking|in some cases|to some extent)\b",
    re.I,
)
HEDGES_KO = re.compile(r"(일 수(도)? 있습니다|일 수(도)? 있어요|것 같습니다|할 수도 있|라고 볼 수 있|경우에 따라)")
NOMINAL_EN = re.compile(r"\b\w{4,}(tion|sion|ment|ance|ence|ity|ness)s?\b", re.I)
TRANSLATIONESE_KO = re.compile(r"(하는 것이다|하는 것입니다|에 대한|에 있어서|에 의해|을 통해|적인 [가-힣]+의 |것은 [가-힣]+것)")
DOUBLE_NEG = re.compile(r"\b(not|never|no)\b[^.?!]{0,30}\b(un\w+|in\w+able|non\w+|without)\b|안 [가-힣]+지 않", re.I)

GENERIC_HEADING = re.compile(
    r"^\s{0,3}#{1,6}\s*(overview|introduction|understanding( the problem)?|background|conclusion|summary|"
    r"solutions?|best practices|key (takeaways|points|considerations)|final thoughts|details|"
    r"개요|소개|결론|요약|정리|배경|마무리)\s*:?\s*$",
    re.I,
)
META_TALK = re.compile(
    r"(let me (break (this|it) down|walk you through|explain)|here'?s (a|the) (breakdown|overview)|"
    r"in this (answer|response)|자세히 (설명|알아)|하나씩 살펴보|정리해 ?드리)",
    re.I,
)
BURIED_EN = re.compile(
    r"^\s*(there are (several|many|a few|multiple|various)\b|it (really )?depends\b|when it comes to\b|"
    r"before (we|i) (dive|get) in|in order to understand\b|this is a (common|great|good|tricky) (question|issue|problem)|"
    r"there('s| is) no (simple|easy|one-size)|the answer (to this )?(is not|isn't) (simple|straightforward))",
    re.I,
)
BURIED_KO = re.compile(r"^\s*(여러 가지|다양한 (요인|방법|측면)|경우에 따라|상황에 따라|~?에 대해 (알아|설명)|이 질문은|많은 (분들|개발자)들?이)")
CAUSAL = re.compile(r"\b(because|so|therefore|since|thus|hence|which means|as a result|that's why)\b|때문|그래서|따라서|그러므로|이유는|왜냐하면|그 결과", re.I)
TERM_SWAPS = [("folder", "directory"), ("routine", "function"), ("app", "application"),
              ("폴더", "디렉터리"), ("폴더", "디렉토리"), ("앱", "애플리케이션")]
BOLD_LEAD = re.compile(r"^\s*([-*+]|\d+[.)])\s+(\*\*|__)")

HANGUL = re.compile(r"[가-힣]")
SENT_SPLIT = re.compile(r"(?<=[.!?。])\s+|(?<=[다요죠음함])\.\s*|\n+")
LIST_ITEM = re.compile(r"^\s*([-*+]|\d+[.)])\s+")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s")
BOLD = re.compile(r"\*\*[^*\n]+\*\*|__[^_\n]+__")
CODE_FENCE = re.compile(r"^```.*?^```", re.S | re.M)


@dataclass
class Finding:
    check: str
    principle: str
    detail: str
    penalty: int


@dataclass
class Report:
    score: int
    words: int
    sentences: int
    avg_sentence_words: float
    lang: str
    findings: list[Finding] = field(default_factory=list)


def strip_code(text: str) -> str:
    return CODE_FENCE.sub(" ", text)


def sentences_of(prose: str) -> list[str]:
    # Headings are labels, not sentences: counting them would dilute the average.
    body = "\n".join(l for l in prose.splitlines() if not HEADING.match(l))
    parts = [p.strip() for p in SENT_SPLIT.split(body)]
    out = []
    for p in parts:
        p = LIST_ITEM.sub("", p).strip()
        if len(p.split()) >= 2:
            out.append(p)
    return out


TABLE_ROW = re.compile(r"^\s*\|")


def lint(text: str) -> Report:
    # Code blocks and table rows are structure, not prose: they aren't paragraphs or sentences.
    prose = "\n".join(l for l in strip_code(text).splitlines() if not TABLE_ROW.match(l))
    lines = prose.splitlines()
    words = prose.split()
    n_words = max(len(words), 1)
    ko = len(HANGUL.findall(prose)) > len(re.findall(r"[A-Za-z]", prose)) * 0.5
    lang = "ko" if ko else "en"
    sents = sentences_of(prose)
    n_sents = max(len(sents), 1)
    full = [s for s in sents if len(s.split()) >= 3] or sents  # 2-word labels don't count toward the average
    avg = sum(len(s.split()) for s in full) / max(len(full), 1)
    findings: list[Finding] = []

    def add(check, principle, detail, penalty):
        findings.append(Finding(check, principle, detail, penalty))

    # 1. Answer-first: preamble in the opening line (primacy / BLUF / coherence)
    first = next((l for l in lines if l.strip()), "")
    first_para = re.split(r"\n\s*\n", prose.strip(), maxsplit=1)[0]
    if PREAMBLE.search(first):
        add("preamble", "Primacy effect + BLUF", f"opens with filler: '{first.strip()[:60]}'", 15)
    if META_TALK.search(first_para):
        add("meta_talk", "Extraneous load", "first paragraph announces the answer instead of giving it", 6)
    elif not PREAMBLE.search(first) and (BURIED_KO if ko else BURIED_EN).search(first):
        add("buried_answer", "BLUF / preference for advance information (#28, AN-49)",
            f"first sentence frames instead of answering: '{first.strip()[:60]}'", 8)

    # 2. Generic outro (recency slot wasted)
    tail = "\n".join([l for l in lines if l.strip()][-2:])
    if OUTRO.search(tail):
        add("outro", "Recency effect / coherence principle", "ends with generic sign-off instead of the key takeaway or next step", 8)

    # 3. Sentence length (processing fluency, working memory)
    # Korean is measured in eojeol (space-separated units): avg <=12 per korean.md; English in words.
    limit, long_at = (12, 20) if ko else (25, 35)
    long_s = [s for s in sents if len(s.split()) > long_at]
    if avg > limit:
        add("sentence_length", "Working-memory load / processing fluency",
            f"average sentence {avg:.1f} {'eojeol' if ko else 'words'} (target <= {limit})", 10)
    if long_s:
        add("long_sentences", "Working-memory load",
            f"{len(long_s)} sentence(s) over {long_at} {'eojeol' if ko else 'words'}", min(4 * len(long_s), 12))

    # 4. Wall of text (segmenting principle)
    paras = [p for p in re.split(r"\n\s*\n", prose) if p.strip()]
    walls = [p for p in paras if len(p.split()) > (70 if ko else 110)]
    if walls:
        add("wall_of_text", "Segmenting principle", f"{len(walls)} paragraph(s) too long to hold in working memory", min(6 * len(walls), 15))

    # 5. List overload (Cowan's 4±1 / chunking)
    run, runs = 0, []
    for l in lines:
        if LIST_ITEM.match(l) and not l.startswith(("    ", "\t")):
            run += 1
        elif l.strip():
            if run:
                runs.append(run)
            run = 0
    if run:
        runs.append(run)
    big = [r for r in runs if r > 5]
    if big:
        add("list_overload", "Chunking (Cowan 4±1)", f"list(s) of {', '.join(map(str, big))} items; group into labeled chunks of <=4", min(5 * len(big), 12))

    # 5b. Fragmented reasoning: mostly bullets, no causal links (#36, HC-16, PL-54)
    content_lines = [l for l in lines if l.strip()]
    list_lines = [l for l in content_lines if LIST_ITEM.match(l)]
    if n_words >= 120 and content_lines and len(list_lines) / len(content_lines) > 0.6 and not CAUSAL.search(prose):
        add("fragmented_reasoning", "Causal connectives (#36) / bullets fragment reasoning (HC-16)",
            "mostly bullets and no because/so: the reader must infer how points connect", 6)

    # 5c. Elegant variation: two names for one thing (PL-33, HC-34)
    low = prose.lower()
    swaps = [f"{a}/{b}" for a, b in TERM_SWAPS
             if re.search(rf"(?<![\w가-힣]){a}(?![a-z])", low) and re.search(rf"(?<![\w가-힣]){b}(?![a-z])", low)]
    if swaps:
        add("term_swap", "Argument overlap: one term per concept (PL-33, HC-34)", f"same thing named two ways: {', '.join(swaps)}", 3)

    # 6. Signal dilution: too much bold (von Restorff only works if rare)
    bolds = len(BOLD.findall(prose))
    items = [l for l in lines if LIST_ITEM.match(l)]
    leads = [l for l in items if BOLD_LEAD.match(l)]
    if len(leads) >= 4 and len(leads) >= 0.6 * len(items):
        add("bold_lead_ins", "Signal dilution (Lorch 1989)", f"{len(leads)} list items start with bold; emphasis becomes decoration", 6)
    elif bolds and bolds / n_words * 100 > 3:
        add("bold_overuse", "Isolation (von Restorff) effect", f"{bolds} bold spans in {n_words} words; emphasis stops working", 8)

    # 7. Over-structuring short answers (coherence / extraneous load)
    heads = sum(1 for l in lines if HEADING.match(l))
    generic = [l.strip() for l in lines if GENERIC_HEADING.match(l)]
    if generic:
        add("generic_heading", "Layer-cake scanning (headings must carry content)", f"content-free heading(s): {', '.join(generic)[:80]}", min(3 * len(generic), 9))
    if heads and n_words < 150:
        add("heading_short", "Coherence principle (extraneous load)", f"{heads} heading(s) in a {n_words}-word answer", 6)

    # 8. Hedging density (cognitive ease, trust calibration)
    hedges = len(HEDGES_KO.findall(prose)) if ko else len(HEDGES_EN.findall(prose))
    if hedges >= 3 and hedges / n_words * 100 > 1.0:
        add("hedging", "Trust calibration / processing fluency", f"{hedges} hedges; state uncertainty once, where it applies", 6)

    # 9. Nominalizations / translationese (verbs are easier than abstract nouns)
    if ko:
        tr = len(TRANSLATIONESE_KO.findall(prose))
        if tr / n_words * 100 > 2:
            add("translationese", "Processing fluency (번역투)", f"{tr} translationese patterns (~에 대한, ~하는 것이다, ~을 통해)", 6)
    else:
        nom = len(NOMINAL_EN.findall(prose))
        if nom / n_words * 100 > 6:
            add("nominalization", "Processing fluency (agent-action clarity)", f"{nom} nominalizations; prefer verbs ('decide' not 'make a decision')", 6)

    # 10. Double negation (negation processing cost)
    dn = len(DOUBLE_NEG.findall(prose))
    if dn:
        add("double_negation", "Negation processing cost", f"{dn} double-negative construction(s)", min(4 * dn, 8))

    score = max(0, 100 - sum(f.penalty for f in findings))
    return Report(score, len(words), len(sents), round(avg, 1), lang, findings)


def grade(score: int) -> str:
    return "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 60 else "D" if score >= 40 else "F"


BADGE_COLORS = {"A": "2ea44f", "B": "97ca00", "C": "dfb317", "D": "fe7d37", "F": "e05d44"}


def badge(score: int) -> str:
    g = grade(score)
    return (f"[![Brain Score](https://img.shields.io/badge/Brain_Score-{score}%2F100_{g}-{BADGE_COLORS[g]})]"
            "(https://github.com/wonjangcloud9/brainres)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="markdown/text file, or - for stdin")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--badge", action="store_true", help="print a shields.io markdown badge for the score")
    a = ap.parse_args()
    text = sys.stdin.read() if a.file == "-" else open(a.file, encoding="utf-8").read()
    r = lint(text)
    if a.json:
        print(json.dumps(asdict(r), ensure_ascii=False, indent=2))
        return 0
    if a.badge:
        print(badge(r.score))
        return 0
    print(f"Brain Score: {r.score}/100 ({grade(r.score)})  ·  {r.words} words · {r.sentences} sentences · avg {r.avg_sentence_words}/sentence · lang={r.lang}")
    for f in sorted(r.findings, key=lambda f: -f.penalty):
        print(f"  -{f.penalty:>2}  {f.check:<16} {f.detail}   [{f.principle}]")
    if not r.findings:
        print("  no issues found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
