import os
import sys
import shutil

# Check command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 hw19.py <source_directory>")
    sys.exit()

source_dir = sys.argv[1]

# Extension mapping
extension_map = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",

    ".py": "Scripts"
}

# Counters
counts = {
    "Images": 0,
    "Documents": 0,
    "Scripts": 0,
    "Misc": 0
}

# Process files
for filename in os.listdir(source_dir):

    source_path = os.path.join(source_dir, filename)

    # Skip directories
    if not os.path.isfile(source_path):
        continue

    ext = os.path.splitext(filename)[1].lower()

    folder = extension_map.get(ext, "Misc")

    destination_folder = os.path.join(source_dir, folder)

    os.makedirs(destination_folder, exist_ok=True)

    destination_path = os.path.join(
        destination_folder,
        filename
    )

    shutil.move(source_path, destination_path)

    counts[folder] += 1

# Print summary
print("\n===== FILE ORGANISER SUMMARY =====")

for category, count in counts.items():
    print(f"{category}: {count} file(s) moved")
