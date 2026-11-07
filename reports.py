import os
from datetime import datetime

REPORT_FOLDER = "reports"

def sort_by_average(students):
    return sorted(students.values(), key=lambda s: s.average(), reverse=True)

def sort_by_name(students):
    return sorted(students.values(), key=lambda s: s.name.lower())

def students_table(student_list):
    lines = []
    lines.append(f"{'ID':<8}{'Name':<24}{'Class':<8}{'Total':>8}{'Average':>10}{'Grade':>7}")
    lines.append("-" * 65)
    for s in student_list:
        lines.append(f"{s.student_id:<8}{s.name:<24}{s.student_class:<8}"
                     f"{s.total():>8.1f}{s.average():>10.2f}{s.grade():>7}")
    return "\n".join(lines)

def report_card(student):
    lines = []
    lines.append("=" * 40)
    lines.append("           STUDENT REPORT CARD")
    lines.append("=" * 40)
    lines.append(f"ID     : {student.student_id}")
    lines.append(f"Name   : {student.name}")
    lines.append(f"Class  : {student.student_class}")
    lines.append(f"Gender : {student.gender}")
    lines.append(f"DOB    : {student.dob}")
    lines.append("-" * 40)
    if len(student.scores) == 0:
        lines.append("No scores recorded yet.")
    else:
        for subject, score in student.scores.items():
            lines.append(f"{subject:<20}{score:>8.1f}")
        lines.append("-" * 40)
        lines.append(f"{'Total':<20}{student.total():>8.1f}")
        lines.append(f"{'Average':<20}{student.average():>8.2f}")
        lines.append(f"{'Grade':<20}{student.grade():>8}")
        lines.append(f"Result entered on: {student.date_entered}")
    lines.append("=" * 40)
    return "\n".join(lines)

def class_statistics(students):
    averages = [s.average() for s in students.values() if len(s.scores) > 0]
    if len(averages) == 0:
        return None
    return max(averages), min(averages), sum(averages) / len(averages)

def statistics_text(students):
    stats = class_statistics(students)
    if stats is None:
        return "No scores recorded yet, so no statistics."
    highest, lowest, class_avg = stats
    return (f"Highest average : {highest:.2f}\n"
            f"Lowest average  : {lowest:.2f}\n"
            f"Class average   : {class_avg:.2f}")

def save_text_report(students):
    os.makedirs(REPORT_FOLDER, exist_ok=True)
    now = datetime.now()
    filename = os.path.join(REPORT_FOLDER, now.strftime("report_%Y%m%d_%H%M%S.txt"))
    content = ["CLASS RESULT REPORT",
               "Generated: " + now.strftime("%Y-%m-%d %H:%M"), "",
               students_table(sort_by_average(students)), "",
               "CLASS STATISTICS", statistics_text(students)]
    with open(filename, "w") as file:
        file.write("\n".join(content) + "\n")
    return filename