#!/bin/bash
BASECMD=/usr/bin/wlr-randr
DISP="${1:-1}"
CMD=""
if [ "$2" = "on" ]; then
    CMD="${BASECMD} --output $DISP --on"
else
    CMD="${BASECMD} --output ${DISP} --off"
fi
$($CMD)
