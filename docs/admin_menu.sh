#!/bin/bash

while true
do
    echo
    echo "================================="
    echo " System Administration Menu"
    echo "================================="
    echo "1. Show Disk Usage"
    echo "2. Show Top 5 CPU-Using Processes"
    echo "3. List Currently Logged-In Users"
    echo "4. Show Failed Login Attempts"
    echo "5. Exit"
    echo "================================="

    read -p "Enter your choice (1-5): " choice

    case "$choice" in

        1)
            echo
            echo "===== Disk Usage ====="
            df -h
            ;;

        2)
            echo
            echo "===== Top 5 CPU Processes ====="
            ps aux --sort=-%cpu | head -6
            ;;

        3)
            echo
            echo "===== Logged-In Users ====="
            who
            ;;

        4)
            echo
            echo "===== Failed Login Attempts ====="

            if [ -f /var/log/auth.log ]; then
                grep "Failed" /var/log/auth.log
            else
                echo "/var/log/auth.log not found."
            fi
            ;;

        5)
            echo "Exiting..."
            break
            ;;

        *)
            echo "Invalid choice. Please enter 1-5."
            ;;

    esac

done
