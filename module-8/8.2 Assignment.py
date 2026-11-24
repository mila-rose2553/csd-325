
"""
Module 8 Assignment
Author: Mariana Baker

Load student records from student.json, display the original list,
append a new student, display the updated list, and save the JSON data.
"""

import json
from pathlib import Path


def print_students(class_list):
    """Print each student's name, ID, and email."""
    for student in class_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , Email = {student['Email']}"
        )


def main():
    """Load, display, update, and save the student list."""
    json_file = Path(__file__).with_name("student.json")

    # Load the JSON file into a Python list of dictionaries.
    with json_file.open("r", encoding="utf-8") as file:
        class_list = json.load(file)

    print("\nThis is the original Student list:")
    print_students(class_list)

    # Add a fictional student record to the list.
    new_student = {
        "F_Name": "Mariana",
        "L_Name": "Baker",
        "Student_ID": 99999,
        "Email": "mariana.baker@example.com"
    }
    class_list.append(new_student)

    print("\nThis is the updated Student list:")
    print_students(class_list)

    # Write the complete updated list back to the JSON file.
    # Using "w" replaces the file with the full list, including the new record.
    with json_file.open("w", encoding="utf-8") as file:
        json.dump(class_list, file, indent=4)

    print("\nThe student.json file was updated.")


if __name__ == "__main__":
    main()
