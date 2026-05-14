FROM python:3.11-slim

WORKDIR /app

# System dependencies for Chromium (headless)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libnss3 libnspr4 libatk-bridge2.0-0 libdrm2 libxkbcommon0 \
    libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 \
    libpango-1.0-0 libcairo2 libasound2 libatspi2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install only Chromium for now
RUN playwright install chromium --with-deps

COPY tests/ tests/
CMD ["pytest", "tests/", "--browser=chromium", "--html=report.html", "--self-contained-html"]
