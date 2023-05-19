#!/bin/sh


echo "Running migrations"

flask db upgrade

echo "Running flask server"
flask run
