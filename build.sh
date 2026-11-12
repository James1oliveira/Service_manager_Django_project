#!/usr/bin/env bash
# Render runs this every time the app is deployed
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py import_original_services
python manage.py seed_demo
