all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	virtualenv --python=python3 venv && venv/bin/pip install ../hseling_lib_fake_corpora_interface && venv/bin/pip install .

run: venv
	FLASK_APP=hseling_api_fake_corpora_interface venv/bin/flask run

test: venv
	HSELING_API_FAKE_CORPORA_INTERFACE_SETTINGS=../settings.cfg venv/bin/python -m unittest discover -s tests

sdist: venv test
	venv/bin/python setup.py sdist
