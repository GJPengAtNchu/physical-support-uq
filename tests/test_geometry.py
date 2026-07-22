import unittest

import numpy as np

from simulation.geometry import (
    balanced_dictionary,
    compensated_rotation,
    profiled_task_residual,
    projective_matching,
    tetrahedron_vertices,
    wrong_support_pair,
)


class GeometryTests(unittest.TestCase):
    def test_tetrahedron_identities(self):
        vertices = tetrahedron_vertices()
        np.testing.assert_allclose(vertices.sum(axis=0), 0.0, atol=1e-14)
        gram = vertices @ vertices.T
        np.testing.assert_allclose(np.diag(gram), 1.0, atol=1e-14)
        np.testing.assert_allclose(
            gram - np.eye(4), -(np.ones((4, 4)) - np.eye(4)) / 3.0, atol=1e-14
        )

    def test_atoms_are_unit_norm(self):
        dictionary = balanced_dictionary(0.122, 0.31)
        np.testing.assert_allclose(
            np.linalg.norm(dictionary, axis=0), 1.0, atol=1e-14
        )

    def test_compensated_sum_is_fixed(self):
        vertices = tetrahedron_vertices()
        total = vertices[0] + vertices[1]
        for angle in np.linspace(0.0, 0.6, 13):
            np.testing.assert_allclose(
                compensated_rotation(angle) @ total, total, atol=1e-14
            )
            dictionary_zero = balanced_dictionary(0.1, 0.0)
            dictionary_angle = balanced_dictionary(0.1, angle)
            np.testing.assert_allclose(
                dictionary_zero[:, [0, 1]].sum(axis=1),
                dictionary_angle[:, [0, 1]].sum(axis=1),
                atol=1e-14,
            )

    def test_wrong_support_distance(self):
        s = 0.09
        beta = 1.2
        first, second = wrong_support_pair(s, beta)
        expected_squared = 2.0 * beta**2 * s**2 * 4.0 / 3.0
        self.assertAlmostEqual(np.linalg.norm(first - second) ** 2, expected_squared, places=13)

    def test_profiled_contrast_formula(self):
        for angle in (0.05, 0.2, 0.5):
            numerical, analytic = profiled_task_residual(0.1, angle, 1.0, 0.4)
            self.assertLess(abs(numerical - analytic) / analytic, 1e-12)
            equal, zero = profiled_task_residual(0.1, angle, 1.0, 0.0)
            self.assertEqual(zero, 0.0)
            self.assertLess(equal, 1e-13)

    def test_identity_projective_matching(self):
        matching, identity_gap, next_best_gap = projective_matching(0.1, 0.6)
        np.testing.assert_array_equal(matching, np.arange(4))
        self.assertAlmostEqual(identity_gap, 0.0, places=14)
        self.assertGreater(next_best_gap, 0.0)


if __name__ == "__main__":
    unittest.main()
