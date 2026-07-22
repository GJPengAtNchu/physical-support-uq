.PHONY: test verify-results reproduce-confirmatory reproduce-posthoc reports manifest

export MPLCONFIGDIR := $(CURDIR)/.cache/matplotlib

test:
	python -m unittest discover -s tests -v

verify-results:
	python -m unittest tests.test_released_results -v

reproduce-confirmatory:
	mkdir -p reproduced/results
	python -m simulation.run_pilot --config config.json --output reproduced/results; code=$$?; test $$code -eq 0 -o $$code -eq 2

reproduce-posthoc:
	mkdir -p reproduced/results/posthoc
	python -m simulation.run_posthoc --config config.json --output reproduced/results/posthoc

reports:
	python -m simulation.build_deliverable

manifest:
	python -m simulation.build_manifest
