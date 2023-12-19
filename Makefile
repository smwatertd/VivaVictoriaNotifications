dev:
	poetry run python src/main.py

test:
	poetry run pytest tests

consume:
	poetry run python src/consume.py
