#!/bin/bash
set -e

echo "Starting Elasticsearch using the official entrypoint..."
# Start the official Elasticsearch entrypoint in the background.
/usr/local/bin/docker-entrypoint.sh &

# Capture the PID of the Elasticsearch process.
ES_PID=$!

echo "Waiting for Elasticsearch to be available..."
until curl -s http://localhost:9200 > /dev/null; do
    sleep 2
done

echo "Elasticsearch is available. Running initialization script..."
python3 /init-elasticsearch.py

# Wait on the Elasticsearch process so the container remains running.
wait $ES_PID