#!/bin/sh


# You must source this script to activate the virtualenv in your shell.
# source my_script.sh


ENV_NAME=django_venv
BLUE='\033[0;34m'
RESET='\033[0m'


# Create a virtualenv based on the ENV_NAME variable.
python3 -m venv $ENV_NAME
echo "${BLUE}${ENV_NAME} virtual environment has been created.${RESET}"
echo

# Activate the virtualenv.
source $ENV_NAME/bin/activate
echo "${BLUE}The virtual environment is activated.${RESET}"
echo

# Install the requirements in the virtualenv.
echo "${BLUE}Installing the requirements...${RESET}"
python3 -m pip install -r requirement.txt


echo

# Show the installed packages.
echo "${BLUE}Installed packages:${RESET}"
python3 -m pip freeze
