FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot files
COPY bot_advanced.py .
COPY config.py .
# COPY .env .

# Run bot
CMD ["python", "bot_advanced.py"]
