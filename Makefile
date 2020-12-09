SHELL := /bin/sh -e

.DEFAULT_GOAL := help


# Helper
.PHONY: help

help:  ## Display this auto-generated help message
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


# Installation
.PHONY: update sync

update:  ## Lock and install build dependencies
	pipenv update --dev
	pipenv clean

sync:  ## Install build dependencies from lock file
	pipenv sync --dev
	pipenv clean


# Development
.PHONY: clean format

clean:  ## Clean project from temp files / dirs
	rm -rf build dist
	find src -type d -name __pycache__ | xargs rm -rf

format:  ## Run auto-formatting linters
	pipenv run black src
	pipenv run isort src


# Deployment
.PHONY: lint test

lint:  ## Run python linters
	pipenv run black --check src
	pipenv run isort --check-only src
	pipenv run pydocstyle src
	pipenv run flake8 src
	pipenv run mypy src

test:  ## Run pytest with all tests
	pipenv run pytest src/tests

package:  ## Build project binary wheel distribution
	pipenv run python setup.py bdist_wheel
