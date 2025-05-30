FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy project
COPY . .

# Run the application
CMD ["sh", "-c", "export DJANGO_SETTINGS_MODULE=website.settings.settings_local && python manage.py migrate && mkdir -p /app/staticfiles && python manage.py collectstatic --noinput && gunicorn website.wsgi:application --bind 0.0.0.0:8000"]