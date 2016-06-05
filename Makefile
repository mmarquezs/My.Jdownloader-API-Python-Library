upload:
	rm -rf build dist myjdapi.egg-info
	python setup.py bdist_wheel --universal
	twine upload dist/*
