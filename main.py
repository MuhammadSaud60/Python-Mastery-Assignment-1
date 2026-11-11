from school_tools import area_of_circle, average, grade, greet, is_even, report


print(f"Circle area (radius 5): {area_of_circle(5)}")
print(f"Is 10 even? {is_even(10)}")
print(greet("Saud", "ur"))

marks = [85, 90, 78]
print(f"Average: {average(marks):.2f}")
print(f"Grade: {grade(average(marks))}")
report("Saud", marks)
