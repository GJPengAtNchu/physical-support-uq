import json
import unittest
from pathlib import Path

import pandas as pd


class ReleasedResultTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.confirmatory = json.loads(
            (cls.root / "results" / "adjudication.json").read_text(encoding="utf-8")
        )
        cls.posthoc = json.loads(
            (cls.root / "results" / "posthoc" / "posthoc_adjudication.json").read_text(
                encoding="utf-8"
            )
        )

    def test_retained_statuses(self):
        self.assertEqual(self.confirmatory["status"], "HOLD_NUMERICAL_EVIDENCE")
        self.assertEqual(self.posthoc["r0_status_unchanged"], "HOLD_NUMERICAL_EVIDENCE")
        self.assertEqual(self.posthoc["status"], "R0_HOLD_BUT_GEOMETRY_ROBUST")

    def test_only_frozen_failure_is_median_spread(self):
        failed = [item["check"] for item in self.confirmatory["checks"] if not item["pass"]]
        self.assertEqual(failed, ["Dictionary product-affinity median spread"])

    def test_primary_scaling_values(self):
        fit = self.confirmatory["scaling"]["jeffreys"]
        self.assertAlmostEqual(fit["slope"], 5.935475127180808, places=12)
        self.assertGreaterEqual(fit["r_squared"], 0.99999 - 1e-12)
        self.assertLessEqual(
            self.confirmatory["gate_collapse"]["maximum_vertical_spread"], 0.024331
        )

    def test_task_controls(self):
        task = self.confirmatory["task_controls"]
        self.assertLessEqual(task["maximum_equal_coefficient_residual"], 1e-12)
        self.assertLessEqual(task["maximum_contrast_formula_relative_error"], 1e-10)
        self.assertTrue(task["same_label_matching_everywhere"])

    def test_expected_row_counts(self):
        self.assertEqual(len(pd.read_csv(self.root / "results" / "confirmatory_batches.csv")), 768)
        self.assertEqual(len(pd.read_csv(self.root / "results" / "confirmatory_summary.csv")), 6)
        self.assertEqual(len(pd.read_csv(self.root / "results" / "gate_curves.csv")), 180)
        self.assertEqual(len(pd.read_csv(self.root / "results" / "task_controls.csv")), 450)
        self.assertEqual(
            len(pd.read_csv(self.root / "results" / "posthoc" / "stress_summary.csv")), 9
        )

    def test_released_figures_exist(self):
        names = [
            "manuscript_candidate_composite.pdf",
            "orientation_sixth_order.pdf",
            "task_invariance.pdf",
            "three_gate_pairwise_curves.pdf",
        ]
        for name in names:
            path = self.root / "results" / "figures" / name
            self.assertTrue(path.is_file() and path.stat().st_size > 0, name)


if __name__ == "__main__":
    unittest.main()
