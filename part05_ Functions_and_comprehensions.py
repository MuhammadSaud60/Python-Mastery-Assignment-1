
"""
    Name: Muhammad Saud
    Cohort: PSEB-AI-PEW-01 (PSEB-AI-PEW-01)

"""


# Warm-up: Small helpers

def area_of_circle(r):
    """
        Find Area of Cricle
    """
    PI = 3.14
    return PI * r**2


def is_even(n):

    """
        Check given number is even or not
    """

    if n % 2 == 0:
        return True
    else:
        return False


def greet(name, lang="en"):

    """
     greet user in different languages (English or Urdu)
    """

    if lang.lower() == 'en':
        return f"Hello, {name}"

    elif lang.lower() == 'ur':
        return f'Salam, {name}'

    else:
        return 'Sorry only English and Urdu Language supported'


# CALLING FUNCTIONS
test1 = area_of_circle(33)
test2 = area_of_circle(60)
test3 = area_of_circle(20)
print(f'test1: {test1}\ntest2: {test2}\ntest3: {test3}')

even_test1 = is_even(10)
even_test2 = is_even(7)
even_test3 = is_even(0)
print(f'even_test1: {even_test1}\neven_test2: {even_test2}\neven_test3: {even_test3}')

greet_test1 = greet('Saud')
greet_test2 = greet('Saud', 'ur')
greet_test3 = greet('Saud', 'fr')
print(f'greet_test1: {greet_test1}\ngreet_test2: {greet_test2}\ngreet_test3: {greet_test3}')



# Build: Marks toolkit

def average(marks):

    """
    Return the average of a non-empty collection of marks.
    """

    if not marks:
        raise ValueError("marks must not be empty")
    return sum(marks) / len(marks)


def grade(avg):
    """
    Return the grade using the Part 2 mark bands.
    """

    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    return "F"


def report(name, marks):
    """
    Display a student's marks, average, and grade.
    """

    avg = average(marks)

    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade(avg)}")



# Challenge: Comprehensions


squares = [number**2 for number in range(1, 11)]

names = ["Saud", "Muhammad", "Ayesha", "Ali"]
long_names = [name for name in names if len(name) > 4]

# `result_sheet` contains (name, average) pairs from Part 4.
averages_by_name = {name: avg for name, avg in result_sheet}
passing_students = [name for name, avg in result_sheet if avg >= 33]
