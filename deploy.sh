#!/usr/bin/env bash
# DEPLOY SCRIPT FOR ELT PROJECT

# Stop on any error
set -e

# Load environment variables
source .env

DOCKER_USERNAME="engineerbee"    #-- My Docker Hub username
IMAGE_NAME="extractor"
TAG="latest"

echo "Building Docker image for extractor..."
docker build -t ${DOCKER_USERNAME}/${IMAGE_NAME}:${TAG} ./extract

echo "Logging into Docker Hub..."
docker login

echo "Pushing image to Docker Hub..."
docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${TAG}

echo "Bringing down old containers (if any)..."
docker-compose down

echo "Starting full ELT pipeline"
docker-compose up -d

echo "Deployment complete. Access your services at:
- PgAdmin: http://localhost:8080
- Metabase: http://localhost:3000
"