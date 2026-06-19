#!/bin/bash

set -e

TOOLS=(
    "git"
    "curl"
    "wget"
    "make"
    "gcc"
    "python3"
    "verilator"
)

declare -a RESULTS

echo "========================================"
echo "   CIT Tool Installation and Verification"
echo "========================================"
echo

sudo apt-get update

install_tool() {
    local tool="$1"

    echo "Processing: $tool"

    if command -v "$tool" >/dev/null 2>&1; then
        echo "  Already installed."
    else
        echo "  Installing..."
        sudo apt-get install -y "$tool"
    fi

    if command -v "$tool" >/dev/null 2>&1; then

        case "$tool" in
            python3)
                VERSION=$(python3 --version 2>&1 | head -1)
                ;;
            gcc)
                VERSION=$(gcc --version 2>&1 | head -1)
                ;;
            make)
                VERSION=$(make --version 2>&1 | head -1)
                ;;
            git)
                VERSION=$(git --version 2>&1 | head -1)
                ;;
            curl)
                VERSION=$(curl --version 2>&1 | head -1)
                ;;
            wget)
                VERSION=$(wget --version 2>&1 | head -1)
                ;;
            verilator)
                VERSION=$(verilator --version 2>&1 | head -1)
                ;;
            *)
                VERSION="Unknown"
                ;;
        esac

        echo "  Verified: $VERSION"
        RESULTS+=("$tool|PASS|$VERSION")
    else
        echo "  Verification failed."
        RESULTS+=("$tool|FAIL|Not Installed")
    fi

    echo
}

for tool in "${TOOLS[@]}"; do
    install_tool "$tool"
done

echo
echo "========================================"
echo "Final Results"
echo "========================================"

printf "%-20s %-10s\n" "TOOL" "STATUS"
printf "%-20s %-10s\n" "--------------------" "----------"

for result in "${RESULTS[@]}"; do
    IFS='|' read -r tool status version <<< "$result"
    printf "%-20s %-10s\n" "$tool" "$status"
done

echo

FAIL_COUNT=0

for result in "${RESULTS[@]}"; do
    IFS='|' read -r tool status version <<< "$result"
    if [[ "$status" == "FAIL" ]]; then
        ((FAIL_COUNT++))
    fi
done

if [[ $FAIL_COUNT -eq 0 ]]; then
    echo "Overall Result: PASS"
else
    echo "Overall Result: FAIL ($FAIL_COUNT tool(s) failed)"
fi
