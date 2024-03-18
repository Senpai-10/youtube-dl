install:
	pipx install -e .

uninstall:
	pipx uninstall .

setup:
	python -m venv .venv
	source .venv/bin/activate
	pip install -e .
