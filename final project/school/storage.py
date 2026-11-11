"""JSON persistence for the student roster."""

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from .models import Student


def load_students(file_path: Path) -> list[Student]:
    """Load and validate students from a JSON file."""
    try:
        with file_path.open("r", encoding="utf-8") as file:
            records: Any = json.load(file)
    except FileNotFoundError:
        return []

    if not isinstance(records, list):
        raise ValueError("The school data file must contain a JSON list.")

    students: list[Student] = []
    seen_roll_numbers: set[int] = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Each student record must be a JSON object.")

        name = record.get("name")
        roll_number = record.get("roll_number")
        marks = record.get("marks")
        if (
            not isinstance(name, str)
            or type(roll_number) is not int
            or not isinstance(marks, list)
            or any(type(mark) is not int for mark in marks)
        ):
            raise ValueError("A student record has invalid fields.")

        student = Student(name=name, roll_number=roll_number, marks=marks)
        if student.roll_number in seen_roll_numbers:
            raise ValueError(f"Duplicate roll number {student.roll_number} in school data.")
        seen_roll_numbers.add(student.roll_number)
        students.append(student)
    return students


def save_students(students: list[Student], file_path: Path) -> None:
    """Write all students to a JSON file."""
    with file_path.open("w", encoding="utf-8") as file:
        json.dump([asdict(student) for student in students], file, indent=2)
        file.write("\n")
