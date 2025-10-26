#!/bin/bash

# Build the Docker image
echo "Building Docker image..."
docker build -t charger-status .

# Stop and remove existing container if it exists
echo "Stopping existing container..."
docker stop charger-status 2>/dev/null || true
docker rm charger-status 2>/dev/null || true

# Run container with restart policy
echo "Starting container with restart policy..."
docker run -d \
  -p 8000:8000 \
  --name charger-status \
  --restart unless-stopped \
  --health-cmd="curl -f http://localhost:8000/ || exit 1" \
  --health-interval=30s \
  --health-timeout=10s \
  --health-retries=3 \
  charger-status

echo "Container started successfully!"
echo "Application is running on http://localhost:8000"
echo "To check status: docker ps"
echo "To view logs: docker logs -f charger-status"