PYTHON=python
PIP=$(PYTHON) -m pip

install:
	$(PIP) install -e .[test]

uninstall:
	$(PIP) uninstall crunch-encrypt

test:
	$(PYTHON) -m pytest -vv tests/

test-with-coverage:
	$(PYTHON) -m pytest --cov=crunch_encrypt --cov-report=html -vv tests/

benchmark:
	$(PYTHON) -m pytest -vv benchmarks/

build:
	rm -rf build *.egg-info dist
	python setup.py sdist bdist_wheel

.PHONY: install uninstall test test-with-coverage benchmark build
