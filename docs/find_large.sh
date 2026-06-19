#!/bin/bash

if [ $# -ne 2 ]
then
    echo "Usage: $0 <directory> <size_in_KB>"
    exit 1
fi

echo "Filename | Size(KB) | Modified Date"
echo "------------------------------------"

find "$1" -type f -size +"${2}"k | while read file
do
    stat --format="%s %y %n" "$file"
done | awk '{
    size_kb = $1 / 1024
    printf "%-40s %-10.2f %s %s\n", $4, size_kb, $2, $3
}' | sort -k2 -n
