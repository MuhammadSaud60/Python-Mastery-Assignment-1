"""
Reusable helper functions for school-related calculations and reports.
""" 


def area_of_circle(r):
    """Return the area of a circle with radius r."""
    pi = 3.14
    return pi * r**2


def is_even(n):
    """Return whether n is even."""
    return n % 2 == 0


def greet(name, lang="en"):
    """Greet a user in English or Urdu."""
    if lang.lower() == "en":
        return f"Hello, {name}"
    if lang.lower() == "ur":
        return f"Salam, {name}"
    return "Sorry only English and Urdu Language supported"


def average(marks):
    """Return the average of a non-empty collection of marks."""
    if not marks:
        raise ValueError("marks must not be empty")
    return sum(marks) / len(marks)


def grade(avg):
    """Return the grade using the Part 2 mark bands."""
    if not 0 <= avg <= 100:
        raise ValueError("marks must be between 0 and 100")
    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 33:
        return "D"
    return "F"


def report(name, marks):
    """Display a student's marks, average, and grade."""
    avg = average(marks)
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade(avg)}")


if __name__ == "__main__":
    print(f"Circle area (radius 5): {area_of_circle(5)}")
    print(f"Is 10 even? {is_even(10)}")
    print(greet("Saud"))
    report("Saud", [85, 90, 78])
