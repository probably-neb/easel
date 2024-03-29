.PHONY: clean virtualenv test docker dist dist-upload build-local

clean:
	find . -name '*.py[co]' -delete

virtualenv:
	virtualenv --prompt '|> easel <| ' env
	env/bin/pip install -r requirements.txt
	env/bin/pip install -r requirements-dev.txt
	env/bin/python setup.py develop
	@echo
	@echo "VirtualENV Setup Complete. Now run: source env/bin/activate"
	@echo

test:
	python -m pytest \
		-v \
		--cov=easel \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/


profile:
	python -m cProfile -o profile.txt -m easel.main -u
	python profile_stats.py

docker: clean
	docker build -t easel:latest .

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

dist-upload:
	twine upload dist/*
