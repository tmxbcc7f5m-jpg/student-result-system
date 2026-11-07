# Student Result Management System

A menu-driven Python program for a secondary school. It registers students,
records their scores, calculates grades and generates reports.
All data is saved in a JSON file.

## Features
- Add, view, search, update and delete students
- Record scores for 5 subjects (Mathematics, English, Physics, Chemistry, Biology)
- Calculates total, average and grade (A to F)
- Shows an individual report card
- Sorts students by average or by name
- Shows class statistics (highest, lowest and class average)
- Saves a text report to a file

## Grading
- 70 and above: A
- 60 to 69: B
- 50 to 59: C
- 40 to 49: D
- Below 40: F

## How to run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run: `python main.py`
5. Choose an option from the menu by typing its number.

Student IDs look like `STU001`. Dates of birth use `YYYY-MM-DD`.

## Files
- main.py: the menu and program start
- student.py: the Student class and student functions
- results.py: total, average and grading
- storage.py: saving and loading the JSON file
- reports.py: reports, sorting and statistics

## Author
TOLUWALASE DABOH