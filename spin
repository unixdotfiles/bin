#!/bin/sh

#Taken from FreeBSD mailing list. BSD licensed: Devin Teske

# Execute a command w/ spinner
spin()
{
	(
		if [ $# -gt 0 ]; then
			# Take commands from positional arguments
			( eval "$@" ) > /dev/null 2>&1
			echo $?
		else
			# Take commands from standard input
			( eval "$( cat )" ) > /dev/null 2>&1
			echo $?
		fi
	) | (
		n=1
		spin="/-\\|"
		DONE=

		printf " "
		while [ ! "$DONE" ]; do
			DONE=$( /bin/sh -c 'read -t 0 DONE; echo $DONE' )
			printf "\b%s" $( echo "$spin" | sed -e \
				"s/.\{0,$(( $n % ${#spin} ))\}\(.\).*/\1/" )
			n=$(( $n + 1 ))
		done
		printf "\b \b"
		exit $DONE
	)
}

spin
