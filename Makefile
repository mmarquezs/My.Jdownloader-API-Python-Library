upload:
	rm -rf build dist myjdapi.egg-info
	python3 setup.py bdist_wheel --universal
	twine upload dist/*
