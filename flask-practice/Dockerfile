FROM python:3.11.3-alpine3.18

WORKDIR /app
EXPOSE 5001

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./blog /app/blog
COPY ./migrations /app/migrations
COPY wsgi.py .
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

ARG FLASK_APP
ARG SQLITE_DB_URI
ARG SQLALCHEMY_TRACK_MODIFICATIONS

ENV FLASK_APP=${FLASK_APP}
ENV SQLITE_DB_URI=${SQLITE_DB_URI}
ENV SQLALCHEMY_TRACK_MODIFICATIONS=${SQLALCHEMY_TRACK_MODIFICATIONS}

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
