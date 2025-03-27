#!/bin/bash
set -e

echo "Starting Elasticsearch using the official entrypoint..."
# Start the official Elasticsearch entrypoint script in the background.
exec /usr/local/bin/docker-entrypoint.sh &

echo "Waiting for Elasticsearch to be available..."
until curl -s http://localhost:9200 > /dev/null; do
    sleep 2
done

echo "Elasticsearch is available. Running initialization script..."
python3 /init-elasticsearch.py

# Wait on the Elasticsearch process so the container remains running.
wait