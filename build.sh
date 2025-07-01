#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit  # exit on error

echo "Installing dependencies..."
pip install --no-cache-dir -r requirements.txt

echo "Running collectstatic..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate

echo "Build completed successfully!"
