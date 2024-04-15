#!/bin/sh


# You must source this script to activate the virtualenv in your shell.
# source my_script.sh


ENV_NAME=django_venv


# Create a virtualenv based on the ENV_NAME variable.
python3 -m venv $ENV_NAME
echo "${ENV_NAME} virtual environment has been created."
echo

# Activate the virtualenv.
source $ENV_NAME/bin/activate
echo "The virtual environment is activated."
echo

# Install the requirements in the virtualenv.
echo "Installing the requirements..."
python3 -m pip install -r requirement.txt


echo

# Show the installed packages.
echo "Installed packages:"
python3 -m pip freeze
