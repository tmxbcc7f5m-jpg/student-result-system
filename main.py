import results
import reports
import storage
from student import (Student, is_valid_id, is_valid_dob, add_student,
                     search_students, update_student, delete_student)

def ask_id(prompt="Student ID (e.g. STU001): "):
    while True:
        student_id = input(prompt).strip().upper()
        if is_valid_id(student_id):
            return student_id
        print("Invalid ID. Use STU followed by 3 digits, e.g. STU001.")

def ask_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This cannot be empty.")

def ask_gender():
    while True:
        value = input("Gender (M/F): ").strip().upper()
        if value in ("M", "F"):
            return value
        print("Please type M or F.")

def ask_dob():
    while True:
        dob = input("Date of birth (YYYY-MM-DD): ").strip()
        if is_valid_dob(dob):
            return dob
        print("Invalid date. Use YYYY-MM-DD, e.g. 2008-05-21.")

def ask_scores(old_scores=None):
    scores = {}
    for subject in results.SUBJECTS:
        while True:
            hint = ""
            if old_scores and subject in old_scores:
                hint = f" [current {old_scores[subject]}]"
            text = input(f"{subject} score (0-100){hint}: ").strip()
            if text == "" and old_scores and subject in old_scores:
                scores[subject] = old_scores[subject]
                break
            try:
                scores[subject] = results.validate_score(text)
                break
            except ValueError:
                print("Invalid score. Enter a number from 0 to 100.")
    return scores

def add_new_student(students):
    print("\n--- Add New Student ---")
    student_id = ask_id()
    if student_id in students:
        print("A student with that ID already exists.")
        return
    name = ask_text("Full name: ")
    student_class = ask_text("Class/Form (e.g. SS1): ").upper()
    gender = ask_gender()
    dob = ask_dob()
    add_student(students, Student(student_id, name, student_class, gender, dob))
    storage.save_students(students)
    print("Student added successfully.")

def view_all_students(students):
    print("\n--- All Students ---")
    if not students:
        print("No students registered yet.")
        return
    print(reports.students_table(reports.sort_by_name(students)))

def search_student(students):
    keyword = ask_text("Enter student ID or name: ")
    found = search_students(students, keyword)
    if not found:
        print("No student found.")
    else:
        print(reports.students_table(found))

def update_student_info(students):
    student_id = ask_id()
    if student_id not in students:
        print("Student not found.")
        return
    print("Press Enter to keep the current value.")
    name = input("New name: ").strip()
    student_class = input("New class: ").strip().upper()
    gender = input("New gender (M/F): ").strip().upper()
    dob = input("New date of birth (YYYY-MM-DD): ").strip()
    if gender and gender not in ("M", "F"):
        print("Invalid gender. Nothing was changed.")
        return
    if dob and not is_valid_dob(dob):
        print("Invalid date. Nothing was changed.")
        return
    update_student(students, student_id, name, student_class, gender, dob)
    storage.save_students(students)
    print("Student updated.")

def delete_student_record(students):
    student_id = ask_id()
    if student_id not in students:
        print("Student not found.")
        return
    confirm = input(f"Delete {students[student_id].name}? (y/n): ").strip().lower()
    if confirm == "y":
        delete_student(students, student_id)
        storage.save_students(students)
        print("Student deleted.")
    else:
        print("Cancelled.")

def record_scores(students):
    student_id = ask_id()
    student = students.get(student_id)
    if student is None:
        print("Student not found.")
        return
    print(f"Entering scores for {student.name}")
    student.set_scores(ask_scores(student.scores))
    storage.save_students(students)
    print(f"Total: {student.total():.1f}  Average: {student.average():.2f}  "
          f"Grade: {student.grade()}")

def show_report_card(students):
    student = students.get(ask_id())
    if student is None:
        print("Student not found.")
        return
    print(reports.report_card(student))

def show_results_list(students):
    if not students:
        print("No students registered yet.")
        return
    choice = input("Sort by (1) average, highest first or (2) name: ").strip()
    if choice == "2":
        print(reports.students_table(reports.sort_by_name(students)))
    else:
        print(reports.students_table(reports.sort_by_average(students)))

def show_statistics(students):
    print(reports.statistics_text(students))

def export_report(students):
    if not students:
        print("No students to report on.")
        return
    try:
        path = reports.save_text_report(students)
    except OSError as error:
        print("Could not save report:", error)
    else:
        print("Report saved to", path)

MENU = """
========== STUDENT RESULT SYSTEM ==========
 1. Add new student
 2. View all students
 3. Search student (ID or name)
 4. Update student information
 5. Delete student
 6. Record / update scores
 7. Show student report card
 8. List results (sorted)
 9. Class statistics
10. Save text report to file
 0. Exit
==========================================="""

def main():
    students = storage.load_students()
    print(f"Loaded {len(students)} student(s).")
    actions = {"1": add_new_student, "2": view_all_students,
               "3": search_student, "4": update_student_info,
               "5": delete_student_record, "6": record_scores,
               "7": show_report_card, "8": show_results_list,
               "9": show_statistics, "10": export_report}
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            storage.save_students(students)
            print("Data saved. Goodbye!")
            break
        elif choice in actions:
            actions[choice](students)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()