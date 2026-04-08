setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

notebook:
	jupyter notebook

app:
	python -m app.app

demo:
	python examples/run_demo.py

validate:
	python examples/validate_bootcamp.py

test:
	pytest -q

docker-up:
	docker compose up --build
