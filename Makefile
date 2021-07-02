SHELL := /bin/bash

install-requirements:
	pip install pip --upgrade
	pip install -r requirements.txt

install-dev-requirements:
	pip install pip --upgrade
	pip install -r requirements.txt
	pip install -r requirements_dev.txt

flake8:
	flake8 autoforecast/

unit-test:
	python3 -m unittest discover src '*_test.py' -v

test-coverage:
	. ./.env && coverage run --source=autoforecast/ -m unittest discover autoforecast '*_test.py' -v
	coverage report -m
