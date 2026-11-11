"""Grade calculations and class ranking."""

from .models import Student


def average(marks: list[int]) -> float:
    """Return the average for a non-empty list of marks."""
    if not marks:
        raise ValueError("Cannot calculate an average without marks.")
    if any(type(mark) is not int or not 0 <= mark <= 100 for mark in marks):
        raise ValueError("Each mark must be an integer between 0 and 100.")
    return sum(marks) / len(marks)


def grade(mark_average: float) -> str:
    """Convert an average mark into a letter grade."""
    if not 0 <= mark_average <= 100:
        raise ValueError("Average must be between 0 and 100.")
    if mark_average >= 80:
        return "A"
    if mark_average >= 70:
        return "B"
    if mark_average >= 60:
        return "C"
    if mark_average >= 33:
        return "D"
    return "F"


def rank_students(students: list[Student]) -> list[Student]:
    """Return students with marks, ordered by average from highest to lowest."""
    students_with_marks = [student for student in students if student.marks]
    return sorted(
        students_with_marks,
        key=lambda student: average(student.marks),
        reverse=True,
    )
