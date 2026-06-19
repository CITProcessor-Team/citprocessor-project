#!/bin/bash

LOGFILE="logfile"
ERROR_COUNT=0

echo "Monitoring $LOGFILE for 30 seconds..."

timeout 30 tail -f "$LOGFILE" | while IFS= read -r line
do
    if echo "$line" | grep -q "ERROR"
    then
        echo "ALERT: $line"
        ERROR_COUNT=$((ERROR_COUNT + 1))
    fi
done

echo
echo "Monitoring finished."
echo "Total errors found: $ERROR_COUNT"
