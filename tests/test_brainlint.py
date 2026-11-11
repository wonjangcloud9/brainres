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

    def test_code_blocks_are_ignored(self):
        text = "Run this:\n\n```\n# Overview\nGreat question! hope this helps\n```\n\nIt prints 42."
        self.assertEqual(checks(text), set())


class CLI(unittest.TestCase):
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
