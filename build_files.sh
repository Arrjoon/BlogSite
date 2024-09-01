#!/bin/bash

# Print commands and exit on error
set -xe

# Install dependencies
python3 -m pip install -r requirements.txt

# Run Django collectstatic
python3 manage.py collectstatic --noinput
