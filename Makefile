install:
	python -m pip install --upgrade pip
		pip install -r requirements.txt

format:	
	black *.ipynb

lint:
	ruff check *.ipynb

#  container-lint:
#  	docker run --rm -i hadolint/hadolint < Dockerfile

test3:
	 python -m pytest -vv --nbval -cov=myapp -cov=main *.ipynb

		
all: install format lint test1  test2 test3 
