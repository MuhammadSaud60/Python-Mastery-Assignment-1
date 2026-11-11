"""
    Name: Muhammad Saud
    Cohort: PSEB-AI-PEW-01 (PSEB-AI-PEW-01)

"""

# warmup: Standard library tour

import math
import random
from datetime import date
import statistics

print("Square root of 144:", math.sqrt(144))

students = ["Saad", "Ali", "Hamza", "Umer"]
print("Random student:", random.choice(students))

today = date.today()
year_end = date(today.year, 12, 31)
print("Days left until 31 December:", (year_end - today).days)

marks = [78, 85, 92, 67, 88]
print("Mean mark:", statistics.mean(marks))
print("Median mark:", statistics.median(marks))



# Build: Your own module

# school_tools.py and main.py created

