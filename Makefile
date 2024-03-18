install:
	pipx install .

uninstall:
	pipx uninstall .

setup:
	python -m venv .venv
	source .venv/bin/activate
	pip install -e .
