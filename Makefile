all: stop clean pp run

stop:
	docker compose down

clean:
	docker container prune -f
	docker image prune -f

pp:
	. fastapi-practice/fastapivenv/bin/activate
	fastapi-practice/fastapivenv/bin/pip freeze > fastapi-practice/requirements.txt

run:
	docker compose up -d --build --remove-orphans