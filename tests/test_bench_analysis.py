"""The benchmark analysis must find a planted effect, stay quiet on null data, and apply exclusions."""
from __future__ import annotations

import importlib.util
import random
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("analyze", ROOT / "bench/analyze.py")
analyze = importlib.util.module_from_spec(spec)
sys.modules["analyze"] = analyze
spec.loader.exec_module(analyze)


def participant(rng, speedup=1.0, acc_base=0.85, acc_bres=0.85, attention=True, minutes=8, pid=None):
    trials = []
    for i in range(8):
        v = "brainres" if i % 2 else "baseline"
        base_ms = rng.lognormvariate(9.6, 0.35)  # ≈ 15 s
        ms = base_ms * (speedup if v == "brainres" else 1.0)
        acc = acc_bres if v == "brainres" else acc_base
        trials.append({"id": f"{i:02d}", "version": v,
                       "q1": {"correct": rng.random() < 0.95, "ms": int(ms), "conf": rng.randint(3, 5)},
                       "q2": {"correct": rng.random() < acc, "ms": 9000, "conf": rng.randint(2, 5)}})
    return {"id": pid or f"p{rng.random():.8f}", "lang": "en", "fluent": True, "attention": attention,
            "started": "2026-11-12T10:00:00Z", "finished": f"2026-11-12T10:{minutes:02d}:00Z",
            "trials": trials, "preference": [{"id": "01", "choice": "brainres"}]}


CONTENTS = {"c1": "causal", "c2": "causal", "c3": "causal", "c4": "causal",
            "p1": "parallel", "p2": "parallel", "p3": "parallel", "p4": "parallel"}


def participant2(rng, causal_gap=0.15, base=0.85, bullet_speedup=0.85):
    trials = []
    ids = sorted(CONTENTS)
    flip = rng.random() < 0.5
    for i, iid in enumerate(ids):
        fmt = "bullets" if (i % 2 == 0) ^ flip else "prose"
        c = CONTENTS[iid]
        acc = base - (causal_gap if (c == "causal" and fmt == "bullets") else 0)
        ms = rng.lognormvariate(9.6, 0.35) * (bullet_speedup if (c == "parallel" and fmt == "bullets") else 1)
        trials.append({"id": iid, "version": fmt, "q1": {"correct": rng.random() < 0.95, "ms": int(ms), "conf": 4},
                       "q2": {"correct": rng.random() < acc, "ms": 9000, "conf": 4}})
    return {"id": f"s{rng.random():.8f}", "study": 2, "lang": "en", "fluent": True, "attention": True,
            "started": "2026-11-12T10:00:00Z", "finished": "2026-11-12T10:09:00Z", "trials": trials, "preference": []}


class Study2(unittest.TestCase):
    def power(self, n, gap, sims=200, seed=1):
        rng = random.Random(seed)
        return sum(analyze.analyze_study2([participant2(rng, causal_gap=gap) for _ in range(n)], CONTENTS)
                   .get("H1", {}).get("supported", False) for _ in range(sims)) / sims

    def test_detects_large_interaction(self):
        rng = random.Random(2)
        r = analyze.analyze_study2([participant2(rng, causal_gap=0.25) for _ in range(150)], CONTENTS)
        self.assertTrue(r["H1"]["supported"], r["H1"])

    def test_null_interaction_rarely_supported(self):
        self.assertLess(self.power(80, 0.0, sims=100), 0.1)

    def test_studies_do_not_mix(self):
        rng = random.Random(9)
        s2 = [participant2(rng) for _ in range(20)]
        self.assertEqual(analyze.analyze(s2)["analyzed"], 0)  # study 1 analysis ignores study 2 submissions
        self.assertEqual(analyze.analyze_study2([participant(rng) for _ in range(5)], CONTENTS)["submitted"], 0)

    def test_item_contents_match_protocol(self):
        c = analyze.study2_contents()
        self.assertEqual(sorted(c.values()).count("causal"), 4)
        self.assertEqual(sorted(c.values()).count("parallel"), 4)


class Analysis(unittest.TestCase):
    def test_detects_planted_speedup_and_non_inferiority(self):
        rng = random.Random(7)
        r = analyze.analyze([participant(rng, speedup=0.75) for _ in range(60)])
        self.assertTrue(r["H1"]["supported"], r["H1"])
        self.assertLess(r["H1"]["time_ratio"], 0.9)
        self.assertTrue(r["claim_allowed"])

    def test_null_effect_does_not_allow_claim(self):
        rng = random.Random(11)
        r = analyze.analyze([participant(rng, speedup=1.0) for _ in range(60)])
        self.assertFalse(r["H1"]["supported"], r["H1"])
        self.assertFalse(r["claim_allowed"])

    def test_accuracy_drop_blocks_claim_even_if_faster(self):
        rng = random.Random(3)
        r = analyze.analyze([participant(rng, speedup=0.7, acc_base=0.9, acc_bres=0.6) for _ in range(60)])
        self.assertFalse(r["H2"]["non_inferior"], r["H2"])
        self.assertFalse(r["claim_allowed"])

    def test_preregistered_exclusions(self):
        rng = random.Random(5)
        subs = [participant(rng), participant(rng, attention=False), participant(rng, minutes=2), participant(rng, pid="dup"),
                participant(rng, pid="dup")]
        r = analyze.analyze(subs)
        self.assertEqual(r["analyzed"], 2)
        self.assertEqual(r["excluded"], {"attention check": 1, "under 3 minutes": 1, "duplicate id": 1})

    def test_wilcoxon_matches_known_value(self):
        # all 8 differences positive → exact two-sided p = 2 / 2^8
        self.assertAlmostEqual(analyze.wilcoxon([1, 2, 3, 4, 5, 6, 7, 8]), 2 / 256)


if __name__ == "__main__":
    unittest.main()
