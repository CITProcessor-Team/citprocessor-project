#!/bin/bash

echo "===== System Information from /proc ====="

echo
echo "1. CPU Cores:"
grep "cpu cores" /proc/cpuinfo | head -1

echo
echo "2. Total RAM:"
grep "MemTotal" /proc/meminfo

echo
echo "3. Command Line of PID 1:"
cat /proc/1/cmdline | tr '\0' ' '
echo

echo
echo "4. System Uptime:"
cat /proc/uptime
