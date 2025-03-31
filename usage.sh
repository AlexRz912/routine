#!/bin/bash

source $ROUTINE/utils/colors.sh

prompt_usage() {
    echo "
Usage:
  

  Available Commands:

  Usage        Prints this very same usage prompt


  	Process Execution:

  		-routines--add <name>	  add one command routine to a main queue that starts at a given hour
  		-routines--add-all	      adds all command routines to a main queue that starts at a given hour

  		-routines--stop <name>    remove one or more command routine from the routine queue that starts at a given hour 
  		-routines--stop-all	      stop all routines

  	Learning:

  		play <name>  Starts commands routine
		all	         Starts all command routine

  	Edition:

	        show <name>  Show routine
	        list	     List all routines
  		new          Create a new routine
  		update       Update an existing routine
  		remove       Remove an existing routine
  		add          Adds an action to an existing routine

		"

}

