# Create student profile dictionary
profile = {
    "name": "Senthoor",
    "roll_number": "23ECE001",
    "branch": "ECE",
    "semester": 3,
    "gpa": 8.5,
    "city": "Chennai"
}

# Print all key-value pairs
print("Student Profile:")
for key, value in profile.items():
    print(f"{key}: {value}")

# (1) Update GPA
profile["gpa"] = 9.0

# (2) Add hobbies
profile["hobbies"] = ["Cricket", "Listening to Music", "Coding"]

# (3) Check if email key exists
if "email" in profile:
    print("\nEmail key exists.")
else:
    print("\nEmail key does not exist.")

# Print updated profile
print("\nUpdated Student Profile:")
for key, value in profile.items():
    print(f"{key}: {value}")
