#!/bin/bash

echo "Dossier courant avant le subshell: $(pwd)"

(
    cd /home/$USER/thinkspaced/cards || exit 1
    echo "Dans le subshell, dossier courant: $(pwd)"
    # Tes commandes ici :
    ls
    cp -r /home/$USER/thinkspaced/cards/routines.json /home/$USER/cards_backup
    cd /home/$USER/cards_backup
    git add .
    git commit -m "card backup"
    echo "Fichier temporaire créé dans le subshell"
)

echo "Dossier courant après le subshell: $(pwd)"
