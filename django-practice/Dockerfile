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
# ARG SECRET_KEY
# ARG SQLITE_DB_URI
# ARG SQLALCHEMY_TRACK_MODIFICATIONS
# ARG MYSQL_USER
# ARG MYSQL_HOST
# ARG MYSQL_PORT

ENV DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}
# ENV SECRET_KEY=${SECRET_KEY}
# ENV SQLITE_DB_URI=${SQLITE_DB_URI}
# ENV SQLALCHEMY_TRACK_MODIFICATIONS=${SQLALCHEMY_TRACK_MODIFICATIONS}
# ENV MYSQL_USER=${MYSQL_USER}
# ENV MYSQL_HOST=${MYSQL_HOST}
# ENV MYSQL_PORT=${MYSQL_PORT}


ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
