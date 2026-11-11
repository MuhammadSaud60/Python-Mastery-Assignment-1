
"""
    Name: Muhammad Saud
    Cohort: PSEB-AI-PEW-01 (PSEB-AI-PEW-01)

"""


# Warm-up: Fix 3 bugs

marks = [90, 25, 70]
passing = []

for index in range(len(marks)):  
    mark = marks[index]
    print(f"Checking marks[{index}] = {mark}")
    if mark > 33:
        passing.append(mark) 
    print(f"Passing marks so far: {passing}")

average_passing = sum(passing) / len(passing)  
print(f"Average of passing marks: {average_passing}")

"""
 # range(len(marks) - 1) skipped the last mark.
 # assigning [mark] discarded earlier passing marks.
 # dividing by len(marks) used the wrong denominator.

"""

# Build: Test your grade function

# test_grades.py created and run 10 pytest pass 


# Challenge: Test the bank account

# test_bank_acccount.py create and 6 pytest passed  