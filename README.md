# Three-gate theorem-native simulation

Reproducibility package for the numerical illustration in:

> Guan-Ju Peng, *Honest Physical-Support Inference after Latent Dictionary
> Learning: Collision Singularities and Minimax Resolution*.

The paper and its brief summary are respectively available at 
https://arxiv.org/abs/2607.16813
and 
https://gist.science/paper/2607.16813.

The code evaluates the three least-favorable comparisons in the paper's
low-dimensional balanced hard core. It reproduces the sixth-order orientation
information, the approximate collapse against `N s^6`, and the
equal-coefficient task invariance / amplitude-contrast control.

## Scientific scope

This package illustrates information geometry. It does **not** implement or
validate the full robust-moment confidence correspondence, conditional
coverage, a certified global optimizer, a scalable solver, high-dimensional
performance, or localization/DOA transfer.

The confirmatory protocol was frozen before its seeds were used. Its retained
status is `HOLD_NUMERICAL_EVIDENCE` because one secondary median-collapse
threshold narrowly missed (`0.0166976` versus `0.015`). The maximum-spread,
sixth-order, quadrature, task-invariance, and projective-matching checks passed.
The separately labeled post-hoc diagnostics cannot change that status; they
show that the geometry is robust.

## Released numerical results

- Jeffreys `s` exponent: `5.9355` (paired-bootstrap 95% CI
  `[5.9249, 5.9468]`, `R^2 = 0.99999`).
- Order-14 all-scale Gauss-Hermite exponent: `5.9342`.
- Maximum cross-`s` product-affinity spread: `0.0243`.
- Equal-coefficient test residual: `6.82e-16`.
- Post-hoc `h` exponent: `1.9431`.
- Nine-cell `(p, nu)` stress range: `5.7592` to `5.9604`.

See `results/THREE_GATE_SIMULATION_ADJUDICATION.md` for the complete
author-facing interpretation and `FROZEN_PROTOCOL.md` for the confirmatory
design.

## Repository layout

```text
simulation/                 exact mixture, geometry, runners, figures/reports
tests/                      unit and released-result integrity tests
results/                    raw CSV/JSON outputs and publication figures
output/pdf/                 human-readable pilot and adjudication reports
config.json                 frozen grids, seeds, and thresholds
FROZEN_PROTOCOL.md          confirmatory protocol
POSTHOC_DIAGNOSTIC_PROTOCOL.md
requirements.txt            exact tested Python environment
environment.yml             equivalent Conda environment
SHA256SUMS                  deterministic package manifest
```

## Quick verification

Python 3.12 is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
make test
make verify-results
sha256sum -c SHA256SUMS
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` and run the
Python commands directly if `make` is unavailable:

```powershell
python -m unittest discover -s tests -v
python -m unittest tests.test_released_results -v
```

## Full reproduction

The confirmatory run uses `6 x 128 x 8192 = 6,291,456` midpoint-mixture draws,
plus deterministic quadrature. It is intentionally much slower than the unit
tests. Results are written under `reproduced/` so the released outputs remain
untouched.

```bash
make reproduce-confirmatory
make reproduce-posthoc
```

`reproduce-confirmatory` accepts process exit code 2 because the frozen
adjudication is `HOLD_NUMERICAL_EVIDENCE`; this is the expected retained result,
not a runtime failure.

To regenerate the reports and manuscript-candidate figure from the released
results:

```bash
python -m simulation.build_deliverable
python -m simulation.build_manifest
```

## Reproducibility notes

- Every collision scale uses the same seed and paired random blocks.
- The one-observation training law is evaluated as an exact 32-component
  zero-mean Gaussian mixture.
- Near collision, nonnegative midpoint identities avoid signed-KL
  cancellation.
- Product affinity is raised to the `N`th power analytically.
- Tensor Gauss-Hermite quadrature provides an independent deterministic check.
- Post-hoc outputs are stored under `results/posthoc/` and remain explicitly
  separated from confirmatory R0.

## License

This project is released under the MIT License. See `LICENSE` for details.

Before making a new public release, review `RELEASE_CHECKLIST.md`.
