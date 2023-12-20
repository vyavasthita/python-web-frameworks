FROM python:3.11.3-alpine3.18

WORKDIR /app
EXPOSE 5003

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install mysqlclient

COPY ./routers /app/routers
COPY *.py .

ARG API_HOST
ARG API_PORT
ARG RELOAD

ENV API_HOST=${API_HOST}
ENV API_PORT=${API_PORT}
ENV RELOAD=${RELOAD}

# CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5003", "--reload" ]

CMD [ "python", "main.py" ]
