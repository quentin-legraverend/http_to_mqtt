#!/bin/bash

# Prepare log files and start outputting logs to stdout
mkdir -p /app/logs
touch /app/logs/gunicorn.log
touch /app/logs/gunicorn-access.log
tail -n 0 -f /app/logs/gunicorn*.log &

exec gunicorn wsgi:app \
    --bind 0.0.0.0:5000 \
    --timeout 1200 \
    --log-level=info \
    --log-file=/app/logs/gunicorn.log \
    --access-logfile=/app/logs/gunicorn-access.log \
"$@"
