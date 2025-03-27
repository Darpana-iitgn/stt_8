  #!/bin/sh
  set -e

  echo "Starting Backend Service..."
  exec uvicorn main:app --host 0.0.0.0 --port 9567