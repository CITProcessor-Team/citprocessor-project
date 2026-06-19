import json

STUDENTS_FILE = "students.json"
SUBJECTS_FILE = "subjects.json"
MARKS_FILE = "marks.json"


# -----------------------------
# LOAD DATA SAFELY
# -----------------------------
def load_data(filename, default):
    try:
        with open(filename, "r") as f:
            data = json.load(f)

            if type(data) != type(default):
                print(f"Warning: {filename} has invalid format. Resetting.")
                return default

            return data

    except FileNotFoundError:
        return default

    except json.JSONDecodeError:
        print(f"Warning: {filename} is corrupted. Resetting.")
        return default

    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return default


students = load_data(STUDENTS_FILE, {})
subjects = load_data(SUBJECTS_FILE, [])
marks = load_data(MARKS_FILE, {})


# -----------------------------
# SAVE DATA
# -----------------------------
def save_all():
    try:
        with open(STUDENTS_FILE, "w") as f:
            json.dump(students, f, indent=4)

        with open(SUBJECTS_FILE, "w") as f:
            json.dump(subjects, f, indent=4)

        with open(MARKS_FILE, "w") as f:
            json.dump(marks, f, indent=4)

    except Exception as e:
        print("Error saving data:", e)


# -----------------------------
# GRADE CALCULATION
# -----------------------------
def get_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


# -----------------------------
# ADD STUDENT
# -----------------------------
def add_student():
    try:
        roll = input("Enter Roll Number: ").strip()

        if roll in students:
            print("Student already exists.")
            return

        name = input("Enter Student Name: ").strip()

        students[roll] = name

        save_all()

        print("Student added successfully.")

    except Exception as e:
        print("Error:", e)


# -----------------------------
# SEARCH STUDENT
# -----------------------------
def search_student():
    try:
        roll = input("Enter Roll Number: ").strip()

        if roll in students:
            print("Roll Number:", roll)
            print("Student Name:", students[roll])
        else:
            print("Student not found.")

    except Exception as e:
        print("Error:", e)


# -----------------------------
# DELETE STUDENT
# -----------------------------
def delete_student():
    try:
        roll = input("Enter Roll Number: ").strip()

        if roll not in students:
            print("Student not found.")
            return

        del students[roll]

        delete_keys = []

        for key in marks:
            if key.startswith(roll + "_"):
                delete_keys.append(key)

        for key in delete_keys:
            del marks[key]

        save_all()

        print("Student deleted successfully.")

    except Exception as e:
        print("Error:", e)


# -----------------------------
# ADD SUBJECT
# -----------------------------
def add_subject():
    try:
        subject = input("Enter Subject Name: ").strip()

        if subject in subjects:
            print("Subject already exists.")
            return

        subjects.append(subject)

        save_all()

        print("Subject added successfully.")

    except Exception as e:
        print("Error:", e)


# -----------------------------
# ENTER MARKS
# -----------------------------
def enter_marks():
    try:
        roll = input("Enter Roll Number: ").strip()

        if roll not in students:
            print("Student not found.")
            return

        if not subjects:
            print("No subjects available.")
            return

        for subject in subjects:

            while True:
                try:
                    mark = float(
                        input(f"Enter marks for {subject}: ")
                    )

                    if 0 <= mark <= 100:
                        break

                    print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Enter a valid number.")

            key = roll + "_" + subject

            marks[key] = mark

        save_all()

        print("Marks saved successfully.")

    except Exception as e:
        print("Error:", e)


# -----------------------------
# REPORT CARD GENERATOR
# -----------------------------
def generate_report_card(roll):

    if roll not in students:
        return "Student not found."

    report = []

    report.append("=" * 50)
    report.append("STUDENT REPORT CARD")
    report.append("=" * 50)
    report.append(f"Roll Number : {roll}")
    report.append(f"Name        : {students[roll]}")
    report.append("")

    total = 0
    count = 0

    report.append(f"{'Subject':15} {'Marks':10} {'Grade'}")
    report.append("-" * 50)

    for subject in subjects:

        key = roll + "_" + subject

        mark = marks.get(key, 0)

        grade = get_grade(mark)

        report.append(
            f"{subject:15} {mark:<10} {grade}"
        )

        total += mark
        count += 1

    report.append("-" * 50)

    average = total / count if count > 0 else 0

    overall_grade = get_grade(average)

    report.append(f"Average Marks : {average:.2f}")
    report.append(f"Overall Grade : {overall_grade}")

    return "\n".join(report)


# -----------------------------
# DISPLAY REPORT CARD
# -----------------------------
def show_report_card():
    try:
        roll = input("Enter Roll Number: ").strip()

        print()
        print(generate_report_card(roll))

    except Exception as e:
        print("Error:", e)


# -----------------------------
# EXPORT REPORT
# -----------------------------
def export_report():
    try:
        roll = input("Enter Roll Number: ").strip()

        report = generate_report_card(roll)

        if report == "Student not found.":
            print(report)
            return

        filename = roll + "_report.txt"

        with open(filename, "w") as f:
            f.write(report)

        print(f"Report exported to {filename}")

    except Exception as e:
        print("Error:", e)


# -----------------------------
# MAIN MENU
# -----------------------------
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Add Subject")
    print("5. Enter Marks")
    print("6. Generate Report Card")
    print("7. Export Report Card")
    print("8. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        add_subject()

    elif choice == "5":
        enter_marks()

    elif choice == "6":
        show_report_card()

    elif choice == "7":
        export_report()

    elif choice == "8":
        save_all()
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
