all: stop clean pp run

stop:
	echo "Stopping Containers"
	docker compose down

clean:
	echo "Cleaning"
	docker container prune -f
	docker image prune -f

pp:
	echo "Activating virtual environment"
	. flask-practice/flaskvenv/bin/activate

	echo "Updating requirements.txt"
	flask-practice/flaskvenv/bin/pip freeze > flask-practice/requirements.txt

	echo "Deactivating virtual environment"
	# . flask-practice/flaskvenv/bin/deactivate

run:
	echo "Running Containers"
	docker compose up -d --build --remove-orphans