"""
    Name: Muhammad Saud
    Cohort: PSEB-AI-PEW-01 (PSEB-AI-PEW-01)

"""

# Warmup:  Student class

class Student:
	def __init__(self, name, roll_number, marks=None):
		self.name = name
		self.roll_number = roll_number
		self.marks = list(marks) if marks is not None else []

	def add_mark(self, mark):
		self.marks.append(mark)

	def average(self):
		return sum(self.marks) / len(self.marks) if self.marks else 0.0

	def display(self):
		return f"{self.name} (Roll {self.roll_number}): avg {self.average():.2f}"


Ali = Student('Ali', 209, marks=[30,70,81])

Ali.add_mark(89)

avg = Ali.average()

result = Ali.display()

print(result)



# Build: Bank account

class BankAccount:
	def __init__(self, owner, balance=0):
		if balance < 0:
			raise ValueError("Balance cannot be negative")
		self.owner = owner
		self.balance = balance
		self.transaction_history = []

	def deposit(self, amount):
		if amount < 0:
			raise ValueError("Deposit amount cannot be negative")
		self.balance += amount
		self.transaction_history.append(f"Deposited {amount:.2f}")

	def withdraw(self, amount):
		if amount < 0:
			raise ValueError("Withdrawal amount cannot be negative")
		if amount > self.balance:
			raise ValueError("Withdrawal exceeds available balance")
		self.balance -= amount
		self.transaction_history.append(f"Withdrew {amount:.2f}")

	def print_history(self):
		print(f"Transaction history for {self.owner}:")
		for transaction in self.transaction_history:
			print(transaction)


account = BankAccount("Ali", 10000)
account.deposit(5000)
account.withdraw(2500)
account.print_history()


# Challenge

class Book:
	
	def __init__(self, title, author, available=True):
		self.title = title
		self.author = author
		self.available = available

	def __str__(self):
		status = "Available" if self.available else "Borrowed"
		return f"{self.title} by {self.author} ({status})"


class Library:
	
	def __init__(self):
		self.books = []

	def add_book(self, book):
		self.books.append(book)

	def borrow(self, title):
		for book in self.books:
			if book.title == title and book.available:
				book.available = False
				return True
		return False

	def return_book(self, title):
		for book in self.books:
			if book.title == title and not book.available:
				book.available = True
				return True
		return False

	def available_books(self):
		return [book for book in self.books if book.available]


class EBook(Book):
	
	def __init__(self, title, author, file_size, available=True):
		super().__init__(title, author, available)
		self.file_size = file_size

	def __str__(self):
		status = "Available" if self.available else "Borrowed"
		return f"{self.title} by {self.author} ({self.file_size} MB, {status})"



library = Library()
library.add_book(Book("The Hobbit", "J.R. Tolkien"))
library.add_book(EBook("Python Basics", "Ahmad", 3.5))

print("Available books:")
for book in library.available_books():
	print(book)

if library.borrow("The Hobbit"):
	print("\nBorrowed The Hobbit")

library.return_book("The Hobbit")
print("\nAfter returning The Hobbit:")
for book in library.available_books():
	print(book)


