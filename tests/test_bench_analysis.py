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
