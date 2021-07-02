SHELL := /bin/bash

activate-venv:
	pip install pip --upgrade
	pip install virtualenv
	virtualenv venv
	source venv/bin/activate

install-requirements:
	pip install pip --upgrade
	pip install -r requirements.txt

install-dev-requirements:
	pip install pip --upgrade
	pip install -r requirements.txt
	pip install -r requirements_dev.txt

flake8:
	flake8 autoforecast/

unit-tests:
	. ./test.env && python -m unittest discover autoforecast '*_test.py' -v

test-coverage:
	. ./.env && coverage run --source=autoforecast/ -m unittest discover autoforecast '*_test.py' -v
	coverage report -m
