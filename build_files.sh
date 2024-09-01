#!/bin/bash

# Print commands and exit on error
set -xe

# Install dependencies
python3 -m pip install -r requirements.txt

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# Run Django collectstatic
python3 manage.py collectstatic --noinput

