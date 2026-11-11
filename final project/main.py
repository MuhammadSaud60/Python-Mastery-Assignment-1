"""Command-line entry point for the school manager."""

import logging
from pathlib import Path

from school.grades import average, grade, rank_students
from school.models import Student
from school.storage import load_students, save_students

DATA_FILE = Path(__file__).with_name("school.json")
MENU_OPTIONS = (
    "1. Add student",
    "2. Add marks",
    "3. Show report card",
    "4. Class ranking",
    "5. Save and exit",
)


def show_menu() -> None:
    """Display the available actions."""
    print("\n===== SCHOOL MANAGER =====")
    for option in MENU_OPTIONS:
        print(option)


def read_integer(prompt: str) -> int | None:
    """Read an integer or report invalid input."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("Please enter a whole number.")
        return None


def find_student(students: list[Student], roll_number: int) -> Student | None:
    """Find a student by roll number."""
    return next(
        (student for student in students if student.roll_number == roll_number),
        None,
    )


def save_roster(students: list[Student], file_path: Path) -> bool:
    """Save the roster and report any file errors."""
    try:
        save_students(students, file_path)
    except OSError as error:
        logging.error("Could not save school data to %s: %s", file_path, error)
        print(f"Could not save school data: {error}")
        return False
    print("School data saved.")
    return True


def add_student(students: list[Student], file_path: Path) -> None:
    """Add a student after validating their name and roll number."""
    name = input("Student name: ").strip()
    if not name:
        print("Student name must not be empty.")
        return

    roll_number = read_integer("Roll number: ")
    if roll_number is None:
        return
    if roll_number <= 0:
        print("Roll number must be a positive integer.")
        return
    if find_student(students, roll_number) is not None:
        print(f"Roll number {roll_number} is already in use.")
        return

    student = Student(name=name, roll_number=roll_number)
    students.append(student)
    print(f"Added {student.name} (roll number {student.roll_number}).")
    save_roster(students, file_path)


def add_marks(students: list[Student], file_path: Path) -> None:
    """Add one validated mark to an existing student's record."""
    roll_number = read_integer("Roll number: ")
    if roll_number is None:
        return
    student = find_student(students, roll_number)
    if student is None:
        print(f"No student found with roll number {roll_number}.")
        return

    mark = read_integer("Mark (0-100): ")
    if mark is None:
        return
    if not 0 <= mark <= 100:
        print("Mark must be between 0 and 100.")
        return

    student.marks.append(mark)
    print(f"Added mark {mark} for {student.name}.")
    save_roster(students, file_path)


def show_report_card(students: list[Student]) -> None:
    """Display one student's marks, average, and grade."""
    roll_number = read_integer("Roll number: ")
    if roll_number is None:
        return
    student = find_student(students, roll_number)
    if student is None:
        print(f"No student found with roll number {roll_number}.")
        return
    if not student.marks:
        print(f"No marks have been recorded for {student.name}.")
        return

    mark_average = average(student.marks)
    print(f"\nReport card: {student.name} (Roll number {student.roll_number})")
    print(f"Marks: {', '.join(str(mark) for mark in student.marks)}")
    print(f"Average: {mark_average:.2f}")
    print(f"Grade: {grade(mark_average)}")


def show_class_ranking(students: list[Student]) -> None:
    """Display students with marks, ordered by average."""
    ranked_students = rank_students(students)
    if not ranked_students:
        print("No students with marks are available to rank.")
        return

    print("\n===== CLASS RANKING =====")
    for position, student in enumerate(ranked_students, start=1):
        mark_average = average(student.marks)
        print(
            f"{position}. {student.name} (Roll {student.roll_number})"
            f" - Average: {mark_average:.2f}, Grade: {grade(mark_average)}"
        )


def main() -> None:
    """Run the menu until the user saves and exits."""
    try:
        students = load_students(DATA_FILE)
    except (OSError, ValueError) as error:
        logging.error("Could not load school data from %s: %s", DATA_FILE, error)
        print(f"Could not load school data: {error}")
        print("The data file was left unchanged. Correct it and restart the program.")
        return

    while True:
        show_menu()
        try:
            choice = input("Choose: ").strip()
        except EOFError:
            print("\nInput ended. Exiting without saving unsaved changes.")
            return

        if choice == "1":
            add_student(students, DATA_FILE)
        elif choice == "2":
            add_marks(students, DATA_FILE)
        elif choice == "3":
            show_report_card(students)
        elif choice == "4":
            show_class_ranking(students)
        elif choice == "5":
            if save_roster(students, DATA_FILE):
                print("Goodbye.")
                return
        else:
            print("Invalid choice. Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
