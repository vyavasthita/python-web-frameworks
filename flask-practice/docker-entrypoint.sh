#!/bin/sh

echo "Running db init"
# flask db stamp head
flask db init

echo "Running db migrate"
flask db migrate

echo "Running db upgrade"
flask db upgrade

echo "Running flask server"
flask run --host 0.0.0.0 --port 5001
