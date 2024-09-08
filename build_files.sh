#!/bin/bash

echo "BUILD START"

# Step 1: Install required Python packages
python3.9 -m pip install -r requirements.txt

# Step 2: Collect static files and clear old ones
python3.9 manage.py collectstatic --noinput --clear

# Step 3: Create the output directory if it doesn't exist
mkdir -p staticfiles_build

# Step 4: Move the collected static files to the output directory
mv static/* staticfiles_build/

echo "BUILD END"
