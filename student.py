import re
from datetime import datetime
import results

ID_PATTERN = r"^STU\d{3}$"

class Student:
    def __init__(self, student_id, name, student_class, gender, dob,
                 scores=None, date_entered=None):
        self.student_id = student_id
        self.name = name
        self.student_class = student_class
        self.gender = gender
        self.dob = dob
        self.scores = scores if scores is not None else {}
        self.date_entered = date_entered

    def total(self):
        return results.calculate_total(self.scores)

    def average(self):
        return results.calculate_average(self.scores)

    def grade(self):
        if len(self.scores) == 0:
            return "-"
        return results.assign_grade(self.average())

    def set_scores(self, scores):
        self.scores = scores
        self.date_entered = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        return {"student_id": self.student_id, "name": self.name,
                "student_class": self.student_class, "gender": self.gender,
                "dob": self.dob, "scores": self.scores,
                "date_entered": self.date_entered}

    @classmethod
    def from_dict(cls, data):
        return cls(data["student_id"], data["name"], data["student_class"],
                   data["gender"], data["dob"], data.get("scores", {}),
                   data.get("date_entered"))

def is_valid_id(student_id):
    return re.match(ID_PATTERN, student_id) is not None

def is_valid_dob(dob):
    try:
        datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        return False
    else:
        return True

def add_student(students, student):
    if student.student_id in students:
        return False
    students[student.student_id] = student
    return True

def search_students(students, keyword):
    keyword = keyword.strip().lower()
    found = []
    for s in students.values():
        if keyword == s.student_id.lower() or keyword in s.name.lower():
            found.append(s)
    return found

def update_student(students, student_id, name=None, student_class=None,
                   gender=None, dob=None):
    student = students.get(student_id)
    if student is None:
        return False
    if name:
        student.name = name
    if student_class:
        student.student_class = student_class
    if gender:
        student.gender = gender
    if dob:
        student.dob = dob
    return True

def delete_student(students, student_id):
    if student_id in students:
        del students[student_id]
        return True
    return False