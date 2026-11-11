"""
    Name: Muhammad Saud
    Cohort: PSEB-AI-PEW-01 (PSEB-AI-PEW-01)

"""

# Warm-up: Countdown generator

# countdown(n) using yield

def countdown(n):
    while n >= 0:
        yield n
        n -= 1


# Loop over countdown(5)

print("Countdown from 5:")
for x in countdown(5):
    print(x)


# # evens(limit) generator

def evens(limit):
    for i in range(0, limit + 1, 2):
        yield i


print("\nEvens up to 10:")
for even in evens(10):
    print(even)



# Build: Big file reader

from pathlib import Path


def read_lines(path):

    """
     Yield lines from text file one at a time.
    """

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")


def only_errors(lines):

    """
    Yield only lines containing the word ERROR.
    """

    for line in lines:
        if "ERROR" in line:
            yield line


error_count = 0
sample_log = Path(__file__).with_name("sample.log")
for error_line in only_errors(read_lines(sample_log)):
    error_count += 1

print(f"\nError lines: {error_count}")



# Challenge: Your own decorators

from functools import wraps
from time import perf_counter


def timer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = function(*args, **kwargs)
        elapsed = perf_counter() - start_time
        print(f"{function.__name__} took {elapsed:.6f} seconds")
        return result

    return wrapper


def log_calls(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__} with args={args}, kwargs={kwargs}")
        return function(*args, **kwargs)

    return wrapper


@timer
@log_calls
def sum_to_one_million():
    return sum(range(1, 1_000_001))


print(f"Sum from 1 to 1,000,000: {sum_to_one_million()}")

