#!/bin/sh


echo "Running migrations"

flask db upgrade

echo "Running flask server"
flask run --host 0.0.0.0 --port 5001
