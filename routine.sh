#!/bin/bash
source ./usage.sh

[[ $1 == usage ]] && prompt_usage && exit 1
[[ $1 == add ]] && python3 add_routine.py && exit 1
[[ $1 == play ]] && python3 play_routine.py && exit 1