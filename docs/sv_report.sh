#!/bin/bash

# Use current directory if no argument is supplied
dir=${1:-.}

printf "%-20s %-10s %-10s %-10s\n" "MODULE" "INPUTS" "OUTPUTS" "LINES"
printf "%-20s %-10s %-10s %-10s\n" "------" "------" "-------" "-----"

find "$dir" -type f -name "*.sv" | while read -r file
do
    # Extract first module name
    module=$(grep -Pom1 '^module\s+\K\w+' "$file")

    # Handle files without module declarations
    [ -z "$module" ] && module="N/A"

    # Count input/output keywords
    inputs=$(grep -c '\binput\b' "$file")
    outputs=$(grep -c '\boutput\b' "$file")

    # Count lines
    lines=$(wc -l < "$file")

    printf "%-20s %-10d %-10d %-10d\n" \
        "$module" "$inputs" "$outputs" "$lines"
done
