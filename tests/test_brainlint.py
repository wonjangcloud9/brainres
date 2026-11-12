"""Golden tests for brainlint. Run: python3 -m unittest discover -s tests -q"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True  # a stale .pyc (same size, same second) once masked a reverted edit
ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "skills" / "brainres" / "scripts" / "brainlint.py"
spec = importlib.util.spec_from_file_location("brainlint", SCRIPT)
brainlint = importlib.util.module_from_spec(spec)
sys.modules["brainlint"] = brainlint  # dataclasses need the module registered
spec.loader.exec_module(brainlint)


def checks(text: str) -> set[str]:
    return {f.check for f in brainlint.lint(text).findings}


class GoldenExamples(unittest.TestCase):
    """Scores of the shipped examples are part of the README; changing them must be deliberate."""

    GOLDEN = {
        "examples/01-react-rerender/before.md": 50,
        "examples/01-react-rerender/after.md": 100,
        "examples/02-ko-cache/before.md": 41,
        "examples/02-ko-cache/after.md": 100,
        "examples/03-concept-index/before.md": 50,
        "examples/03-concept-index/after.md": 100,
        "examples/04-comparison-db/before.md": 78,
        "examples/04-comparison-db/after.md": 100,
        "examples/05-risk-flaky/before.md": 66,
        "examples/05-risk-flaky/after.md": 100,
        "examples/06-misconception-incognito/before.md": 71,
        "examples/06-misconception-incognito/after.md": 100,
    }

    def test_golden_scores(self):
        for path, expected in self.GOLDEN.items():
            with self.subTest(path=path):
                text = (ROOT / path).read_text(encoding="utf-8")
                self.assertEqual(brainlint.lint(text).score, expected)

    def test_language_detection(self):
        self.assertEqual(brainlint.lint((ROOT / "examples/02-ko-cache/after.md").read_text()).lang, "ko")
        self.assertEqual(brainlint.lint((ROOT / "examples/01-react-rerender/after.md").read_text()).lang, "en")


class Checks(unittest.TestCase):
    def test_clean_answer_scores_100(self):
        r = brainlint.lint("Use Postgres. It handles your 2 GB of data and joins well.\n\nNext: run `createdb app`.")
        self.assertEqual(r.score, 100, r.findings)

    def test_preamble_en_and_ko(self):
        self.assertIn("preamble", checks("Great question! The answer is 42."))
        self.assertIn("preamble", checks("좋은 질문입니다! 답은 42입니다."))
        self.assertIn("preamble", checks("That's an interesting question! The answer is 42."))
        self.assertNotIn("preamble", checks("The answer is 42."))

    def test_meta_talk(self):
        self.assertIn("meta_talk", checks("Let me break this down for you.\n\nThe answer is 42."))

    def test_outro(self):
        self.assertIn("outro", checks("The answer is 42.\n\nHope this helps!"))
        self.assertIn("outro", checks("답은 42입니다.\n\n궁금한 점이 있으시면 언제든지 물어보세요!"))
        self.assertNotIn("outro", checks("The answer is 42.\n\nNext: run the tests."))

    def test_list_overload_threshold(self):
        five = "\n".join(f"- item {i} here" for i in range(5))
        six = "\n".join(f"- item {i} here" for i in range(6))
        self.assertNotIn("list_overload", checks("Options:\n\n" + five))
        self.assertIn("list_overload", checks("Options:\n\n" + six))

    def test_bold_lead_ins(self):
        text = "Causes:\n\n" + "\n".join(f"- **Cause {i}**: detail text" for i in range(4))
        self.assertIn("bold_lead_ins", checks(text))

    def test_generic_heading(self):
        self.assertIn("generic_heading", checks("## Overview\n\nThe answer is 42."))
        self.assertIn("generic_heading", checks("## 개요\n\n답은 42입니다."))
        self.assertNotIn("generic_heading", checks("## Cause: stale cache\n\nThe cache is stale."))

    def test_heading_in_short_answer(self):
        self.assertIn("heading_short", checks("## Cause: stale cache\n\nThe cache is stale."))

    def test_hedging(self):
        text = "It might work. It may fail. Perhaps it is fine. Possibly not. " * 2
        self.assertIn("hedging", checks(text))

    def test_translationese_ko(self):
        text = "캐시에 대한 이해를 통해 성능에 대한 개선에 있어서 중요한 것입니다. 데이터에 대한 처리를 통해 확인합니다."
        self.assertIn("translationese", checks(text))

    def test_double_negation(self):
        self.assertIn("double_negation", checks("It is not uncommon for builds to fail."))

    def test_korean_long_sentence_in_eojeol(self):
        long_ko = " ".join(["캐시를"] * 21) + " 씁니다."
        self.assertIn("long_sentences", checks(long_ko))
        self.assertNotIn("long_sentences", checks(" ".join(["캐시를"] * 15) + " 씁니다."))

    def test_korean_average_limit(self):
        para = " ".join([" ".join(["데이터를"] * 13) + " 저장합니다."] * 3)
        self.assertIn("sentence_length", checks(para))

    def test_headings_are_not_sentences(self):
        r = brainlint.lint("## Cause: stale cache after deploy\n\nThe cache is stale. Clear it now.")
        self.assertEqual(r.sentences, 2)

    def test_tables_are_not_paragraphs(self):
        rows = "\n".join(f"| {i} | " + "word " * 20 + "|" for i in range(8))
        text = "Comparison:\n\n| # | Notes |\n|---|---|\n" + rows
        self.assertNotIn("wall_of_text", checks(text))
        self.assertNotIn("long_sentences", checks(text))

    def test_buried_answer(self):
        self.assertIn("buried_answer", checks("There are several factors to consider here. Use Redis."))
        self.assertIn("buried_answer", checks("It depends on your traffic. Use Redis."))
        self.assertIn("buried_answer", checks("Choosing a database is a crucial decision that depends on many factors. Use SQLite."))
        self.assertIn("buried_answer", checks("여러 가지 방법이 있습니다. 메모리 캐시를 쓰세요."))
        self.assertNotIn("buried_answer", checks("Use Redis. There are several reasons."))
        # a preamble is already penalized; don't double-count the same opening
        self.assertNotIn("buried_answer", checks("Great question! There are several factors."))

    def test_fragmented_reasoning(self):
        bullets = "\n".join(f"- Point {i} describes a separate fact about the cache layer and its timing behaviour under load"
                             for i in range(8))
        self.assertIn("fragmented_reasoning", checks("Notes:\n\n" + bullets))
        linked = bullets.replace("Point 3 describes", "Point 3 matters because it describes")
        self.assertNotIn("fragmented_reasoning", checks("Notes:\n\n" + linked))

    def test_numbered_steps_are_not_fragmented_reasoning(self):
        steps = "\n".join(f"{i}. Step {i} does one concrete thing to the database and the replica server here" for i in range(1, 8))
        self.assertNotIn("fragmented_reasoning", checks("Do this:\n\n" + steps))

    def test_nested_items_do_not_count_toward_the_parent_list(self):
        text = "Steps:\n\n1. One\n2. Two\n3. Three\n4. Four, with options:\n   - a\n   - b\n   - c"
        self.assertNotIn("list_overload", checks(text))

    def test_term_swap(self):
        self.assertIn("term_swap", checks("Open the folder. Then list the directory contents."))
        self.assertIn("term_swap", checks("Open the app. The application starts on port 3000."))
        self.assertIn("term_swap", checks("폴더를 여세요. 그 디렉터리 안에 파일이 있습니다."))
        self.assertNotIn("term_swap", checks("Open the application. This approach is fast."))

    def test_line_level_rules(self):
        cases = {
            "scope_ambiguity": ("All tests didn't pass on main.", "None of the tests passed on main."),
            "bare_this": ("This is slow. This means the cache is cold.", "This query is slow. The cache is cold."),
            "former_latter": ("Use Redis or Memcached; the former persists data.", "Use Redis; Redis persists data."),
            "minimizer": ("Simply run the migration.", "Run the migration."),
            "understanding_check": ("Run it twice. Does that make sense?", "Run it twice. Expect the second run to print OK."),
            "emoji": ("Done 🎉 Ship it 🚀", "Done. Ship it."),
            "boilerplate_warning": ("Use the flag. This is not financial advice.", "Use the flag. It deletes the cache, so back it up first."),
            "invented_confidence": ("It's the cache (~80% sure).", "It's probably the cache; check the hit rate in the logs."),
        }
        for check, (bad, good) in cases.items():
            with self.subTest(check=check):
                self.assertIn(check, checks(bad))
                self.assertNotIn(check, checks(good))

    def test_grounded_numbers_are_not_invented_confidence(self):
        for ok in ["The trial reported a 95% confidence interval of 2–4%.", "About 64% of runs will fail (1 − 0.98^50)."]:
            self.assertNotIn("invented_confidence", checks(ok))
        self.assertIn("invented_confidence", checks("원인은 StrictMode예요 (~90% 확신)."))

    def test_inline_code_is_quoted_not_said(self):
        self.assertNotIn("invented_confidence", checks("Never write `~80% sure` without a source."))
        self.assertNotIn("minimizer", checks("The linter flags `simply` and `just run`."))

    def test_check_marks_are_not_emoji(self):
        self.assertNotIn("emoji", checks("✓ Do this. ✗ Not that. ✓ Then this."))

    def test_html_comments_are_ignored(self):
        text = "The answer is 42. It is the product of 6 and 7."
        self.assertEqual(brainlint.lint("<!-- Q: what is it? -->\n\n" + text).sentences, brainlint.lint(text).sentences)

    def test_code_blocks_are_ignored(self):
        text = "Run this:\n\n```\n# Overview\nGreat question! hope this helps\n```\n\nIt prints 42."
        self.assertEqual(checks(text), set())


class QuestionAware(unittest.TestCase):
    def kinds(self):
        return brainlint.question_kind

    def test_question_kinds(self):
        k = brainlint.question_kind
        self.assertEqual(k("Is 0.1 + 0.2 === 0.3 true in JavaScript?"), "yesno")
        self.assertEqual(k("Incognito mode hides my browsing from my ISP, right?"), "yesno")
        self.assertEqual(k("Should I use REST or GraphQL?"), "choice")
        self.assertEqual(k("파이썬에서 리스트랑 튜플 중에 뭘 써야 해?"), "choice")
        self.assertEqual(k("이 설정 그대로 배포해도 돼?"), "yesno")
        self.assertIsNone(k("What is a race condition?"))
        self.assertIsNone(k("도커랑 가상머신 차이가 뭐야?"))

    def test_yesno_first_word(self):
        q = "Is 0.1 + 0.2 === 0.3 true in JavaScript?"
        self.assertIn("yesno_not_first", {f.check for f in brainlint.lint("JavaScript uses floats. So no.", q).findings})
        self.assertNotIn("yesno_not_first", {f.check for f in brainlint.lint("No, it is false.", q).findings})
        self.assertNotIn("yesno_not_first", {f.check for f in brainlint.lint("네, 배포해도 돼요.", "이 설정 그대로 배포해도 돼?").findings})

    def test_no_recommendation_closes_the_blind_spot(self):
        for ex, flagged in (("04-comparison-db", True), ("02-ko-cache", True)):
            q = (ROOT / f"examples/{ex}/question.md").read_text().strip()
            before = {f.check for f in brainlint.lint((ROOT / f"examples/{ex}/before.md").read_text(), q).findings}
            after = {f.check for f in brainlint.lint((ROOT / f"examples/{ex}/after.md").read_text(), q).findings}
            self.assertEqual("no_recommendation" in before, flagged, ex)
            self.assertNotIn("no_recommendation", after, ex)

    def test_without_question_scores_are_unchanged(self):
        text = (ROOT / "examples/04-comparison-db/before.md").read_text()
        self.assertEqual(brainlint.lint(text).score, 78)


class RewriteSafety(unittest.TestCase):
    def test_keeps_everything(self):
        orig = "Set `timeout=30` before 9 am. Do not restart the DB. See https://example.com/docs."
        new = "Do not restart the DB. Before 9 am, set `timeout=30` (https://example.com/docs)."
        self.assertEqual(brainlint.compare(orig, new), [])

    def test_detects_dropped_payload(self):
        orig = "Keep 3 replicas. Never run `rm -rf /data`. Docs: https://example.com/a."
        new = "Keep replicas. Run cleanup carefully."
        problems = " ".join(brainlint.compare(orig, new))
        self.assertIn("missing number: 3", problems)
        self.assertIn("missing code/command: rm -rf /data", problems)
        self.assertIn("missing URL", problems)
        self.assertIn("negations/limiters dropped", problems)

    def test_list_numbering_is_not_payload(self):
        self.assertEqual(brainlint.compare("1. Open it\n2. Close it", "- Open it\n- Close it"), [])

    def test_korean_negation_drop(self):
        self.assertTrue(brainlint.compare("서버를 재시작하지 않아요.", "서버를 재시작해요."))


class CLI(unittest.TestCase):
    def test_badge(self):
        out = subprocess.run([sys.executable, str(SCRIPT), "--badge", "-"], input="The answer is 42.",
                             capture_output=True, text=True, check=True).stdout.strip()
        self.assertTrue(out.startswith("[![Brain Score](https://img.shields.io/badge/Brain_Score-100%2F100_A-2ea44f)]"))

    def test_json_output_schema(self):
        out = subprocess.run(
            [sys.executable, str(SCRIPT), "--json", "-"],
            input="Great question! The answer is 42.",
            capture_output=True, text=True, check=True,
        ).stdout
        data = json.loads(out)
        self.assertEqual(set(data), {"score", "words", "sentences", "avg_sentence_words", "lang", "findings"})
        self.assertEqual(data["findings"][0]["check"], "preamble")


if __name__ == "__main__":
    unittest.main()
