import unittest

import numpy as np

from simulation.exact_mixture import (
    GaussianMixture,
    midpoint_pair_batch,
    product_affinity_deficit,
)


class ExactMixtureTests(unittest.TestCase):
    def setUp(self):
        self.first = GaussianMixture.bernoulli_gaussian(0.1, 0.0, 0.2, 0.5)

    def test_weights_and_covariances(self):
        self.assertAlmostEqual(float(self.first.weights.sum()), 1.0, places=14)
        self.assertEqual(len(self.first.weights), 32)
        eigenvalues = np.linalg.eigvalsh(self.first.covariances)
        self.assertGreaterEqual(float(eigenvalues.min()), 0.5 - 1e-12)

    def test_logpdf_is_finite(self):
        rng = np.random.default_rng(123)
        observations = self.first.sample(100, rng)
        self.assertTrue(np.isfinite(self.first.logpdf(observations)).all())

    def test_identical_pair_has_zero_diagnostics(self):
        result = midpoint_pair_batch(
            self.first, self.first, 2048, np.random.default_rng(321)
        )
        self.assertLess(result["jeffreys"], 1e-28)
        self.assertLess(result["affinity_deficit"], 1e-28)

    def test_product_affinity(self):
        deficit = 1e-6
        sample_size = 1_000_000
        expected = 1.0 - (1.0 - deficit) ** sample_size
        actual = float(product_affinity_deficit(deficit, sample_size))
        self.assertLess(abs(actual - expected), 2e-11)


if __name__ == "__main__":
    unittest.main()
