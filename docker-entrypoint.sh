#!/bin/bash
set -e

./wait-for-it.sh ${DB_HOST}:${DB_PORT} -t 600 -s -- echo 'database is alive'

# migrate database
flask db upgrade
