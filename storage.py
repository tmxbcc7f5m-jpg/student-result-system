import json
import os
from student import Student

DATA_FOLDER = "data"
DATA_FILE = os.path.join(DATA_FOLDER, "students.json")

def load_students():
    students = {}
    if not os.path.exists(DATA_FILE):
        return students
    try:
        file = open(DATA_FILE, "r")
        data = json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: could not read the data file. Starting empty.")
        return students
    else:
        for item in data:
            student = Student.from_dict(item)
            students[student.student_id] = student
    finally:
        try:
            file.close()
        except NameError:
            pass
    return students

def save_students(students):
    os.makedirs(DATA_FOLDER, exist_ok=True)
    data = [s.to_dict() for s in students.values()]
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except OSError as error:
        print("Error saving data:", error)
        return False
    return True