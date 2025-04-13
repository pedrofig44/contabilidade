#!/bin/bash

# Stop any existing containers
docker-compose down

# Build and start the containers
docker-compose up --build -d

# Apply migrations
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

echo "DUARAMA website is now running at http://localhost:8000"
echo "To view logs: docker-compose logs -f"
echo "To stop: docker-compose down"