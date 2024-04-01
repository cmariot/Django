#!/bin/sh

ENV_NAME=django_venv

# Créer un virtualenv sous python3 nommé django_venv.
python3 -m venv $ENV_NAME

# Activer le virtualenv.
source $ENV_NAME/bin/activate

# Installer le fichier requirement.txt que vous avez créé dans ce VirtualEnv.
pip install -r requirement.txt

# En quittant, le virtualenv doit être activé.
echo "Le nom du virtualenv est :"
echo $VIRTUAL_ENV
