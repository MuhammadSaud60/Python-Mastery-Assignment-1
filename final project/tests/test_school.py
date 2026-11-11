"""Tests for the school manager."""

import json
from pathlib import Path

import pytest

import main as school_main
from school.grades import average, grade, rank_students
from school.models import Student
from school.storage import load_students, save_students


def test_student_defaults_to_no_marks() -> None:
    student = Student("Amina", 12)

    assert student.marks == []


def test_student_rejects_out_of_range_mark() -> None:
    with pytest.raises(ValueError, match="between 0 and 100"):
        Student("Amina", 12, [101])


def test_average_and_grade() -> None:
    mark_average = average([80, 90, 70])

    assert mark_average == 80
    assert grade(mark_average) == "A"


def test_grade_boundaries() -> None:
    assert [grade(mark) for mark in [80, 70, 60, 33, 32]] == [
        "A",
        "B",
        "C",    
        "D",
        "F",
    ]


def test_average_rejects_empty_marks() -> None:
    with pytest.raises(ValueError, match="without marks"):
        average([])


def test_ranking_is_descending_and_excludes_students_without_marks() -> None:
    students = [
        Student("Amina", 12, [75, 85]),
        Student("Bilal", 13),
        Student("Sara", 14, [90, 100]),
    ]

    assert [student.name for student in rank_students(students)] == ["Sara", "Amina"]


def test_load_and_save_round_trip(tmp_path: Path) -> None:
    file_path = tmp_path / "school.json"
    students = [Student("Amina", 12, [87, 92])]

    save_students(students, file_path)

    assert load_students(file_path) == students


def test_load_missing_file_returns_empty_roster(tmp_path: Path) -> None:
    assert load_students(tmp_path / "missing.json") == []


def test_load_rejects_invalid_json(tmp_path: Path) -> None:
    file_path = tmp_path / "school.json"
    file_path.write_text("{invalid", encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        load_students(file_path)


def test_load_rejects_duplicate_roll_numbers(tmp_path: Path) -> None:
    file_path = tmp_path / "school.json"
    file_path.write_text(
        json.dumps(
            [
                {"name": "Amina", "roll_number": 12, "marks": []},
                {"name": "Sara", "roll_number": 12, "marks": []},
            ]
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Duplicate roll number"):
        load_students(file_path)


def test_menu_flow_saves_and_reports_student(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    file_path = tmp_path / "school.json"
    responses = iter(
        ["invalid", "1", "Amina", "42", "2", "42", "91", "3", "42", "4", "5"]
    )

    def provide_response(_prompt: str) -> str:
        return next(responses)

    monkeypatch.setattr(school_main, "DATA_FILE", file_path)
    monkeypatch.setattr("builtins.input", provide_response)

    school_main.main()

    output = capsys.readouterr().out
    assert load_students(file_path) == [Student("Amina", 42, [91])]
    assert "Invalid choice" in output
    assert "Average: 91.00" in output
    assert "Grade: A" in output
    assert "CLASS RANKING" in output
