.PHONY: clean install run

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

python-packages:
	pip install -r requirements.txt

install: python-packages

run:
	python main.py
