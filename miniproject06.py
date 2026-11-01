import json
import csv
import os
import datetime


JSON_FILE = "students.json"
CSV_FILE = "students.csv"
LOG_FILE = "activity_log.txt"
TEXT_FILE = "student_summary.txt"


# Load existing student records
def load_students():

    if not os.path.exists(JSON_FILE):
        return {}

    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            students = json.load(file)

        if not isinstance(students, dict):
            raise ValueError("Student data must be a dictionary.")

        return students

    except (json.JSONDecodeError, ValueError) as error:
        print("Error loading student records:", error)
        print("The original JSON file has been preserved.")
        return None


# Save student records in JSON
def save_students(students):

    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

    print("Record saved successfully to students.json.")


# Add timestamped activity to log file
def add_log(message):

    current_time = datetime.datetime.now()

    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")


# Take marks from user
def get_marks():

    marks = {}

    subjects = ["Python", "Maths", "DBMS"]

    for subject in subjects:

        while True:

            try:
                value = float(input(f"{subject} marks: "))

                if 0 <= value <= 100:
                    marks[subject] = value
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    return marks


# Add a new student
def add_student(students):

    print("\n----- ADD NEW STUDENT -----")

    student_id = input("Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id in students:
        print("This student ID already exists.")
        return

    name = input("Student Name: ").strip()
    department = input("Department: ").strip()

    if not name or not department:
        print("Name and department cannot be empty.")
        return

    marks = get_marks()

    students[student_id] = {
        "name": name,
        "department": department,
        "marks": marks
    }

    save_students(students)

    add_log(f"New student added: {student_id}")


# Update an existing student
def update_student(students):

    print("\n----- UPDATE STUDENT -----")

    student_id = input("Enter Student ID: ").strip()

    if student_id not in students:
        print("Student record not found.")
        return

    print("Current Name:", students[student_id]["name"])
    print("Current Department:", students[student_id]["department"])

    new_name = input("Enter new name (blank to keep old): ").strip()
    new_department = input(
        "Enter new department (blank to keep old): "
    ).strip()

    if new_name:
        students[student_id]["name"] = new_name

    if new_department:
        students[student_id]["department"] = new_department

    print("\nEnter updated subject marks:")

    students[student_id]["marks"] = get_marks()

    save_students(students)

    add_log(f"Student record updated: {student_id}")


# Display one student record
def search_student(students):

    print("\n----- SEARCH STUDENT -----")

    student_id = input("Enter Student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print("\nStudent ID:", student_id)
    print("Name:", student["name"])
    print("Department:", student["department"])

    print("\nSubject Marks:")

    for subject, marks in student["marks"].items():
        print(f"{subject}: {marks}")


# Display all student records
def display_students(students):

    print("\n----- ALL STUDENT RECORDS -----")

    if not students:
        print("No student records available.")
        return

    for student_id, student in students.items():

        print("\nStudent ID:", student_id)
        print("Name:", student["name"])
        print("Department:", student["department"])

        for subject, marks in student["marks"].items():
            print(f"{subject}: {marks}")

        print("-----------------------------")


# Export student records to CSV
def export_csv(students):

    if not students:
        print("No records available for export.")
        return

    headers = [
        "Student ID",
        "Name",
        "Department",
        "Python",
        "Maths",
        "DBMS"
    ]

    with open(
        CSV_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(headers)

        for student_id, student in students.items():

            writer.writerow([
                student_id,
                student["name"],
                student["department"],
                student["marks"]["Python"],
                student["marks"]["Maths"],
                student["marks"]["DBMS"]
            ])

    print("CSV export completed:", CSV_FILE)

    add_log("Student records exported to CSV")


# Demonstrate JSON string operations
def json_string_demo(students):

    print("\n----- JSON STRING OPERATIONS -----")

    if not students:
        print("No student record available.")
        return

    student_id = input("Enter Student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    record = students[student_id]

    # Convert Python dictionary into JSON string
    json_text = json.dumps(record, indent=4)

    print("\nJSON String:")
    print(json_text)

    # Convert JSON string back into Python dictionary
    converted_record = json.loads(json_text)

    print("\nConverted Python Dictionary:")
    print(converted_record)


# Demonstrate read() method
def read_entire_log():

    print("\n----- COMPLETE ACTIVITY LOG -----")

    if not os.path.exists(LOG_FILE):
        print("No activity log found.")
        return

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    if content:
        print(content)
    else:
        print("Log file is empty.")


# Demonstrate readline() method
def read_first_log():

    print("\n----- FIRST LOG ENTRY -----")

    if not os.path.exists(LOG_FILE):
        print("No activity log found.")
        return

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        line = file.readline()

    if line:
        print(line)
    else:
        print("Log file is empty.")


# Demonstrate readlines() method
def read_all_lines():

    print("\n----- LOG ENTRIES -----")

    if not os.path.exists(LOG_FILE):
        print("No activity log found.")
        return

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if lines:
        for line in lines:
            print(line, end="")
    else:
        print("Log file is empty.")


# Demonstrate writelines() method
def save_text_summary(students):

    if not students:
        print("No student records available.")
        return

    lines = []

    lines.append("STUDENT RECORD SUMMARY\n")
    lines.append("======================\n\n")

    for student_id, student in students.items():

        lines.append(f"Student ID: {student_id}\n")
        lines.append(f"Name: {student['name']}\n")
        lines.append(f"Department: {student['department']}\n")

        for subject, marks in student["marks"].items():
            lines.append(f"{subject}: {marks}\n")

        lines.append("\n")

    with open(TEXT_FILE, "w", encoding="utf-8") as file:
        file.writelines(lines)

    print("Text summary saved:", TEXT_FILE)


# Main menu
def main():

    print("======================================")
    print("   STUDENT RECORDS MANAGEMENT SYSTEM")
    print("======================================")

    students = load_students()

    # Stop if existing JSON data cannot be loaded safely
    if students is None:
        print("Program stopped to protect existing student data.")
        return

    while True:

        print("\n========== MAIN MENU ==========")

        print("1. Add Student")
        print("2. Update Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Export Records to CSV")
        print("6. JSON String Operations")
        print("7. View Activity Log")
        print("8. View First Log Entry")
        print("9. View All Log Lines")
        print("10. Save Text Summary")
        print("11. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            update_student(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            display_students(students)

        elif choice == "5":
            export_csv(students)

        elif choice == "6":
            json_string_demo(students)

        elif choice == "7":
            read_entire_log()

        elif choice == "8":
            read_first_log()

        elif choice == "9":
            read_all_lines()

        elif choice == "10":
            save_text_summary(students)

        elif choice == "11":
            print("\nThank you for using Student Records System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()