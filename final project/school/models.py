"""Student data model."""

from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    roll_number: int
    marks: list[int] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.name = self.name.strip()
        if not self.name:
            raise ValueError("Student name must not be empty.")
        if type(self.roll_number) is not int or self.roll_number <= 0:
            raise ValueError("Roll number must be a positive integer.")
        if any(type(mark) is not int or not 0 <= mark <= 100 for mark in self.marks):
            raise ValueError("Each mark must be an integer between 0 and 100.")
