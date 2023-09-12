# Student Management Script

## Overview

This Python script provides a simple student management system for tracking student information, grades, and attendance. It defines two classes, `Student` and `Grade`, along with supporting functions. You can use this script to create and manage student records, add grades, mark attendance, and check if a student has passed a class based on their grades.

## Features

- Create and manage student records with names, years, grades, and attendance.
- Add grades to a student's record and check if they pass a class.
- Mark attendance for specific classes on specific days.
- Calculate the total score of a student's grades.

## Classes

### `Student` Class

- Constructor: Initializes student name, year, grades list, and attendance dictionary.
- `__repr__`: Returns a string representation of the student's name and year.
- `add_grade(grade)`: Adds a grade to the student's grades list if it's of type `Grade`.
- `mark_attendance(class_name, day, attended)`: Marks attendance for a specific class on a given day.
- `calculate_grades_total()`: Calculates the total score of the student's grades.

### `Grade` Class

- Constructor: Initializes the grade's score and the minimum passing score.
- `is_passing(student_grade)`: Checks if the student's grade is above or below the minimum passing score and prints the result.

## Functions

### `get_day()` Function

- Gets the current day of the week as a string (e.g., "Monday") using the `datetime` module.

