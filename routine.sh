#!/bin/bash

source $ROUTINE/usage.sh

[[ -z $1 || $1 == usage ]] && prompt_usage && exit 1
[[ $1 == add ]] && python3 $ROUTINE/add_routine.py && exit 1
[[ $1 == play ]] && python3 $ROUTINE/play_routine.py && exit 1

[[ $1 == all ]] && python3 $ROUTINE/update_retention_rate.py && python3 $ROUTINE/play_all_routines.py && exit 1

[[ $1 == update_retention_rate ]] && python3 $ROUTINE/update_retention_rate.py && exit 1
