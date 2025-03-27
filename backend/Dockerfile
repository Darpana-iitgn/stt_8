FROM python:3.9-alpine

WORKDIR /app

# Install dependencies without caching to reduce image size
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend source files
COPY . .

# Ensure the entrypoint script is executable
RUN chmod +x entrypoint.sh

EXPOSE 9567

ENTRYPOINT ["/entrypoint.sh"]