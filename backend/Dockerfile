FROM python:3.9-alpine

WORKDIR /app

# Install dependencies (without cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend files into /app
COPY . .

# Ensure the entrypoint script is executable
RUN chmod +x entrypoint.sh

EXPOSE 9567

# Use full path since WORKDIR is /app
ENTRYPOINT ["/app/entrypoint.sh"]