#!/bin/bash

set -euo pipefail

# Check arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <source_directory> <backup_directory>"
    exit 1
fi

SOURCE_DIR="$1"
BACKUP_DIR="$2"

# Validate source directory
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory does not exist."
    exit 1
fi

# Create backup directory if needed
mkdir -p "$BACKUP_DIR"

# Timestamp
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Source directory name
DIR_NAME=$(basename "$SOURCE_DIR")

# Archive filename
ARCHIVE="$BACKUP_DIR/${DIR_NAME}_${TIMESTAMP}.tar.gz"

echo "Creating backup..."

# Create archive
tar -czf "$ARCHIVE" -C "$(dirname "$SOURCE_DIR")" "$DIR_NAME"

echo "Verifying archive..."

# Verify archive integrity
if tar -tzf "$ARCHIVE" >/dev/null 2>&1; then
    STATUS="SUCCESS"
    echo "Verification successful."
else
    STATUS="FAILED"
    echo "Verification failed!"
    exit 1
fi

echo "Cleaning old backups..."

# Keep only 5 most recent backups
ls -tp "$BACKUP_DIR"/*.tar.gz 2>/dev/null | tail -n +6 | while read -r oldfile
do
    rm -f "$oldfile"
done

# Write log entry
echo "$(date '+%Y-%m-%d %H:%M:%S') | $STATUS | Source: $SOURCE_DIR | Archive: $ARCHIVE" >> ~/backups.log

echo "Backup completed successfully."
echo "Archive: $ARCHIVE"
