#!/bin/bash
set -e

echo "Starting Elasticsearch using the official entrypoint..."
# Call the official entrypoint script in the background.
/usr/local/bin/docker-entrypoint.sh &

echo "Waiting for Elasticsearch to be available..."
until curl -s http://localhost:9200 > /dev/null; do
    sleep 2
done

echo "Elasticsearch is available. Running initialization script..."
python /init-elasticsearch.py

wait