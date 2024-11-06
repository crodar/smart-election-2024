FROM python:3.11-slim

# Install Chrome and dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    apt-transport-https \
    ca-certificates \
    curl \
    unzip \
    chromium \
    chromium-driver

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set Chrome options for running in container
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver
ENV PYTHONUNBUFFERED=1

# Add Chrome flags for running in container
ENV CHROME_FLAGS="--no-sandbox --headless --disable-gpu --disable-dev-shm-usage"

# Default command will run test-dem first, then start the main script
CMD ["sh", "-c", "python smart-election-2024.py --test-dem && python smart-election-2024.py"]
