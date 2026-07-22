# Public-release checklist

- [x] Choose and add a software `LICENSE` (MIT).
- [x] Set the final GitHub repository name and add its URL to `CITATION.cff`.
- Confirm that the manuscript title and arXiv/journal citation are current.
- [x] Run `make test` and `make verify-results`.
- [x] Run `python -m simulation.build_manifest` and verify
  `sha256sum -c SHA256SUMS`.
- [x] Confirm that no secret, absolute workspace path, manuscript source, review
  draft, or temporary file is present.
- Tag the exact public release used by the paper.
