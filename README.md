## Installation instructions:


**Installing this tool**

`cd /home/$USER && git clone git@github.com:AlexRz912/routine.git`

Create a cards folder in the home directory with routines.json file in it

`cd /home/$USER && mkdir cards && touch cards/routines.json`


**Dependencies**

If Python3 and pipx aren't installed:

```
sudo apt update && \
sudo apt install python3 pipx
```

Installing pipx should install numpy in the meantime which is necessary for spaced repetition interval calculation.
If you want to make sure numpy is installed:

`pipx install numpy`



**Environment variables and aliases**


Add these to your ~/.bashrc file (or zshrc or whatever custom shell scripting config)

*as non root user*

```
export ROUTINE=/home/$USER/routine
export CARDS=/home/$USER/cards
```

*as root user*

```
export ROUTINE=/root/routine
export CARDS=/root/cards
```

You could also want to create a parent directory for both cards and routine tool, it would look like this:

```
export ROUTINE=/home/$USER/custom_folder/routine
export CARDS=/home/$USER/custom_folder/cards
```

Add this to your ~/.aliases file

`alias rt='$ROUTINE/routine.sh'`

Now you should be good to call routine.sh anywhere in your terminal with alias rt : 

`rt add`
`rt play`
`rt all`
