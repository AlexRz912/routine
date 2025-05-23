#!/bin/bash

(
    cd /home/$USER/thinkspaced/cards || exit 1
    cp -r /home/$USER/thinkspaced/cards/routines.json $BACKUP
    cd $BACKUP
    git add .
    git commit -m "card backup"
    git push
)

