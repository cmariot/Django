#!/bin/sh

# afficher la version utilisée de pip
pip --version

# installer la version de développement de path.py depuis son repo GitHub,
# dans un dossier qui doit s’appeler local_lib, placé dans le dossier de rendu.
# Si la librairie a déjà été installé dans ce dossier, l’installation doit alors l’écraser.
if [ -d ../local_lib ]; then
    rm -rf ../local_lib
fi
git clone https://github.com/jaraco/path ../local_lib

# Il doit écrire les logs d’installation de path.py dans un fichier ayant pour
# extension .log
pip install -e ../local_lib > ../local_lib/install.log
cat ../local_lib/install.log

# Si la librairie a été correctement installée, il doit finalement exécuter le petit pro- gramme que vous devez également créer.
if [ -d ../local_lib ]; then
    python3 my_program.py
fi
