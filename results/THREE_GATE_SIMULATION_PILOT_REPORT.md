# Three-gate theorem-native simulation pilot

**Status: `HOLD_NUMERICAL_EVIDENCE`**

## Executive conclusion

The pilot did not clear every frozen requirement. Failed checks: Dictionary product-affinity median spread.

## Primary estimates

- Jeffreys log-log slope: `5.9355` (paired bootstrap 95% CI `5.9249` to `5.9468`).
- Affinity-deficit log-log slope: `5.9355` (paired bootstrap 95% CI `5.9249` to `5.9464`).
- Dictionary product-affinity maximum transition-band spread: `0.02433`.
- Maximum equal-coefficient residual: `6.824e-16`.
- Gauss-Hermite cross-check: `PASS`.

## Frozen checks

| Check | Value | Requirement | Result |
|---|---:|---:|:---:|
| Jeffreys log-log slope | 5.93548 | inside [5.8, 6.2] | PASS |
| Jeffreys R-squared | 0.99999 | >= 0.995 | PASS |
| Jeffreys/s^6 max-min ratio | 1.06855 | <= 1.15 | PASS |
| Jeffreys maximum relative CI half-width | 0.0356856 | <= 0.05 | PASS |
| Jeffreys half-sample slope difference | 0.0076656 | <= 0.15 | PASS |
| Affinity deficit log-log slope | 5.93547 | inside [5.8, 6.2] | PASS |
| Affinity deficit R-squared | 0.99999 | >= 0.995 | PASS |
| Affinity deficit/s^6 max-min ratio | 1.06855 | <= 1.15 | PASS |
| Affinity deficit maximum relative CI half-width | 0.0356856 | <= 0.05 | PASS |
| Affinity deficit half-sample slope difference | 0.00766631 | <= 0.15 | PASS |
| Jeffreys / (8 affinity deficit) | [1, 1] | inside [0.95, 1.05] | PASS |
| Dictionary product-affinity maximum spread | 0.0243307 | <= 0.04 | PASS |
| Dictionary product-affinity median spread | 0.0166976 | <= 0.015 | FAIL |
| Equal-coefficient test residual | 6.82354e-16 | <= 1e-12 | PASS |
| Two-atom contrast formula relative error | 7.01189e-15 | <= 1e-10 | PASS |
| Same-label projective matching | PASS | is PASS | PASS |
| Gauss-Hermite cross-check | PASS | is PASS | PASS |

## Stress grid

The stress grid was run only after the confirmatory evidence was available. It was not run because the confirmatory gate did not pass.

## Interpretation boundary

All three gate panels use product affinity. For the parent and support pairs it is analytic under equal-covariance Gaussians; for the dictionary pair it is estimated from the one-observation 32-component mixture and raised to the Nth power exactly. The CSV also records exact parent/support Bayes errors and affinity-based dictionary Bayes-error bounds. None of these quantities is the output of the full robust moment correspondence. The simulation therefore demonstrates the information geometry only.

## Reproducibility

- Protocol: `THREE-GATE-SIM-PILOT-R0`.
- Confirmatory observations per collision scale: `1,048,576`.
- Confirmatory seed: `2026072201`.
- Machine-readable results and all figure source data are included beside this report.
