# Use lightweight Python base image
FROM python:3.11-slim-bookworm

# Set working directory inside the container
WORKDIR /app

# Copy dependency list into container
COPY requirements.txt .

# Install system dependencies and Python packages
RUN apt-get update && apt-get install -y \
    curl \
    cron \
    postgresql-client \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt

# Copy your ETL script
COPY extract.py .

# Set up cron job to run every day at midnight (00:00)
RUN echo "0 0 * * * python /app/extract.py >> /var/log/cron.log 2>&1" > /etc/cron.d/etl-cron

# Apply correct permissions and register cron job
RUN chmod 0644 /etc/cron.d/etl-cron && crontab /etc/cron.d/etl-cron

# Create log file
RUN touch /var/log/cron.log

# Start cron and keep container alive
CMD ["sh", "-c", "cron && tail -f /var/log/cron.log"]
