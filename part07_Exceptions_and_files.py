    
"""
    Name: Muhammad Saud
    Cohort: PSEB-AI-PEW-01 (PSEB-AI-PEW-01)

"""


# warmup: Safe division

while True:
    try: 
        num_1 = int(input('Enter First Number: '))
        num_2 = int(input('Enter Second Number: '))

        if num_1 == 0 and num_2 == 0:
            break

        print(num_1 / num_2)
    except ValueError:
        print('Please Enter number only')

    except ZeroDivisionError:
        print('Second number must not be 0.')


# build: daily diary

import datetime


today_note = input("Enter today's note: ")

with open('diary.txt', 'a', encoding='utf-8') as diary_file:
    diary_file.write(f"{datetime.date.today()}: {today_note}\n")

while True:
    print('\n1. Read all past entries')
    print('2. Exit')
    choice = input('Choose an option: ')

    if choice == '1':
        try:
            with open('diary.txt', 'r', encoding='utf-8') as diary_file:
                print(diary_file.read())
        except FileNotFoundError:
            print('No entries yet')
    elif choice == '2':
        break
    else:
        print('Invalid option')


# build: save the Part 4 result sheet

import csv
import json

STUDENTS = {
    'Ali': [85, 90, 78],
    'Saad': [76, 88, 92],
    'Khan': [5, 81, 87],
    'Abid': [79, 85, 88],
    'Zaid': [90, 87, 82],
}

results = []
for name, marks in STUDENTS.items():
    result = {
        'name': name,
        'mark_1': marks[0],
        'mark_2': marks[1],
        'mark_3': marks[2],
        'average': round(sum(marks) / len(marks), 2),
    }
    results.append(result)

fieldnames = ['name', 'mark_1', 'mark_2', 'mark_3', 'average']
with open('results.csv', 'w', newline='', encoding='utf-8') as results_file:
    writer = csv.DictWriter(results_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

with open('results.json', 'w', encoding='utf-8') as results_file:
    json.dump(results, results_file, indent=4)
