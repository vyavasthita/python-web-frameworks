all: stop clean pp run

stop:
	docker compose down

clean:
	docker container prune -f
	docker image prune -f

pp:
	. flask-practice/flaskvenv/bin/activate
	flask-practice/flaskvenv/bin/pip freeze > flask-practice/requirements.txt

run:
	docker compose up -d --build --remove-orphans