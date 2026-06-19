#!/usr/bin/env bash

INSTALLED=0

for tool in git python3 verilator yosys make
do
    if command -v "$tool" > /dev/null 2>&1; then
        echo "INSTALLED: $tool"
        INSTALLED=$((INSTALLED + 1))
    else
        echo "MISSING: $tool"
    fi
done

echo "$INSTALLED/5 tools installed."

