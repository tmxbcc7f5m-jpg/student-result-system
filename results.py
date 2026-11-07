SUBJECTS = ("Mathematics", "English", "Physics", "Chemistry", "Biology")

def calculate_total(scores):
    return sum(scores.values())

def calculate_average(scores):
    if len(scores) == 0:
        return 0.0
    return calculate_total(scores) / len(scores)

def assign_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def validate_score(text):
    score = float(text)
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    return score 
print(assign_grade(75))
print(assign_grade(35))