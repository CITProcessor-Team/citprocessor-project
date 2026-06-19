import json

# Load records from JSON file
def load_records(filename="students.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Save records to JSON file
def save_records(records, filename="students.json"):
    with open(filename, "w") as f:
        json.dump(records, f, indent=2)


# Add a student
def add_student(records, name, roll, gpa):
    student = {
        "name": name,
        "roll": roll,
        "gpa": gpa
    }
    records.append(student)


# Find a student by roll number
def find_by_roll(records, roll):
    for student in records:
        if student["roll"] == roll:
            return student
    return None


# Delete a student by roll number
def delete_student(records, roll):
    for student in records:
        if student["roll"] == roll:
            records.remove(student)
            return True
    return False


# Print all students sorted by GPA
def print_all_sorted_by_gpa(records):
    sorted_records = sorted(
        records,
        key=lambda r: r["gpa"],
        reverse=True
    )

    print("\nStudents Sorted by GPA:")
    for student in sorted_records:
        print(
            f"Name: {student['name']}, "
            f"Roll: {student['roll']}, "
            f"GPA: {student['gpa']}"
        )


# Main Program
records = load_records()

add_student(records, "Ravi", "101", 8.7)
add_student(records, "Priya", "102", 9.1)
add_student(records, "Arun", "103", 8.4)

save_records(records)

student = find_by_roll(records, "102")
if student:
    print("Found Student:")
    print(student)

deleted = delete_student(records, "103")
if deleted:
    print("\nStudent with roll 103 deleted.")

save_records(records)

print_all_sorted_by_gpa(records)
