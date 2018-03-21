.PHONY: venv test clean clean_all

venv:
	virtualenv venv
	venv/bin/pip install tox

test: venv
	venv/bin/tox

clean:
	rm -rf venv
	rm -rf .tox
	rm -rf python_testing_framework.egg-info
	rm -rf build
	rm -rf dist

clean_all: clean
	rm -rf .pytest_cache
	rm -rf .coverage
