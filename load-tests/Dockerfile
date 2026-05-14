FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY locustfile.py .

# Default: run headless for 30 seconds, 10 users, spawn rate 2
CMD ["locust", "--headless", "--run-time", "30s", "--users", "10", "--spawn-rate", "2", "--host", "https://hapi.fhir.org", "-f", "locustfile.py"]
