all: clean stop pp

clean:
	echo "Cleaning"

stop:
	echo "Stopping Containers"
	docker compose down

pp:
	echo "Activating virtual environment"
	source flask-practice/flaskvenv/bin/activate

	echo "Updating requirements.txt"
	pip freeze > flask-practice/requirements.txt

	echo "Deactivating virtual environment"
	source deactivate

run:
	echo "Running Containers"
	docker compose up --build --remove-orphans