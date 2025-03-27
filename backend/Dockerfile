FROM python:3.9-alpine

WORKDIR /app

# Install dependencies without caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend files into /app
COPY . .

# Ensure entrypoint.sh is executable
RUN chmod +x entrypoint.sh

EXPOSE 9567

# Use the full path of the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]