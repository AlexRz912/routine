#!/bin/bash
source $ROUTINE/usage.sh

[[ $1 == usage ]] && prompt_usage && exit 1
[[ $1 == add ]] && python3 $ROUTINE/add_routine.py && exit 1
[[ $1 == play ]] && python3 $ROUTINE/play_routine.py && exit 1