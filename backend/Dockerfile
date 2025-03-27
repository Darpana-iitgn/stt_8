FROM python:3.9-alpine

WORKDIR /app

# Install dependencies (no cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code (make sure entrypoint.sh uses LF line endings)
COPY . .

# Ensure the entrypoint script is executable
RUN chmod +x entrypoint.sh

EXPOSE 9567

ENTRYPOINT ["/entrypoint.sh"]