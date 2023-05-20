FROM python:3.11.3-alpine3.18

WORKDIR /app
EXPOSE 5002

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install mysqlclient

COPY ./blog /app/blog
COPY ./user /app/user
# COPY ./migrations /app/migrations
COPY manage.py .
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

ARG DJANGO_SUPERUSER_PASSWORD
ENV DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
