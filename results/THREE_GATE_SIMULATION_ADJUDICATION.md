# Three-gate simulation: combined adjudication

## Bottom line

The theorem-native simulation **works scientifically**, but the frozen R0 status remains `HOLD_NUMERICAL_EVIDENCE`. One secondary median-collapse threshold missed narrowly; it must not be relabeled as a confirmatory pass. Independent post-hoc checks show that the underlying information geometry is robust enough to justify a modest numerical illustration in the manuscript.

| Item | Result |
|---|---:|
| Jeffreys s exponent | 5.9355 |
| Paired bootstrap 95% CI | [5.9249, 5.9468] |
| R-squared | 0.999990 |
| Dictionary maximum cross-s spread | 0.0243 |
| Frozen median-spread criterion | 0.0167 vs 0.015 (FAIL) |
| Equal-coefficient residual | 6.824e-16 |
| h exponent (post-hoc) | 1.9431 |
| Stress-grid s exponents (post-hoc) | 5.7592 to 5.9604 |
| All-s order-14 quadrature exponent | 5.9342 |

## Why R0 is HOLD rather than NO-GO

The only failed frozen check was `Dictionary product-affinity median spread`: `0.016698` against `<= 0.015`. The maximum-spread criterion passed, all sixth-order and numerical-integrity criteria passed, and deterministic quadrature reproduced the exponent. The near-miss therefore does not indicate a failed phenomenon; it records that the finite-s curves retain a small higher-order drift.

## Manuscript recommendation

Add one compact three-panel figure and roughly two short paragraphs, provided an equal amount of text is compressed elsewhere to preserve the SIMODS length limit. Put the task-invariance and p/nu stress diagnostics in the supplement.

Permitted claim:

> In the q=4 Bernoulli-Gaussian hard core, exact-mixture calculations exhibit the > predicted sixth-order orientation information and an approximate product-experiment > collapse against Ns^6; equal coefficients leave the test mean invariant, whereas > amplitude contrast opens the prescribed task secant.

Do not claim validation of the full robust moment correspondence, conditional coverage, a scalable algorithm, or localization transfer.

## Formal status separation

- Confirmatory R0: `HOLD_NUMERICAL_EVIDENCE`.
- Post-hoc interpretation: `R0_HOLD_BUT_GEOMETRY_ROBUST`.
- Integration recommendation: `ADD_THEOREM_NATIVE_ILLUSTRATION_WITH_SCOPE_LIMITS`.
