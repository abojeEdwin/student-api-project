.PHONY: install run test
install:
	.venv/bin/pip install -r requirements.txt
run:
	flask run
test:
	.venv/bin/pytest -v