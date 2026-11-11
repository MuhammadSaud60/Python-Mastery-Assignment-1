"""
    Name: Muhammad Saud
    Cohort: PSEB-AI-PEW-01 (PSEB-AI-PEW-01)

"""



# warm-up: add hints


def area_of_circle(r: float) -> float:
    """
        Find Area of Cricle
    """
    PI = 3.14
    return PI * r**2


def is_even(n: int) -> bool:
    """
        Check given number is even or not
    """
    if n % 2 == 0:
        return True
    else:
        return False


def greet(name: str, lang: str = "en") -> str:
    """
     greet user in different languages (English or Urdu)
    """
    if lang.lower() == 'en':
        return f"Hello, {name}"
    elif lang.lower() == 'ur':
        return f'Salam, {name}'
    else:
        return 'Sorry only English and Urdu Language supported'


def average(marks: list[int]) -> float:
    """
    Return the average of a non-empty collection of marks.
    """
    if not marks:
        raise ValueError("marks must not be empty")
    return sum(marks) / len(marks)


def grade(avg: float) -> str:
    """
    Return the grade using the Part 2 mark bands.
    """
    if not 0 <= avg <= 100:
        raise ValueError("marks must be between 0 and 100")
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 33:
        return "D"
    return "F"


def report(name: str, marks: list[int]) -> None:
    """
    Display a student's marks, average, and grade.
    """
    avg = average(marks)
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade(avg)}")


# Build: Product dataclass

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path


@dataclass(order=True)
class Product:
    name: str
    price: float
    stock: int
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("price must not be negative")
        if self.stock < 0:
            raise ValueError("stock must not be negative")


products = [
    Product("Notebook", 3.50, 12, ["stationery"]),
    Product("Pen", 1.25, 0, ["stationery", "writing"]),
    Product("Backpack", 24.99, 5, ["school", "bags"]),
    Product("Calculator", 15.00, 0, ["school", "electronics"]),
    Product("Ruler", 0.99, 20, ["stationery"]),
]

print("Out-of-stock products:")
for product in products:
    if product.stock == 0:
        print(product)



# challenge 


products_file = Path(__file__).with_name("products.json")

with products_file.open("w", encoding="utf-8") as file:
    json.dump([asdict(product) for product in products], file, indent=4)

with products_file.open("r", encoding="utf-8") as file:
    loaded_products = [Product(**d) for d in json.load(file)]

loaded_products.sort(key=lambda product: product.price)

print("\nProducts sorted by price:")
for product in loaded_products:
    print(product)

