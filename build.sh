#!/bin/bash
set -e  # Exit on error

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Make sure the script is executable
chmod +x build.sh 