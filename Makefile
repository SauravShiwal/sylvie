install:
	python setup.py sdist bdist_wheel
	python setup.py install --user
